"""Refresh the existing international schedule without changing its regional mix.
Official channel HTML is discovery only. A login/challenge/missing result preserves the last verified entry and timestamp, records a failure, and does not certify current live status.
Publish only after the source changes and actual player behavior have been reviewed.
"""
from pathlib import Path
import argparse,json,re,urllib.request,datetime,concurrent.futures
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='.');ap.add_argument('--input',default='favorite-news.json');args=ap.parse_args();P=Path(args.output_dir);P.mkdir(parents=True,exist_ok=True)
src=Path(args.input);m=json.loads(src.read_text());assert m.get('version')==2,'International v2 manifest required. Do not replace it with the old four-source list.'
now=datetime.datetime.now(datetime.timezone.utc).isoformat();errors=[]
def fetch(u):return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8','replace')
def refresh(a):
 try:
  s=fetch(a['channel_url']);mch=re.search(r'ytInitialData\s*=\s*',s)
  if not mch:raise ValueError('No channel data, possible provider restriction')
  d=json.JSONDecoder().raw_decode(s[mch.end():])[0];candidates=[]
  def walk(x):
   if isinstance(x,dict):
    if 'lockupViewModel'in x:
     v=x['lockupViewModel'];flat=json.dumps(v.get('contentImage',{}));meta=v.get('metadata',{}).get('lockupMetadataViewModel',{});candidates.append((v.get('contentId'),meta.get('title',{}).get('content'),'THUMBNAIL_OVERLAY_BADGE_STYLE_LIVE'in flat))
    if 'videoRenderer'in x:
     v=x['videoRenderer'];flat=json.dumps(v.get('thumbnailOverlays',[]));candidates.append((v.get('videoId'),''.join(r.get('text','')for r in v.get('title',{}).get('runs',[])),'LIVE'in flat))
    for v in x.values():walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(d)
  candidates=[x for x in candidates if x[0]and re.fullmatch(r'[\w-]{11}',x[0])and x[1]and x[2]==a['live']]
  if not candidates:raise ValueError('No matching live/recorded official candidate')
  # Fixed editorial source slot. A discovered replacement is proposed, not silently certified playable.
  v=candidates[0];return a,{'source':a['source'],'candidate_id':v[0],'candidate_title':v[1],'candidate_live':v[2],'checked_at':now,'requires_review':True}
 except Exception as e:return a,{'source':a['source'],'error':type(e).__name__,'checked_at':now,'retained_last_verified':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=5)as ex:results=list(ex.map(refresh,m['videos']))
proposals=[r for _,r in results];m['refresh_attempted_at']=now;m['pending_source_review']=proposals;m['errors']=[r for r in proposals if 'error'in r]
# updated_at and verified_at deliberately remain unchanged until independent review.
(P/'news-manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'retained_slots':len(m['videos']),'retained_mix':sum(v['live']for v in m['videos']),'review_candidates':len(proposals)-len(m['errors']),'errors':m['errors'],'publication_ready':False},ensure_ascii=False))
