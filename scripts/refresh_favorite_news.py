from pathlib import Path
import json,re,urllib.request,datetime,concurrent.futures
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--output-dir',default='.');args=parser.parse_args();P=Path(args.output_dir);P.mkdir(parents=True,exist_ok=True)
SOURCES=[{'name':'Bloomberg','favorite':'https://www.bloomberg.com/asia','url':'https://www.youtube.com/@markets/streams','live_only':True},{'name':'연합뉴스','favorite':'https://www.yna.co.kr/','url':'https://www.youtube.com/channel/UCj3_t5p4L4aFsvdW3uHjnnw/videos'},{'name':'뉴스타파','favorite':'https://newstapa.org/','url':'https://www.youtube.com/channel/UCeFUGS2VCOb6DO3BiUgvwNA/videos'},{'name':'오마이TV','favorite':'https://www.ohmynews.com/','url':'https://www.youtube.com/channel/UClAfLVQYZSLrMAQQ_SXPVZw/videos'}]
def get(u):return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Accept-Language':'ko-KR,ko;q=0.9'}),timeout=30).read().decode('utf-8','replace')
def collect(src):
 s=get(src['url']+'?hl=ko&gl=KR');(P/(src['name']+'-channel.html')).write_text(s);m=re.search(r'ytInitialData\s*=\s*',s);j=json.JSONDecoder().raw_decode(s[m.end():])[0];locks=[]
 def walk(x):
  if isinstance(x,dict):
   if 'lockupViewModel'in x:locks.append(x['lockupViewModel'])
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(j);out=[]
 for x in locks:
  vid=x.get('contentId','');meta=x.get('metadata',{}).get('lockupMetadataViewModel',{});title=meta.get('title',{}).get('content','');over=x.get('contentImage',{}).get('thumbnailViewModel',{}).get('overlays',[]);flat=json.dumps(over,ensure_ascii=False);live='THUMBNAIL_OVERLAY_BADGE_STYLE_LIVE'in flat
  if not re.fullmatch(r'[\w-]{11}',vid) or not title or 'UPCOMING'in flat or 'Upcoming'in flat or '예정'in flat:continue
  if src.get('live_only')and not live:continue
  paths=[]
  def hrefs(o):
   if isinstance(o,dict):
    u=o.get('webCommandMetadata',{}).get('url','')
    if u.startswith('/watch?')and ('v='+vid)in u:paths.append(u)
    for v in o.values():hrefs(v)
   elif isinstance(o,list):
    for v in o:hrefs(v)
  hrefs(x)
  if not paths:continue
  out.append({'id':vid,'source':src['name'],'title':title,'url':'https://www.youtube.com'+paths[0],'channel_url':src['url'],'favorite_url':src['favorite'],'live':live,'published_label':json.dumps(meta.get('metadata',{}),ensure_ascii=False),'verified_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
  if len(out)>=3:break
 return out
rows=[];errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:
 fs={ex.submit(collect,s):s for s in SOURCES}
 data={}
 for f,s in fs.items():
  try:data[s['name']]=f.result()
  except Exception as e:errors.append({'source':s['name'],'error':type(e).__name__})
 for n in range(3):
  for src in SOURCES:
   ar=data.get(src['name'],[])
   if n<len(ar):rows.append(ar[n])
seen=set();rows=[r for r in rows if not(r['id']in seen or seen.add(r['id']))]
import xml.etree.ElementTree as ET
ns={'a':'http://www.w3.org/2005/Atom','yt':'http://www.youtube.com/xml/schemas/2015'};dates={}
for src in SOURCES:
 channel=src['url'].split('/channel/')[-1].split('/')[0] if '/channel/'in src['url']else None
 if not channel:continue
 try:
  xml=get('https://www.youtube.com/feeds/videos.xml?channel_id='+channel)
  for e in ET.fromstring(xml).findall('a:entry',ns):dates[e.findtext('yt:videoId',namespaces=ns)]=e.findtext('a:published',namespaces=ns)
 except Exception as e:errors.append({'source':src['name'],'feed_error':type(e).__name__})
for r in rows:
 if r['id']in dates:r['published_at']=dates[r['id']]
manifest={'updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'refresh_note':'공개 채널 확인 · 생방송은 제공사 송출 · 녹화 목록은 00:30/21:00 KST 발행 작업에서 갱신','sources':SOURCES,'videos':rows,'errors':errors}
assert len(rows)>=7 and any(r['live']for r in rows),(len(rows),errors)
(P/'news-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));print(json.dumps({'count':len(rows),'videos':[{k:r[k]for k in ['source','id','title','url','live']}for r in rows],'errors':errors},ensure_ascii=False,indent=2))
