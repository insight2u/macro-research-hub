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
add("· 시황","· Markets","· 行情","· 市況","· Mercados","· Рынки","· الأسواق","· Masoko")
add("뉴스1/파이낸셜뉴스","News1/Financial News","News1/Financial News","News1/Financial News","News1/Financial News","News1/Financial News","News1/Financial News","News1/Financial News")
add("· 뉴스핌","· Newspim","· Newspim","· Newspim","· Newspim","· Newspim","· Newspim","· Newspim")
add("한국경제","Korea Economic Daily","韩国经济","韓国経済","Korea Economic Daily","Korea Economic Daily","Korea Economic Daily","Korea Economic Daily")
add("마이다스의 재테크","Midas's Personal Finance","迈达斯的理财","マイダスの資産運用","Finanzas personales de Midas","Личные финансы Мидаса","التمويل الشخصي من ميداس","Fedha binafsi za Midasi")
add("11/18 보강판 · 물가·고용·실물경제","11/18 Supplement · Prices, Jobs & Real Economy","11/18 补充版 · 物价·就业·实体经济","11/18 補強版 · 物価・雇用・実体経済","11/18 Suplemento · Precios, empleo y economía real","11/18 Дополнение · Цены, занятость, реальная экономика","11/18 ملحق · الأسعار والوظائف والاقتصاد الحقيقي","11/18 Nyongeza · Bei, ajira na uchumi halisi")
add("11/18 Morning Edition · 시장·환율·VIX","11/18 Morning Edition · Markets, FX & VIX","11/18 Morning Edition · 市场·汇率·VIX","11/18 Morning Edition · 市場・為替・VIX","11/18 Morning Edition · Mercados, divisas y VIX","11/18 Morning Edition · Рынки, валюты, VIX","11/18 Morning Edition · الأسواق والصرف وVIX","11/18 Morning Edition · Masoko, fedha na VIX")
add("11/18 Morning Edition · 임금·생산성","11/18 Morning Edition · Wages & Productivity","11/18 Morning Edition · 工资·生产率","11/18 Morning Edition · 賃金・生産性","11/18 Morning Edition · Salarios y productividad","11/18 Morning Edition · Зарплаты и производительность","11/18 Morning Edition · الأجور والإنتاجية","11/18 Morning Edition · Mishahara na tija")
add("-- 오버레이 없음 --","-- No overlay --","-- 无叠加 --","-- オーバーレイなし --","-- Sin superposición --","-- Без наложения --","-- بدون طبقة --","-- Bila safu --")
add("원/달러 환율 (1964~2026, 한국은행/서울외환)","KRW/USD Rate (1964~2026, BOK/Seoul FX)","韩元/美元汇率 (1964~2026, 韩国银行/首尔外汇)","ウォン/ドル為替 (1964~2026, 韓国銀行/ソウル外為)","Tipo KRW/USD (1964~2026, BOK/Seúl FX)","Курс вона/доллар (1964~2026, Банк Кореи/Сеул FX)","سعر صرف الوون/الدولار (1964~2026, بنك كوريا/سيول للصرف)","Kiwango cha KRW/USD (1964~2026, BOK/Seoul FX)")
add("韓 기준금리 (1999~2026, 한국은행)","KR Policy Rate (1999~2026, BOK)","韩国基准利率 (1999~2026, 韩国银行)","韓国政策金利 (1999~2026, 韓国銀行)","Tipo oficial coreano (1999~2026, BOK)","Ключевая ставка Кореи (1999~2026, Банк Кореи)","السعر المرجعي الكوري (1999~2026, بنك كوريا)","Kiwango cha Korea (1999~2026, BOK)")
add("美 연준 기준금리 (1954~2026, FRED)","US Fed Funds Rate (1954~2026, FRED)","美联储基准利率 (1954~2026, FRED)","米政策金利 (1954~2026, FRED)","Tipo de la Fed (1954~2026, FRED)","Ставка ФРС (1954~2026, FRED)","سعر الفائدة الفيدرالي (1954~2026, FRED)","Kiwango cha Fed (1954~2026, FRED)")
add("韓 실질 GDP 성장률 (1954~2026, KOSIS)","KR Real GDP Growth (1954~2026, KOSIS)","韩国实际GDP增长率 (1954~2026, KOSIS)","韓国実質GDP成長率 (1954~2026, KOSIS)","Crecimiento del PIB real coreano (1954~2026, KOSIS)","Реальный рост ВВП Кореи (1954~2026, KOSIS)","نمو الناتج المحلي الحقيقي الكوري (1954~2026, KOSIS)","Ukuaji wa PIB halisi (1954~2026, KOSIS)")
add("KOSPI 지수 (1980~2026, KRX)","KOSPI Index (1980~2026, KRX)","KOSPI指数 (1980~2026, KRX)","KOSPI指数 (1980~2026, KRX)","Índice KOSPI (1980~2026, KRX)","Индекс KOSPI (1980~2026, KRX)","مؤشر كوسبي (1980~2026, KRX)","Kipimo cha KOSPI (1980~2026, KRX)")
add("KOSDAQ 지수 (1996~2026, KRX)","KOSDAQ Index (1996~2026, KRX)","KOSDAQ指数 (1996~2026, KRX)","KOSDAQ指数 (1996~2026, KRX)","Índice KOSDAQ (1996~2026, KRX)","Индекс KOSDAQ (1996~2026, KRX)","مؤشر كوسداك (1996~2026, KRX)","Kipimo cha KOSDAQ (1996~2026, KRX)")
add("韓 국고채 3년물 금리 (1995~2026, 한국은행)","KR 3Y Treasury Yield (1995~2026, BOK)","韩国3年期国债利率 (1995~2026, 韩国银行)","韓国国債3年物金利 (1995~2026, 韓国銀行)","Rendimiento del bono coreano a 3 años (1995~2026, BOK)","Доходность 3-летних облигаций Кореи (1995~2026, Банк Кореи)","عائد سندات كوريا لأجل 3 سنوات (1995~2026, بنك كوريا)","Riba ya hatifungani ya miaka 3 (1995~2026, BOK)")
add("韓 국고채 10년물 금리 (2000~2026, 한국은행)","KR 10Y Treasury Yield (2000~2026, BOK)","韩国10年期国债利率 (2000~2026, 韩国银行)","韓国国債10年物金利 (2000~2026, 韓国銀行)","Rendimiento del bono coreano a 10 años (2000~2026, BOK)","Доходность 10-летних облигаций Кореи (2000~2026, Банк Кореи)","عائد سندات كوريا لأجل 10 سنوات (2000~2026, بنك كوريا)","Riba ya hatifungani ya miaka 10 (2000~2026, BOK)")
add("韓 국고채 10Y-3Y 스프레드 (2000~2026, 한국은행)","KR 10Y-3Y Spread (2000~2026, BOK)","韩国国债10Y-3Y利差 (2000~2026, 韩国银行)","韓国国債10年-3年スプレッド (2000~2026, 韓国銀行)","Diferencial 10Y-3Y coreano (2000~2026, BOK)","Спред 10Y-3Y Кореи (2000~2026, Банк Кореи)","فارق العائد 10-3 سنوات (2000~2026, بنك كوريا)","Tofauti ya 10Y-3Y (2000~2026, BOK)")
add("美 국채 10년물 금리 (1962~2026, FRED)","US 10Y Treasury Yield (1962~2026, FRED)","美国10年期国债利率 (1962~2026, FRED)","米国債10年物金利 (1962~2026, FRED)","Rendimiento del bono de EE. UU. a 10 años (1962~2026, FRED)","Доходность 10-летних США (1962~2026, FRED)","عائد سندات أمريكا لأجل 10 سنوات (1962~2026, FRED)","Riba ya hatifungani ya Marekani miaka 10 (1962~2026, FRED)")
add("美 국채 2년물 금리 (1976~2026, FRED)","US 2Y Treasury Yield (1976~2026, FRED)","美国2年期国债利率 (1976~2026, FRED)","米国債2年物金利 (1976~2026, FRED)","Rendimiento del bono de EE. UU. a 2 años (1976~2026, FRED)","Доходность 2-летних США (1976~2026, FRED)","عائد سندات أمريكا لأجل سنتين (1976~2026, FRED)","Riba ya hatifungani ya Marekani miaka 2 (1976~2026, FRED)")
add("美 국채 10Y-2Y 장단기차 (1976~2026, FRED)","US 10Y-2Y Spread (1976~2026, FRED)","美国10Y-2Y利差 (1976~2026, FRED)","米10年-2年金利差 (1976~2026, FRED)","Diferencial 10Y-2Y de EE. UU. (1976~2026, FRED)","Спред 10Y-2Y США (1976~2026, FRED)","فارق العائد الأمريكي 10-2 (1976~2026, FRED)","Tofauti ya 10Y-2Y ya Marekani (1976~2026, FRED)")
add("달러 인덱스 DXY (1971~2026, FRED)","Dollar Index DXY (1971~2026, FRED)","美元指数DXY (1971~2026, FRED)","ドル指数DXY (1971~2026, FRED)","Índice dólar DXY (1971~2026, FRED)","Индекс доллара DXY (1971~2026, FRED)","مؤشر الدولار DXY (1971~2026, FRED)","Kipimo cha dola DXY (1971~2026, FRED)")
add("100엔/원 환율 (1970~2026, 하나은행)","100 JPY/KRW Rate (1970~2026, Hana Bank)","100日元/韩元汇率 (1970~2026, 韩亚银行)","100円/ウォン為替 (1970~2026, ハナ銀行)","Tipo 100 JPY/KRW (1970~2026, Hana Bank)","Курс 100 иен/вона (1970~2026, Hana Bank)","سعر 100 ين/وون (1970~2026, بنك هانا)","Kiwango cha 100 JPY/KRW (1970~2026, Hana Bank)")
add("엔/달러 환율 (1971~2026, BOJ)","JPY/USD Rate (1971~2026, BOJ)","日元/美元汇率 (1971~2026, 日本央行)","円/ドル為替 (1971~2026, 日銀)","Tipo JPY/USD (1971~2026, BOJ)","Курс иена/доллар (1971~2026, BOJ)","سعر الين/الدولار (1971~2026, BOJ)","Kiwango cha JPY/USD (1971~2026, BOJ)")
add("韓 소비자물가지수 CPI (1965~2026, 통계청)","KR CPI (1965~2026, KOSTAT)","韩国CPI (1965~2026, 统计厅)","韓国CPI (1965~2026, 統計庁)","IPC coreano (1965~2026, KOSTAT)","ИПЦ Кореи (1965~2026, KOSTAT)","مؤشر أسعار المستهلك الكوري (1965~2026, KOSTAT)","CPI ya Korea (1965~2026, KOSTAT)")
add("美 소비자물가지수 CPI (1953~2026, BLS/FRED)","US CPI (1953~2026, BLS/FRED)","美国CPI (1953~2026, BLS/FRED)","米CPI (1953~2026, BLS/FRED)","IPC de EE. UU. (1953~2026, BLS/FRED)","ИПЦ США (1953~2026, BLS/FRED)","مؤشر أسعار المستهلك الأمريكي (1953~2026, BLS/FRED)","CPI ya Marekani (1953~2026, BLS/FRED)")
add("美 근원 PCE 물가지수 (1959~2026, BEA/FRED)","US Core PCE Index (1959~2026, BEA/FRED)","美国核心PCE物价指数 (1959~2026, BEA/FRED)","米コアPCE物価指数 (1959~2026, BEA/FRED)","Índice PCE subyacente de EE. UU. (1959~2026, BEA/FRED)","Базовый индекс PCE США (1959~2026, BEA/FRED)","مؤشر PCE الأساسي الأمريكي (1959~2026, BEA/FRED)","Kipimo cha PCE cha msingi (1959~2026, BEA/FRED)")
add("韓 실업률 (1963~2026, 통계청)","KR Unemployment Rate (1963~2026, KOSTAT)","韩国失业率 (1963~2026, 统计厅)","韓国失業率 (1963~2026, 統計庁)","Tasa de paro coreana (1963~2026, KOSTAT)","Безработица Кореи (1963~2026, KOSTAT)","معدل البطالة الكوري (1963~2026, KOSTAT)","Kiwango cha ukosefu wa ajira (1963~2026, KOSTAT)")
add("美 실업률 (1953~2026, BLS/FRED)","US Unemployment Rate (1953~2026, BLS/FRED)","美国失业率 (1953~2026, BLS/FRED)","米失業率 (1953~2026, BLS/FRED)","Tasa de paro de EE. UU. (1953~2026, BLS/FRED)","Безработица США (1953~2026, BLS/FRED)","معدل البطالة الأمريكي (1953~2026, BLS/FRED)","Kiwango cha ukosefu wa ajira Marekani (1953~2026, BLS/FRED)")
add("韓 경기종합지수 선행순환변동치 (1970~2026, 통계청)","KR CLI Leading Cyclical (1970~2026, KOSTAT)","韩国综合指数先行循环变动值 (1970~2026, 统计厅)","韓国景気総合指数・先行循環変動値 (1970~2026, 統計庁)","Índice compuesto adelantado coreano (1970~2026, KOSTAT)","Опережающий индекс Кореи (1970~2026, KOSTAT)","المؤشر المركب المتقدم الكوري (1970~2026, KOSTAT)","Kipimo cha mbele cha Korea (1970~2026, KOSTAT)")
add("韓 경기종합지수 동행순환변동치 (1970~2026, 통계청)","KR CLI Coincident Cyclical (1970~2026, KOSTAT)","韩国综合指数同步循环变动值 (1970~2026, 统计厅)","韓国景気総合指数・一致循環変動値 (1970~2026, 統計庁)","Índice compuesto coincidente coreano (1970~2026, KOSTAT)","Совпадающий индекс Кореи (1970~2026, KOSTAT)","المؤشر المركب المصاحب الكوري (1970~2026, KOSTAT)","Kipimo cha sasa cha Korea (1970~2026, KOSTAT)")
add("OECD 한국 경기선행지수 CLI (1975~2026, OECD)","OECD Korea CLI (1975~2026, OECD)","OECD韩国经济先行指数CLI (1975~2026, OECD)","OECD韓国景気先行指数CLI (1975~2026, OECD)","CLI de Corea de la OCDE (1975~2026, OECD)","CLI Кореи от ОЭСР (1975~2026, OECD)","مؤشر OECD المتقدم لكوريا (1975~2026, OECD)","CLI ya Korea ya OECD (1975~2026, OECD)")
add("韓 제조업 생산지수 (1975~2026, 통계청)","KR Manufacturing Production Index (1975~2026, KOSTAT)","韩国制造业生产指数 (1975~2026, 统计厅)","韓国鉱工業生産指数 (1975~2026, 統計庁)","Índice de producción manufacturera coreano (1975~2026, KOSTAT)","Индекс промпроизводства Кореи (1975~2026, KOSTAT)","مؤشر الإنتاج الصناعي الكوري (1975~2026, KOSTAT)","Kipimo cha uzalishaji wa Korea (1975~2026, KOSTAT)")
add("韓 소비자심리지수 CSI (2008~2026, 한국은행)","KR Consumer Sentiment CSI (2008~2026, BOK)","韩国消费者心理指数CSI (2008~2026, 韩国银行)","韓国消費者心理指数CSI (2008~2026, 韓国銀行)","Índice de confianza del consumidor coreano (2008~2026, BOK)","Индекс потребительских настроений Кореи (2008~2026, Банк Кореи)","مؤشر ثقة المستهلك الكوري (2008~2026, بنك كوريا)","Kipimo cha hisia za watumiaji (2008~2026, BOK)")
add("WTI 국제 원유 (1983~2026, NYMEX/EIA)","WTI Crude Oil (1983~2026, NYMEX/EIA)","WTI国际原油 (1983~2026, NYMEX/EIA)","WTI原油 (1983~2026, NYMEX/EIA)","Crudo WTI (1983~2026, NYMEX/EIA)","Нефть WTI (1983~2026, NYMEX/EIA)","خام غرب تكساس WTI (1983~2026, NYMEX/EIA)","Mafuta ya WTI (1983~2026, NYMEX/EIA)")
add("국제 금(Gold) 선물 (1975~2026, COMEX)","Gold Futures (1975~2026, COMEX)","国际黄金期货 (1975~2026, COMEX)","金先物 (1975~2026, COMEX)","Futuros del oro (1975~2026, COMEX)","Фьючерсы на золото (1975~2026, COMEX)","عقود الذهب الآجلة (1975~2026, COMEX)","Soko la dhahabu la baadaye (1975~2026, COMEX)")
add("구리(Dr. Copper) 선물 (1988~2026, LME/COMEX)","Copper (Dr. Copper) Futures (1988~2026, LME/COMEX)","铜(Dr. Copper)期货 (1988~2026, LME/COMEX)","銅(Dr. Copper)先物 (1988~2026, LME/COMEX)","Futuros del cobre (Dr. Copper) (1988~2026, LME/COMEX)","Фьючерсы на медь (Dr. Copper) (1988~2026, LME/COMEX)","عقود النحاس الآجلة (1988~2026, LME/COMEX)","Soko la shaba la baadaye (1988~2026, LME/COMEX)")
add("클락슨 신조선가지수 (1988~2026, Clarksons)","Clarksons Newbuilding Price Index (1988~2026, Clarksons)","克拉克森新造船价格指数 (1988~2026, Clarksons)","クラークソン新造船価指数 (1988~2026, Clarksons)","Índice de precios de construcción naval Clarksons (1988~2026, Clarksons)","Индекс цен на новые суда Clarksons (1988~2026, Clarksons)","مؤشر كلاركسون لأسعار السفن الجديدة (1988~2026, Clarksons)","Kipimo cha bei za meli mpya (1988~2026, Clarksons)")
add("S&P 500 지수 (1957~2026, FRED)","S&P 500 Index (1957~2026, FRED)","标普500指数 (1957~2026, FRED)","S&P 500指数 (1957~2026, FRED)","Índice S&P 500 (1957~2026, FRED)","Индекс S&P 500 (1957~2026, FRED)","مؤشر S&P 500 (1957~2026, FRED)","Kipimo cha S&P 500 (1957~2026, FRED)")
add("나스닥 종합지수 (1971~2026, NASDAQ)","Nasdaq Composite (1971~2026, NASDAQ)","纳斯达克综合指数 (1971~2026, NASDAQ)","ナスダック総合指数 (1971~2026, NASDAQ)","Nasdaq Composite (1971~2026, NASDAQ)","Индекс Nasdaq (1971~2026, NASDAQ)","مؤشر ناسداك المركب (1971~2026, NASDAQ)","Kipimo cha Nasdaq (1971~2026, NASDAQ)")
add("필라델피아 반도체지수 SOX (1993~2026, PHLX)","Philadelphia Semiconductor Index SOX (1993~2026, PHLX)","费城半导体指数SOX (1993~2026, PHLX)","フィラデルフィア半導体指数SOX (1993~2026, PHLX)","Índice de semiconductores de Filadelfia SOX (1993~2026, PHLX)","Индекс полупроводников Филадельфии SOX (1993~2026, PHLX)","مؤشر فيلادلفيا لأشباه الموصلات SOX (1993~2026, PHLX)","Kipimo cha nusu conductors SOX (1993~2026, PHLX)")
add("원/달러 환율 (KRW/USD)","KRW/USD Exchange Rate","韩元/美元汇率 (KRW/USD)","ウォン/ドル為替 (KRW/USD)","Tipo de cambio KRW/USD","Курс вона/доллар (KRW/USD)","سعر صرف الوون/الدولار","Kiwango cha KRW/USD")
add("美 연준 기준금리 (%)","US Fed Funds Rate (%)","美联储基准利率 (%)","米政策金利 (%)","Tipo de la Fed (%)","Ставка ФРС (%)","سعر الفائدة الفيدرالي (%)","Kiwango cha Fed (%)")
add("韓 실질 GDP 성장률 (%)","KR Real GDP Growth (%)","韩国实际GDP增长率 (%)","韓国実質GDP成長率 (%)","Crecimiento del PIB real coreano (%)","Реальный рост ВВП Кореи (%)","نمو الناتج المحلي الحقيقي الكوري (%)","Ukuaji wa PIB halisi (%)")
add("KOSPI 지수 (p)","KOSPI Index (p)","KOSPI指数 (p)","KOSPI指数 (p)","Índice KOSPI (p)","Индекс KOSPI (p)","مؤشر كوسبي (p)","Kipimo cha KOSPI (p)")
add("WTI 국제 원유 ($)","WTI Crude Oil ($)","WTI国际原油 ($)","WTI原油 ($)","Crudo WTI ($)","Нефть WTI ($)","خام غرب تكساس ($)","Mafuta ya WTI ($)")
add("원/달러 환율 (원)","KRW/USD Rate (KRW)","韩元/美元汇率 (韩元)","ウォン/ドル為替 (ウォン)","Tipo KRW/USD (KRW)","Курс вона/доллар (вона)","سعر الوون/الدولار (وون)","Kiwango cha KRW/USD (KRW)")
add("💵 원/달러 환율","💵 KRW/USD Rate","💵 韩元/美元汇率","💵 ウォン/ドル為替","💵 Tipo KRW/USD","💵 Курс вона/доллар","💵 سعر الوون/الدولار","💵 Kiwango cha KRW/USD")
add("🏛️ 한미 기준금리차","🏛️ Korea-US Policy Rate Gap","🏛️ 韩美基准利率差","🏛️ 韓米政策金利差","🏛️ Diferencial de tipos Corea-EE. UU.","🏛️ Разница ставок Кореи и США","🏛️ فارق الفائدة بين كوريا وأمريكا","🏛️ Tofauti ya viwango Korea-Marekani")
add("📊 실질 GDP 성장률","📊 Real GDP Growth","📊 实际GDP增长率","📊 実質GDP成長率","📊 Crecimiento del PIB real","📊 Реальный рост ВВП","📊 نمو الناتج المحلي الحقيقي","📊 Ukuaji wa PIB halisi")
add("📈 코스피 (KOSPI)","📈 KOSPI","📈 韩国KOSPI","📈 KOSPI","📈 KOSPI","📈 KOSPI","📈 كوسبي","📈 KOSPI")
add("모든 분야","All Fields","全部分类","すべての分野","Todos los campos","Все рубрики","جميع المجالات","Sehemu zote")
add("22.05 취임","22.05 Inauguration","22.05 就任","22.05 就任","22.05 Investidura","22.05 Инаугурация","22.05 التنصيب","22.05 Kuapishwa")
add("22.08 펠로시","22.08 Pelosi","22.08 佩洛西","22.08 ペロシ","22.08 Pelosi","22.08 Пелоси","22.08 بيلوسي","22.08 Pelosi")
add("22.09 비속어","22.09 Hot-mic remark","22.09 粗口风波","22.09 失言","22.09 Comentario vulgar","22.09 Скандал с репликой","22.09 التعليق المسيء","22.09 Maneno mabaya")
add("22.10 이태원","22.10 Itaewon","22.10 梨泰院","22.10 梨泰院","22.10 Itaewon","22.10 Итэвон","22.10 إيتايون","22.10 Itaewon")
add("22.12 화물연대","22.12 Truckers' strike","22.12 货运联盟罢工","22.12 貨物連帯スト","22.12 Huelga de camioneros","22.12 Забастовка дальнобойщиков","22.12 إضراب سائقي الشاحنات","22.12 Mgomo wa madereva")
add("23.03 강제동원","23.03 Forced labor","23.03 强征劳工","23.03 徴用工","23.03 Trabajo forzoso","23.03 Принудительный труд","23.03 العمل القسري","23.03 Kazi ya lazima")
add("23.04 방미","23.04 US visit","23.04 访美","23.04 訪米","23.04 Visita a EE. UU.","23.04 Визит в США","23.04 زيارة أمريكا","23.04 Ziara ya Marekani")
add("23.08 캠프데이비드","23.08 Camp David","23.08 戴维营","23.08 キャンプデービッド","23.08 Camp David","23.08 Кэмп-Дэвид","23.08 كامب ديفيد","23.08 Camp David")
add("23.10 강서보선","23.10 Gangseo by-election","23.10 江西补选","23.10 江西補選","23.10 Elección parcial de Gangseo","23.10 Довыборы в Кансо","23.10 انتخابات جانغسو الفرعية","23.10 Uchaguzi mdogo wa Gangseo")
add("24.01 특검거부","24.01 Special counsel veto","24.01 否决特检","24.01 特検拒否","24.01 Veto a la fiscalía especial","24.01 Вето на спецпрокуратуру","24.01 رفض التحقيق الخاص","24.01 Katazo la uchunguzi maalum")
add("24.02 의대증원","24.02 Med school expansion","24.02 医学院扩招","24.02 医学部増員","24.02 Ampliación de medicina","24.02 Расширение медвузов","24.02 توسعة كليات الطب","24.02 Ongezeko la vyuo vya udaktari")
add("24.04 총선참패","24.04 Election defeat","24.04 大选惨败","24.04 総選挙惨敗","24.04 Derrota electoral","24.04 Поражение на выборах","24.04 الهزيمة الانتخابية","24.04 Kushindwa uchaguzi")
add("24.06 대왕고래","24.06 Great Whale","24.06 大王鲸","24.06 大王クジラ","24.06 Gran Ballena","24.06 Большой кит","24.06 الحوت العظيم","24.06 Nyangumi Mkubwa")
add("24.09 체코원전","24.09 Czech nuclear deal","24.09 捷克核电","24.09 チェコ原発","24.09 Nuclear checa","24.09 АЭС в Чехии","24.09 محطة التشيك النووية","24.09 Nishati ya nyuklia ya Czech")
add("24.10 명태균녹취","24.10 Myung Tae-kyun tapes","24.10 明泰均录音","24.10 ミョン・テギュン録音","24.10 Cintas de Myung Tae-kyun","24.10 Записи Мён Тхэ Гюна","24.10 تسجيلات ميونغ تاي غيون","24.08 Rekodi za Myung")
add("26.10 현재","26.10 Present","26.10 现在","26.10 現在","26.10 Actualidad","26.10 Настоящее","26.10 الحاضر","26.10 Sasa")
add("2022.05 취임 ~ 2026.10 현재","2022.05 Inauguration ~ 2026.10 Present","2022.05 就任 ~ 2026.10 现在","2022.05 就任 ~ 2026.10 現在","2022.05 Investidura ~ 2026.10 Actualidad","2022.05 Инаугурация ~ 2026.10 Настоящее","2022.05 التنصيب ~ 2026.10 الحاضر","2022.05 Kuapishwa ~ 2026.10 Sasa")
add("1년1Q","Y1Q1","1年Q1","1年Q1","A1T1","Г1К1","س1 ر1","M1R1")
add("1년2Q","Y1Q2","1年Q2","1年Q2","A1T2","Г1К2","س1 ر2","M1R2")
add("1년3Q","Y1Q3","1年Q3","1年Q3","A1T3","Г1К3","س1 ر3","M1R3")
add("1년4Q","Y1Q4","1年Q4","1年Q4","A1T4","Г1К4","س1 ر4","M1R4")
add("2년2Q","Y2Q2","2年Q2","2年Q2","A2T2","Г2К2","س2 ر2","M2R2")
add("2년4Q","Y2Q4","2年Q4","2年Q4","A2T4","Г2К4","س2 ر4","M2R4")
add("3년2Q","Y3Q2","3年Q2","3年Q2","A3T2","Г3К2","س3 ر2","M3R2")
add("3년4Q","Y3Q4","3年Q4","3年Q4","A3T4","Г3К4","س3 ر4","M3R4")
add("4년2Q","Y4Q2","4年Q2","4年Q2","A4T2","Г4К2","س4 ر2","M4R2")
add("4년4Q","Y4Q4","4年Q4","4年Q4","A4T4","Г4К4","س4 ر4","M4R4")
add("5년2Q","Y5Q2","5年Q2","5年Q2","A5T2","Г5К2","س5 ر2","M5R2")
add("5년4Q","Y5Q4","5年Q4","5年Q4","A5T4","Г5К4","س5 ر4","M5R4")
add("⚡ AI·생산성","⚡ AI & Productivity","⚡ AI·生产率","⚡ AI・生産性","⚡ IA y productividad","⚡ ИИ и производительность","⚡ الذكاء الاصطناعي والإنتاجية","⚡ AI na tija")
add("거시경제 & AI 부채","Macroeconomy & AI Debt","宏观经济与AI债务","マクロ経済とAI債務","Macroeconomía y deuda de IA","Макроэкономика и долг ИИ","الاقتصاد الكلي وديون الذكاء الاصطناعي","Uchumi mkubwa na deni la AI")
add("거시경제 & 글로벌 금융시장 전략","Macroeconomy & Global Markets Strategy","宏观经济与全球金融市场策略","マクロ経済とグローバル金融市場戦略","Macroeconomía y estrategia de mercados globales","Макроэкономика и стратегия мировых рынков","الاقتصاد الكلي واستراتيجية الأسواق العالمية","Uchumi mkubwa na mikakati ya masoko ya dunia")
add("거시경제 & 금융시장","Macroeconomy & Financial Markets","宏观经济与金融市场","マクロ経済と金融市場","Macroeconomía y mercados financieros","Макроэкономика и финансовые рынки","الاقتصاد الكلي والأسواق المالية","Uchumi mkubwa na masoko ya fedha")
add("거시경제 & 서민금융","Macroeconomy & Household Finance","宏观经济与民生金融","マクロ経済と庶民金融","Macroeconomía y finanzas populares","Макроэкономика и народные финансы","الاقتصاد الكلي والتمويل الشعبي","Uchumi mkubwa na fedha za wananchi")
add("거시경제 & 통화정책","Macroeconomy & Monetary Policy","宏观经济与货币政策","マクロ経済と金融政策","Macroeconomía y política monetaria","Макроэкономика и денежная политика","الاقتصاد الكلي والسياسة النقدية","Uchumi mkubwa na sera ya fedha")
add("경제","Economy","经济","経済","Economía","Экономика","اقتصاد","Uchumi")
add("경제·금융소비자","Economy & Financial Consumers","经济·金融消费者","経済・金融消費者","Economía y consumidores financieros","Экономика и финансовые потребители","الاقتصاد ومستهلكو الخدمات المالية","Uchumi na watumiaji wa fedha")
add("경제·농업","Economy & Agriculture","经济·农业","経済・農業","Economía y agricultura","Экономика и сельское хозяйство","الاقتصاد والزراعة","Uchumi na kilimo")
add("경제·산업","Economy & Industry","经济·产业","経済・産業","Economía e industria","Экономика и промышленность","الاقتصاد والصناعة","Uchumi na viwanda")
add("경제·소비","Economy & Consumption","经济·消费","経済・消費","Economía y consumo","Экономика и потребление","الاقتصاد والاستهلاك","Uchumi na matumizi")
add("경제·에너지","Economy & Energy","经济·能源","経済・エネルギー","Economía y energía","Экономика и энергетика","الاقتصاد والطاقة","Uchumi na nishati")
add("경제·유통","Economy & Distribution","经济·流通","経済・流通","Economía y distribución","Экономика и дистрибуция","الاقتصاد والتوزيع","Uchumi na usambazaji")
add("경제·제도","Economy & Institutions","经济·制度","経済・制度","Economía e instituciones","Экономика и институты","الاقتصاد والمؤسسات","Uchumi na taasisi")
add("공정거래 & 플랫폼 규제","Fair Trade & Platform Regulation","公平交易与平台监管","公正取引とプラットフォーム規制","Comercio justo y regulación de plataformas","Честная конкуренция и регулирование платформ","التجارة العادلة وتنظيم المنصات","Biashara ya haki na udhibiti wa majukwaa")
add("국내 정치 & 노동 정책","Domestic Politics & Labor Policy","国内政治与劳动政策","国内政治と労働政策","Política interior y política laboral","Внутренняя политика и трудовая политика","السياسة الداخلية وسياسة العمل","Siasa za ndani na sera za kazi")
add("국내 정치 & 사법","Domestic Politics & Judiciary","国内政治与司法","国内政治と司法","Política interior y judicatura","Внутренняя политика и судебная власть","السياسة الداخلية والقضاء","Siasa za ndani na mahakama")
add("국내 정치 & 여론","Domestic Politics & Public Opinion","国内政治与舆论","国内政治と世論","Política interior y opinión pública","Внутренняя политика и общественное мнение","السياسة الداخلية والرأي العام","Siasa za ndani na maoni ya umma")
add("국내 정치 & 재정 정책","Domestic Politics & Fiscal Policy","国内政治与财政政策","国内政治と財政政策","Política interior y política fiscal","Внутренняя политика и бюджетная политика","السياسة الداخلية والسياسة المالية","Siasa za ndani na sera ya bajeti")
add("국내 정치 & 헌법 제도","Domestic Politics & Constitutional System","国内政治与宪法制度","国内政治と憲法制度","Política interior y sistema constitucional","Внутренняя политика и конституционный строй","السياسة الداخلية والنظام الدستوري","Siasa za ndani na mfumo wa katiba")
add("국내 정치 & 헌법 질서","Domestic Politics & Constitutional Order","国内政治与宪法秩序","国内政治と憲法秩序","Política interior y orden constitucional","Внутренняя политика и конституционный порядок","السياسة الداخلية والنظام الدستوري","Siasa za ndani na utaratibu wa katiba")
add("국제·관광경제","International & Tourism Economy","国际·旅游经济","国際・観光経済","Internacional y economía del turismo","Международное и туристическая экономика","الدولية واقتصاد السياحة","Kimataifa na uchumi wa utalii")
add("국제·산업","International & Industry","国际·产业","国際・産業","Internacional e industria","Международное и промышленность","الدولية والصناعة","Kimataifa na viwanda")
add("글로벌 & 빅테크 AI","Global & Big Tech AI","全球与大型科技AI","グローバルとビッグテックAI","Global e IA de las big tech","Глобальное и ИИ бигтеха","العالمية وذكاء الشركات الكبرى","Kimataifa na AI ya kampuni kubwa")
add("글로벌 거시경제 & 자산배분 전략","Global Macro & Asset Allocation","全球宏观与资产配置策略","グローバルマクロと資産配分戦略","Macro global y asignación de activos","Глобальная макроэкономика и распределение активов","الاقتصاد الكلي العالمي وتخصيص الأصول","Uchumi wa dunia na mgawanyo wa mali")
add("글로벌 거시경제 & 지정학 전략","Global Macro & Geopolitical Strategy","全球宏观与地缘政治策略","グローバルマクロと地政学戦略","Macro global y estrategia geopolítica","Глобальная макроэкономика и геополитика","الاقتصاد الكلي العالمي والاستراتيجية الجيوسياسية","Uchumi wa dunia na mikakati ya kijiografia")
add("글로벌 거시경제 & 통화지정학","Global Macro & Currency Geopolitics","全球宏观与货币地缘政治","グローバルマクロと通貨地政学","Macro global y geopolítica monetaria","Глобальная макроэкономика и валютная геополитика","الاقتصاد الكلي العالمي وجيوسياسية العملات","Uchumi wa dunia na siasa za sarafu")
add("글로벌 매크로 & 연준","Global Macro & the Fed","全球宏观与美联储","グローバルマクロとFRB","Macro global y la Fed","Глобальная макроэкономика и ФРС","الاقتصاد الكلي العالمي والاحتياطي الفيدرالي","Uchumi wa dunia na Fed")
add("글로벌 반도체 패권 & 테크 전략","Global Chip Hegemony & Tech Strategy","全球半导体霸权与科技战略","グローバル半導体覇権とテック戦略","Hegemonía de chips y estrategia tecnológica","Глобальное лидерство в чипах и техстратегия","الهيمنة العالمية على الرقائق واستراتيجية التقنية","Uongozi wa chipsi na mikakati ya teknolojia")
add("글로벌 빅테크 & AI 자본시장 전략","Global Big Tech & AI Capital Markets","全球大型科技与AI资本市场战略","グローバルビッグテックとAI資本市場戦略","Big tech global y mercados de capital de IA","Глобальный бигтех и рынки капитала ИИ","الشركات التقنية الكبرى وأسواق رأس مال الذكاء الاصطناعي","Kampuni kubwa na masoko ya mtaji wa AI")
add("글로벌 빅테크 & AI 전략","Global Big Tech & AI Strategy","全球大型科技与AI战略","グローバルビッグテックとAI戦略","Big tech global y estrategia de IA","Глобальный бигтех и стратегия ИИ","الشركات التقنية الكبرى واستراتيجية الذكاء الاصطناعي","Kampuni kubwa na mikakati ya AI")
add("글로벌 지정학 & 거시 정치 전략","Global Geopolitics & Macro Political Strategy","全球地缘政治与宏观政治战略","グローバル地政学とマクロ政治戦略","Geopolítica global y estrategia macropolítica","Глобальная геополитика и макрополитика","الجيوسياسية العالمية واستراتيجية السياسة الكلية","Siasa za kijiografia na mikakati ya siasa")
add("글로벌 지정학 & 에너지 경제","Global Geopolitics & Energy Economy","全球地缘政治与能源经济","グローバル地政学とエネルギー経済","Geopolítica global y economía de la energía","Глобальная геополитика и энергоэкономика","الجيوسياسية العالمية واقتصاد الطاقة","Siasa za kijiografia na uchumi wa nishati")
add("글로벌 지정학 & 통상 전략","Global Geopolitics & Trade Strategy","全球地缘政治与通商战略","グローバル地政学と通商戦略","Geopolítica global y estrategia comercial","Глобальная геополитика и торговая стратегия","الجيوسياسية العالمية واستراتيجية التجارة","Siasa za kijiografia na mikakati ya biashara")
add("기술·소비트렌드","Tech & Consumer Trends","技术·消费趋势","技術・消費トレンド","Tecnología y tendencias de consumo","Технологии и потребительские тренды","التقنية واتجاهات الاستهلاك","Teknolojia na mitindo ya matumizi")
add("기업·지배구조","Corporate Governance","企业·治理结构","企業・ガバナンス","Empresas y gobierno corporativo","Компании и корпоративное управление","الشركات والحوكمة","Makampuni na utawala")
add("기업재무 & 배당주 인텔리전스","Corporate Finance & Dividend Intelligence","企业财务与股息股情报","企業財務と配当株インテリジェンス","Finanzas corporativas e inteligencia de dividendos","Корпоративные финансы и дивиденды","المالية المؤسسية ومعلومات الأسهم الموزعة","Fedha za makampuni na habari za gawio")
add("도시·공간경제학 & 부동산 자산 전략","Urban Economics & Real Estate Strategy","城市·空间经济学与房地产资产战略","都市・空間経済学と不動産資産戦略","Economía urbana y estrategia inmobiliaria","Городская экономика и стратегия недвижимости","اقتصاد المدن واستراتيجية الأصول العقارية","Uchumi wa miji na mikakati ya nyumba")
add("문화 & 영화 산업","Culture & Film Industry","文化与电影产业","文化と映画産業","Cultura e industria del cine","Культура и киноиндустрия","الثقافة وصناعة السينما","Utamaduni na tasnia ya filamu")
add("문화 & 음악산업","Culture & Music Industry","文化与音乐产业","文化と音楽産業","Cultura e industria musical","Культура и музыкальная индустрия","الثقافة وصناعة الموسيقى","Utamaduni na tasnia ya muziki")
add("문화 & 축제 경제 거버넌스","Culture & Festival Economy Governance","文化与节日经济治理","文化と祭り経済ガバナンス","Cultura y gobernanza de la economía de festivales","Культура и управление фестивальной экономикой","الثقافة وحوكمة اقتصاد المهرجانات","Utamaduni na utawala wa uchumi wa tamasha")
add("문화·공간경제","Culture & Spatial Economy","文化·空间经济","文化・空間経済","Cultura y economía del espacio","Культура и пространственная экономика","الثقافة واقتصاد المكان","Utamaduni na uchumi wa nafasi")
add("문화·공연","Culture & Performance","文化·演出","文化・公演","Cultura y espectáculos","Культура и представления","الثقافة والعروض","Utamaduni na maonyesho")
add("문화·영화","Culture & Film","文化·电影","文化・映画","Cultura y cine","Культура и кино","الثقافة والسينما","Utamaduni na filamu")
add("문화유산 & 국가유산 정책","Cultural Heritage & National Heritage Policy","文化遗产与国家遗产政策","文化遺産と国家遺産政策","Patrimonio cultural y política de patrimonio nacional","Культурное наследие и государственная политика","التراث الثقافي وسياسة التراث الوطني","Urithi wa tamaduni na sera za kitaifa")
add("문화콘텐츠 & 지식사회","Cultural Content & Knowledge Society","文化内容与知识社会","文化コンテンツと知識社会","Contenidos culturales y sociedad del conocimiento","Культурный контент и общество знаний","المحتوى الثقافي ومجتمع المعرفة","Maudhui ya tamaduni na jamii ya maarifa")
add("방송 브리핑 & 국제 정치","Broadcast Briefing & International Politics","广播简报与国际政治","放送ブリーフィングと国際政治","Resumen informativo y política internacional","Эфирный брифинг и мировая политика","موجز البث والسياسة الدولية","Taarifa za runinga na siasa za kimataifa")
add("방송 브리핑 & 시사 분석","Broadcast Briefing & Current Affairs","广播简报与时事分析","放送ブリーフィングと時事分析","Resumen informativo y análisis de actualidad","Эфирный брифинг и анализ событий","موجز البث وتحليل الأحداث","Taarifa za runinga na uchambuzi")
add("방송·교육경제","Broadcast & Education Economics","广播·教育经济","放送・教育経済","Difusión y economía de la educación","Вещание и экономика образования","البث واقتصاد التعليم","Runinga na uchumi wa elimu")
add("방송·금융문해력","Broadcast & Financial Literacy","广播·金融素养","放送・金融リテラシー","Difusión y educación financiera","Вещание и финансовая грамотность","البث والثقافة المالية","Runinga na elimu ya fedha")
add("방송·문화산업","Broadcast & Culture Industry","广播·文化产业","放送・文化産業","Difusión e industria cultural","Вещание и культурная индустрия","البث والصناعة الثقافية","Runinga na tasnia ya tamaduni")
add("방송·보건경제","Broadcast & Health Economics","广播·健康经济","放送・健康経済","Difusión y economía de la salud","Вещание и экономика здравоохранения","البث واقتصاد الصحة","Runinga na uchumi wa afya")
add("방송·정치사회","Broadcast & Political Society","广播·政治社会","放送・政治社会","Difusión y sociedad política","Вещание и политическое общество","البث والمجتمع السياسي","Runinga na jamii ya kisiasa")
add("밸류업 & 기업재무 인텔리전스","Value-up & Corporate Finance Intelligence","价值提升与企业财务情报","バリューアップと企業財務インテリジェンス","Value-up e inteligencia de finanzas corporativas","Value-up и корпоративные финансы","تعزيز القيمة ومعلومات المالية المؤسسية","Kuongeza thamani na habari za fedha")
add("부동산 & 거시경제 자산배분","Real Estate & Macro Asset Allocation","房地产与宏观经济资产配置","不動産とマクロ資産配分","Inmobiliaria y asignación macro de activos","Недвижимость и макрораспределение активов","العقارات وتخصيص الأصول الكلي","Nyumba na mgawanyo wa mali")
add("부동산 공간경제학 & 자산배분 전략","Real Estate Spatial Economics & Asset Strategy","房地产空间经济学与资产配置战略","不動産空間経済学と資産配分戦略","Economía espacial inmobiliaria y estrategia de activos","Пространственная экономика недвижимости","الاقتصاد المكاني للعقارات واستراتيجية الأصول","Uchumi wa nafasi ya nyumba na mikakati")
add("사회 & 공공 질서 정책","Society & Public Order Policy","社会与公共秩序政策","社会と公共秩序政策","Sociedad y política de orden público","Общество и политика общественного порядка","المجتمع وسياسة النظام العام","Jamii na sera za utulivu wa umma")
add("사회 & 교육 정책","Society & Education Policy","社会与教育政策","社会と教育政策","Sociedad y política educativa","Общество и образовательная политика","المجتمع وسياسة التعليم","Jamii na sera za elimu")
add("사회 & 노동 정책","Society & Labor Policy","社会与劳动政策","社会と労働政策","Sociedad y política laboral","Общество и трудовая политика","المجتمع وسياسة العمل","Jamii na sera za kazi")
add("사회 & 청년 정책","Society & Youth Policy","社会与青年政策","社会と青年政策","Sociedad y política de juventud","Общество и молодёжная политика","المجتمع وسياسة الشباب","Jamii na sera za vijana")
add("사회·디지털 안전","Society & Digital Safety","社会·数字安全","社会・デジタル安全","Sociedad y seguridad digital","Общество и цифровая безопасность","المجتمع والسلامة الرقمية","Jamii na usalama wa kidijitali")
add("사회·생활정책","Society & Everyday Policy","社会·生活政策","社会・生活政策","Sociedad y políticas de vida diaria","Общество и бытовая политика","المجتمع وسياسات الحياة اليومية","Jamii na sera za maisha")
add("사회·소상공인","Society & Small Business Owners","社会·小工商户","社会・小商工人","Sociedad y pequeños comerciantes","Общество и малый бизнес","المجتمع وأصحاب المتاجر الصغيرة","Jamii na wafanyabiashara wadogo")
add("사회·주거복지","Society & Housing Welfare","社会·居住福利","社会・住宅福祉","Sociedad y bienestar de vivienda","Общество и жилищное благополучие","المجتمع ورفاهية السكن","Jamii na ustawi wa makazi")
add("사회·주거정책","Society & Housing Policy","社会·居住政策","社会・住宅政策","Sociedad y política de vivienda","Общество и жилищная политика","المجتمع وسياسة الإسكان","Jamii na sera za makazi")
add("사회·행정","Society & Administration","社会·行政","社会・行政","Sociedad y administración","Общество и администрация","المجتمع والإدارة","Jamii na utawala")
add("사회문화 비평 & 지식사회학","Sociocultural Criticism & Sociology of Knowledge","社会文化批评与知识社会学","社会文化批評と知識社会学","Crítica sociocultural y sociología del conocimiento","Социокультурная критика и социология знания","النقد الاجتماعي الثقافي وعلم اجتماع المعرفة","Ukosoaji wa kitamaduni na sosholojia")
add("산업 & 모빌리티","Industry & Mobility","产业与出行","産業とモビリティ","Industria y movilidad","Промышленность и мобильность","الصناعة والتنقل","Viwanda na usafiri")
add("산업 & 반도체 패권","Industry & Semiconductor Hegemony","产业与半导体霸权","産業と半導体覇権","Industria y hegemonía de semiconductores","Промышленность и лидерство в полупроводниках","الصناعة والهيمنة على أشباه الموصلات","Viwanda na uongozi wa semiconductors")
add("소비자학·인구경제학","Consumer Studies & Population Economics","消费者学·人口经济学","消費者学・人口経済学","Estudios del consumidor y economía de la población","Потребительские исследования и демоэкономика","دراسات المستهلك واقتصاد السكان","Masomo ya watumiaji na uchumi wa watu")
add("소비트렌드·산업","Consumer Trends & Industry","消费趋势·产业","消費トレンド・産業","Tendencias de consumo e industria","Потребительские тренды и промышленность","اتجاهات الاستهلاك والصناعة","Mitindo ya matumizi na viwanda")
add("소비트렌드·생활경제","Consumer Trends & Everyday Economy","消费趋势·生活经济","消費トレンド・生活経済","Tendencias de consumo y economía cotidiana","Потребительские тренды и повседневная экономика","اتجاهات الاستهلاك واقتصاد الحياة اليومية","Mitindo ya matumizi na uchumi wa maisha")
add("외환 & 지정학","FX & Geopolitics","外汇与地缘政治","為替と地政学","Divisas y geopolítica","Валюта и геополитика","الصرف الأجنبي والجيوسياسية","Fedha za kigeni na siasa za kijiografia")
add("원자재 & 산업 금융 인텔리전스","Commodities & Industrial Finance Intelligence","原材料与产业金融情报","原材料と産業金融インテリジェンス","Materias primas e inteligencia financiera industrial","Сырьё и промышленные финансы","المواد الخام ومعلومات التمويل الصناعي","Malighafi na habari za fedha za viwanda")
add("재벌·기업지배구조","Chaebol & Corporate Governance","财阀·企业治理结构","財閥・企業ガバナンス","Chaebol y gobierno corporativo","Чеболи и корпоративное управление","التشيبول وحوكمة الشركات","Chaebol na utawala wa makampuni")
add("재벌·소비트렌드","Chaebol & Consumer Trends","财阀·消费趋势","財閥・消費トレンド","Chaebol y tendencias de consumo","Чеболи и потребительские тренды","التشيبول واتجاهات الاستهلاك","Chaebol na mitindo ya matumizi")
add("정치 & 국방 정책","Politics & Defense Policy","政治与国防政策","政治と国防政策","Política y política de defensa","Политика и оборонная политика","السياسة وسياسة الدفاع","Siasa na sera za ulinzi")
add("정치·금융지배구조","Politics & Financial Governance","政治·金融治理结构","政治・金融ガバナンス","Política y gobernanza financiera","Политика и финансовое управление","السياسة وحوكمة المالية","Siasa na utawala wa fedha")
add("정치·기술","Politics & Technology","政治·技术","政治・技術","Política y tecnología","Политика и технологии","السياسة والتقنية","Siasa na teknolojia")
add("정치·외교안보","Politics & Diplomacy/Security","政治·外交安全","政治・外交安保","Política y diplomacia/seguridad","Политика и дипломатия/безопасность","السياسة والدبلوماسية والأمن","Siasa na diplomasia/usalama")
add("정치·자본시장","Politics & Capital Markets","政治·资本市场","政治・資本市場","Política y mercados de capital","Политика и рынки капитала","السياسة وأسواق رأس المال","Siasa na masoko ya mtaji")
add("정치·재정","Politics & Public Finance","政治·财政","政治・財政","Política y hacienda pública","Политика и бюджет","السياسة والمالية العامة","Siasa na fedha za umma")
add("🌍 글로벌 지정학","🌍 Global Geopolitics","🌍 全球地缘政治","🌍 グローバル地政学","🌍 Geopolítica global","🌍 Глобальная геополитика","🌍 الجيوسياسية العالمية","🌍 Siasa za kijiografia")
add("🎥 🎬 유튜브 (글로벌 영상 아카이브)","🎥 🎬 YouTube (Global Video Archive)","🎥 🎬 YouTube（全球视频档案）","🎥 🎬 YouTube（グローバル映像アーカイブ）","🎥 🎬 YouTube (Archivo de vídeo global)","🎥 🎬 YouTube (глобальный видеоархив)","🎥 🎬 يوتيوب (أرشيف الفيديو العالمي)","🎥 🎬 YouTube (Kumbukumbu za video)")
add("🏢 산업·기업·부동산","🏢 Industry, Business & Real Estate","🏢 产业·企业·房地产","🏢 産業・企業・不動産","🏢 Industria, empresa e inmobiliaria","🏢 Промышленность, бизнес и недвижимость","🏢 الصناعة والشركات والعقارات","🏢 Viwanda, biashara na nyumba")
add("📊 거시경제·금융","📊 Macro & Finance","📊 宏观经济·金融","📊 マクロ経済・金融","📊 Macro y finanzas","📊 Макроэкономика и финансы","📊 الاقتصاد الكلي والمالية","📊 Uchumi mkubwa na fedha")
add("📚 ⚡ AI·글쓰기·프로젝트 & AI 프롬프트","📚 ⚡ AI, Writing, Projects & AI Prompts","📚 ⚡ AI·写作·项目与AI提示词","📚 ⚡ AI・ライティング・プロジェクトとAIプロンプト","📚 ⚡ IA, escritura, proyectos y prompts de IA","📚 ⚡ ИИ, письмо, проекты и промпты","📚 ⚡ الذكاء الاصطناعي والكتابة والمشاريع والأوامر","📚 ⚡ AI, uandishi, miradi na maelekezo")
add("📚 🌏 PSB (소셜리스닝 & 시대 키워드)","📚 🌏 PSB (Social Listening & Zeitgeist Keywords)","📚 🌏 PSB（社交聆听与时代关键词）","📚 🌏 PSB（ソーシャルリスニングと時代キーワード）","📚 🌏 PSB (Escucha social y palabras clave de la época)","📚 🌏 PSB (соцмониторинг и ключевые слова эпохи)","📚 🌏 PSB (الاستماع الاجتماعي وكلمات العصر)","📚 🌏 PSB (Kusikiliza mitandao na maneno muhimu)")
add("📚 🏢 Biz (기업·경영·재벌사)","📚 🏢 Biz (Companies, Management & Chaebol History)","📚 🏢 Biz（企业·经营·财阀史）","📚 🏢 Biz（企業・経営・財閥史）","📚 🏢 Biz (Empresas, gestión e historia de chaebol)","📚 🏢 Biz (компании, менеджмент и история чеболей)","📚 🏢 Biz (الشركات والإدارة وتاريخ التشيبول)","📚 🏢 Biz (Makampuni, usimamizi na historia ya chaebol)")
add("📚 💰 Consumers (소비자학·소비트렌드)","📚 💰 Consumers (Consumer Studies & Trends)","📚 💰 Consumers（消费者学·消费趋势）","📚 💰 Consumers（消費者学・消費トレンド）","📚 💰 Consumers (Estudios y tendencias del consumidor)","📚 💰 Consumers (потребительские исследования и тренды)","📚 💰 Consumers (دراسات المستهلك والاتجاهات)","📚 💰 Consumers (Masomo na mitindo ya watumiaji)")
add("📚 💻 GlobalDB (글로벌 지정학·국가DB)","📚 💻 GlobalDB (Global Geopolitics & Country DB)","📚 💻 GlobalDB（全球地缘政治·国家数据库）","📚 💻 GlobalDB（グローバル地政学・国家DB）","📚 💻 GlobalDB (Geopolítica global y base de datos de países)","📚 💻 GlobalDB (глобальная геополитика и база стран)","📚 💻 GlobalDB (الجيوسياسية العالمية وقاعدة بيانات الدول)","📚 💻 GlobalDB (Siasa za dunia na data za nchi)")
add("📚 🔍 Economy (거시경제·금융·투자)","📚 🔍 Economy (Macro, Finance & Investment)","📚 🔍 Economy（宏观经济·金融·投资）","📚 🔍 Economy（マクロ経済・金融・投資）","📚 🔍 Economy (Macro, finanzas e inversión)","📚 🔍 Economy (макроэкономика, финансы, инвестиции)","📚 🔍 Economy (الاقتصاد الكلي والمالية والاستثمار)","📚 🔍 Economy (Uchumi mkubwa, fedha na uwekezaji)")
add("📚 🔠 Contents (문화·예술·인문·콘텐츠)","📚 🔠 Contents (Culture, Arts, Humanities & Content)","📚 🔠 Contents（文化·艺术·人文·内容）","📚 🔠 Contents（文化・芸術・人文・コンテンツ）","📚 🔠 Contents (Cultura, artes, humanidades y contenidos)","📚 🔠 Contents (культура, искусство, гуманитарные науки)","📚 🔠 Contents (الثقافة والفنون والإنسانيات والمحتوى)","📚 🔠 Contents (Utamaduni, sanaa na maudhui)")
add("경제·무역","Economy & Trade","经济·贸易","経済・貿易","Economía y comercio","Экономика и торговля","الاقتصاد والتجارة","Uchumi na biashara")
add("경제·월간 리뷰","Economy & Monthly Review","经济·月度回顾","経済・月次レビュー","Economía y revisión mensual","Экономика и месячный обзор","الاقتصاد والمراجعة الشهرية","Uchumi na mapitio ya mwezi")
add("경제·주간 리뷰","Economy & Weekly Review","经济·每周回顾","経済・週次レビュー","Economía y revisión semanal","Экономика и недельный обзор","الاقتصاد والمراجعة الأسبوعية","Uchumi na mapitio ya wiki")
add("경제·해외증시","Economy & Global Stock Markets","经济·海外股市","経済・海外株式市場","Economía y bolsas internacionales","Экономика и зарубежные рынки","الاقتصاد والأسواق الأجنبية","Uchumi na masoko ya hisa za nje")
add("국제·사회","International & Society","国际·社会","国際・社会","Internacional y sociedad","Международное и общество","الدولية والمجتمع","Kimataifa na jamii")
add("문화·전시","Culture & Exhibitions","文化·展览","文化・展示","Cultura y exposiciones","Культура и выставки","الثقافة والمعارض","Utamaduni na maonyesho")
add("사회","Society","社会","社会","Sociedad","Общество","المجتمع","Jamii")
add("📚 🚕 Industry (산업·기술·반도체·모빌리티)","📚 🚕 Industry (Industry, Tech, Chips & Mobility)","📚 🚕 Industry（产业·技术·半导体·出行）","📚 🚕 Industry（産業・技術・半導体・モビリティ）","📚 🚕 Industry (Industria, tecnología, chips y movilidad)","📚 🚕 Industry (промышленность, технологии, чипы, мобильность)","📚 🚕 Industry (الصناعة والتقنية والرقائق والتنقل)","📚 🚕 Industry (Viwanda, teknolojia, chipsi na usafiri)")
add("📚 🧛‍♂️ Government (정치·정부·정책)","📚 🧛‍♂️ Government (Politics, Government & Policy)","📚 🧛‍♂️ Government（政治·政府·政策）","📚 🧛‍♂️ Government（政治・政府・政策）","📚 🧛‍♂️ Government (Política, gobierno y políticas)","📚 🧛‍♂️ Government (политика, правительство, политика)","📚 🧛‍♂️ Government (السياسة والحكومة والسياسات)","📚 🧛‍♂️ Government (Siasa, serikali na sera)")
add("🔠 문화·콘텐츠","🔠 Culture & Content","🔠 文化·内容","🔠 文化・コンテンツ","🔠 Cultura y contenidos","🔠 Культура и контент","🔠 الثقافة والمحتوى","🔠 Utamaduni na maudhui")
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
