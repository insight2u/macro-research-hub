(()=>{'use strict';
const D={"ko": {"heading": "11/22 · 만평", "title": "보고서의 산, 판단의 시간", "a": "보고서는 다 썼어요!", "b": "결정할 근거는요?", "meaning": "분석 자료가 빨리 늘어도 사람의 검토와 책임까지 자동으로 빨라지지는 않습니다. 보고서의 산과 모래시계는 편집부의 창작 풍자이며 실제 기업이나 인물의 발언이 아닙니다.", "fact": "맥킨지 10월15일 기고와 오늘03번 기사를 바탕으로 판단의 병목을 묻습니다. 생산성이나 수익률을 나타낸 통계 그림이 아닙니다.", "credit": "11월22일용으로 새로 만든 전체3D 장면입니다.", "source": "맥킨지 원문", "article": "관련 기사03", "archive": "이전 만평 · 11/21", "pause": "움직임 멈추기", "play": "움직임 재생", "open": "장면 원본 보기", "motion": "16초 무음 반복 동영상. 카메라 이동, 작은 국소 움직임과 모래 효과를 더한 제한 애니메이션입니다.", "guest": "", "citizen": ""}, "en": {"heading": "11/22 · Editorial cartoon", "title": "A mountain of reports, time for judgment", "a": "The reports are done!", "b": "And the grounds for a decision?", "meaning": "Faster analysis does not automatically speed up human review or accountability. The mountain of reports and hourglass are fictional editorial satire, not a real company or a quotation from a real person.", "fact": "Based on McKinsey's October 15 essay and article03 in this issue. This scene is not a chart of productivity or returns.", "credit": "An entirely new 3D scene created for November 22.", "source": "McKinsey source", "article": "Related article 03", "archive": "Previous cartoon · 11/21", "pause": "Pause motion", "play": "Play motion", "open": "View original scene", "motion": "A 16-second silent loop with camera movement, small local movements and falling sand. Limited animation.", "guest": "", "citizen": ""}, "zh": {"heading": "11/22 · 讽刺漫画", "title": "报告的山，判断的时间", "a": "报告都写好了！", "b": "决策的依据呢？", "meaning": "分析资料增多得更快，并不代表人的审阅与责任也会自动加快。报告的山与沙漏是编辑部虚构讽刺，并非真实企业或人物的发言。", "fact": "依据麦肯锡10月15日文章及本期第03篇，追问判断的瓶颈。这不是展示生产率或收益率的统计图。", "credit": "为11月22日全新制作的完整3D场景。", "source": "麦肯锡原文", "article": "相关文章03", "archive": "往期漫画 · 11/21", "pause": "暂停动画", "play": "播放动画", "open": "查看原始场景", "motion": "16秒无声循环视频。镜头移动、局部小动作和落沙效果组成的有限动画。", "guest": "", "citizen": ""}, "ja": {"heading": "11/22 · 風刺漫画", "title": "報告書の山、判断の時間", "a": "報告書は全部できた！", "b": "決めるための根拠は？", "meaning": "分析資料が速く増えても、人の検討と責任まで自動的に速くなるわけではありません。報告書の山と砂時計は編集部の創作風刺で、実在企業や人物の発言ではありません。", "fact": "マッキンゼー10月15日寄稿と今号の記事03をもとに、判断のボトルネックを問います。生産性や収益率を示す統計図ではありません。", "credit": "11月22日のために新しく制作した全体3Dの場面です。", "source": "マッキンゼー原文", "article": "関連記事03", "archive": "前の風刺漫画 · 11/21", "pause": "動きを止める", "play": "動きを再生", "open": "元の場面を見る", "motion": "16秒の無音ループ動画。カメラ移動、局所的な小さな動き、落ちる砂を加えた限定アニメーションです。", "guest": "", "citizen": ""}},f=document.getElementById('nr-daily-cartoon');if(!f)return;
const v=f.querySelector('.nr-cartoon-image'),b=f.querySelector('.nr-cartoon-motion'),a=f.querySelector('.nov20-bubble-a'),c=f.querySelector('.nov20-bubble-b');let L='ko';
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
#nr-daily-cartoon .nov20-bubble-a{left:2%;top:3%;width:39%}
#nr-daily-cartoon .nov20-bubble-b{right:2%;top:auto;bottom:4%;width:43%}
#nr-daily-cartoon .nov20-bubble:after{content:'';position:absolute;top:calc(100% - 2px);width:15px;height:30px;background:#fff;clip-path:polygon(0 0,100% 0,20% 100%);filter:drop-shadow(1px 1px 0 #382b26);transform-origin:top}
#nr-daily-cartoon .nov20-bubble-a:after{left:53%;transform:rotate(-9deg)}
#nr-daily-cartoon .nov20-bubble-b:after{left:24%;top:auto;bottom:calc(100% - 2px);transform:rotate(174deg)}
#nr-daily-cartoon .nr-cartoon-motion{min-height:44px;padding:10px 4px;cursor:pointer}
#nr-daily-cartoon .nov20-original{display:inline-block;min-height:44px;line-height:44px}
`;document.head.append(css);
function text(sel,t){const e=f.querySelector(sel);if(e&&e.textContent!==t)e.textContent=t;}
function sync(){c.classList.remove('waiting');c.setAttribute('aria-hidden','false');}
function apply(){L=document.documentElement.dataset.lang||'ko';if(!D[L])L='en';const q=D[L];f.lang=L;f.dir=L==='ar'?'rtl':'ltr';text('h2',q.heading);text('figcaption>strong',q.title);text('.nov20-bubble-a strong',q.guest);text('.nov20-bubble-a span',q.a);text('.nov20-bubble-b strong',q.citizen);text('.nov20-bubble-b span',q.b);text('.nov20-meaning',q.meaning);text('.nr-cartoon-fact',q.fact);text('.nov20-credit',q.credit);text('.nov20-source',q.source);text('.nov20-related',q.article);text('.nov20-archive',q.archive);text('.nov20-motion-note',q.motion);text('.nov20-original',q.open);v.setAttribute('aria-label',q.title+' · '+q.a+' '+q.b);if(b)b.textContent=v.paused?q.play:q.pause;sync();}
f.querySelector('.nov20-related').href='#article=report-2026-11-22-03-ai-strategy-judgment-capacity';
if(b)b.addEventListener('click',()=>{if(v.paused)v.play().catch(()=>{});else v.pause();apply();});v.addEventListener('play',()=>{if(b)b.textContent=D[L].pause;});v.addEventListener('pause',()=>{if(b)b.textContent=D[L].play;});v.muted=true;if(matchMedia('(prefers-reduced-motion: reduce)').matches)v.pause();else v.play().catch(()=>{});
new MutationObserver(apply).observe(document.documentElement,{attributes:true,attributeFilter:['data-lang']});
apply();
})();