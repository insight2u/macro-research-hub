# -*- coding: utf-8 -*-
"""Insert 8-language localization (lang bar, UI dictionary, themes, music, RTL) into index.html."""
import json, re, sys, os

SRC = 'index.html'
src = open(SRC, encoding='utf-8').read()

# ---------------- translation keys: {korean: {lang: text}} ----------------
K = {}
def add(ko, en, zh, ja, es, ru, ar, sw):
    K[ko] = {'en': en, 'zh': zh, 'ja': ja, 'es': es, 'ru': ru, 'ar': ar, 'sw': sw}

# nav
add("기사 검색","Article Search","文章搜索","記事検索","Buscar artículos","Поиск статей","البحث في المقالات","Tafuta makala")
add("오늘 기사","Today's Articles","今日文章","今日の記事","Artículos de hoy","Статьи дня","مقالات اليوم","Makala ya leo")
add("10대 코너","Ten Desks","十大栏目","10のコーナー","Diez secciones","10 рубрик","عشرة أقسام","Sehemu kumi")
add("지식·통계 DB","Knowledge & Stats DB","知识·统计数据库","知識・統計DB","Conocimiento y datos","БД знаний и статистики","قاعدة المعرفة والإحصاءات","Maarifa na takwimu")
add("영화·음악","Film & Music","电影·音乐","映画・音楽","Cine y música","Кино и музыка","سينما وموسيقى","Filamu na muziki")
add("전문도서","Books","专业图书","専門書","Libros","Книги","كتب","Vitabu")
add("인문·철학","Humanities & Philosophy","人文·哲学","人文・哲学","Humanidades y filosofía","Гуманитарные науки и философия","إنسانيات وفلسفة","Jamii na falsafa")
add("만평","Cartoons","漫画评论","風刺漫画","Viñetas","Карикатуры","كاريكاتير","Vibonzo")
add("홈페이지 맵","Site Map","网站地图","サイトマップ","Mapa del sitio","Карта сайта","خريطة الموقع","Ramani ya tovuti")
add("YouTube 구독 ↗","Subscribe on YouTube ↗","订阅 YouTube ↗","YouTube 登録 ↗","Suscribirse en YouTube ↗","Подписка на YouTube ↗","اشترك في يوتيوب ↗","Jiandikishe YouTube ↗")
add("Spotify 팔로우 ↗","Follow on Spotify ↗","关注 Spotify ↗","Spotify フォロー ↗","Seguir en Spotify ↗","Слушать на Spotify ↗","تابع على سبوتيفاي ↗","Fuata Spotify ↗")
add("팟캐스트 듣기 ↗","Listen to the Podcast ↗","收听播客 ↗","ポッドキャスト ↗","Escuchar el pódcast ↗","Слушать подкаст ↗","استمع إلى البودكاست ↗","Sikiliza podikasti ↗")
add("개인 페이스북 ↗","Personal Facebook ↗","个人 Facebook ↗","個人 Facebook ↗","Facebook personal ↗","Личный Facebook ↗","فيسبوك شخصي ↗","Facebook binafsi ↗")
# headings
add("같은 제목으로 보고 들으세요","Read and Listen by Title","按标题阅读收听","同じタイトルで読む・聴く","Lea y escuche por título","Читайте и слушайте по заголовку","اقرأ واستمع بالعنوان نفسه","Soma na sikiliza kwa kichwa")
add("오늘의 기사 10","Today's Top 10","今日十文","今日の記事 10選","Los 10 artículos de hoy","10 статей дня","أهم 10 مقالات اليوم","Makala 10 bora ya leo")
add("THE TEN DESKS · 10대 코너","THE TEN DESKS","THE TEN DESKS · 十大栏目","THE TEN DESKS · 10のコーナー","THE TEN DESKS · Diez secciones","THE TEN DESKS · 10 рубрик","THE TEN DESKS · عشرة أقسام","THE TEN DESKS · Sehemu kumi")
add("기사 검색 · 아카이브","Search · Archive","文章搜索·存档","記事検索・アーカイブ","Búsqueda · Archivo","Поиск · Архив","البحث · الأرشيف","Tafuta · Kumbukumbu")
# search inputs
add("제목·본문 검색","Search title & body","搜索标题和正文","タイトル・本文を検索","Buscar título y texto","Поиск по заголовку и тексту","ابحث في العنوان والنص","Tafuta kichwa na mwili")
add("기사 검색어 입력","Enter search terms","输入搜索词","検索語を入力","Escriba su búsqueda","Введите запрос","أدخل كلمة البحث","Weka neno la kutafuta")
add("기사 제목과 본문 검색","Search article titles and body","搜索文章标题和正文","記事のタイトルと本文を検索","Buscar en títulos y texto","Поиск по заголовкам и тексту статей","البحث في عناوين المقالات ونصوصها","Tafuta vichwa na mwili wa makala")
add("기사 제목·본문 검색","Search article title & body","搜索文章标题·正文","記事タイトル・本文検索","Buscar título y texto del artículo","Поиск по заголовку и тексту статьи","البحث في عنوان المقال ونصه","Tafuta kichwa na mwili wa makala")
# buttons / misc
add("움직임 멈춤","Pause motion","停止动画","動きを停止","Pausar movimiento","Остановить движение","إيقاف الحركة","Simamisha mwendo")
add("움직임 재생","Resume motion","播放动画","動きを再生","Reanudar movimiento","Возобновить движение","تشغيل الحركة","Endeleza mwendo")
add("전체 기사 검색 ↗","Search all articles ↗","搜索全部文章 ↗","全記事を検索 ↗","Buscar todos los artículos ↗","Искать во всех статьях ↗","ابحث في كل المقالات ↗","Tafuta makala yote ↗")
add("👤 연구소장 프로필 보기 ▾","👤 Director's Profile ▾","👤 所长简介 ▾","👤 所長プロフィール ▾","👤 Perfil del director ▾","👤 Профиль директора ▾","👤 ملف المدير ▾","👤 Wasifu wa mkurugenzi ▾")
add("🎵 10초 음악 하이라이트 모드","🎵 10-second music highlights","🎵 10秒音乐精选","🎵 10秒音楽ハイライト","🎵 Lo mejor de la música en 10 s","🎵 Музыка: 10-секундные фрагменты","🎵 مقتطفات موسيقية 10 ثوانٍ","🎵 Mwanga wa muziki wa sekunde 10")
add("보고서 전문 열기 (Quick Read) >","Open full report (Quick Read) >","打开报告全文 (Quick Read) >","レポート全文を開く (Quick Read) >","Abrir informe completo (Quick Read) >","Открыть отчёт полностью (Quick Read) >","افتح التقرير الكامل (قراءة سريعة) >","Fungua ripoti kamili (usomaji wa haraka) >")
add("전문 읽기","Read full text","阅读全文","全文を読む","Leer texto completo","Читать полностью","اقرأ النص الكامل","Soma maandishi kamili")
add("🔍 원본 고화질 확대","🔍 View full-resolution","🔍 查看高清原图","🔍 高画質で拡大","🔍 Ampliar en alta resolución","🔍 Увеличить оригинал","🔍 تكبير بجودة عالية","🔍 Ongeza picha kamili")
add("기사 전문 읽기","Read the full article","阅读文章全文","記事全文を読む","Leer el artículo completo","Читать статью целиком","اقرأ المقال كاملاً","Soma makala kamili")
add("데일리샷 매크로 리서치 · RYUYOUNGSUN","DailyShot Macro Research · RYUYOUNGSUN","每日宏观研究 · RYUYOUNGSUN","デイリーショット・マクロリサーチ · RYUYOUNGSUN","DailyShot Macro Research · RYUYOUNGSUN","DailyShot Macro Research · RYUYOUNGSUN","ديلي شوت لأبحاث الاقتصاد الكلي · RYUYOUNGSUN","DailyShot Macro Research · RYUYOUNGSUN")
add("동작 멈추기","Stop motion","停止动画","モーション停止","Detener movimiento","Остановить анимацию","أوقف الحركة","Simamisha mwendo")
add("국제 뉴스룸","World Newsroom","国际新闻室","国際ニュースルーム","Sala de prensa internacional","Международные новости","غرفة الأخبار الدولية","Chumba cha habari za kimataifa")
add("방송 제어 · 출처","Broadcast controls · Sources","播放控制·来源","放送コントロール・出典","Controles · Fuentes","Управление · Источники","التحكم في البث · المصادر","Udhibiti wa matangazo · Vyanzo")
add("아침판","Morning Edition","早间版","朝刊","Edición de la mañana","Утренний выпуск","الطبعة الصباحية","Toleo la asubuhi")
add("닫기","Close","关闭","閉じる","Cerrar","Закрыть","إغلاق","Funga")
add("닫기 ×","Close ×","关闭 ×","閉じる ×","Cerrar ×","Закрыть ×","إغلاق ×","Funga ×")
add("이 기사 직접 링크 ↗","Direct link to this article ↗","本文直接链接 ↗","この記事の直接リンク ↗","Enlace directo a este artículo ↗","Прямая ссылка на статью ↗","رابط مباشر لهذا المقال ↗","Kiungo cha moja kwa moja cha makala hii ↗")
add("부제","Subtitle","副题","サブタイトル","Subtítulo","Подзаголовок","العنوان الفرعي","Kichwa kidogo")
add("주요뉴스 다시보기","Replay top news","重播要闻","主要ニュース再視聴","Repetir noticias destacadas","Повтор главных новостей","إعادة أهم الأخبار","Tazama tena habari kuu")
add("기준일별 지표","Indicators by reference date","按基准日指标","基準日別指標","Indicadores por fecha de referencia","Показатели по дате","مؤشرات حسب تاريخ المرجع","Viashiria kwa tarehe")
add("자동 실시간 아님","Not live/auto","非自动实时","自動リアルタイムではありません","No es en vivo automático","Не в реальном времени","ليس مباشراً تلقائياً","Si moja kwa moja")
add("리포트 제목","Report title","报告标题","レポートタイトル","Título del informe","Название отчёта","عنوان التقرير","Kichwa cha ripoti")
# desks (new + legacy aliases)
add("오늘의 경제 체온계","Today's Economy Thermometer","今日经济体温计","今日の経済体温計","Termómetro económico de hoy","Экономический термометр дня","مقياس حرارة الاقتصاد اليوم","Kipima joto cha uchumi cha leo")
add("오늘의 멀미 지수","Today's Economy Thermometer","今日经济体温计","今日の経済体温計","Termómetro económico de hoy","Экономический термометр дня","مقياس حرارة الاقتصاد اليوم","Kipima joto cha uchumi cha leo")
add("공장장 보고 드립니다","Factory Manager's Report","厂长报告","工場長の報告","Informe del jefe de fábrica","Доклад директора завода","تقرير مدير المصنع","Ripoti ya meneja wa kiwanda")
add("불 안 꺼지는 공장","Factory Manager's Report","厂长报告","工場長の報告","Informe del jefe de fábrica","Доклад директора завода","تقرير مدير المصنع","Ripoti ya meneja wa kiwanda")
add("회장님의 도박판","The Chairman's Gambling Table","会长的赌桌","会長の賭け場","La mesa de apuestas del presidente","Игорный стол председателя","طاولة قمار الرئيس","Meza ya kamari ya mwenyekiti")
add("트렌드人CheckCard","Trend人CheckCard","趋势人CheckCard","トレンド人CheckCard","Tendencia人CheckCard","Тренд人CheckCard","اتجاه人CheckCard","Trendi人CheckCard")
add("글로벌이코노믹뉴스(국제경제)","Global Economic News (International Economy)","全球经济新闻(国际经济)","グローバル経済ニュース(国際経済)","Noticias económicas globales (Economía internacional)","Глобальные экономические новости (Международная экономика)","أخبار الاقتصاد العالمي (الاقتصاد الدولي)","Habari za uchumi wa dunia (Uchumi wa kimataifa)")
add("라이프人정글(사회)","Life人Jungle (Society)","生活人丛林(社会)","ライフ人ジャングル(社会)","Vida人Jungla (Sociedad)","Жизнь人Джунгли (Общество)","حياة人الغابة (المجتمع)","Maisha人Msitu (Jamii)")
add("역사·정치지리","History & Political Geography","历史·政治地理","歴史・政治地理","Historia y geografía política","История и политическая география","التاريخ والجغرافيا السياسية","Historia na jiografia ya kisiasa")
add("(기업)","(Business)","(企业)","(企業)","(Empresas)","(Компании)","(الشركات)","(Makampuni)")
add("(문화)","(Culture)","(文化)","(文化)","(Cultura)","(Культура)","(الثقافة)","(Utamaduni)")
add("마이다스의 Z-Tech", "Midas's Z-Tech", "迈达斯的Z-Tech", "マイダスのZ-Tech", "Z-Tech de Midas", "Z-Tech Мидаса", "Z-Tech ميداس", "Z-Tech ya Midasi")
add("계산대 앞 3초","3 Seconds at the Register","收银台前三秒","レジ前3秒","3 segundos en la caja","3 секунды у кассы","3 ثوانٍ عند الصندوق","Sekunde 3 mbele ya kasha")
add("여의도 한 입, 외교 한 접시","A Bite of Yeouido, a Plate of Diplomacy","汝矣岛一口，外交一盘","汝矣島ひと口、外交ひと皿","Un bocado de Yeouido, un plato de diplomacia","Кусочек Йоидо, блюдо дипломатии","قضمة من يويدو وطبق من الدبلوماسية","Kijiko cha Yeouido, sahani ya diplomasia")
add("엄마찾아삼만리","Finding Mom Across 30,000 Li","万里寻母记","母をたずねて三千里","En busca de mamá, 30.000 li","В поисках мамы за 30 000 ли","البحث عن أمي عبر 30 ألف لي","Kumtafuta mama maili 30,000")
add("공항 전광판","Finding Mom Across 30,000 Li","万里寻母记","母をたずねて三千里","En busca de mamá, 30.000 li","В поисках мамы за 30 000 ли","البحث عن أمي عبر 30 ألف لي","Kumtafuta mama maili 30,000")
add("오늘의 반상회","Today's Neighborhood Meeting","今日班常会","今日の町内会","La reunión vecinal de hoy","Сегодняшний сход жильцов","مجلس الحي اليوم","Baraza la mtaa la leo")
add("월급이 퇴근했습니다","The Paycheck Has Left the Office","工资已下班","給料は退勤しました","El sueldo ya salió del trabajo","Зарплата ушла с работы","الراتب غادر الدوام","Mshahara ameondoka kazini")
add("도파민 배달왔습니다","Dopamine Delivered","多巴胺已送达","ドーパミン配達完了","Dopamina entregada","Дофамин доставлен","تم توصيل الدوبامين","Dopamine imefika")
add("타임머신 택배기사","Time-Machine Courier","时光机快递员","タイムマシン配達員","Mensajero de la máquina del tiempo","Курьер машины времени","ساعي آلة الزمن","Msafirishaji wa mashine ya wakati")
# desk taglines
add("물가·금리·환율·고용·소비까지","Prices, rates, FX, jobs and spending","物价·利率·汇率·就业·消费","物価・金利・為替・雇用・消費まで","Precios, tipos, divisas, empleo y consumo","Цены, ставки, курсы, занятость, потребление","الأسعار والفائدة والصرف والوظائف والاستهلاك","Bei, viwango, ubadilishaji, ajira na matumizi")
add("굴뚝도 칩도 수다 중","Chimneys and chips are talking","烟囱和芯片都在聊天","煙突もチップもおしゃべり中","Chimeneas y chips, de charla","Трубы и чипы разговаривают","المداخن والرقائق تتحدث","Michirizi na chipsi vinaongea")
add("장부가 열렸습니다","The ledger is open","账本已打开","帳簿が開かれました","El libro mayor está abierto","Книга учёта открыта","الدفاتر مفتوحة","Daftari limefunguliwa")
add("가격표가 수상합니다","That price tag looks suspicious","价格标签很可疑","値札があやしい","La etiqueta del precio es sospechosa","Ценник выглядит подозрительно","بطاقة السعر مثيرة للريبة","Lebo ya bei ina shaka")
add("국회에서 세계지도까지","From the Assembly to the world map","从国会到世界地图","国会から世界地図まで","Del parlamento al mapa mundial","От парламента до карты мира","من البرلمان إلى خريطة العالم","Kutoka bungeni hadi ramani ya dunia")
add("여권 없이 세계일주","Around the world without a passport","无护照环游世界","パスポートなしで世界一周","La vuelta al mundo sin pasaporte","Вокруг света без паспорта","حول العالم بلا جواز سفر","Kuzunguka dunia bila pasipoti")
add("반장님 알림장","The monitor's notice board","班长通知栏","学級委員のお知らせ帳","El tablón del delegado","Доска объявлений старосты","لوحة إعلانات ممثل الصف","Ubao wa matangazo wa kiranja")
add("통장 탈출 대작전","The great bank-account escape","存折大逃亡","通帳脱出大作戦","La gran fuga de la cuenta bancaria","Великий побег со счёта","عملية الهروب الكبرى من الحساب البنكي","Operesheni kubwa ya kutoroka akaunti")
add("감성 과적 주의보","Emotional overload advisory","感性过载警报","感性オーバーロード注意報","Alerta de sobrecarga emocional","Предупреждение: эмоциональная перегрузка","تحذير من زخم عاطفي زائد","Tahadhari ya mzigo wa hisia")
add("어제가 도착했습니다","Yesterday has arrived","昨天已送达","昨日が届きました","Ayer ha llegado","Вчерашний день доставлен","وصل أمس","Jana imefika")
# desk category tags
add("경제지표","Economic indicators","经济指标","経済指標","Indicadores económicos","Экономические индикаторы","مؤشرات اقتصادية","Viashiria vya uchumi")
add("산업·ICT","Industry & ICT","产业·ICT","産業・ICT","Industria y TIC","Промышленность и ICT","الصناعة وتقنية المعلومات","Viwanda na ICT")
add("기업","Business","企业","企業","Empresas","Компании","الشركات","Makampuni")
add("소비·유통","Consumer & Retail","消费·流通","消費・流通","Consumo y distribución","Потребление и ритейл","الاستهلاك والتوزيع","Matumizi na usambazaji")
add("정치·외교","Politics & Diplomacy","政治·外交","政治・外交","Política y diplomacia","Политика и дипломатия","السياسة والدبلوماسية","Siasa na diplomasia")
add("세계경제","World Economy","世界经济","世界経済","Economía mundial","Мировая экономика","الاقتصاد العالمي","Uchumi wa dunia")
add("사회·교육","Society & Education","社会·教育","社会・教育","Sociedad y educación","Общество и образование","المجتمع والتعليم","Jamii na elimu")
add("생활금융","Personal Finance","生活金融","生活金融","Finanzas personales","Личные финансы","التمويل الشخصي","Fedha binafsi")
add("문화","Culture","文化","文化","Cultura","Культура","الثقافة","Utamaduni")
add("역사·정치·지리","History, Politics & Geography","历史·政治·地理","歴史・政治・地理","Historia, política y geografía","История, политика, география","التاريخ والسياسة والجغرافيا","Historia, siasa na jiografia")
# front-10 hero headlines
add("급커브에서 먼저 볼 것은 속도계다","On a sharp curve, watch the speedometer first","急转弯时先看车速表","急カーブではまず速度計を見よ","En una curva cerrada, mira primero el velocímetro","На крутом повороте смотри сначала на спидометр","عند المنعطف الحاد، انظر أولاً إلى عداد السرعة","Kwenye kona kali, angalia kwanza kipima mwendo")
add("로켓을 잡은 다음, 비용을 잡을 차례","The rocket is caught; now for the cost","抓住了火箭，接下来要抓成本","ロケットは捕らえた、次はコストだ","El cohete está atrapado; ahora toca el coste","Ракета поймана — теперь очередь за расходами","أُمسك بالصاروخ، والآن حان دور التكلفة","Roketi imekamata; sasa ni zamu ya gharama")
add("광산을 샀다고 공급망을 얻는 것은 아니다","Buying a mine doesn't buy a supply chain","买下矿山不等于获得供应链","鉱山を買っても供給網は手に入らない","Comprar una mina no es comprar la cadena de suministro","Купить шахту не значит получить цепочку поставок","شراء منجم لا يعني امتلاك سلسلة الإمداد","Kununua mgodi si kupata mnyororo wa usambazaji")
add("AI에게 추천을 맡겨도 결제까지 맡길까","AI can recommend — should it also pay?","把推荐交给AI，支付也交给它吗？","AIに推薦は任せても、決済まで任せるか","La IA recomienda, ¿también debe pagar?","ИИ рекомендует — но доверить ли ему оплату?","الذكاء الاصطناعي يوصي، فهل نعهد إليه بالدفع أيضاً؟","AI inaweza kupendekeza — je, ilipie pia?")
add("성장률이 올라도 내 월급이 멈추는 이유","Why growth rises while my paycheck stalls","增长率上升，我的工资却原地踏步的原因","成長率が上がっても給料が止まる理由","Por qué crece la economía y mi sueldo no","Почему рост есть, а зарплата стоит","لماذا يرتفع النمو بينما يتوقف راتبي","Kwa nini ukuaji unaongezeka lakini mshahara unasimama")
add("롯데의 새 조직도, 권한보다 성과표를 보자","Lotte's new org chart: read the scorecard, not the titles","乐天新组织图：看成绩单而非权限","ロッテの新組織図、権限より成績表を見よう","El nuevo organigrama de Lotte: mire los resultados, no los cargos","Новая структура Lotte: смотрим на результаты, а не на полномочия","الهيكل الجديد للوتة: لننظر إلى النتائج لا إلى الصلاحيات","Chati mpya ya Lotte: angalia matokeo, si mamlaka")
add("수능 대책, 현장 점검과 법 개정은 다른 시간표다","Exam policy: inspections and legal reform run on different clocks","高考对策：现场检查与修法各有时间表","入試対策、現場点検と法改正は別の時間表","Medidas para el examen: inspección y reforma legal llevan ritmos distintos","Меры к экзамену: проверки и поправки идут по разным графикам","إجراءات الامتحان: التفتيش الميداني وتعديل القانون على جدولين مختلفين","Sera ya mtihani: ukaguzi na marekebisho ya sheria vina ratiba tofauti")
add("정상회의의 동사를 읽는 법","How to read the verbs of a summit","如何读懂峰会的动词","首脳会談の動詞を読む方法","Cómo leer los verbos de una cumbre","Как читать глаголы саммита","كيف تقرأ أفعال القمة","Jinsi ya kusoma vitenzi vya mkutano wa kilele")
add("김치는 상품이고, 김장은 관계다","Kimchi is a product; kimjang is a relationship","泡菜是商品，做泡菜是关系","キムチは商品、キムジャンは関係だ","El kimchi es un producto; el kimjang es un vínculo","Кимчи — товар, а кимчжан — отношения","الكيمتشي سلعة، أما الكيمجانغ فعلاقة","Kimchi ni bidhaa; kimjang ni uhusiano")
add("마타하리, 이름표보다 두꺼운 기록","Mata Hari: a record thicker than the name tag","玛塔·哈丽：比名牌更厚重的记录","マタ・ハリ、名札より厚い記録","Mata Hari: un registro más grueso que la etiqueta","Мата Хари: архив толще именной таблички","ماتا هاري: سجل أثخن من بطاقة الاسم","Mata Hari: kumbukumbu nzito kuliko lebo ya jina")
# 2026-11-18 report titles + subtitles
add("오늘의 경제 체온계 | 주가는 내려도 공장은 돌고, 장바구니는 무거울 수 있다","Economy Thermometer | Stocks may fall while factories hum and baskets grow heavy","今日经济体温计 | 股价下跌，工厂仍在运转，菜篮子可能变沉","今日の経済体温計 | 株価は下がっても工場は回り、買い物かごは重いかもしれない","Termómetro económico | Las acciones bajan, pero las fábricas giran y la cesta pesa","Экономический термометр | Акции падают, заводы работают, а корзина дорожает","مقياس حرارة الاقتصاد | قد تهبط الأسهم بينما تدور المصانع وتثقل السلة","Kipima joto cha uchumi | Hisa zinaweza kushuka huku viwanda vikifanya kazi na kikapu kikizidi")
add("도파민 배달왔습니다 | 꽃 너머의 오키프, 작품 수보다 먼저 볼 연결","Dopamine Delivered | O'Keeffe beyond the flowers: the circle to see before the catalogue","多巴胺已送达 | 花朵之外的欧姬芙：先看连接，再看作品数量","ドーパミン配達完了 | 花の向こうのオキーフ、作品数より先に見るつながり","Dopamina entregada | O'Keeffe más allá de las flores: la red antes que el catálogo","Дофамин доставлен | О'Кифф за пределами цветов: связи важнее каталога","تم توصيل الدوبامين | أوكيف خلف الزهور: الشبكة قبل عدد الأعمال","Dopamine imefika | O'Keeffe zaidi ya maua: mtandao kabla ya idadi ya kazi")
add("엄마찾아삼만리 | 관제망은 복구됐나, 정상화라는 말의 확인 범위","Finding Mom 30,000 Li | Is the ATC network restored? What 'normal' really covers","万里寻母记 | 空管网络恢复了吗？核实“正常”的范围","母をたずねて三千里 | 管制網は復旧したか——「正常化」の確認範囲","En busca de mamá | ¿Se recuperó la red de control aéreo? Qué cubre la 'normalidad'","В поисках мамы | Восстановлена ли сеть УВД? Что стоит за словом «нормализация»","البحث عن أمي | هل عادت شبكة المراقبة الجوية؟ وما حدود كلمة «العودة للطبيعي»","Kumtafuta mama | Je, mtandao wa udhibiti wa anga umerejeshwa? Maana ya 'kawaida'")
add("오늘의 반상회 | 시험의 신뢰, 기기를 금지하는 것에서 끝나지 않는다","Neighborhood Meeting | Exam trust doesn't end with banning devices","今日班常会 | 考试信任不止于禁止设备","今日の町内会 | 試験への信頼は端末禁止では終わらない","Reunión vecinal | La confianza en el examen no acaba con prohibir dispositivos","Сход жильцов | Доверие к экзамену не исчерпывается запретом устройств","مجلس الحي | ثقة الامتحان لا تنتهي عند حظر الأجهزة","Baraza la mtaa | Uaminifu wa mtihani hauishii kupiga marufuku vifaa")
add("여의도 한 입, 외교 한 접시 | 순방의 달력, 예정과 성과 사이에 선을 긋다","A Bite of Yeouido | The tour calendar: a line between plans and results","汝矣岛一口，外交一盘 | 出访日程：在计划与成果之间划线","汝矣島ひと口、外交ひと皿 | 外遊の日程——予定と成果のあいだに線を引く","Un bocado de Yeouido | La agenda de la gira: entre lo previsto y los resultados","Кусочек Йоидо | Календарь турне: черта между планами и итогами","قضمة من يويدو | جدول الجولة: خط بين المواعيد والإنجازات","Kijiko cha Yeouido | Kalenda ya ziara: mstari kati ya mipango na matokeo")
add("공장장 보고 드립니다 | 전력 사용 승인은 받았다, 제련소 완공과는 다르다","Factory Report | Power-use approval secured — not the same as a finished smelter","厂长报告 | 已获用电批准，但这不同于冶炼厂竣工","工場長の報告 | 電力使用の承認は取れた——製錬所完成とは別だ","Informe de fábrica | Permiso eléctrico concedido; no es lo mismo que la fundición terminada","Доклад с завода | Разрешение на электроснабжение получено — это не завершённый завод","تقرير المصنع | تمت الموافقة على الكهرباء، وهذا يختلف عن اكتمال المصفاة","Ripoti ya kiwanda | Idhini ya umeme imepatikana — si sawa na kukamilika kwa kiwanda")
add("공장장 보고 드립니다 | 예고편은 끝났다, 엔비디아 실적과 전망을 나누자","Factory Report | The trailer is over: let's separate Nvidia's results from its outlook","厂长报告 | 预告片结束了：分清英伟达的业绩与展望","工場長の報告 | 予告編は終わった——エヌビディアの実績と見通しを分けよう","Informe de fábrica | Se acabó el tráiler: separemos los resultados de Nvidia de sus previsiones","Доклад с завода | Трейлер окончен: отделим результаты Nvidia от прогнозов","تقرير المصنع | انتهى الإعلان التشويقي: لنفصل نتائج إنفيديا عن توقعاتها","Ripoti ya kiwanda | Tangazo limekwisha: tutofautishe matokeo ya Nvidia na matarajio")
add("오늘의 경제 체온계 | 수출의 열기와 가계의 체감, 같은 온도일까","Economy Thermometer | Export heat vs. household feel: same temperature?","今日经济体温计 | 出口热度与家庭体感，是同一温度吗","今日の経済体温計 | 輸出の熱さと家計の体感、同じ温度か","Termómetro económico | Calor exportador y bolsillo doméstico: ¿misma temperatura?","Экономический термометр | Жар экспорта и ощущения домохозяйств — одна температура?","مقياس حرارة الاقتصاد | حرارة الصادرات وإحساس الأسر: هل هما الدرجة نفسها؟","Kipima joto cha uchumi | Joto la mauzo ya nje na hisia za kaya: ni joto moja?")
add("오늘의 경제 체온계 | 지난주 반등은 기록, 이번 주 판단은 새 자료로","Economy Thermometer | Last week's rebound is on record; this week calls for fresh data","今日经济体温计 | 上周反弹已成记录，本周判断需看新数据","今日の経済体温計 | 先週の反発は記録、今週の判断は新しいデータで","Termómetro económico | El rebote pasado quedó atrás; esta semana manda el dato nuevo","Экономический термометр | Прошлый отскок — в архиве, выводы недели — по новым данным","مقياس حرارة الاقتصاد | ارتداد الأسبوع الماضي صار سجلاً، وحكم هذا الأسبوع ببيانات جديدة","Kipima joto cha uchumi | Rejea la wiki iliyopita ni rekodi; hukumu ya wiki hii na data mpya")
add("오늘의 경제 체온계 | 반등 뒤의 하락, 이제는 실적을 읽을 시간","Economy Thermometer | A dip after the rebound: time to read the earnings","今日经济体温计 | 反弹后的下跌：现在是读业绩的时候","今日の経済体温計 | 反発後の下落、今こそ決算を読む時間","Termómetro económico | Caída tras el rebote: hora de leer los resultados","Экономический термометр | Спад после отскока: время читать отчётность","مقياس حرارة الاقتصاد | هبوط بعد الارتداد: حان وقت قراءة النتائج","Kipima joto cha uchumi | Kushuka baada ya kupanda: ni wakati wa kusoma matokeo")
add("물가·금리·환율·고용·소비·생산·투자를 함께 읽는 보강판","Supplement reading prices, rates, FX, jobs, consumption, output and investment together","综合解读物价·利率·汇率·就业·消费·生产·投资的补充版","物価・金利・為替・雇用・消費・生産・投資をまとめて読む補強版","Edición ampliada: precios, tipos, divisas, empleo, consumo, producción e inversión","Дополненный выпуск: цены, ставки, курсы, занятость, потребление, производство, инвестиции","نسخة معززة تقرأ الأسعار والفائدة والصرف والوظائف والاستهلاك والإنتاج والاستثمار معاً","Toleo lililoboreshwa linalosoma bei, viwango, fedha, ajira, matumizi, uzalishaji na uwekezaji pamoja")
add("11월16일 원주제 · 11월18일 자료확인 별도 수정판","Nov 16 original topic · Nov 18 verified revision","11月16日原题·11月18日核实修订版","11月16日の原本題・11月18日確認の修正版","Tema original del 16 nov · revisión verificada del 18 nov","Тема 16 ноября · проверенная правка от 18 ноября","الموضوع الأصلي 16 نوفمبر · نسخة منقحة مؤكدة 18 نوفمبر","Mada ya awali Nov 16 · marekebisho yaliyothibitishwa Nov 18")

LANGS = ['en','zh','ja','es','ru','ar','sw']
DICT = {l: {} for l in LANGS}
for ko, m in K.items():
    for l in LANGS:
        DICT[l][ko] = m[l]

MUSIC = {
 'en': {'src':'https://commons.wikimedia.org/wiki/Special:FilePath/Greensleeves.ogg',
        'label':'♪ Greensleeves (English folk)',
        'page':'https://commons.wikimedia.org/wiki/File:Greensleeves.ogg',
        'credit':'Greensleeves — CambridgeBayWeather, CC BY 3.0, via Wikimedia Commons',
        'href':'https://commons.wikimedia.org/wiki/File:Greensleeves.ogg'},
 'zh': {'src':'https://commons.wikimedia.org/wiki/Special:FilePath/%E4%BA%8C%E6%B3%89%E6%98%A0%E6%9C%88.ogg',
        'label':'♪ 二泉映月 (二胡)',
        'page':'https://commons.wikimedia.org/wiki/File:%E4%BA%8C%E6%B3%89%E6%98%A0%E6%9C%88.ogg',
        'credit':'二泉映月 (The Moon Reflected on the Second Spring) — 张沛坚 Zhang Peijian, CC BY-SA 4.0, via Wikimedia Commons',
        'href':'https://commons.wikimedia.org/wiki/File:%E4%BA%8C%E6%B3%89%E6%98%A0%E6%9C%88.ogg'},
 'es': {'src':'https://commons.wikimedia.org/wiki/Special:FilePath/Romance_An%C3%B3nimo_(Jeux_interdits).ogg',
        'label':'♪ Romance Anónimo (guitarra)',
        'page':'https://commons.wikimedia.org/wiki/File:Romance_An%C3%B3nimo_(Jeux_interdits).ogg',
        'credit':'Romance Anónimo (Spanish guitar) — CC0, via Wikimedia Commons',
        'href':'https://commons.wikimedia.org/wiki/File:Romance_An%C3%B3nimo_(Jeux_interdits).ogg'},
 'ar': {'src':'https://commons.wikimedia.org/wiki/Special:FilePath/Solo_Oud_and_Ceramic_Darbuka_-_Arab_Instruments.webm',
        'label':'♪ عود ودربوكة',
        'page':'https://commons.wikimedia.org/wiki/File:Solo_Oud_and_Ceramic_Darbuka_-_Arab_Instruments.webm',
        'credit':'Solo Oud & Ceramic Darbuka — Arab Instruments, CC BY 3.0, via Wikimedia Commons',
        'href':'https://commons.wikimedia.org/wiki/File:Solo_Oud_and_Ceramic_Darbuka_-_Arab_Instruments.webm'},
}

BCAST = {'en': [['확인시점 기준', 'as of verification time'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', 'an editorial allocation weighing international coverage and recognition, not a measured ranking of influence'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', 'restricted or ended streams are skipped, so actual viewing share varies'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', 'actual live availability varies by provider, region and connection'], ['재생 제한/멈춤은 자동 건너뜀', 'playback restrictions/stops are auto-skipped'], ['정기 발행 준비에서 목록 재검증', 'list re-verified during scheduled publishing prep'], ['목록·생방송 확인', 'Playlist & live verified'], ['약 90초씩 순환', 'rotating every ~90s'], ['확인 시점 기준', 'as of verification time'], ['주요녹화', 'recorded'], ['재생 중', 'Now playing'], ['다시보기', 'Replay'], ['생방송', 'Live'], ['슬롯 중', 'slots:'], ['각 약90초', '~90s each'], ['편성', 'Lineup'], ['남은 ', 'left '], ['한국', 'South Korea'], ['중국', 'China'], ['미국', 'US'], ['일본', 'Japan'], ['유럽', 'Europe'], ['카타르', 'Qatar'], ['독일', 'Germany'], ['프랑스', 'France'], ['영국', 'UK'], ['러시아', 'Russia'], ['기타', 'Other'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1s', True]], 'zh': [['확인시점 기준', '以核验时间为准'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', '这是基于国际报道范围与知名度的编辑分配，并非影响力的实测排名'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', '受限或已结束的内容会被跳过，实际观看比例会有所不同'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', '实际直播可用性因提供商/地区/网络环境而异'], ['재생 제한/멈춤은 자동 건너뜀', '播放限制/停止将自动跳过'], ['정기 발행 준비에서 목록 재검증', '在定期发布准备中重新核验列表'], ['목록·생방송 확인', '列表与直播已核验'], ['약 90초씩 순환', '约每90秒轮换'], ['확인 시점 기준', '以核验时间为准'], ['주요녹화', '录播'], ['재생 중', '播放中'], ['다시보기', '回放'], ['생방송', '直播'], ['슬롯 중', '个时段中'], ['각 약90초', '各约90秒'], ['편성', '编排'], ['남은 ', '剩余'], ['한국', '韩国'], ['중국', '中国'], ['미국', '美国'], ['일본', '日本'], ['유럽', '欧洲'], ['카타르', '卡塔尔'], ['독일', '德国'], ['프랑스', '法国'], ['영국', '英国'], ['러시아', '俄罗斯'], ['기타', '其他'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1秒', True]], 'ja': [['확인시점 기준', '確認時点基準'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', '国際報道の範囲と認知度を考慮した編成配分であり、影響力の実測順位ではありません'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', '制限・終了時はスキップされるため、実際の視聴比率は変動します'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', '実際の視聴可否は提供元・地域・接続環境によって異なります'], ['재생 제한/멈춤은 자동 건너뜀', '再生制限・停止は自動でスキップします'], ['정기 발행 준비에서 목록 재검증', '定期発行の準備でリストを再検証しました'], ['목록·생방송 확인', 'リスト・ライブ確認済み'], ['약 90초씩 순환', '約90秒ごとに切り替え'], ['확인 시점 기준', '確認時点基準'], ['주요녹화', '録画'], ['재생 중', '再生中'], ['다시보기', '再放送'], ['생방송', 'ライブ'], ['슬롯 중', '枠のうち'], ['각 약90초', '各約90秒'], ['편성', '編成'], ['남은 ', '残り'], ['한국', '韓国'], ['중국', '中国'], ['미국', '米国'], ['일본', '日本'], ['유럽', '欧州'], ['카타르', 'カタール'], ['독일', 'ドイツ'], ['프랑스', 'フランス'], ['영국', '英国'], ['러시아', 'ロシア'], ['기타', 'その他'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1秒', True]], 'es': [['확인시점 기준', 'según el momento de verificación'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', 'una asignación editorial según cobertura internacional y reconocimiento, no un ranking medido de influencia'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', 'las transmisiones restringidas o finalizadas se omiten, así que el porcentaje real varía'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', 'la disponibilidad real varía según proveedor, región y conexión'], ['재생 제한/멈춤은 자동 건너뜀', 'las restricciones/paradas de reproducción se omiten automáticamente'], ['정기 발행 준비에서 목록 재검증', 'lista reverificada durante la preparación de la publicación programada'], ['목록·생방송 확인', 'Lista y directos verificados'], ['약 90초씩 순환', 'rotando cada ~90 s'], ['확인 시점 기준', 'según el momento de verificación'], ['주요녹화', 'grabado'], ['재생 중', 'Reproduciendo'], ['다시보기', 'Reposición'], ['생방송', 'En vivo'], ['슬롯 중', 'espacios:'], ['각 약90초', '~90 s cada uno'], ['편성', 'Programación'], ['남은 ', 'quedan '], ['한국', 'Corea del Sur'], ['중국', 'China'], ['미국', 'EE. UU.'], ['일본', 'Japón'], ['유럽', 'Europa'], ['카타르', 'Catar'], ['독일', 'Alemania'], ['프랑스', 'Francia'], ['영국', 'Reino Unido'], ['러시아', 'Rusia'], ['기타', 'Otros'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1 s', True]], 'ru': [['확인시점 기준', 'на момент проверки'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', 'редакционное распределение с учётом международного охвата и узнаваемости, а не измеренный рейтинг влияния'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', 'ограниченные или завершённые трансляции пропускаются, поэтому фактическая доля просмотра отличается'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', 'фактическая доступность зависит от провайдера, региона и соединения'], ['재생 제한/멈춤은 자동 건너뜀', 'ограничения/остановки воспроизведения пропускаются автоматически'], ['정기 발행 준비에서 목록 재검증', 'список перепроверен при подготовке очередного выпуска'], ['목록·생방송 확인', 'Список и эфиры проверены'], ['약 90초씩 순환', 'смена каждые ~90 с'], ['확인 시점 기준', 'на момент проверки'], ['주요녹화', 'запись'], ['재생 중', 'Воспроизведение'], ['다시보기', 'Повтор'], ['생방송', 'Эфир'], ['슬롯 중', 'слотов:'], ['각 약90초', 'по ~90 с'], ['편성', 'Сетка'], ['남은 ', 'осталось '], ['한국', 'Корея'], ['중국', 'Китай'], ['미국', 'США'], ['일본', 'Япония'], ['유럽', 'Европа'], ['카타르', 'Катар'], ['독일', 'Германия'], ['프랑스', 'Франция'], ['영국', 'Великобритания'], ['러시아', 'Россия'], ['기타', 'Другое'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1 с', True]], 'ar': [['확인시점 기준', 'حسب وقت التحقق'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', 'توزيع تحريري يراعي نطاق التغطية الدولية والشهرة، وليس ترتيبًا مقاسًا للتأثير'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', 'تُتخطى القنوات المقيّدة أو المنتهية، لذا تختلف نسب المشاهدة الفعلية'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', 'تختلف الإتاحة الفعلية حسب المزوّد والمنطقة وجودة الاتصال'], ['재생 제한/멈춤은 자동 건너뜀', 'تُتخطى قيود/توقفات التشغيل تلقائيًا'], ['정기 발행 준비에서 목록 재검증', 'أُعيد التحقق من القائمة أثناء التحضير للنشر الدوري'], ['목록·생방송 확인', 'تم التحقق من القائمة والبث المباشر'], ['약 90초씩 순환', 'تتبدل كل 90 ثانية تقريبًا'], ['확인 시점 기준', 'حسب وقت التحقق'], ['주요녹화', 'مسجّل'], ['재생 중', 'قيد التشغيل'], ['다시보기', 'إعادة'], ['생방송', 'مباشر'], ['슬롯 중', 'خانات:'], ['각 약90초', '~90 ثانية لكل منها'], ['편성', 'التشكيلة'], ['남은 ', 'المتبقي '], ['한국', 'كوريا'], ['중국', 'الصين'], ['미국', 'الولايات المتحدة'], ['일본', 'اليابان'], ['유럽', 'أوروبا'], ['카타르', 'قطر'], ['독일', 'ألمانيا'], ['프랑스', 'فرنسا'], ['영국', 'بريطانيا'], ['러시아', 'روسيا'], ['기타', 'أخرى'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', '$1 ث', True]], 'sw': [['확인시점 기준', 'kulingana na wakati wa uthibitishaji'], ['국제보도 범위와 인지도를 고려한 편집배분이며 영향력의 실측순위는 아닙니다', 'ni mgawanyo wa uhariri unaozingatia uwepo wa habari za kimataifa na umaarufu, si nafasi iliyopimwa ya ushawishi'], ['제한·종료 시 건너뛰므로 실제 시청 비율은 달라집니다', 'zilizozuiliwa au kumalizika hurukwa, hivyo viwango halisi vya kutazama hutofautiana'], ['실제 생방송 이용률은 제공사/지역/접속환경에 따라 달라집니다', 'upatikanaji halisi hutofautiana kulingana na mtoa huduma, eneo na mtandao'], ['재생 제한/멈춤은 자동 건너뜀', 'vizuizi/visimamizi vya kucheza vinarukwa kiotomatiki'], ['정기 발행 준비에서 목록 재검증', 'orodha ilithibitishwa tena wakati wa maandalizi ya uchapishaji wa kawaida'], ['목록·생방송 확인', 'Orodha na matangazo ya moja kwa moja yamethibitishwa'], ['약 90초씩 순환', 'inazunguka kila ~sekunde 90'], ['확인 시점 기준', 'kulingana na wakati wa uthibitishaji'], ['주요녹화', 'iliyorekodiwa'], ['재생 중', 'Inacheza sasa'], ['다시보기', 'Tazama tena'], ['생방송', 'Moja kwa moja'], ['슬롯 중', 'sehemu:'], ['각 약90초', 'kila moja ~sekunde 90'], ['편성', 'Mpangilio'], ['남은 ', 'zimebaki '], ['한국', 'Korea Kusini'], ['중국', 'China'], ['미국', 'Marekani'], ['일본', 'Japani'], ['유럽', 'Ulaya'], ['카타르', 'Qatar'], ['독일', 'Ujerumani'], ['프랑스', 'Ufaransa'], ['영국', 'Uingereza'], ['러시아', 'Urusi'], ['기타', 'Nyingine'], ['초 KST', ' KST'], ['(\\d+)시 ', '$1:', True], ['(\\d+)분 ', '$1:', True], ['(\\d+)초', 'sekunde $1', True]]}

# full-body translations {report_id: {lang: markdown}}
body_i18n = {}
if os.path.exists('body_i18n.json'):
    body_i18n = json.load(open('body_i18n.json', encoding='utf-8'))

# merge extra translation batches (keyed {ko: {lang: text}})
if os.path.exists('i18n_extra.json'):
    extra = json.load(open('i18n_extra.json', encoding='utf-8'))
    for ko, m in extra.items():
        for l, t in m.items():
            if l in DICT:
                DICT[l][ko] = t

FALLBACK = {
 'en': 'Full translation of this article is in progress. The Korean original is shown below.',
 'zh': '本文完整翻译正在准备中，以下为韩语原文。',
 'ja': '本文の全文翻訳は準備中です。韓国語の原文を表示します。',
 'es': 'La traducción completa de este artículo está en preparación; se muestra el original en coreano.',
 'ru': 'Полный перевод этой статьи готовится; ниже показан корейский оригинал.',
 'ar': 'الترجمة الكاملة لهذا المقال قيد الإعداد؛ يظهر النص الكوري الأصلي أدناه.',
 'sw': 'Tafsiri kamili ya makala hii inaendelea; tunaonyesha asili ya Kikorea hapa chini.',
}

LANG_BAR = '''
<div id="lang-bar" aria-label="Language selection / 언어 선택">
  <span id="lang-bar-label">언어 · Language</span>
  <button type="button" data-lang="ko" class="lang-btn">한국어</button>
  <button type="button" data-lang="en" class="lang-btn">English</button>
  <button type="button" data-lang="zh" class="lang-btn">中文</button>
  <button type="button" data-lang="ja" class="lang-btn">日本語</button>
  <button type="button" data-lang="es" class="lang-btn">Español</button>
  <button type="button" data-lang="ru" class="lang-btn">Русский</button>
  <button type="button" data-lang="ar" class="lang-btn">العربية</button>
  <button type="button" data-lang="sw" class="lang-btn">Kiswahili</button>
  <span id="lang-music-wrap" hidden>
    <button type="button" id="lang-music" aria-pressed="false"></button>
    <a id="lang-music-credit" target="_blank" rel="noopener"></a>
  </span>
</div>
'''

STYLE = '''
<style id="i18n-themes">
#lang-bar{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;padding:8px 0;border-bottom:1px solid var(--line);font-size:13px}
#lang-bar-label{font-size:10px;letter-spacing:2px;color:var(--muted);font-weight:800;margin-right:4px}
#lang-bar .lang-btn{background:none;border:none;padding:2px 2px;color:var(--muted);border-bottom:2px solid transparent;font-size:13px}
#lang-bar .lang-btn:hover{color:var(--ink)}
#lang-bar .lang-btn.active{color:var(--ink);font-weight:800;border-bottom-color:var(--accent)}
#lang-music-wrap{display:inline-flex;align-items:center;gap:8px;margin-left:auto}
#lang-music{background:var(--accent);color:#fff;border:none;border-radius:14px;padding:4px 12px;font-size:12px;font-weight:700}
#lang-music-credit{font-size:10px;color:var(--muted);max-width:340px;line-height:1.3}
@media (max-width:640px){#lang-bar{font-size:12px;gap:4px 8px}#lang-music-wrap{margin-left:0;width:100%}}
html[data-lang="en"] #daily-newsroom{--paper:#f1f4f7;--accent:#33597f;background-image:repeating-linear-gradient(45deg,rgba(51,89,127,.045) 0 2px,transparent 2px 14px)}
html[data-lang="zh"] #daily-newsroom{--paper:#f7f0e2;--accent:#a03428;background-image:radial-gradient(rgba(160,52,40,.06) 1px,transparent 1.6px);background-size:22px 22px}
html[data-lang="ja"] #daily-newsroom{--paper:#eef2f4;--accent:#3a5a6b;background-image:repeating-radial-gradient(circle at 0 0,transparent 0 18px,rgba(58,90,107,.05) 18px 19px)}
html[data-lang="es"] #daily-newsroom{--paper:#f8efe3;--accent:#b05a2a;background-image:repeating-conic-gradient(from 0deg at 100% 0,rgba(176,90,42,.05) 0deg 6deg,transparent 6deg 30deg)}
html[data-lang="ru"] #daily-newsroom{--paper:#eceff4;--accent:#4a5d78;background-image:repeating-linear-gradient(-45deg,rgba(74,93,120,.05) 0 3px,transparent 3px 18px)}
html[data-lang="ar"] #daily-newsroom{--paper:#f5eedd;--accent:#1e6f68;background-image:repeating-linear-gradient(45deg,rgba(30,111,104,.05) 0 1.5px,transparent 1.5px 12px),repeating-linear-gradient(-45deg,rgba(30,111,104,.05) 0 1.5px,transparent 1.5px 12px)}
html[data-lang="sw"] #daily-newsroom{--paper:#f4ecda;--accent:#7a5a20;background-image:repeating-linear-gradient(90deg,rgba(122,90,32,.05) 0 2px,transparent 2px 16px)}
html[dir="rtl"] #daily-newsroom .nr-nav,html[dir=rtl] #lang-bar{direction:rtl}
</style>
'''

SCRIPT_HEAD = '''
<script id="i18n-init">
(function(){
"use strict";
var DICT = __DICT__;
var MUSIC = __MUSIC__;
var LANGS = ['ko','en','zh','ja','es','ru','ar','sw'];
var cur = 'ko';
try { cur = localStorage.getItem('magazine-lang') || 'ko'; } catch(e) {}
if (LANGS.indexOf(cur) < 0) cur = 'ko';
var origCache = new Map();
var FALLBACK = __FALLBACK__;
window.BODY_I18N = __BODYI18N__;
var audio = null, playing = false;

function norm(t){ return t.replace(/\\s+/g,' ').trim(); }
function translateText(v, lang){
  var d = DICT[lang]; if(!d) return null;
  var k = norm(v);
  if (d[k] !== undefined) {
    var lead = v.match(/^\\s*/)[0], trail = v.match(/\\s*$/)[0];
    return lead + d[k] + trail;
  }
  if (k.length > 0 && k.length <= 140) {
    var keys = Object.keys(d);
    var out = v, changed = false;
    for (var iter=0; iter<5; iter++){
      var kk = norm(out), hit = null;
      for (var i=0;i<keys.length;i++){ if (keys[i].length >= 4 && kk.indexOf(keys[i]) >= 0 && (!hit || keys[i].length > hit.length)) hit = keys[i]; }
      if (!hit) break;
      var nout = out.split(hit).join(d[hit]);
      if (nout === out) break;
      out = nout; changed = true;
    }
    if (changed) return out;
  }
  return null;
}
function walk(root, lang){
  var skip = {'SCRIPT':1,'STYLE':1,'NOSCRIPT':1};
  var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {acceptNode:function(n){
    var p = n.parentElement;
    if (!p || skip[p.tagName]) return NodeFilter.FILTER_REJECT;
    if (p.closest && p.closest('#lang-bar')) return NodeFilter.FILTER_REJECT;
    return NodeFilter.FILTER_ACCEPT;
  }});
  var nodes = [], n;
  while ((n = tw.nextNode())) nodes.push(n);
  for (var i=0;i<nodes.length;i++){
    var t = translateText(nodes[i].nodeValue, lang);
    if (t !== null && t !== nodes[i].nodeValue){
      if (!origCache.has(nodes[i])) origCache.set(nodes[i], nodes[i].nodeValue);
      nodes[i].nodeValue = t;
    }
  }
}
var attrCache = new Map();
function translateAttrs(lang){
  var els = document.querySelectorAll('[aria-label],[title],[placeholder]');
  for (var i=0;i<els.length;i++){
    var el = els[i];
    if (el.closest && el.closest('#lang-bar')) continue;
    var rec = attrCache.get(el); if(!rec){ rec={}; attrCache.set(el, rec); }
    ['aria-label','title','placeholder'].forEach(function(a){
      var v = el.getAttribute(a); if(!v) return;
      var orig = (rec[a] !== undefined) ? rec[a] : v;
      var t = translateText(orig, lang);
      if (t !== null){
        if (rec[a] === undefined) rec[a] = v;
        if (el.getAttribute(a) !== t.trim()) el.setAttribute(a, t.trim());
      }
    });
  }
}
function restoreKo(){
  origCache.forEach(function(v, k){
    if (k && k.isConnected) k.nodeValue = v;
  });
  origCache.clear();
  attrCache.forEach(function(rec, el){
    if (!el.isConnected) return;
    for (var a in rec) el.setAttribute(a, rec[a]);
  });
  attrCache.clear();
}
function updateMusic(){
  var wrap = document.getElementById('lang-music-wrap');
  var btn = document.getElementById('lang-music');
  var cr = document.getElementById('lang-music-credit');
  if (!wrap || !btn || !cr) return;
  var m = MUSIC[cur];
  if (audio){ audio.pause(); playing = false; }
  if (!m){ wrap.hidden = true; return; }
  wrap.hidden = false;
  btn.textContent = '▶ ' + m.label;
  btn.setAttribute('aria-pressed','false');
  btn.onclick = function(){
    if (!audio || audio.dataset.lang !== cur){
      audio = new Audio(m.src);
      audio.dataset.lang = cur;
      audio.onended = function(){ playing=false; btn.textContent='▶ '+m.label; btn.setAttribute('aria-pressed','false'); };
      audio.onerror = function(){ playing=false; btn.textContent='▶ '+m.label; btn.setAttribute('aria-pressed','false'); };
    }
    if (playing){ audio.pause(); playing=false; btn.textContent='▶ '+m.label; btn.setAttribute('aria-pressed','false'); }
    else { audio.play().then(function(){ playing=true; btn.textContent='⏸ '+m.label; btn.setAttribute('aria-pressed','true'); }).catch(function(){ playing=false; }); }
  };
  cr.textContent = m.credit;
  cr.href = m.page;
  cr.href = m.href;
}
var BCAST = __BCAST__;
var BCAST_IDS = ['nm-kind','nm-status','nm-updated','nm-mix','nm-playlist','nm-source'];
function fixBroadcast(lang){
  var pairs = BCAST[lang]; if (!pairs) return;
  BCAST_IDS.forEach(function(id){
    var el = document.getElementById(id); if (!el) return;
    var t = el.textContent;
    for (var i=0;i<pairs.length;i++){
      if (pairs[i][2]) t = t.replace(new RegExp(pairs[i][0],'g'), pairs[i][1]);
      else t = t.split(pairs[i][0]).join(pairs[i][1]);
    }
    if (t !== el.textContent) el.textContent = t;
  });
}
function applyLang(lang, save){
  cur = lang;
  if (save) { try { localStorage.setItem('magazine-lang', lang); } catch(e){} }
  restoreKo();
  document.documentElement.setAttribute('data-lang', lang);
  if (window.__nrRenderBody && window.__nrCurrent) window.__nrRenderBody(window.__nrCurrent);
  document.documentElement.dir = (lang === 'ar') ? 'rtl' : 'ltr';
  document.querySelectorAll('#lang-bar .lang-btn').forEach(function(b){
    b.classList.toggle('active', b.dataset.lang === lang);
  });
  if (lang !== 'ko'){ walk(document.body, lang); translateAttrs(lang); fixBroadcast(lang); tagUntranslated(); }
  updateMusic();
}
var pending = null;
var obs = new MutationObserver(function(muts){
  if (cur === 'ko') return;
  if (pending) clearTimeout(pending);
  pending = setTimeout(function(){ walk(document.body, cur); translateAttrs(cur); fixBroadcast(cur); }, 180);
});
function tagUntranslated(){
  if (cur === 'ko') return;
  document.querySelectorAll('[role="dialog"], dialog').forEach(function(d){
    if (window.__nrCurrent && window.BODY_I18N && (window.BODY_I18N[window.__nrCurrent.id]||{})[cur]){
      var ex = d.querySelector('.i18n-fallback-note'); if (ex) ex.remove();
      return;
    }
    var note = d.querySelector('.i18n-fallback-note');
    if (note && note.dataset.lang === cur) return;
    if (!note){
      note = document.createElement('div');
      note.className = 'i18n-fallback-note';
      note.style.cssText = 'background:#fff8e1;border:1px solid #d4b45a;color:#6b5a1a;padding:8px 12px;margin:0 0 12px;font-size:12px;border-radius:4px;line-height:1.5';
      d.insertBefore(note, d.firstChild);
    }
    note.dataset.lang = cur;
    note.textContent = FALLBACK[cur] || FALLBACK.en;
  });
}
obs.observe(document.body, {childList:true, subtree:true});
setInterval(tagUntranslated, 700);
document.querySelectorAll('#lang-bar .lang-btn').forEach(function(b){
  b.addEventListener('click', function(){ applyLang(b.dataset.lang, true); });
});
if (cur !== 'ko'){
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function(){ applyLang(cur, false); });
  else applyLang(cur, false);
} else {
  document.querySelectorAll('#lang-bar .lang-btn').forEach(function(b){
    b.classList.toggle('active', b.dataset.lang === 'ko');
  });
}
})();
</script>
'''

script = SCRIPT_HEAD.replace('__DICT__', json.dumps(DICT, ensure_ascii=False)).replace('__MUSIC__', json.dumps(MUSIC, ensure_ascii=False)).replace('__FALLBACK__', json.dumps(FALLBACK, ensure_ascii=False)).replace('__BCAST__', json.dumps(BCAST, ensure_ascii=False)).replace('__BODYI18N__', json.dumps(body_i18n, ensure_ascii=False))

anchor = '<nav aria-label="주제 이동" class="nr-nav">'
assert anchor in src, "nav anchor missing"
assert src.count(anchor) == 1
# idempotent: strip any previous insertion first
src = re.sub(r'\n?<div id="lang-bar".*?</div>\s*(?=<nav aria-label="주제 이동")', '\n', src, flags=re.S)
src = re.sub(r'\n?<style id="i18n-themes">.*?</style>\s*', '\n', src, flags=re.S)
src = re.sub(r'\n?<script id="i18n-init">.*?</script>\s*', '\n', src, flags=re.S)
src = src.replace(anchor, LANG_BAR + anchor, 1)

tail = '</body>'
assert src.rstrip().endswith('</html>')
src = src.replace('</body>', STYLE + script + '</body>', 1)

open(SRC, 'w', encoding='utf-8').write(src)
open('/tmp/i18n-script.js', 'w', encoding='utf-8').write(script[len('<script id="i18n-init">'):].rsplit('</script>',1)[0].lstrip('\n'))
print("OK inserted. new len:", len(src))
print("dict keys:", sum(len(v) for v in DICT.values()))
