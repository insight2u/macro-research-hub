#!/usr/bin/env python3
"""Choose one canonical editorial desk from text with a shrinkage LDA score.
Uses an editorial seed feature map and labeled November21/22 articles.
Scores are ranking scores, not calibrated probabilities or proven accuracy.
Author may override only with a recorded content-based reason. Never changes old articles.
Usage: python scripts/classify_article.py --file article.md [--title '...']
"""
from pathlib import Path
import argparse,json,math,re
DESKS={
'경제 체온계':'물가 금리 환율 통계 소비자물가 GDP 성장률 고용 중앙은행 경제지표 기준금리',
'공장장 보고':'반도체 공장 산업 제조 데이터센터 전력 기술 인프라 공급망 설비 GPU 수출통제',
'회장님의 도박판':'기업 경영 인수 합병 지배구조 실적 경영자 전략 의사결정 조직 이사회',
'트렌드人체크카드':'소비 유통 쇼핑 할인 상품 브랜드 직구 가격 반품 블랙프라이데이',
'여의도 한 입, 외교 한 접시':'국회 정치 외교 대통령 정상회담 정부 선거 법안 협상 안보',
'돈 벌러 세계속으로':'세계경제 국제경제 유럽 중국 일본 미국 무역 관세 재정 국제통화',
'라이프人정글':'사회 교육 시험 공정성 복지 건강 의료 노동 학교 청년 생활 안전',
'마이다스의 Z-Tech':'투자 주식 채권 자산 금융 은퇴 가계 저축 대출 배당 소유 재테크',
'도파민성애자':'책 독서 저자 서평 미술 전시 영화 공연 음악 문화 예술 Today’s Book',
'역사로 오늘을 읽다':'역사 고대 신라 백제 당나라 왕조 전투 성곽 대야성 사료 역사적'}
TERMS=list(dict.fromkeys(' '.join(DESKS.values()).split()))
def vec(text,title=''):
 t=(title+' '+title+' '+text).lower();return [min(4,t.count(w.lower()))for w in TERMS]
def fit():
 root=Path(__file__).resolve().parents[1];s=(root/'assets/data/knowledge-items.js').read_text();a=s.index('const reports = ')+len('const reports = ');rows,_=json.JSONDecoder().raw_decode(s[a:]);samples=[]
 for d,words in DESKS.items():samples.append((d,vec(words*2)))
 for r in rows:
  if r.get('date')in ['2026.11.21','2026.11.22'] and r.get('category')in DESKS:samples.append((r['category'],vec(r.get('summary','')+' '+r.get('full_markdown','')[:1400],r['title'])))
 means={d:[sum(v[i]for c,v in samples if c==d)/sum(c==d for c,v in samples)for i in range(len(TERMS))]for d in DESKS}
 var=[sum((v[i]-means[c][i])**2 for c,v in samples)/max(1,len(samples)-len(DESKS))+2.0 for i in range(len(TERMS))]
 return means,var,len(samples)
def classify(text,title=''):
 means,var,n=fit();x=vec(text,title);scores={d:sum(x[i]*m[i]/var[i]-.5*m[i]*m[i]/var[i]for i in range(len(x)))for d,m in means.items()};rank=sorted(scores,key=scores.get,reverse=True)
 # Explicit book and personal-finance cues preserve the owner's fixed desk meanings.
 if re.search(r"today[’']s book|저자 소개|예스24",text+' '+title,re.I):pick='도파민성애자';reason='Book review format has an explicit canonical desk.'
 elif '존리'in text+title and any(w in text+title for w in ['소유','가계','은퇴']):pick='마이다스의 Z-Tech';reason='Household investing and ownership, not corporate strategy.'
 else:pick=rank[0];reason='Highest pooled-diagonal shrinkage LDA ranking score; semantic review required for close scores.'
 return {'category':pick,'reason':reason,'method':'editorial-keyword shrinkage linear discriminant score with canonical format rules','training_examples':n,'ranking':[{'category':d,'score':round(scores[d],3)}for d in rank[:3]],'warning':'Ranking scores are not probabilities; no out-of-sample accuracy claimed.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--file',required=True);p.add_argument('--title',default='');a=p.parse_args();print(json.dumps(classify(Path(a.file).read_text(),a.title),ensure_ascii=False,indent=2))
