#!/usr/bin/env python3
"""Insert the shared reader-importance block using editor-verified sentences."""
from pathlib import Path
import argparse,html
p=argparse.ArgumentParser();p.add_argument('--file',required=True);p.add_argument('--sentences',nargs='+',required=True);a=p.parse_args()
if not 1<=len(a.sentences)<=3:p.error('Supply 1 to 3 fact-checked sentences')
f=Path(a.file);s=f.read_text()
if 'class="why-important"' in s:raise SystemExit('Existing block preserved; edit it explicitly')
block='<aside class="why-important" aria-label="왜 중요한가"><h2>왜 중요한가</h2><p>'+ '<br>'.join(html.escape(t) for t in a.sentences)+'</p></aside>'
css='<style>.why-important{margin:20px 0;padding:16px 20px;background:#e6eeea;border-left:4px solid #086b70}.why-important h2{font:700 17px/1.4 system-ui;margin:0 0 8px;padding:0;border:0}.why-important p{font-size:16px;line-height:1.8;margin:0}</style>'
start=s.find('</h1>')
if start<0:raise SystemExit('No article heading; file unchanged')
s=s[:start+5]+block+s[start+5:];s=s.replace('</head>',css+'</head>',1);f.write_text(s);print('Inserted verified importance block:',f.name)
