(function(){
'use strict';
const source=/^(?:출처(?:와.*| 목록)?|확인 자료|보완 출처|참조 범위|평론과 참조 범위|공식 영상·음원과 확인 자료|Sources?(?: vérifiées?| and Scope of Verification| and reading scope)?|References|Official video, audio and sources|出典.*|参考資料.*|参考范围|影评与参考范围|視聴と確認範囲|参考资料.*|確認資料.*|核实资料.*|核實資料.*|查证资料.*|查證資料.*|来源.*|参考来源.*|參考來源.*|出处|公式映像・音源と確認資料|官方影像、音源与核对资料|Fuentes?(?: consultadas?)?|Источники.*|Проверенный источник|Проверенные источники|المصادر.*|المصدر.*|Vyanzo(?: vilivyohakikiwa)?|Chanzo kilichohakikiwa|(?:Geprüfte )?Quellen?|Fonti(?: verificate)?|Fonte verificata)$/i;
const speech=/낭독\s*원고|낭독용|방송용 원고|^(?:Read.aloud|Narration|Reading) script$|^朗[读読]原稿$/i;
let timer;
function normalize(){
const a=document.getElementById('ar-article');if(!a)return;
let end=a.querySelector(':scope > .article-sources-end');
const headings=[...a.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(h=>!h.closest('.article-sources-end'));
for(const h of headings){const text=h.textContent.trim(),isSource=source.test(text);if(!isSource&&!speech.test(text))continue;
const level=+h.tagName[1];let node=h,block=[];
while(node){if(node!==h&&((/^H[1-6]$/.test(node.nodeName)&&+node.nodeName[1]<=level)||/^(ASIDE|NAV|SECTION)$/.test(node.nodeName)))break;block.push(node);node=node.nextSibling;}
if(isSource){if(!end){end=document.createElement('section');end.className='article-sources-end';end.setAttribute('aria-label','Sources');}for(const n of block)end.append(n);}else for(const n of block)n.remove();}
for(const p of [...a.querySelectorAll('p')]){const text=p.textContent;if(/아래 낭독 원고는/.test(text))p.textContent=text.replace(/\s*아래 낭독 원고는 읽기용이며 새 팟캐스트 오디오를 발행했다는 뜻은 아닙니다\./,'');}
if(end&&a.lastElementChild!==end)a.append(end);
}
function queue(){clearTimeout(timer);timer=setTimeout(normalize,0);}
document.addEventListener('DOMContentLoaded',()=>{const a=document.getElementById('ar-article');if(a)new MutationObserver(queue).observe(a,{childList:true,subtree:true});normalize();});
window.addEventListener('dailyshot:reader-rendered',queue);
})();
