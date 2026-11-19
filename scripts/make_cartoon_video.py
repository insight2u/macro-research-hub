#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_cartoon_video.py — 매일 만평 스틸 이미지를 무음 루프 애니메이션(MP4)으로 변환.

Daily pipeline (매일 아침 만평 제작 절차):
  1. 그날의 만평 장면 PNG를 만든다 (기존 절차와 동일, 예: images/cartoon/<date>-cartoon-scene.png).
  2. 스펙 JSON을 작성한다 (scripts/cartoon_specs/<date>.json 복사 후 수정):
     - image: 원본 장면 PNG 경로
     - bubbles: 말풍선 문구·위치·등장/퇴장 시각 (말풍선은 영상 안에 구워짐)
     - regions: 숨쉬기(브리딩) 움직임을 줄 캐릭터 영역 (원본 픽셀 좌표)
     - camera: 시간대별 카메라 위치/줌 키프레임 (첫 값과 마지막 값이 같아야 매끄러운 루프)
  3. 실행: python3 scripts/make_cartoon_video.py scripts/cartoon_specs/<date>.json
     → <out>.mp4 생성 (H.264, 무음, yuv420p, faststart). 포스터는 원본 PNG 재사용.
  4. index.html의 #nr-daily-cartoon <video> src/poster를 새 파일로 교체.
  5. 배포 후 실제 재생 화면(PC/모바일)을 캡처해 확인.

의존: pillow, numpy, ffmpeg(시스템), Noto Sans KR(없으면 자동 다운로드, 추가 지출 없음).
"""
import json, math, os, subprocess, sys, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_PATH = os.path.expanduser('~/.local/share/fonts/NotoSansKR.ttf')
FONT_URL = 'https://github.com/google/fonts/raw/main/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf'


def ensure_font():
    if not os.path.exists(FONT_PATH):
        os.makedirs(os.path.dirname(FONT_PATH), exist_ok=True)
        urllib.request.urlretrieve(FONT_URL, FONT_PATH)
    return FONT_PATH


def font(size, bold=False, path=None):
    f = ImageFont.truetype(path or FONT_PATH, size)
    for axes in (([700], [100, 700]) if bold else ([400], [100, 400])):
        try:
            f.set_variation_by_axes(axes)
            break
        except Exception:
            continue
    return f


def shape_text(text, rtl):
    """Arabic/RTL: reshape and apply bidi so PIL can draw it."""
    if rtl:
        import arabic_reshaper
        from bidi.algorithm import get_display
        return get_display(arabic_reshaper.reshape(text))
    return text


def ease(t):
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, t)))


def back_out(t):
    """overshoot ease for bubble pop-in"""
    t = max(0.0, min(1.0, t))
    c = 1.70158
    return 1 + (c + 1) * ((t - 1) ** 3) + c * ((t - 1) ** 2)


class Camera:
    def __init__(self, keys, src_w, src_h, out_w, out_h):
        self.keys = sorted(keys, key=lambda k: k['t'])
        self.sw, self.sh, self.ow, self.oh = src_w, src_h, out_w, out_h

    def state(self, t):
        ks = self.keys
        if t <= ks[0]['t']:
            return ks[0]['cx'], ks[0]['cy'], ks[0]['z']
        for a, b in zip(ks, ks[1:]):
            if a['t'] <= t <= b['t']:
                f = ease((t - a['t']) / (b['t'] - a['t'])) if b['t'] > a['t'] else 0
                return (a['cx'] + (b['cx'] - a['cx']) * f,
                        a['cy'] + (b['cy'] - a['cy']) * f,
                        a['z'] + (b['z'] - a['z']) * f)
        return ks[-1]['cx'], ks[-1]['cy'], ks[-1]['z']

    def rect(self, t):
        cx, cy, z = self.state(t)
        w = self.sw / z
        h = w * self.oh / self.ow
        if h > self.sh / z:  # keep aspect sane on odd sources
            h = self.sh / z
            w = h * self.ow / self.oh
        cx = max(w / 2, min(self.sw - w / 2, cx * self.sw))
        cy = max(h / 2, min(self.sh - h / 2, cy * self.sh))
        return cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2

    def to_frame(self, sx, sy, t):
        x0, y0, x1, y1 = self.rect(t)
        return (sx - x0) / (x1 - x0) * self.ow, (sy - y0) / (y1 - y0) * self.oh, self.ow / (x1 - x0)


class Warper:
    """Localized radial 'breathing' displacement inside an ellipse; edges stay pinned."""

    def __init__(self, region):
        self.cx, self.cy = region['center']
        self.rx, self.cy_r = region['radius'][0], region['radius'][1]
        self.ry = region['radius'][1]
        self.amp = region.get('amp', 3.0)
        self.cycles = region.get('cycles', 4)
        self.phase = region.get('phase', 0.0)
        self.t_from = region.get('t_from', 0.0)
        self.t_to = region.get('t_to', 1e9)
        pad = 8
        self.x0 = int(self.cx - self.rx - pad); self.x1 = int(self.cx + self.rx + pad)
        self.y0 = int(self.cy - self.ry - pad); self.y1 = int(self.cy + self.ry + pad)
        yy, xx = np.mgrid[self.y0:self.y1, self.x0:self.x1].astype(np.float64)
        nx = (xx - self.cx) / self.rx
        ny = (yy - self.cy) / self.ry
        r = np.sqrt(nx * nx + ny * ny)
        w = np.clip(1 - r, 0, 1)
        self.weight = np.cos(w * math.pi / 2) ** 2
        norm = np.maximum(r, 1e-6)
        self.dirx = nx / norm
        self.diry = ny / norm
        self.xx = xx
        self.yy = yy

    def _map_frame(self, t, cam):
        cx, cy, s = cam.to_frame(self.cx, self.cy, t)
        rx, ry = self.rx * s, self.ry * s
        pad = 8
        x0 = max(0, int(cx - rx - pad)); x1 = min(cam.ow, int(cx + rx + pad))
        y0 = max(0, int(cy - ry - pad)); y1 = min(cam.oh, int(cy + ry + pad))
        if x1 - x0 < 8 or y1 - y0 < 8:
            return None
        yy, xx = np.mgrid[y0:y1, x0:x1].astype(np.float64)
        nx = (xx - cx) / rx
        ny = (yy - cy) / ry
        r = np.sqrt(nx * nx + ny * ny)
        weight = np.cos(np.clip(1 - r, 0, 1) * math.pi / 2) ** 2
        norm = np.maximum(r, 1e-6)
        return x0, y0, x1, y1, xx, yy, nx / norm, ny / norm, weight

    def apply(self, arr, t, cam):
        if not (self.t_from <= t <= self.t_to):
            return
        m = self._map_frame(t, cam)
        if m is None:
            return
        x0, y0, x1, y1, xx, yy, dirx, diry, weight = m
        disp = self.amp * (cam.ow / 1370.0) * math.sin(2 * math.pi * self.cycles * t / 16.0 + self.phase)
        if abs(disp) < 0.05:
            return
        sxx = xx - dirx * disp * weight
        syy = yy - diry * disp * weight
        patch = arr[y0:y1, x0:x1]
        arr[y0:y1, x0:x1] = bilinear(patch, sxx - x0, syy - y0)


def bilinear(img, xs, ys):
    h, w = img.shape[:2]
    x0 = np.clip(np.floor(xs).astype(np.int64), 0, w - 2)
    y0 = np.clip(np.floor(ys).astype(np.int64), 0, h - 2)
    fx = np.clip(xs - x0, 0, 1)[..., None]
    fy = np.clip(ys - y0, 0, 1)[..., None]
    return ((img[y0, x0] * (1 - fx) * (1 - fy) + img[y0, x0 + 1] * fx * (1 - fy) +
             img[y0 + 1, x0] * (1 - fx) * fy + img[y0 + 1, x0 + 1] * fx * fy)).astype(np.uint8)


def draw_bubble(spec, scale, alpha):
    """Render one speech bubble to an RGBA layer at full canvas size."""
    rtl = spec.get('rtl', False)
    fpath = spec.get('font')
    x0, y0, x1, y1 = spec['box']
    tip = spec['tail']
    cw, ch = spec['_canvas']
    layer = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
    bw, bh = x1 - x0, y1 - y0
    bubble = Image.new('RGBA', (bw + 40, bh + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(bubble)
    a = int(255 * alpha)
    pad_x = spec.get('pad_x', 30)
    pad_y = spec.get('pad_y', 22)
    fs = spec.get('font_size', 46)
    max_w = bw - 2 * pad_x
    # auto-fit: shrink font until every line fits the bubble width
    while fs > 20:
        fits = True
        for line in spec['lines']:
            wline = sum(font(fs, bold, fpath).getlength(shape_text(text, rtl)) for text, bold, color in line)
            if wline > max_w:
                fits = False
                break
        if fits and fs * 1.5 * len(spec['lines']) <= bh - 2 * pad_y + fs * 0.5:
            break
        fs -= 2
    # shadow + body
    d.rounded_rectangle([23, 23, 23 + bw, 23 + bh], radius=26, fill=(37, 31, 33, int(a * 0.10)))
    d.rounded_rectangle([20, 20, 20 + bw, 20 + bh], radius=26, fill=(255, 255, 255, a),
                        outline=(200, 206, 199, a), width=3)
    # tail: triangle from bottom edge toward tip
    bx = 20 + bw // 2
    tip_local = (tip[0] - (x0 - 20), tip[1] - (y0 - 20))
    d.polygon([(bx - 26, 18 + bh), (bx + 26, 18 + bh), tip_local], fill=(255, 255, 255, a))
    d.line([(bx - 26, 19 + bh), tip_local], fill=(200, 206, 199, a), width=3)
    d.line([(bx + 26, 19 + bh), tip_local], fill=(200, 206, 199, a), width=3)
    # text lines: list of lines, each a list of [text, bold, color]
    ty = 20 + pad_y
    for line in spec['lines']:
        spans = list(reversed(line)) if rtl else line
        wline = sum(font(fs, bold, fpath).getlength(shape_text(text, rtl)) for text, bold, color in line)
        tx = 20 + (bw - pad_x - wline if rtl else pad_x)
        for text, bold, color in spans:
            f = font(fs, bold, fpath)
            t = shape_text(text, rtl)
            d.text((tx, ty), t, font=f, fill=(*color, a))
            tx += d.textlength(t, font=f)
        ty += int(fs * 1.5)
    if scale != 1.0:
        nw = max(1, int(bubble.width * scale))
        nh = max(1, int(bubble.height * scale))
        bubble = bubble.resize((nw, nh), Image.LANCZOS)
        ox = x0 - 20 + (bubble.width * 0) - int((nw - (bw + 40)) / 2)
        oy = y0 - 20 - int((nh - (bh + 60)) / 2)
    else:
        ox, oy = x0 - 20, y0 - 20
    layer.alpha_composite(bubble, (int(ox), int(oy)))
    return layer


def make_glow(size=260, color=(255, 214, 90)):
    g = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    d.ellipse([size * 0.18, size * 0.18, size * 0.82, size * 0.82], fill=(*color, 110))
    return g.filter(ImageFilter.GaussianBlur(size / 5))


def make_dot(r):
    s = r * 6
    g = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(g)
    d.ellipse([s / 2 - r, s / 2 - r, s / 2 + r, s / 2 + r], fill=(255, 255, 255, 150))
    return g.filter(ImageFilter.GaussianBlur(r / 1.5))


def render(spec_path):
    with open(spec_path, encoding='utf-8') as f:
        spec = json.load(f)
    ensure_font()
    out_w, out_h = spec.get('size', [1600, 980])
    fps = spec.get('fps', 24)
    dur = spec.get('duration', 16.0)
    n = int(fps * dur)
    src = Image.open(spec['image']).convert('RGB')
    big = src.resize((src.width * 2, src.height * 2), Image.LANCZOS)  # oversampled for zoom quality
    cam = Camera(spec['camera'], src.width * 2, src.height * 2, out_w, out_h)
    # region coords are given in original-image pixels; convert to oversampled space
    regions = []
    for r in spec.get('regions', []):
        rr = dict(r)
        rr['center'] = [r['center'][0] * 2, r['center'][1] * 2]
        rr['radius'] = [r['radius'][0] * 2, r['radius'][1] * 2]
        regions.append(Warper(rr))
    for b in spec.get('bubbles', []):
        b['_canvas'] = (out_w, out_h)
    glow = make_glow()
    glow_spec = spec.get('glow')  # {center:[x,y], t_from, t_to} in original px
    glint = spec.get('glint')     # {center:[x,y], radius, t_from, t_to} in original px
    dust = []
    if spec.get('dust', True):
        import random
        rng = random.Random(7)
        for _ in range(12):
            dust.append((rng.uniform(0, out_w), rng.uniform(0, out_h * 0.75),
                         rng.uniform(14, 42), rng.uniform(6, 20), rng.uniform(0, 6.28),
                         rng.choice([1, 2]), make_dot(rng.choice([3, 4, 6]))))
    frames_dir = spec.get('_frames_dir', '/tmp/cartoon_frames')
    os.makedirs(frames_dir, exist_ok=True)
    for old in os.listdir(frames_dir):
        os.remove(os.path.join(frames_dir, old))
    for i in range(n):
        t = i / fps
        x0, y0, x1, y1 = cam.rect(t)
        frame = big.crop((int(x0), int(y0), int(x1), int(y1))).resize((out_w, out_h), Image.LANCZOS)
        arr = np.asarray(frame).copy()
        for w in regions:
            w.apply(arr, t, cam)
        frame = Image.fromarray(arr).convert('RGBA')
        # glow pulse
        if glow_spec and glow_spec['t_from'] <= t <= glow_spec['t_to']:
            gt = (t - glow_spec['t_from']) / (glow_spec['t_to'] - glow_spec['t_from'])
            alpha = 0.5 + 0.5 * math.sin(gt * math.pi * 6)
            gx, gy, gs = cam.to_frame(glow_spec['center'][0] * 2, glow_spec['center'][1] * 2, t)
            g = glow.resize((int(260 * gs / 2), int(260 * gs / 2)), Image.LANCZOS)
            g.putalpha(g.getchannel('A').point(lambda v: int(v * alpha * 0.8)))
            frame.alpha_composite(g, (int(gx - g.width / 2), int(gy - g.height / 2)))
        # magnifier glint sweep
        if glint and glint['t_from'] <= t <= glint['t_to']:
            gt = (t - glint['t_from']) / (glint['t_to'] - glint['t_from'])
            lx, ly, ls = cam.to_frame(glint['center'][0] * 2, glint['center'][1] * 2, t)
            lr = glint['radius'] * ls
            sweep = (gt * 2.4 - 1.2) * lr * 2
            ov = Image.new('RGBA', (out_w, out_h), (0, 0, 0, 0))
            d = ImageDraw.Draw(ov)
            d.line([(lx + sweep - lr * 0.5, ly - lr), (lx + sweep + lr * 0.5, ly + lr)],
                   fill=(255, 255, 255, 90), width=max(6, int(lr * 0.35)))
            mask = Image.new('L', (out_w, out_h), 0)
            ImageDraw.Draw(mask).ellipse([lx - lr, ly - lr, lx + lr, ly + lr], fill=110)
            ov.putalpha(Image.composite(ov.getchannel('A'), Image.new('L', (out_w, out_h), 0), mask))
            frame.alpha_composite(ov)
        # dust motes (periodic so the loop is seamless)
        ov = Image.new('RGBA', (out_w, out_h), (0, 0, 0, 0))
        for px, py, ax, ay, ph, cyc, sprite in dust:
            dx = px + ax * math.sin(2 * math.pi * cyc * t / dur + ph)
            dy = py + ay * math.sin(2 * math.pi * cyc * t / dur + ph * 1.7)
            dx = max(0, min(out_w - sprite.width, int(dx)))
            dy = max(0, min(out_h - sprite.height, int(dy)))
            ov.alpha_composite(sprite, (dx, dy))
        frame.alpha_composite(ov)
        # speech bubbles
        for b in spec.get('bubbles'):
            if t < b['t_in'] - 0.5 or t > b['t_out'] + 0.6:
                continue
            if t < b['t_in']:
                sc, al = 0.8, 0.0
            elif t < b['t_in'] + 0.5:
                sc = 0.8 + 0.2 * back_out((t - b['t_in']) / 0.5)
                al = min(1.0, (t - b['t_in']) / 0.25)
            elif t <= b['t_out']:
                sc, al = 1.0, 1.0
            else:
                sc, al = 0.97, max(0.0, 1 - (t - b['t_out']) / 0.6)
            if al > 0:
                frame.alpha_composite(draw_bubble(b, sc, al))
        frame.convert('RGB').save(os.path.join(frames_dir, 'f%04d.jpg' % i), quality=92)
        if i % 60 == 0:
            print('frame %d/%d' % (i, n), flush=True)
    out = spec['out']
    subprocess.run(['ffmpeg', '-y', '-framerate', str(fps), '-i', os.path.join(frames_dir, 'f%04d.jpg'),
                    '-c:v', 'libx264', '-preset', 'medium', '-crf', '22', '-pix_fmt', 'yuv420p',
                    '-movflags', '+faststart', '-an', out], check=True)
    print('WROTE', out, os.path.getsize(out), 'bytes')


if __name__ == '__main__':
    render(sys.argv[1])
