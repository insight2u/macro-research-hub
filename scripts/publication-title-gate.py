#!/usr/bin/env python3
"""Fail publication when an unreviewed private-title token appears in tracked text."""
from pathlib import Path
import subprocess,json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
TOKEN='\uc758\uc7a5'
BASE=ROOT/'scripts/publication-title-baseline.json'
allowed=json.loads(BASE.read_text())
failed=[];total=0
for name in subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines():
 p=ROOT/name
 if p.suffix not in {'.html','.js','.json','.md','.txt','.xml','.svg','.csv'} or name.startswith('scripts/') or not p.is_file():continue
 try:s=p.read_text()
 except UnicodeError:continue
 hits=[hashlib.sha256(s[max(0,m.start()-24):m.end()+24].encode()).hexdigest() for m in re.finditer(TOKEN,s)]
 total+=len(hits)
 old=list(allowed.get(name,[]))
 for h in hits:
  if h in old:old.remove(h)
  else:failed.append(name)
if failed:
 print('STOP: unreviewed title-token context in '+', '.join(sorted(set(failed))));sys.exit(1)
print(f'PASS: {total} existing third-party/compound contexts match the reviewed baseline; no new title-token contexts.')
