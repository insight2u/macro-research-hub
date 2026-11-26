#!/usr/bin/env python3
"""Refresh confirmed public YouTube RSS entries. Fail closed, retain last good snapshot."""
import json,re,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RSS='https://www.youtube.com/feeds/videos.xml?channel_id=UCQLg57KWFEweA6IiXJPteLA'
def main():
 raw=urllib.request.urlopen(RSS,timeout=30).read()
 ns={'a':'http://www.w3.org/2005/Atom','yt':'http://www.youtube.com/xml/schemas/2015'}
 out=[]
 for e in ET.fromstring(raw).findall('a:entry',ns):
  title=e.findtext('a:title','',ns);vid=e.findtext('yt:videoId','',ns)
  d=re.match(r'(\d{4})[-.](\d{2})[-.](\d{2})',title)
  if not d or not re.fullmatch(r'[A-Za-z0-9_-]{11}',vid):continue
  out.append(dict(id=vid,title=title,url='https://www.youtube.com/watch?v='+vid,date='.'.join(d.groups()),article=''))
 if not out:raise ValueError('No valid RSS entries; last good snapshot retained')
 latest=max(x['date'] for x in out);out=[x for x in out if x['date']==latest]
 out.sort(key=lambda x:0 if '경제 체온계' in x['title'] else 1)
 for i,x in enumerate(out):x['order']=i
 p=ROOT/'assets/data/dailyshot-player.js';s=p.read_text()
 s,n=re.subn(r'/\* RSS_SNAPSHOT_START \*/.*?/\* RSS_SNAPSHOT_END \*/','/* RSS_SNAPSHOT_START */\nif(l===\'ko\')entries.push(...'+json.dumps(out,ensure_ascii=False)+');\n/* RSS_SNAPSHOT_END */',s,flags=re.S)
 if n!=1:raise ValueError('Missing snapshot markers')
 p.write_text(s)
 p=ROOT/'index.html';s=p.read_text();x=out[0]
 import html
 fallback='<p id="youtube-static-fallback">최신 확인 회차 · '+html.escape(x['date'])+' · <a href="'+x['url']+'" target="_blank" rel="noopener">'+html.escape(x['title'])+'</a>. 플레이어가 열리지 않으면 이 링크로 시청하세요.</p>'
 s,n=re.subn(r'<p id="youtube-static-fallback">.*?</p>',fallback,s,flags=re.S)
 if n!=1:raise ValueError('Missing static fallback')
 p.write_text(s)
 print('Synced',latest,len(out),'public RSS entries')
if __name__=='__main__':main()
