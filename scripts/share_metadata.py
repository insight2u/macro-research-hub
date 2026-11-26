#!/usr/bin/env python3
"""Add/check basic share cards for every static HTML page before publishing.
Run: python scripts/share_metadata.py --apply ; then --check.
Pages with hand-set tags retain their own titles, images and descriptions.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,html,re,sys
BASE='https://insight2u.github.io/macro-research-hub/'
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.title='';self.in_title=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='title':self.in_title=True
  if tag=='meta':self.meta[a.get('property',a.get('name',''))]=a.get('content','')
 def handle_endtag(self,tag):
  if tag=='title':self.in_title=False
 def handle_data(self,data):
  if self.in_title:self.title+=data
parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
failed=[]
for p in ROOT.rglob('*.html'):
 if any(x.startswith('.') for x in p.relative_to(ROOT).parts) or 'preview' in p.name:continue
 s=p.read_text();d=Page();d.feed(s);rel=p.relative_to(ROOT).as_posix()
 defaults={'og:type':'website' if rel in ['index.html','pay.html'] else 'article','og:site_name':'데일리샷 매크로 리서치','og:locale':'ko_KR','og:title':d.title.split(' | 데일리샷')[0] or '데일리샷 매크로 리서치','og:description':d.meta.get('description') or '데일리샷 매크로 리서치의 기사와 보고서를 읽고 관련 방송으로 들어 보세요.','og:url':BASE+('' if rel=='index.html' else rel),'og:image':'https://lh3.googleusercontent.com/d/1shysoUyFGMLxXgbL416TNzzn9D-GIxwF','og:image:type':'image/png','og:image:width':'1200','og:image:height':'630'}
 defaults.update({'twitter:card':'summary_large_image','twitter:title':d.meta.get('og:title') or defaults['og:title'],'twitter:description':d.meta.get('og:description') or defaults['og:description'],'twitter:image':d.meta.get('og:image') or defaults['og:image']})
 missing={k:v for k,v in defaults.items() if not d.meta.get(k)}
 if args.apply and missing:
  block='\n<!-- Default link preview metadata. Keep these in new page templates. -->\n'+'\n'.join('<meta '+('name' if k.startswith('twitter:') else 'property')+'="'+k+'" content="'+html.escape(v,quote=True)+'"/>' for k,v in missing.items())+'\n'
  if '</head>' not in s:failed.append(rel+': missing head');continue
  p.write_text(s.replace('</head>',block+'</head>'));d.meta.update(missing)
 if missing and not args.apply:failed.append(rel+': missing '+','.join(missing))
 for k in ['og:url','og:image']:
  if d.meta.get(k) and not d.meta[k].startswith('https://'):failed.append(rel+': nonabsolute '+k)
 image=d.meta.get('og:image','')
 if image.startswith(BASE) and not (ROOT/image[len(BASE):]).is_file():failed.append(rel+': image file absent')
if failed:print('\n'.join(failed));sys.exit(1)
print('Share metadata verified for all static HTML pages.')
