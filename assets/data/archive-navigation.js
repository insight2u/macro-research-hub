(()=>{
'use strict';
const labels={
ko:['전문 읽기','기사 직접 링크 ↗','일치하는 기사가 없습니다. 다른 검색어나 분야를 선택해 주세요.','기사 더 보기','모든 분야','제목·본문 검색','오늘 수정판부터 기존 기사 전문까지. 제목·본문을 검색하세요. 오래된 글은 당시 기준이며 현재 사실로 자동 갱신되지 않습니다.','한국어 원문'],
en:['Read full article','Direct article link ↗','No matching articles. Try another term or field.','More articles','All fields','Search titles and text','Search current and archived articles. Older articles reflect their publication date and are not automatically updated.','Korean original'],
ja:['全文を読む','記事の直接リンク ↗','該当する記事がありません。検索語や分野を変えてください。','さらに表示','すべての分野','見出し・本文を検索','最新記事と過去の記事を検索できます。過去の記事は発行当時の内容で、自動更新されません。','韓国語原文'],
zh:['阅读全文','文章直接链接 ↗','没有匹配的文章。请尝试其他关键词或领域。','更多文章','所有领域','搜索标题和正文','搜索最新及历史文章。旧文章反映发表时的情况，不会自动更新。','韩语原文'],
es:['Leer artículo completo','Enlace directo al artículo ↗','No hay artículos coincidentes. Pruebe otro término o tema.','Más artículos','Todos los temas','Buscar en títulos y texto','Busque artículos actuales y del archivo. Los antiguos reflejan la fecha de publicación y no se actualizan automáticamente.','Original en coreano'],
ru:['Читать полностью','Прямая ссылка на статью ↗','Совпадений нет. Попробуйте другое слово или раздел.','Ещё статьи','Все разделы','Поиск по заголовкам и тексту','Поиск новых и архивных статей. Старые материалы отражают дату публикации и не обновляются автоматически.','Корейский оригинал'],
ar:['قراءة المقال كاملاً','رابط مباشر للمقال ↗','لا توجد مقالات مطابقة. جرّب كلمة أو مجالاً آخر.','المزيد من المقالات','جميع المجالات','البحث في العناوين والنصوص','ابحث في المقالات الحالية والأرشيف. تعكس المقالات القديمة وقت نشرها ولا تُحدّث تلقائيًا.','الأصل الكوري'],
sw:['Soma makala yote','Kiungo cha moja kwa moja ↗','Hakuna makala zinazolingana. Jaribu neno au mada nyingine.','Makala zaidi','Mada zote','Tafuta vichwa na maandishi','Tafuta makala za sasa na za zamani. Makala za zamani zinaonyesha hali wakati wa kuchapishwa, hazisasishwi kiotomatiki.','Asili ya Kikorea'],
fr:["Lire l'article","Lien direct vers l'article ↗","Aucun article correspondant. Essayez un autre terme ou thème.","Plus d'articles","Tous les thèmes","Rechercher dans les titres et le texte","Recherchez les articles récents et archivés. Les anciens reflètent leur date de publication et ne sont pas actualisés automatiquement.","Original coréen"],
de:['Vollständigen Artikel lesen','Direktlink zum Artikel ↗','Keine passenden Artikel. Versuchen Sie einen anderen Begriff oder Bereich.','Weitere Artikel','Alle Bereiche','Titel und Text durchsuchen','Aktuelle und archivierte Artikel durchsuchen. Ältere Artikel entsprechen dem Stand der Veröffentlichung und werden nicht automatisch aktualisiert.','Koreanisches Original'],
it:["Leggi l'articolo completo","Link diretto all'articolo ↗","Nessun articolo trovato. Prova un altro termine o argomento.","Altri articoli","Tutti gli argomenti","Cerca nei titoli e nel testo","Cerca articoli attuali e di archivio. Quelli precedenti riflettono la data di pubblicazione e non si aggiornano automaticamente.","Originale coreano"]
};
const lang=()=>document.documentElement.dataset.lang||'ko',list=()=>labels[lang()]||labels.en;
window.magazineArchiveLabel=k=>list()[{read:0,direct:1,empty:2}[k]];
// BEGIN NOV22 CATEGORY LABELS
const nov22CategoryLabels={"en": {"경제 체온계": "Economy Thermometer", "공장장 보고": "Factory Manager's Report", "회장님의 도박판": "The Chairman's Gamble", "트렌드人체크카드": "Trend Check Card", "여의도 한 입, 외교 한 접시": "A Bite of Yeouido, a Plate of Diplomacy", "돈 벌러 세계속으로": "Into the World to Make Money", "라이프人정글": "Life in the Human Jungle", "마이다스의 Z-Tech": "Midas's Z-Tech", "도파민성애자": "Dopamine Lovers", "역사로 오늘을 읽다": "Reading Today Through History"}, "zh": {"경제 체온계": "经济体温计", "공장장 보고": "厂长报告", "회장님의 도박판": "董事长的赌局", "트렌드人체크카드": "趋势人消费卡", "여의도 한 입, 외교 한 접시": "汝矣岛一口，外交一盘", "돈 벌러 세계속으로": "到世界去赚钱", "라이프人정글": "生活丛林", "마이다스의 Z-Tech": "迈达斯的Z-Tech", "도파민성애자": "多巴胺爱好者", "역사로 오늘을 읽다": "用历史读今天"}, "ja": {"경제 체온계": "経済の体温計", "공장장 보고": "工場長レポート", "회장님의 도박판": "会長の賭け", "트렌드人체크카드": "トレンド人チェックカード", "여의도 한 입, 외교 한 접시": "汝矣島を一口、外交を一皿", "돈 벌러 세계속으로": "世界へ稼ぎに行こう", "라이프人정글": "暮らしのジャングル", "마이다스의 Z-Tech": "ミダスのZ-Tech", "도파민성애자": "ドーパミン愛好家", "역사로 오늘을 읽다": "歴史で今日を読む"}};
// END NOV22 CATEGORY LABELS
function record(r){
 const md=((window.BODY_I18N||{})[r.id]||{})[lang()];
 if(lang()==='ko')return r;
 if(!md)return {title:r.title+' ['+list()[7]+']',summary:r.summary,category:((nov22CategoryLabels[lang()]||{})[r.category]||r.category)+' ['+list()[7]+']'};
 const lines=md.split('\n');const title=(r.id==='report-2026-11-22-12-todays-book'?"Today's Book · "+(lines.find(t=>/^##\s/.test(t))||'').replace(/^##\s+/,''):(lines.find(t=>/^#\s/.test(t))||'').replace(/^#\s+/,''))||r.title;
 const prose=lines.find(t=>t.trim()&&!/^(Cover source:|封面来源|表紙出典)/.test(t)&&!/^(#|\*|!|\[|<|\||-|출처)/.test(t)&&t.trim().length>70)||'';
 return {title:title.replace(/\*([^*]+)\*/g,'$1'),category:(nov22CategoryLabels[lang()]||{})[r.category]|| (r.date==='2026.11.21'?r.category:(title.includes('|')?title.split('|')[0].trim():title.split('｜')[0].trim())),summary:prose.length>330?prose.slice(0,330)+'…':prose};
}
window.magazineArchiveRecord=record;
window.magazineArchiveText=r=>{const md=((window.BODY_I18N||{})[r.id]||{})[lang()]||'';return [record(r).title,md].join(' ').normalize('NFKC').toLocaleLowerCase();};
window.magazineArchiveCount=(total,n,search)=>{
 const l=lang();return ({ko:`${total}개 기사 중 ${n}개${search?' 검색 결과':''}`,en:`${n} of ${total} articles${search?' match':''}`,ja:`全${total}件中${n}件${search?'が一致':''}`,zh:`共${total}篇，${n}篇${search?'匹配':''}`,es:`${n} de ${total} artículos${search?' coinciden':''}`,ru:`${n} из ${total} статей${search?' найдено':''}`,ar:`${n} من ${total} مقالًا${search?' مطابقًا':''}`,sw:`Makala ${n} kati ya ${total}${search?' zinalingana':''}`,fr:`${n} articles sur ${total}${search?' correspondent':''}`,de:`${n} von ${total} Artikeln${search?' gefunden':''}`,it:`${n} articoli su ${total}${search?' corrispondono':''}`})[l]||`${n} / ${total}`;
};
function dailyEdition(){
 const l=lang(),all=typeof reports!=='undefined'?reports:[],eligible=all.filter(r=>/^report-\d{4}-\d{2}-\d{2}-\d{2,}-/.test(r.id)&&(l==='ko'||((window.BODY_I18N||{})[r.id]||{})[l]));
 const dates=[...new Set(eligible.map(r=>r.date))].sort().reverse();
 const date=dates.find(d=>eligible.filter(r=>r.date===d).length>=10);if(!date)return;
 const selected=eligible.filter(r=>r.date===date).sort((a,b)=>a.id.localeCompare(b.id)),grid=document.getElementById('nr-article-grid');if(!grid)return;
 const signature=l+':'+date+':'+selected.map(r=>r.id).join(',');if(grid.dataset.editionSignature===signature)return;grid.dataset.editionSignature=signature;grid.replaceChildren();
 const heading=document.querySelector('#nr-recent h2'),stamp=document.querySelector('#nr-recent small');
 const titles={ko:'오늘의 기사',en:'Latest articles',ja:'今日の記事',zh:'今日文章',es:'Última edición · Top 10',ru:'Последний выпуск · Топ-10',ar:'أحدث إصدار · أهم 10',sw:'Toleo la karibuni · 10 bora',fr:'Dernière édition · Top 10',de:'Neueste Ausgabe · Top 10',it:'Ultima edizione · Top 10'};
 if(heading)heading.textContent=titles[l]||titles.en;if(stamp)stamp.textContent=date;
 selected.forEach(r=>{const local=record(r),a=document.createElement('article');a.className='nr-card';a.dataset.articleId=r.id;const k=document.createElement('b');k.textContent=local.category+' · '+r.date;const h=document.createElement('h3');h.textContent=r.date==='2026.11.21'?local.title.replace(/^[^|]+\|\s*/,''):local.title;h.style.cursor='pointer';const p=document.createElement('p');p.textContent=local.summary;const b=document.createElement('button');b.className='nr-read';b.textContent=list()[0]+' →';const open=()=>window.newspaperArchive?.openArticle(r.id);h.onclick=open;p.onclick=open;b.onclick=open;a.append(k,h,p,b);grid.append(a)});
}
window.magazineArchiveRefresh=()=>{
 dailyEdition();
 const v=list();for(const [id,index] of [['ar-top',6],['ar-more',3]]){const e=document.getElementById(id);if(e)e.textContent=v[index];}
 const q=document.getElementById('ar-query');if(q){q.placeholder=v[5];q.setAttribute('aria-label',v[5]);}
 const category=document.getElementById('ar-category');if(category){category.options[0].textContent=v[4];const rr=typeof reports!=='undefined'?reports:[];for(const op of [...category.options].slice(1)){const r=rr.find(r=>r.category===op.value&&((window.BODY_I18N||{})[r.id]||{})[lang()]);op.textContent=lang()==='ko'?op.value:r?record(r).category:op.value+' ['+v[7]+']';}}
 if(window.newspaperArchive)window.newspaperArchive.search();
 document.querySelectorAll('.ar-direct-link').forEach(a=>{const u=new URL(a.href);u.searchParams.set('lang',lang());a.href=u.href;});
};
window.addEventListener('dailyshot:reader-rendered',()=>setTimeout(()=>{document.querySelectorAll('.ar-direct-link').forEach(a=>{const u=new URL(a.href);u.searchParams.set('lang',lang());a.href=u.href;});},0));
})();
