#!/usr/bin/env python3
"""Refresh public feed snapshots, excluding the other magazine's sections."""
from pathlib import Path
import urllib.request,xml.etree.ElementTree as ET,json,re,datetime
ROOT=Path(__file__).resolve().parents[1]
URL='https://www.youtube.com/feeds/videos.xml?channel_id=UCQLg57KWFEweA6IiXJPteLA'
NS={'a':'http://www.w3.org/2005/Atom','yt':'http://www.youtube.com/xml/schemas/2015'}
INNOVATION={'오늘의 혁신','정책을 읽다','국회와 제도','쟁점과 검증','사람과 기록','지역과 역사'}
feed=ET.fromstring(urllib.request.urlopen(URL,timeout=30).read());items=[]
for e in feed.findall('a:entry',NS):
 title=e.findtext('a:title',namespaces=NS) or '';parts=[x.strip() for x in title.split('|')]
 if len(parts)<3 or parts[1] in INNOVATION:continue
 id=e.findtext('yt:videoId',namespaces=NS)
 if not re.fullmatch(r'[A-Za-z0-9_-]{11}',id or ''):continue
 published=e.findtext('a:published',namespaces=NS)
 # Content date is independent from the public release date.
 date=parts[0].replace('-','.')
 items.append(dict(id=id,title=title,url=e.find('a:link',NS).get('href'),date=date,published_at=published,article='',order=len(items)))
if not items:raise RuntimeError('No matching feed entries; prior snapshot preserved')
p=ROOT/'assets/data/dailyshot-player.js';s=p.read_text()
block="/* RSS_SNAPSHOT_START */\nif(l==='ko')entries.push(..."+json.dumps(items,ensure_ascii=False)+");\n/* RSS_SNAPSHOT_END */"
s,n=re.subn(r'/\* RSS_SNAPSHOT_START \*/.*?/\* RSS_SNAPSHOT_END \*/',lambda m:block,s,flags=re.S);assert n==1;p.write_text(s)
(ROOT/'assets/data/broadcast-rss-snapshot.json').write_text(json.dumps(dict(source_url=URL,updated_at=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat(),items=items),ensure_ascii=False,indent=2)+'\n')
# Update the no-script fallback and cache key together with the feed snapshot.
import html
p=ROOT/'index.html';s=p.read_text();x=items[0]
fallback='<p id="youtube-static-fallback">최신 확인 회차 · '+x['date']+' · <a href="'+x['url']+'" rel="noopener" target="_blank">'+html.escape(x['title'])+'</a>. 플레이어가 열리지 않으면 이 링크로 시청하세요.</p>'
s=re.sub(r'<p id="youtube-static-fallback">.*?</p>',lambda m:fallback,s,count=1,flags=re.S)
stamp=datetime.datetime.now().strftime('%Y%m%d%H%M')
s=re.sub(r'dailyshot-player.js\?v=[^"\s]+','dailyshot-player.js?v=rss'+stamp,s)
p.write_text(s)
print('Updated general feed snapshot:',len(items),'entries; latest content date',max(x['date'] for x in items))
