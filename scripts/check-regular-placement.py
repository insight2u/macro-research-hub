from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
s=(R/'index.html').read_text()
assert not re.search(r'<(?:section|article)[^>]+id=[\"\x27]ktng-feature',s),'Regular news must not be a standalone lead feature'
assert 'id="nr-article-grid"' in s and 'id="nr-recent"' in s
rows=json.loads((R/'assets/data/section-catalog.json').read_text())['rows']
r=next(x for x in rows if x['id']=='report-2026-11-26-housing-integrated')
assert r['date']=='2026.11.26','Housing regular report must remain in today article date set'
assert 'housing-integrated-20261126.html' in r['urls']['ko']
print('Regular placement checks passed')
