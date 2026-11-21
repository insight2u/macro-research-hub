(()=>{'use strict';
const D={"ko": {"heading": "11/21 · 만평", "title": "축하 리본보다 무거운 것", "guest": "가족 캐릭터", "a": "전월 -0.1%, 안정 축하?", "citizen": "가족 캐릭터", "b": "전년 +7.2% 무게는요?", "meaning": "작은 한 달의 하락에 축하 리본을 달아도 일 년 전보다 높은 생산자물가의 무게는 남습니다. 대사와 공장 장면은 편집부의 창작 풍자이며 실제 인물·공장을 묘사한 것이 아닙니다.", "fact": "한국은행 11월 20일 발표: 2026년 10월 생산자물가지수(잠정), 전월 대비 -0.1%, 전년 동월 대비 +7.2%. 소비자물가나 특정 공산품 가격이 아닙니다.", "credit": "11월 21일 기사를 위해 새로 만든 전체 3D 장면입니다.", "source": "한국은행 원문", "article": "관련 기사 01", "archive": "이전 만평 · 11/20", "pause": "움직임 멈추기", "play": "움직임 재생", "open": "장면 원본 보기", "motion": "정지 이미지 만평입니다."}, "en": {"heading": "11/21 · Editorial cartoon", "title": "Heavier than a victory ribbon", "guest": "Family character", "a": "Down 0.1% this month. Celebrate?", "citizen": "Family character", "b": "What about the 7.2% yearly weight?", "meaning": "A tiny monthly fall does not erase the weight of higher producer prices over a year. The dialogue and factory are fictional editorial satire, not a depiction of a real person or factory.", "fact": "Bank of Korea, Nov 20: October 2026 provisional producer price index, -0.1% month on month and +7.2% year on year. These are not consumer prices or prices of a specific industrial product.", "credit": "An entirely new 3D scene created for the November 21 article.", "source": "Bank of Korea source", "article": "Related article 01", "archive": "Previous cartoon · 11/20", "pause": "움직임 멈추기", "play": "움직임 재생", "open": "View original scene", "motion": "A still-image editorial cartoon."}, "ja": {"heading": "11/21 · 風刺漫画", "title": "祝福のリボンより重いもの", "guest": "家族キャラクター", "a": "前月比-0.1%、安定を祝う？", "citizen": "家族キャラクター", "b": "前年比+7.2%の重さは？", "meaning": "わずかな前月比の下落を祝っても、一年前より高い生産者物価の重さは残ります。台詞と工場は創作の風刺で、実在の人物や工場を描いたものではありません。", "fact": "韓国銀行11月20日発表：2026年10月生産者物価指数（暫定）、前月比-0.1%、前年同月比+7.2%。消費者物価や特定の工業製品価格ではありません。", "credit": "11月21日の記事のために新しく作った全体3Dの場面です。", "source": "韓国銀行の原文", "article": "関連記事01", "archive": "前の風刺漫画 · 11/20", "pause": "움직임 멈추기", "play": "움직임 재생", "open": "元の場面を見る", "motion": "静止画の風刺漫画です。"}, "zh": {"heading": "11/21 · 讽刺漫画", "title": "比庆祝彩带更重的东西", "guest": "家庭角色", "a": "环比-0.1%，庆祝稳定？", "citizen": "家庭角色", "b": "同比+7.2%的重量呢？", "meaning": "一个月的小幅下降，并没有抹去生产者价格高于一年前的重量。对白和工厂场景均为编辑部虚构讽刺，并非真实人物或工厂。", "fact": "韩国银行11月20日公布：2026年10月生产者价格指数（初值），环比-0.1%，同比+7.2%。不是消费者价格，也不是某种工业品的价格。", "credit": "为11月21日文章全新制作的完整3D场景。", "source": "韩国银行原文", "article": "相关文章01", "archive": "往期漫画 · 11/20", "pause": "움직임 멈추기", "play": "움직임 재생", "open": "查看原始场景", "motion": "静态讽刺漫画。"}},f=document.getElementById('nr-daily-cartoon');if(!f)return;
const v=f.querySelector('img.nr-cartoon-image'),b=f.querySelector('.nr-cartoon-motion'),a=f.querySelector('.nov20-bubble-a'),c=f.querySelector('.nov20-bubble-b');let L='ko';
const css=document.createElement('style');css.textContent=`
#nr-daily-cartoon{margin:0 0 22px;padding-bottom:18px;border-bottom:1px solid var(--line)}
#nr-daily-cartoon figcaption{font-size:12px;line-height:1.6;color:#685c56;margin-top:10px}
#nr-daily-cartoon figcaption>strong{font-size:14px;color:#251f21}
#nr-daily-cartoon a{color:#215c50}
#nr-daily-cartoon .nr-cartoon-frame{background:#f7f4ef;padding:10px;box-sizing:border-box}
#nr-daily-cartoon .nov20-bubble{position:relative;box-sizing:border-box;margin:0 0 9px;padding:10px 12px;border:1px solid #b9c8c2;border-radius:12px;background:#fff;font-family:Arial,sans-serif;font-size:15px;line-height:1.5;transition:opacity .3s;overflow-wrap:anywhere}
#nr-daily-cartoon .nov20-bubble strong{display:block;font-size:11px;letter-spacing:.02em;color:#215c50}
#nr-daily-cartoon .nov20-bubble span{display:block}
#nr-daily-cartoon .nov20-bubble-b{margin:10px 0 0;background:#eff5f2;min-height:82px}
#nr-daily-cartoon .nov20-bubble-a{min-height:82px}
#nr-daily-cartoon .nov20-bubble-b.waiting{opacity:0}
#nr-daily-cartoon .nov20-motion-note{font-size:11px;color:#685c56;line-height:1.5}
#nr-daily-cartoon .nov20-credit{font-size:11px;color:#685c56}
#nr-daily-cartoon figcaption p{margin:8px 0 0}
@media(max-width:760px){#daily-newsroom .nr-layout{grid-template-columns:minmax(0,1fr)!important}#daily-newsroom .nr-side{min-width:0;max-width:100%}#nr-daily-cartoon .nr-cartoon-frame{padding:10px 18px}#nr-daily-cartoon .nov20-motion-note{padding:0 18px}#nr-daily-cartoon .nov20-bubble{font-size:15px}#nr-daily-cartoon .nov20-bubble-a,#nr-daily-cartoon .nov20-bubble-b{min-height:78px}}
@media(prefers-reduced-motion:reduce){#nr-daily-cartoon .nov20-bubble{transition:none}}
#nr-daily-cartoon .nr-cartoon-image{display:block;width:100%;height:auto;max-width:100%;border:0;border-radius:0}

#nr-daily-cartoon .nr-cartoon-frame{padding:0!important;position:relative;isolation:isolate;overflow:hidden;container-type:inline-size}
#nr-daily-cartoon .nov20-bubble{position:absolute;z-index:2;margin:0!important;min-height:0!important;padding:7px 8px;border:1.5px solid #382b26;border-radius:48% / 28%;background:#fff!important;box-shadow:1px 2px 0 #382b2626;font-size:clamp(10px,3.1cqw,15px)!important;line-height:1.32;overflow:visible;text-align:center;word-break:normal;overflow-wrap:anywhere}
#nr-daily-cartoon .nov20-bubble strong{display:none}
#nr-daily-cartoon[lang=ko] .nov20-bubble{word-break:keep-all;overflow-wrap:normal}
#nr-daily-cartoon .nov20-bubble-a{left:2%;top:4%;width:25%}
#nr-daily-cartoon .nov20-bubble-b{right:2%;top:5%;width:39%}
#nr-daily-cartoon .nov20-bubble:after{content:'';position:absolute;top:calc(100% - 2px);width:15px;height:30px;background:#fff;clip-path:polygon(0 0,100% 0,20% 100%);filter:drop-shadow(1px 1px 0 #382b26);transform-origin:top}
#nr-daily-cartoon .nov20-bubble-a:after{left:53%;transform:rotate(-9deg)}
#nr-daily-cartoon .nov20-bubble-b:after{left:48%;transform:rotate(-6deg)}
`;document.head.append(css);
function text(sel,t){const e=f.querySelector(sel);if(e&&e.textContent!==t)e.textContent=t;}
function sync(){c.classList.remove('waiting');c.setAttribute('aria-hidden','false');}
function apply(){L=document.documentElement.dataset.lang||'ko';if(!D[L])L='en';const q=D[L];f.lang=L;f.dir=L==='ar'?'rtl':'ltr';text('h2',q.heading);text('figcaption>strong',q.title);text('.nov20-bubble-a strong',q.guest);text('.nov20-bubble-a span',q.a);text('.nov20-bubble-b strong',q.citizen);text('.nov20-bubble-b span',q.b);text('.nov20-meaning',q.meaning);text('.nr-cartoon-fact',q.fact);text('.nov20-credit',q.credit);text('.nov20-source',q.source);text('.nov20-related',q.article);text('.nov20-archive',q.archive);text('.nov20-motion-note',q.motion);text('.nov20-original',q.open);v.setAttribute('alt',q.title+' · '+q.a+' '+q.b);sync();}
f.querySelector('.nov20-related').href='#article=report-2026-11-21-01-producer-prices-two-speeds';
new MutationObserver(apply).observe(document.documentElement,{attributes:true,attributeFilter:['data-lang']});
apply();
})();