#!/usr/bin/env python3
"""Attach a rights-grounded caption, never infer a license from a public URL."""
import argparse,html
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--file',required=True);p.add_argument('--description',required=True);p.add_argument('--creator',required=True);p.add_argument('--provider',required=True);p.add_argument('--rights',required=True);p.add_argument('--source-url',required=True);p.add_argument('--changes',default='변경 없음');a=p.parse_args()
if not a.source_url.startswith('https://'):p.error('Use a verified original HTTPS source')
f=Path(a.file);s=f.read_text()
if 'class="image-credit"' in s:raise SystemExit('Existing credit preserved; edit explicitly')
cap='<figcaption class="image-credit">'+ ' · '.join(html.escape(t) for t in [a.description,a.creator,a.provider,a.rights,a.changes])+' · <a href="'+html.escape(a.source_url,quote=True)+'" target="_blank" rel="noopener noreferrer">원본 보기 ↗</a></figcaption>'
i=s.find('</figure>')
if i<0:raise SystemExit('No figure; file unchanged')
# Do not duplicate an existing caption.
start=s.rfind('<figure',0,i)
if '<figcaption' in s[start:i]:raise SystemExit('Figure already has a caption; merge manually')
f.write_text(s[:i]+cap+s[i:]);print('Inserted verified credit')
