#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_cartoon_video_langs.py — 만평 애니메이션의 7개 언어 말풍선 변형 생성.

Usage: python3 scripts/make_cartoon_video_langs.py scripts/cartoon_specs/2026-11-19.json [lang ...]
Output: images/cartoon/<base>.<lang>.mp4 per language (ko = base file from make_cartoon_video.py).
Daily use: translate the two bubble lines below for the day's lines, then run.
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_cartoon_video import render

FONTS = os.path.expanduser('~/.local/share/fonts')
INK = [37, 31, 33]
GREEN = [33, 92, 80]

# label = bubble speaker label (bold), lines split to fit the bubble
LANGS = {
 'en': {'font': FONTS + '/NotoSansKR.ttf', 'rtl': False,
        'b1': [['Bill ', '“We raised the punishment,'], ['so fairness grew too, right?”']],
        'b2': [['Citizen ', '“That\'s the sentence.'], ['Fairness is what we check now.”']]},
 'zh': {'font': FONTS + '/NotoSansSC.ttf', 'rtl': False,
        'b1': [['法案 ', '“惩罚加重了，'], ['公平也更大了吧？”']],
        'b2': [['市民 ', '“那是刑罚。'], ['公平从现在开始检验。”']]},
 'ja': {'font': FONTS + '/NotoSansJP.ttf', 'rtl': False,
        'b1': [['法案 ', '「罰を重くしたから、'], ['公正も大きくなったよね？」']],
        'b2': [['市民 ', '「それは量刑です。'], ['公正はこれから確かめます。」']]},
 'es': {'font': FONTS + '/NotoSansKR.ttf', 'rtl': False,
        'b1': [['Proyecto ', '“Si la pena es mayor,'], ['la justicia también, ¿no?”']],
        'b2': [['Ciudadano ', '“Esa es la pena.'], ['La justicia se comprueba ahora.”']]},
 'ru': {'font': FONTS + '/NotoSans.ttf', 'rtl': False,
        'b1': [['Законопроект ', '«Наказание ужесточили,'], ['значит, справедливости больше?»']],
        'b2': [['Гражданин ', '«Это срок.'], ['Справедливость мы теперь проверяем.»']]},
 'ar': {'font': FONTS + '/NotoNaskhArabic.ttf', 'rtl': True,
        'b1': [['مشروع القانون ', '"شددنا العقوبة،'], ['فزادت العدالة أيضًا، أليس كذلك؟"']],
        'b2': [['المواطن ', '"تلك هي العقوبة.'], ['أما العدالة فنتحقق منها الآن."']]},
 'sw': {'font': FONTS + '/NotoSansKR.ttf', 'rtl': False,
        'b1': [['Muswada ', '“Tumeongeza adhabu,'], ['haki nayo imeongezeka, sivyo?”']],
        'b2': [['Mwananchi ', '“Hiyo ni adhabu.'], ['Haki tunaihakikisha sasa.”']]},
}


def build(base_spec, lang):
    meta = LANGS[lang]
    spec = copy.deepcopy(base_spec)
    for key, bub in (('b1', 0), ('b2', 1)):
        lines = []
        for idx, line in enumerate(meta[key]):
            if idx == 0:
                spans = [[line[0], True, GREEN]] + [[e, False, INK] for e in line[1:]]
            else:
                spans = [[e, False, INK] for e in line]
            lines.append(spans)
        spec['bubbles'][bub]['lines'] = lines
        spec['bubbles'][bub]['font'] = meta['font']
        spec['bubbles'][bub]['rtl'] = meta['rtl']
    root, ext = os.path.splitext(base_spec['out'])
    spec['out'] = root + '.' + lang + ext
    spec['_frames_dir'] = '/tmp/cartoon_frames_' + lang
    return spec


if __name__ == '__main__':
    base = json.load(open(sys.argv[1], encoding='utf-8'))
    langs = sys.argv[2:] or list(LANGS)
    for lang in langs:
        print('=== rendering', lang, flush=True)
        render_obj = build(base, lang)
        tmp = '/tmp/cartoon_spec_%s.json' % lang
        json.dump(render_obj, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False)
        render(tmp)
