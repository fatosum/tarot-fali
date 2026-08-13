import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Tarot Bakımı",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Beyaz/gold tül dalgaları ve yıldız tozlu arka plan estetiği
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background: 
    radial-gradient(circle at 50% 30%, rgba(255, 255, 255, 0.07) 0%, transparent 60%),
    linear-gradient(135deg, #0b0714 0%, #161026 50%, #08040d 100%);
color: #f3f4f6;
font-family: 'Cinzel', 'Inter', serif;
background-attachment: fixed;
}

h1, h2, h3 { 
color: #fef08a !important; 
font-family: 'Cinzel', serif; 
text-shadow: 0 2px 10px rgba(255, 215, 0, 0.2);
}
p, label, span { color: #e2e8f0 !important; }

.stButton>button {
width: 100%;
background: linear-gradient(135deg, #c59b27 0%, #8a6414 100%);
color: #ffffff;
border-radius: 12px;
font-size: 16px;
height: 50px;
border: 1px solid #ffd700;
font-weight: 600;
box-shadow: 0 4px 20px rgba(197, 155, 39, 0.4);
transition: all 0.3s ease;
}
.stButton>button:hover {
background: linear-gradient(135deg, #e5b83b 0%, #c59b27 100%);
box-shadow: 0 6px 25px rgba(229, 184, 59, 0.6);
}

.tarot-card-box {
background: rgba(22, 14, 38, 0.85);
border: 1px solid rgba(197, 155, 39, 0.4);
padding: 24px;
border-radius: 16px;
margin-bottom: 20px;
backdrop-filter: blur(16px);
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
}

.tarot-back {
background: 
    radial-gradient(circle at 50% 50%, rgba(255, 215, 0, 0.15) 0%, transparent 70%),
    linear-gradient(135deg, #12091f 0%, #221438 50%, #12091f 100%);
border: 2px solid #dfb135;
border-radius: 14px;
width: 100%;
height: 140px;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
text-align: center;
box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), inset 0 0 18px rgba(212, 175, 55, 0.3);
margin-bottom: 4px;
transition: all 0.3s ease;
}

.tarot-back:hover {
transform: translateY(-4px);
border-color: #ffe875;
box-shadow: 0 10px 25px rgba(212, 175, 55, 0.5);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


def burc_hesapla(dogum_tarihi):
  gun = dogum_tarihi.day
  ay = dogum_tarihi.month

  if (ay == 3 and gun >= 21) or (ay == 4 and gun <= 20):
    return "Koç"
  elif (ay == 4 and gun >= 21) or (ay == 5 and gun <= 20):
    return "Boğa"
  elif (ay == 5 and gun >= 21) or (ay == 6 and gun <= 21):
    return "İkizler"
  elif (ay == 6 and gun >= 22) or (ay == 7 and gun <= 22):
    return "Yengeç"
  elif (ay == 7 and gun >= 23) or (ay == 8 and gun <= 22):
    return "Aslan"
  elif (ay == 8 and gun >= 23) or (ay == 9 and gun <= 22):
    return "Başak"
  elif (ay == 9 and gun >= 23) or (ay == 10 and gun <= 23):
    return "Terazi"
  elif (ay == 10 and gun >= 24) or (ay == 11 and gun <= 21):
    return "Akrep"
  elif (ay == 11 and gun >= 22) or (ay == 12 and gun <= 21):
    return "Yay"
  elif (ay == 12 and gun >= 22) or (ay == 1 and gun <= 19):
    return "Oğlak"
  elif (ay == 1 and gun >= 20) or (ay == 2 and gun <= 18):
    return "Kova"
  else:
    return "Balık"
tarot_veritabani = {
    # --- BÜYÜK ARKANA (0 - 21) ---
    "0 - DİVANE / APTAL (THE FOOL)": {
        "duz_gecmis": "Geçmişte büyük riskler almış, hiçbir şeyin seni durdurmasına izin vermeden saf bir cesaretle yola çıkmışsın.",
        "duz_simdi": "Şu an hayatında yepyeni bir sayfa açılıyor; içindeki saf merakla bilinmeyene adım atıyorsun.",
        "duz_gelecek": "Gelecekte karşına taptaze fırsatlar çıkacak, sıfırdan başlayacağın maceralar seni bekliyor.",
        "ters_gecmis": "Geçmişte düşüncesizce atılan adımlar ve hesapsız riskler başına bazı işler açmış.",
        "ters_simdi": "Şu an bir adım atmaktan korkuyor, korkaklık ile saflık arasında sıkışıp kalmış durumdasın.",
        "ters_gelecek": "Gelecekte potansiyel fırsatları kaçırmamak için aşırı temkinli yapından biraz sıyrılman gerekecek."
    },
    "1 - BÜYÜCÜ (THE MAGICIAN)": {
        "duz_gecmis": "Geçmişte elindeki tüm yetenekleri ve araçları ustalıkla bir araya getirerek somut başarılar elde etmişsin.",
        "duz_simdi": "Şu an kaderini kendi ellerinle yazma gücüne ve iradesine sahipsin; ne dilesen gerçeğe dönüştürebilirsin.",
        "duz_gelecek": "Gelecekte projelerini hayata geçirmek için harika bir döneme girecek, etrafını büyüleyeceksin.",
        "ters_gecmis": "Geçmişte yeteneklerini yanlış yönlendirmiş ya da potansiyelini manipülasyon için harcamış olabilirsin.",
        "ters_simdi": "Şu an elindeki imkanları kullanamıyor, enerjini dağınık harcıyor ve kendine güvensizlik duyuyorsun.",
        "ters_gelecek": "Gelecekte aldatıcı durumlara ve potansiyelini harcamaya karşı dikkatli olmalısın."
    },
    "2 - AZİZE (THE HIGH PRIESTESS)": {
        "duz_gecmis": "Geçmişte mantığından ziyade iç sesine ve sezgilerine kulak vererek doğru kararlar almışsın.",
        "duz_simdi": "Şu an dış dünyadan uzaklaşıp kendi iç sesini dinlemen, sırları ve görünmeyen gerçeği fark etmen gerekiyor.",
        "duz_gelecek": "Gelecekte sezgilerinin seni asla yanıltmadığını görecek, manevi olarak derinleşeceksin.",
        "ters_gecmis": "Geçmişte iç sesini bastırmış, sezgilerini görmezden gelerek hatalı yollara sapmışsın.",
        "ters_simdi": "Şu an içsel sesinle olan bağın zayıflamış durumda; bazı sırlar ya da saklanan gerçekler kafanı karıştırıyor.",
        "ters_gelecek": "Gelecekte dedikodulara ve sezgilerini yanlış yorumlamaya karşı uyanık olmalısın."
    },
    "3 - İMPARATORİÇE (THE EMPRESS)": {
        "duz_gecmis": "Geçmişte bolluk, bereket, yaratıcılık ve sevgi dolu bir besleme dönemi geride kalmış.",
        "duz_simdi": "Şu an üretkenliğin zirvesindesin; doğayla uyum içinde, hayatın tadını çıkaran bir enerjiye sahipsin.",
        "duz_gelecek": "Gelecekte maddi ve manevi anlamda büyük bir bolluk, büyüme ve huzur seni bekliyor.",
        "ters_gecmis": "Geçmişte aşırı düşkünlük ya da tükenmişlik hissi yaratıcılığını tıkamış.",
        "ters_simdi": "Şu an kendini ihmal etmiş hissedebilir, üretkenlikte düşüş ve şefkat eksikliği yaşayabilirsin.",
        "ters_gelecek": "Gelecekte öz bakımına ve kişisel sınırlarına daha çok dikkat etmen gerekebilir."
    },
    "4 - İMPARATOR (THE EMPEROR)": {
        "duz_gecmis": "Geçmişte hayatına çeki düzen vermiş, güçlü bir disiplin ve otorite kurarak sağlam temeller atmışsın.",
        "duz_simdi": "Şu an hayatında kontrolü eline alma, kuralları koyma ve liderlik etme zamanındasın.",
        "duz_gelecek": "Gelecekte iş ve kariyer hayatında sağlam bir konuma gelecek, düzeni kuracaksın.",
        "ters_gecmis": "Geçmişte aşırı baskıcı ya da katı tutumların çevrendekilerle çatışma yaratmış.",
        "ters_simdi": "Şu an otorite figürleriyle sorunlar yaşıyor ya da hayatındaki kontrolü tamamen kaybetmiş hissediyorsun.",
        "ters_gelecek": "Gelecekte katı kurallardan esneklik kazanmaya doğru evrilmen gerekecek."
    },
    "5 - HİEROFANT / AZİZ (THE HIEROPHANT)": {
        "duz_gecmis": "Geçmişte geleneksel değerlere bağlı kalmış, kurallara uyarak güvenli yollardan yürümüşsün.",
        "duz_simdi": "Şu an bir mentorun rehberliğine ihtiyaç duyabilir ya da toplumsal kurallara uyum sağlayabilirsin.",
        "duz_gelecek": "Gelecekte resmi anlaşmalar, evlilik veya toplumsal kabul gören kalıcı adımlar atabilirsin.",
        "ters_gecmis": "Geçmişte kalıplaşmış kurallara başkaldırmış, gelenekleri yıkmışsın.",
        "ters_simdi": "Şu an dogmalardan sıkılmış, kendi inanç sistemini kurmak istiyor ancak arada kalmış hissediyorsun.",
        "ters_gelecek": "Gelecekte gelenek dışı seçimler yaparken yakın çevrenin tepkileriyle karşılaşabilirsin."
    },
    "6 - AŞIKLAR (THE LOVERS)": {
        "duz_gecmis": "Geçmişte hayatını kökten değiştiren büyük bir değerler veya ilişki seçimi yapmışsın.",
        "duz_simdi": "Şu an kalbinle mantığın arasında kaldığın kritik bir dönemeçtesin; uyum ve bağ arıyorsun.",
        "duz_gelecek": "Gelecekte hayatını birleştireceğin ortaklıklar ya da ruhuna hitap eden harika bir birliktelik kapıda.",
        "ters_gecmis": "Geçmişte yanlış bir ilişki ya da hatalı bir ortaklık seçiminden dolayı pişmanlıklar yaşamışsın.",
        "ters_simdi": "Şu an değerler çatışması yaşıyor, kararsızlıklar içinde bocalıyorsun.",
        "ters_gelecek": "Gelecekte ilişkilerde yaşanan uyumsuzlukları çözmek için dürüst yüzleşmeler yapman gerekecek."
    },
    "7 - SAVAŞ ARABASI (THE CHARIOT)": {
        "duz_gecmis": "Geçmişte büyük engelleri iradenle aşmış, kararlılıkla hedefine kilitlenip zafer kazanmışsın.",
        "duz_simdi": "Şu an tüm zıt enerjileri kontrolün altında tutarak hızla ilerliyor, zafer için direksiyonu sıkı tutuyorsun.",
        "duz_gelecek": "Gelecekte rakiplerini geride bırakacak ve uzun süredir istediğin başarıya ulaşacaksın.",
        "ters_gecmis": "Geçmişte kontrolü kaybettiğin için projelerin yarım kalmış veya yön duygusu kaybolmuş.",
        "ters_simdi": "Şu an iki farklı yöne çekiliyormuş gibi hissediyor, iradeni toplamakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte aceleci kararların kazalara veya başarısızlıklara yol açmaması için yavaşlamalısın."
    },
    "8 - GÜÇ (STRENGTH)": {
        "duz_gecmis": "Geçmişte kaba kuvvetle değil, sabır, şefkat ve içsel cesaretle büyük bir zorluğun üstesinden gelmişsin.",
        "duz_simdi": "Şu an kendi içsel gücünü keşfediyor, en vahşi dürtülerini bile zarafetle dizginliyorsun.",
        "duz_gelecek": "Gelecekte özgüvenin sayesinde en sert sorunları bile tatlılıkla ve başarıyla çözeceksin.",
        "ters_gecmis": "Geçmişte özgüven eksikliği yaşamış, içsel gücünü başkalarına kaptırmışsın.",
        "ters_simdi": "Şu an sabrın tükeniyor gibi hissedebilir, öfke kontrolü konusunda zorlanabilirsin.",
        "ters_gelecek": "Gelecekte kendine olan inancını yeniden tazeleyerek içsel korkularını yeneceksin."
    },
    "9 - ERMİŞ (THE HERMIT)": {
        "duz_gecmis": "Geçmişte kalabalıklardan uzaklaşıp kendi içine dönmüş, ruhsal bir arayış ve bilgelik dönemi geçirmişsin.",
        "duz_simdi": "Şu an dünyevi gürültüden uzaklaşıp kendi iç ışığını bulma, mola verme ve aydınlanma zamanındasın.",
        "duz_gelecek": "Gelecekte aradığın derin cevapları kendi iç dünyanda bulacak, başkalarına da ışık olacaksın.",
        "ters_gecmis": "Geçmişte aşırı yalnızlık çekmiş, dünyadan koparak depresif bir izolasyon yaşamışsın.",
        "ters_simdi": "Şu an insanlardan kaçıyor ama bunu yalnızlaşmak için değil adeta kaybolmak için yapıyorsun.",
        "ters_gelecek": "Gelecekte tekrar topluma karışacak, kabuğundan dışarı çıkmaya başlayacaksın."
    },
    "10 - KADER ÇARKI (WHEEL OF FORTUNE)": {
        "duz_gecmis": "Geçmişte kaderin akışını değiştiren ani ve beklenmedik dönüm noktaları yaşamışsın.",
        "duz_simdi": "Şu an çark senin lehine dönüyor; şansın ve fırsatların kapını çaldığı ilahi bir akıştasın.",
        "duz_gelecek": "Gelecekte hayatında köklü ve olumlu döngüsel değişimler seni bekliyor.",
        "ters_gecmis": "Geçmişte şanssızlıklar silsilesi ve ardı arkası kesilmeyen aksilikler seni yormuş.",
        "ters_simdi": "Şu an işlerin ters gittiğini hissedebilir, kötü giden bir döngünün içinde sıkışmış gibi hissedebilirsin.",
        "ters_gelecek": "Gelecekte bu kötü şans döngüsü kırılacak, sabırlı olman gereken bir döneme giriyorsun."
    },
    "11 - ADALET (JUSTICE)": {
        "duz_gecmis": "Geçmişte tamamen mantık, hakkaniyet ve dürüstlük çerçevesinde kararlar alıp ektiklerini biçmişsin.",
        "duz_simdi": "Şu an attığın adımların sonuçlarıyla yüzleşiyor, hak ettiğin dengeli kararı bekliyorsun.",
        "duz_gelecek": "Gelecekte hukuki veya resmi konularda adalet yerini bulacak, haklılığın tescillenecek.",
        "ters_gecmis": "Geçmişte haksızlığa uğramış ya da adil olmayan yargılarda bulunmuş olabilirsin.",
        "ters_simdi": "Şu an hayatında bir dengesizlik var; sorumluluklardan kaçma eğilimin artmış.",
        "ters_gelecek": "Gelecekte dürüstlükten şaşmamak ve tarafsız kalmak geleceğini kurtaracak."
    },
    "12 - ASILAN ADAM (THE HANGED MAN)": {
        "duz_gecmis": "Geçmişte olayların akışına teslim olmuş, fedakarlık yaparak bakış açını tamamen değiştirmişsin.",
        "duz_simdi": "Şu an her şey askıda gibi görünse de bu duraklama sana olaylara dışarıdan bakma fırsatı veriyor.",
        "duz_gelecek": "Gelecekte yaşadığın bu duraksama dönemi sana bambaşka bir vizyon ve aydınlanma getirecek.",
        "ters_gecmis": "Geçmişte gereksiz fedakarlıklar yapmış, kendini boşuna kurban etmişsin.",
        "ters_simdi": "Şu an direndiğin için işler sarpa sarıyor; bırakılması gereken şeyleri tutmakta ısrarcısın.",
        "ters_gelecek": "Gelecekte boşuna kürek çekmeyi bırakıp olayları akışına bıraktığında rahatlayacaksın."
    },
    "13 - ÖLÜM (DEATH)": {
        "duz_gecmis": "Geçmişte mijozunu, eski bir alışkanlığını veya bir dönemi tamamen bitirip geride bırakmışsın.",
        "duz_simdi": "Şu an köklü bir dönüşüm sürecindesin; eski olan ölüyor ki yerine yepyeni ve güçlü bir şey gelebilsin.",
        "duz_gelecek": "Gelecekte hayatında taşları yerinden oynatacak muazzam bir yenilenme ve yeniden doğuş var.",
        "ters_gecmis": "Geçmişte bitmesi gereken şeyleri uzatmış, değişime direnerek acı çekmişsin.",
        "ters_simdi": "Şu an değişimden korkuyor, geçmişe sıkı sıkıya tutunarak kaçınılmaz sonu geciktiriyorsun.",
        "ters_gelecek": "Gelecekte direnç göstermeyi bıraktığında bu dönüşümün ne kadar özgürleştirici olduğunu göreceksin."
    },
    "14 - DENGE / ÖLÇÜLÜLÜK (TEMPERANCE)": {
        "duz_gecmis": "Geçmişte zıtlıkları uyumla harmanlamış, sabırlı ve ılımlı tutumunla huzuru bulmuşsun.",
        "duz_simdi": "Şu an hayatında şifa, denge ve içsel huzur arayışı hakim; her şeyi kararınca yaşıyorsun.",
        "duz_gelecek": "Gelecekte taşlar yerine oturacak, sabrının meyvesini huzurlu bir dengeyle alacaksın.",
        "ters_gecmis": "Geçmişte aşırılıklar, sabırsızlıklar ve dengesiz ilişkiler seni yıpratmış.",
        "ters_simdi": "Şu an hayatın şirazesi kaymış durumda; aşırılıklardan kaçınmalı, orta yolu bulmalısın.",
        "ters_gelecek": "Gelecekte iç dengeni yeniden sağlamak için sakinleştirici ve dinlendirici adımlar atacaksın."
    },
    "15 - ŞEYTAN (THE DEVIL)": {
        "duz_gecmis": "Geçmişte toksik bağlar, maddiyata aşırı düşkünlük veya kötü alışkanlıklarca esir alınmışsın.",
        "duz_simdi": "Şu an seni aşağı çeken tutkuların, korkuların veya bağımlılıklarınla yüzleşiyorsun.",
        "duz_gelecek": "Gelecekte o görünmez zincirlerin aslında senin zihninde olduğunu fark edip özgürleşme şansı bulacaksın.",
        "ters_gecmis": "Geçmişte büyük bir bağımlılıktan veya toksik bir ilişkiden kurtulmayı başarmışsın.",
        "ters_simdi": "Şu an zincirlerini kırmaya başladığın, farkındalık kazandığın bir uyanış anındasın.",
        "ters_gelecek": "Gelecekte zihinsel tuzaklara bir daha düşmemek için güçlü sınırlar çizeceksin."
    },
    "16 - YIKIK KULE (THE TOWER)": {
        "duz_gecmis": "Geçmişte üzerine kurulu olduğu temeller çürük olan her şey ani ve sarsıcı bir şekilde yıkılmış.",
        "duz_simdi": "Şu an hayatında büyük bir şok veya ani bir gerçekle yüzleşme dönemi; kaos hâkim.",
        "duz_gelecek": "Gelecekte bu yıkım sayesinde yalanlar temizlenecek ve üzerine çok daha sağlam bir dünya kuracaksın.",
        "ters_gecmis": "Geçmişte büyük bir krizden kıl payı kurtulmuş ya da felaketi ertelemişsin.",
        "ters_simdi": "Şu an içten içe yıkımın farkındasın ama bunu bastırmaya, felaketi önlemeye çalışıyorsun.",
        "ters_gelecek": "Gelecekte kaçınılmaz olan o değişim gerçekleşecek ve sonunda rahat bir nefes alacaksın."
    },
    "17 - YILDIZ (THE STAR)": {
        "duz_gecmis": "Geçmişte fırtınalar kopmuş ama ardından içini ısıtan ilahi bir umut ve şifa doğmuş.",
        "duz_simdi": "Şu an geleceğe dair inancın taze, ilhamla dolusun ve evrenin seni koruduğunu hissediyorsun.",
        "duz_gelecek": "Gelecekte hayallerinin gerçeğe dönüştüğü, parlak, huzurlu ve şanslı bir dönem seni bekliyor.",
        "ters_gecmis": "Geçmişte umutsuzluğa kapılmış, inancını tamamen yitirmişsin.",
        "ters_simdi": "Şu an motivasyonun düşük, geleceğe dair şüpheler duyuyor ve kendini ışıksız hissediyorsun.",
        "ters_gelecek": "Gelecekte içindeki o sönen umut kıvılcımını yeniden parlatacak güzel haberler alacaksın."
    },
    "18 - AY (THE MOON)": {
        "duz_gecmis": "Geçmişte belirsizlikler, gizli düşmanlıklar ve kuruntu dolu korkular zihnini bulandırmış.",
        "duz_simdi": "Şu an suların bulanık olduğu, hiçbir şeyin göründüğü gibi olmadığı gizemli ve kuşkulu bir zamandasın.",
        "duz_gelecek": "Gelecekte sisler dağılacak, gerçeğin ne olduğunu net bir şekilde göreceksin.",
        "ters_gecmis": "Geçmişte kuruntuların ve paranoyaların yersiz olduğunu sonradan fark etmişsin.",
        "ters_simdi": "Şu an korkularının üzerine gitmeye başladığın, sis perdesini aralamaya çalıştığın bir an.",
        "ters_gelecek": "Gelecekte aldanmalara ve yanılsamalara karşı uyanık kalmayı öğreneceksin."
    },
    "19 - GÜNEŞ (THE SUN)": {
        "duz_gecmis": "Geçmişte büyük bir neşe, başarı, takdir görme ve mutluluk dönemi yaşamışsın.",
        "duz_simdi": "Şu an enerjin tavan yapmış durumda; her şey yolunda gidiyor, etrafa neşe saçıyorsun.",
        "duz_gelecek": "Gelecekte hayatın her alanında aydınlık, başarı ve tatmin dolu günler seni bekliyor.",
        "ters_gecmis": "Geçmişte mutluluğuna gölge düşmüş, hak ettiğin değeri görememişsin.",
        "ters_simdi": "Şu an içindeki neşe biraz sönmüş gibi görünse de ufak bir kıvılcımla yeniden parlayabilirsin.",
        "ters_gelecek": "Gelecekte bulutlar dağılacak ve güneş senin için yeniden tüm ihtişamıyla doğacak."
    },
    "20 - MAHKEME (JUDGEMENT)": {
        "duz_gecmis": "Geçmişte geçmişin muhasebesini yapmış, eski hatalardan arınarak uyanış yaşamışsın.",
        "duz_simdi": "Şu an hayatında bir dönüm noktasındasın; ilahi bir çağrı alıyor, büyük kararlar veriyorsun.",
        "duz_gelecek": "Gelecekte geçmişinle barışacak, yaptıklarının ödülünü alarak özgürleşeceksin.",
        "ters_gecmis": "Geçmişte sürekli kendini suçlamış, pişmanlıklarınla kendini kahretmişsin.",
        "ters_simdi": "Şu an sorumluluklardan kaçıyor, yapman gereken o büyük yüzleşmeyi erteliyorsun.",
        "ters_gelecek": "Gelecekte vicdan muhasebesini tamamlayıp nihayet huzurlu bir karara varacaksın."
    },
    "21 - DÜNYA (THE WORLD)": {
        "duz_gecmis": "Geçmişte uzun soluklu bir döngüyü başarıyla tamamlamış, büyük bir hedefe ulaşmışsın.",
        "duz_simdi": "Şu an bir devrin kapandığı, bütünleşme, mutluluk ve tamlanma hissinin doruğundaysın.",
        "duz_gelecek": "Gelecekte hayatında muazzam bir başarı, mezuniyet veya taçlanma dönemi seni bekliyor.",
        "ters_gecmis": "Geçmişte bir türlü kapatamadığın yarım kalan hikayeler seni yormuş.",
        "ters_simdi": "Şu an sona yaklaşmış olmana rağmen son adımı atmakta veya projeyi bitirmekte zorlanıyorsun.",
        "ters_gelecek": "Gelecekte o son engeli de aşarak hak ettiğin büyük kutlamayı yapacaksın."
    },

    # --- KÜÇÜK ARKANA: ASALAR (WANDS) ---
    "ASALARIN ASI (ACE OF WANDS)": {
        "duz_gecmis": "Geçmişte aniden alevlenen harika bir fikir veya tutkulu bir girişim başlatmışsın.",
        "duz_simdi": "Şu an içindeki yaratıcı ateş coşkuyla yanıyor; yeni bir projeye başlamak için mükemmel bir enerjidesin.",
        "duz_gelecek": "Gelecekte önünü açacak çok heyecan verici ve enerjik fırsatlar kapını çalacak.",
        "ters_gecmis": "Geçmişte heyecanla başlayan projeler motivasyon eksikliğinden sönüp gitmiş.",
        "ters_simdi": "Şu an enerjinin düşük olduğunu ve projelerinde erteleme eğilimi gösterdiğini hissedebilirsin.",
        "ters_gelecek": "Gelecekte fırsatları kaçırmamak için içindeki ateşi yeniden körüklemen gerekecek."
    },
    "ASALARIN İKİLİSİ (TWO OF WANDS)": {
        "duz_gecmis": "Geçmişte geleceğe yönelik büyük planlar yapmış, yeni ufuklar için strateji belirlemişsin.",
        "duz_simdi": "Şu an elinde seçenekler var; ya mevcut konumunda kalacaksın ya da dünyaya açılacaksın.",
        "duz_gelecek": "Gelecekte ortaklı büyük planların hayata geçeceği seyahatler veya girişimler olacak.",
        "ters_gecmis": "Geçmişte yanlış planlamalar ve korkak kararlar yüzünden fırsatlar kaçmış.",
        "ters_simdi": "Şu an gelecekten korkuyor, adım atmak ile mevcut alanda kalmak arasında kararsız kalıyorsun.",
        "ters_gelecek": "Gelecekte vizyonunu genişleterek bu kararsızlık döngüsünden çıkacaksın."
    },
    "ASALARIN ÜÇLÜSÜ (THREE OF WANDS)": {
        "duz_gecmis": "Geçmişte attığın adımların ilk meyvelerini toplamış, ufku genişletmişsin.",
        "duz_simdi": "Şu an beklediğin gemilerin limana yanaşmasını izliyor, gelecek için umutla dolusun.",
        "duz_gelecek": "Gelecekte ticari veya kişisel genişleme, yurtdışı bağlantılı işler seni bekliyor.",
        "ters_gecmis": "Geçmişte beklentiler boşa çıkmış, yatırımlar gecikmiş.",
        "ters_simdi": "Şu an işlerin yavaş gitmesinden ve planların gecikmesinden dolayı sabırsızlanıyorsun.",
        "ters_gelecek": "Gelecekte sabırlı bekleyişin karşılığını alacak ve doğru stratejiyi kuracaksın."
    },
    "ASALARIN DÖRDÜLSÜ (FOUR OF WANDS)": {
        "duz_gecmis": "Geçmişte aileyle, dostlarla kutlanan mutlu bir yuva veya düğün/kutlama dönemi olmuş.",
        "duz_simdi": "Şu an huzurun, güvenin ve kutlamanın tadını çıkarıyor, aidiyet hissediyorsun.",
        "duz_gelecek": "Gelecekte evlilik, yeni bir eve taşınma veya kalıcı huzur kutlamaları kapıda.",
        "ters_gecmis": "Geçmişte aile içi huzursuzluklar veya yarım kalmış kutlamalar yaşanmış.",
        "ters_simdi": "Şu an ev ortamında ya da ilişkilerde geçici bir gerginlik ve uyumsuzluk hissedebilirsin.",
        "ters_gelecek": "Gelecekte aradığın aile sıcaklığını ve güvenli limanı yeniden inşa edeceksin."
    },
    "ASALARIN BEŞLİSİ (FIVE OF WANDS)": {
        "duz_gecmis": "Geçmişte rekabet dolu, fikir çatışmalarının ve ego savaşlarının olduğu bir ortamdan geçmişsin.",
        "duz_simdi": "Şu an çevrendeki insanlarla fikir ayrılıkları yaşıyor, sesini duyurmaya çalışıyorsun.",
        "duz_gelecek": "Gelecekte bu rekabet ortamı seni daha güçlü kılacak ancak sabırlı olman gerekecek.",
        "ters_gecmis": "Geçmişte gereksiz tartışmalardan ve kavgacı ortamlardan kaçınmayı seçmişsin.",
        "ters_simdi": "Şu an çatışmalardan uzak durmaya çalışıyor, içsel bir sükunet arıyorsun.",
        "ters_gelecek": "Gelecekte anlaşmazlıkları uzlaşmacı bir dille geride bırakacaksın."
    },
    "ASALARIN ALTILISI (SIX OF WANDS)": {
        "duz_gecmis": "Geçmişte büyük bir başarı elde etmiş, herkesin takdirini toplayarak zafer kazanmışsın.",
        "duz_simdi": "Şu an emeklerinin karşılığını alıyor, haklı bir gurur ve özgüven yaşıyorsun.",
        "duz_gelecek": "Gelecekte topluluk önünde övgü alacağın, adından söz ettireceğin gelişmeler var.",
        "ters_gecmis": "Geçmişte başarıya çok yaklaşmışken son anda takdir görmemişsin.",
        "ters_simdi": "Şu an özgüvenin biraz zedelenmiş olabilir, hak ettiğin değeri göremediğini düşünüyorsun.",
        "ters_gelecek": "Gelecekte bu geçici gölge kalkacak ve yeniden parlayacaksın."
    },
    "ASALARIN YEDİLİSİ (SEVEN OF WANDS)": {
        "duz_gecmis": "Geçmişte kendi haklarını, pozisyonunu ve fikirlerini sonuna kadar savunmuşsun.",
        "duz_simdi": "Şu an birilerine veya eleştirilere karşı kendi mevziini savunmak zorunda olduğun bir zamandasın.",
        "duz_gelecek": "Gelecekte direncini koruduğun sürece karşına çıkan baskılara galip geleceksin.",
        "ters_gecmis": "Geçmişte baskılara boyun eğmiş ya da mücadeleden vazgeçmişsin.",
        "ters_simdi": "Şu an kendini tükenmiş hissediyor, artık insanlarla mücadele etmek istemiyorsun.",
        "ters_gelecek": "Gelecekte gereksiz savaşları bırakıp kendi huzurunu önceliklendireceksin."
    },
    "ASALARIN SEKİZLİSİ (EIGHT OF WANDS)": {
        "duz_gecmis": "Geçmişte her şey inanılmaz bir hızla gelişmiş, olaylar ardı ardına akmış.",
        "duz_simdi": "Şu an haberler çok hızlı geliyor; seyahatler, ani kararlar ve baş döndürücü bir tempo içindesin.",
        "duz_gelecek": "Gelecekte işlerin mucizevi bir hızla çözüleceği ve hareketli bir döneme gireceksin.",
        "ters_gecmis": "Geçmişte yaşanan ani gelişmeler planları altüst etmiş, gecikmeler yaşanmış.",
        "ters_simdi": "Şu an işlerin yavaşlamasından ya da yanlış anlaşılmalardan ötürü bir kaos hissediyorsun.",
        "ters_gelecek": "Gelecekte hızı kontrol altına alarak yanlış anlamaları düzelteceksin."
    },
    "ASALARIN DOKUZLUSU (NINE OF WANDS)": {
        "duz_gecmis": "Geçmişte çok yorulmuş ama pes etmeyerek sonuna kadar direnmeyi bilmişsin.",
        "duz_simdi": "Şu an diken üstündesin; daha önce yaşadığın yaralardan dolayı kendini koruma halindesin.",
        "duz_gelecek": "Gelecekte son bir engelin kaldı, biraz daha direnirsen zafer senin olacak.",
        "ters_gecmis": "Geçmişte paranoyalar ve tükenmişlik yüzünden erken havlu atmışsın.",
        "ters_simdi": "Şu an savunma duvarların çok yüksek, kimsenin yaklaşmasına izin vermiyorsun.",
        "ters_gelecek": "Gelecekte bu savunmacı zırhı yavaş yavaş üzerindne çıkaracaksın."
    },
    "ASALARIN ONLUSU (TEN OF WANDS)": {
        "duz_gecmis": "Geçmişte her sorumluluğu tek başına sırtlanmış, aşırı yük altında ezilmişsin.",
        "duz_simdi": "Şu an omuzlarında dünyanın yükü var; işler çok ağır geliyor ve yorulmuşsun.",
        "duz_gelecek": "Gelecekte bu ağır yükleri başkalarıyla paylaşacak ya da bazılarını çöpe atıp rahatlayacaksın.",
        "ters_gecmis": "Geçmişte yükleri zamanında bırakamadığın için tükenmişlik sendromu yaşamışsın.",
        "ters_simdi": "Şu an sorumlulukların altında eziliyorsun ama yardım istemekte inat ediyorsun.",
        "ters_gelecek": "Gelecekte yüklerinden kurtulup hafiflemenin ve özgürleşmenin tadını çıkaracaksın."
    },
    "ASALARIN VALESİ (PAGE OF WANDS)": {
        "duz_gecmis": "Geçmişte yeni bir maceraya atılma arzusuyla dolu, hevesli adımlar atmışsın.",
        "duz_simdi": "Şu an öğrenmeye açık, enerjik, heyecan verici haberler getiren bir ruh halindesin.",
        "duz_gelecek": "Gelecekte sürpriz bir seyahat veya yaratıcı bir teklif kapını çalacak.",
        "ters_gecmis": "Geçmişte hevesin kursağında kalmış, sorumsuzca hareketler yapılmış.",
        "ters_simdi": "Şu an odaklanma sorunu yaşıyor, başladığın işleri yarıda bırakıyorsun.",
        "ters_gelecek": "Gelecekte dağınık enerjini toparlayarak daha istikrarlı adımlar atacaksın."
    },
    "ASALARIN ŞÖVALYESİ (KNIGHT OF WANDS)": {
        "duz_gecmis": "Geçmişte fevri, tutkulu ve macera peşinde koşan cesur hamleler yapmışsın.",
        "duz_simdi": "Şu an yerinde duramıyor, hızla hareket etmek ve büyük riskler almak istiyorsun.",
        "duz_gelecek": "Gelecekte hayatına hareket katacak tutkulu bir seyahat veya ani bir olay yaşanacak.",
        "ters_gecmis": "Geçmişte aceleci ve düşüncesiz kararlar başına dert açmış.",
        "ters_simdi": "Şu an sabırsızlığın ve öfken yüzünden ilişkilerde gerginlikler yaşayabilirsin.",
        "ters_gelecek": "Gelecekte fevri davranışların kontrolünü ele alarak daha dengeli olacaksın."
    },
    "ASALARIN KRALİÇESİ (QUEEN OF WANDS)": {
        "duz_gecmis": "Geçmişte özgüvenli, karizmatik, sıcakkanlı ve yönlendirici bir duruş sergilemişsin.",
        "duz_simdi": "Şu an etrafına ışık saçıyor, bağımsızlığınla ve cazibenle herkesi etkiliyorsun.",
        "duz_gelecek": "Gelecekte sosyal hayatında ve kariyerinde parlayacağın otoriter ama sevecen bir dönem var.",
        "ters_gecmis": "Geçmişte kıskançlık, ego çatışmaları veya özgüven kırılması yaşanmış.",
        "ters_simdi": "Şu an enerjinin düştüğünü hissedebilir, manipülatif ortamlara maruz kalabilirsin.",
        "ters_gelecek": "Gelecekte içindeki o güçlü karizmatik kadını/enerjiyi yeniden ayağa kaldıracaksın."
    },
    "ASALARIN KRALI (KING OF WANDS)": {
        "duz_gecmis": "Geçmişte vizyoner liderlik yapmış, büyük projeleri başarıyla yönetmişsin.",
        "duz_simdi": "Şu an ilham veren, kararlı, büyük resmi gören ve vizyon sahibi bir lider konumundasın.",
        "duz_gelecek": "Gelecekte büyük bir işin başına geçecek veya otoritenle kitleleri yönlendireceksin.",
        "ters_gecmis": "Geçmişte baskıcı, buyurgan ve aceleci bir liderlik tarzı tepki çekmiş.",
        "ters_simdi": "Şu an sabırsız ve otoriter tavırlarınla çevrendekileri zor durumda bırakabilirsin.",
        "ters_gelecek": "Gelecekte vizyonunu daha yapıcı ve esnek bir dille insanlara aktaracaksın."
    },

    # --- KÜÇÜK ARKANA: KUPALAR (CUPS) ---
    "KUPALARIN ASI (ACE OF CUPS)": {
        "duz_gecmis": "Geçmişte kalbini açan muazzam bir aşk, ilahi bir sevgi veya duygusal yenilenme yaşamışsın.",
        "duz_simdi": "Şu an kalbin sevgiyle tağşiş olmuş durumda; yeni bir ilişki veya büyük bir huzur kapında.",
        "duz_gelecek": "Gelecekte duygusal olarak seni tatmin edecek, ruhunu doyuran muazzam bağlar kuracaksın.",
        "ters_gecmis": "Geçmişte kırık bir kalple ya da bastırılmış duygularla baş etmeye çalışmışsın.",
        "ters_simdi": "Şu an duygusal olarak tıkanmış, sevgini göstermekte zorlanan bir yapısın.",
        "ters_gelecek": "Gelecekte kalbindeki o buzlar eriyecek ve yeniden sevgiye kapı açacaksın."
    },
    "KUPALARIN İKİLİSİ (TWO OF CUPS)": {
        "duz_gecmis": "Geçmişte ruh eşi seviyesinde uyumlu bir ortaklık veya aşk ilişkisi kurulmuş.",
        "duz_simdi": "Şu an karşılıklı anlaşma, uyum, sevgi ve iki kalbin birleştiği özel bir bağın içindesin.",
        "duz_gelecek": "Gelecekte hayatını birleştireceğin çok özel bir ortaklık ya da evlilik teklifi gelebilir.",
        "ters_gecmis": "Geçmişte ilişkilerde kopukluklar, yanlış anlamalar ve uyumsuzluklar yaşanmış.",
        "ters_simdi": "Şu an sevdiğin kişiyle aranızda iletişim kopukluğu veya dengesizlik hissedebilirsin.",
        "ters_gelecek": "Gelecekte taraflar arasındaki buzları eriterek yeniden uyumu yakalayacaksınız."
    },
    "KUPALARIN ÜÇLÜSÜ (THREE OF CUPS)": {
        "duz_gecmis": "Geçmişte dostlarla birlikte kutlanan, neşeli ve keyifli bir sosyal dönem geçirilmiş.",
        "duz_simdi": "Şu an arkadaşlarınla bir arada olmak, kutlama yapmak ve keyifli anlar paylaşmak için harika bir an.",
        "duz_gelecek": "Gelecekte düğün, parti veya mutlu toplu buluşmalarla enerjini yükselteceksin.",
        "ters_gecmis": "Geçmişte dedikodular, fesatlıklar veya sosyal çevreden uzaklaşma yaşanmış.",
        "ters_simdi": "Şu an sosyal hayatta aşırılığa kaçma ya da arkandan çevrilen dedikodularla karşılaşabilirsin.",
        "ters_gelecek": "Gelecekte sahte dostlukları eleyip gerçek dostlarınla daha samimi bağlar kuracaksın."
    },
    "KUPALARIN DÖRDÜLSÜ (FOUR OF CUPS)": {
        "duz_gecmis": "Geçmişte sunulan fırsatları görmezden gelmiş, bıkkınlık ve tatminsizlik yaşamışsın.",
        "duz_simdi": "Şu an mevcuttan sıkılmış, içine kapanmış ve etrafındaki güzellikleri fark edemez haldesin.",
        "duz_gelecek": "Gelecekte bu apatiden sıyrılarak önüne çıkan yeni fırsatları fark edeceksin.",
        "ters_gecmis": "Geçmişte depresif halden çıkarak yeniden hayata tutunmaya başlamışsın.",
        "ters_simdi": "Şu an kabuğundan çıkmaya başladığın, uyanışa geçtiğin bir döneme giriyorsun.",
        "ters_gelecek": "Gelecekte hayata küsmek yerine yeni heyecanların peşinden gideceksin."
    },
    "KUPALARIN BEŞLİSİ (FIVE OF CUPS)": {
        "duz_gecmis": "Geçmişte dökülen sütlere üzülmüş, kayıplar ve hayal kırıklıkları yüzünden yas tutmuşsun.",
        "duz_simdi": "Şu an geçmişteki bir pişmanlığa takılıp kalmış, kalan güzellikleri göremiyorsun.",
        "duz_gelecek": "Gelecekte yas dönemi bitecek ve arkada kalan sağlam bağları fark edip teselli bulacaksın.",
        "ters_gecmis": "Geçmişteki acıları affetmiş, kalbini iyileştirmeye başlamışsın.",
        "ters_simdi": "Şu an yavaş yavaş affetme ve geçmişin yükünden arınma sürecindesin.",
        "ters_gelecek": "Gelecekte kayıplarını birer ders olarak kabul edip umutla ileriye bakacaksın."
    },
    "KUPALARIN ALTILISI (SIX OF CUPS)": {
        "duz_gecmis": "Geçmişin tatlı anıları, çocukluk dostları veya nostalji dolu günler zihnini sarmış.",
        "duz_simdi": "Şu an geçmişten gelen biriyle karşılaşabilir veya saf, masum sevgi enerjisi hissedebilirsin.",
        "duz_gelecek": "Gelecekte eski güzel günlerin huzurunu ve saf sevgiyi yeniden bulacaksın.",
        "ters_gecmis": "Geçmişe aşırı takılıp kalmak şimdiki zamanı kaçırmana neden olmuş.",
        "ters_simdi": "Şu an nostaljide takılı kalmış, büyümekten kaçan bir çocuk psikolojisi sergiliyor olabilirsin.",
        "ters_gelecek": "Gelecekte geçmişin gölgesinden çıkıp şimdiki zamanın gerçekleriyle yüzleşeceksin."
    },
    "KUPALARIN YEDİLİSİ (SEVEN OF CUPS)": {
        "duz_gecmis": "Geçmişte hayalperest dünyalar kurmuş, gerçekçi olmayan seçenekler arasında kafan karılmış.",
        "duz_simdi": "Şu an seçenekler çok fazla ama bunların hangisi gerçek hangisi illüzyon ayırt etmekte zorlanıyorsun.",
        "duz_gelecek": "Gelecekte hayal ile gerçeği ayırt edecek ve doğru seçimi netçe yapacaksın.",
        "ters_gecmis": "Geçmişteki yanılgılardan uyanmış, gerçekçi adımlar atmaya başlamışsın.",
        "ters_simdi": "Şu an sisler dağılıyor ve hayallerinden sıyrılarak ayakların yere basmaya başlıyor.",
        "ters_gelecek": "Gelecekte net bir vizyonla hedefine odaklanacaksın."
    },
    "KUPALARIN SEKİZLİSİ (EIGHT OF CUPS)": {
        "duz_gecmis": "Geçmişte sana artık duygusal olarak yetmeyen bir durumu veya yeri arkanda bırakıp gitmişsin.",
        "duz_simdi": "Şu an ruhsal olarak olgunlaşmak için bazı şeyleri terk etme, arayışa çıkma zamanındasın.",
        "duz_gelecek": "Gelecekte daha anlamlı bir yaşam arayışıyla yeni ve manevi yollara yürüyeceksin.",
        "ters_gecmis": "Geçmişte gitmekten korkmuş, mutsuz olduğun bir durumda kalmaya devam etmişsin.",
        "ters_simdi": "Şu an gitme korkusu ile kalma acısı arasında sıkışıp kalmış durumdasın.",
        "ters_gelecek": "Gelecekte nihayet gereken cesareti toplayıp seni tüketen yerden uzaklaşacaksın."
    },
    "KUPALARIN DOKUZLUSU (NINE OF CUPS)": {
        "duz_gecmis": "Geçmişte dileklerin kabul olmuş, keyif, konfor ve tatmin dolu harika anlar yaşamışsın.",
        "duz_simdi": "Şu an 'Dilek Kartı' olarak bilinir; keyfin yerinde, oldukça mutlu ve tatmin hissediyorsun.",
        "duz_gelecek": "Gelecekte tüm isteklerinin gerçekleşeceği tatmin dolu günler seni bekliyor.",
        "ters_gecmis": "Geçmişte açgözlülük veya tatminsizlik yüzünden elindekilerin kıymeti bilinmemiş.",
        "ters_simdi": "Şu an dıştan her şey mükemmel görünse de içten bir tatminsizlik yaşıyorsun.",
        "ters_gelecek": "Gelecekte gerçek mutluluğun maddiyatta değil iç huzurda olduğunu fark edeceksin."
    },
    "KUPALARIN ONLUSU (TEN OF CUPS)": {
        "duz_gecmis": "Geçmişte mutlu aile tablosu, huzurlu yuva ve ilahi sevgi tam anlamıyla yaşanmış.",
        "duz_simdi": "Şu an hayatında huzurun, aile bağlarının ve duygusal mutluluğun zirvesindesin.",
        "duz_gelecek": "Gelecekte uzun ömürlü, huzurlu, mutlu bir aile ve yuva kurma olasılığın çok yüksek.",
        "ters_gecmis": "Geçmişte aile içi çatışmalar veya idealize edilen mutluluğun yıkılması yaşanmış.",
        "ters_simdi": "Şu an ev içinde veya yakın ilişkilerde geçici bir uyumsuzluk ve mutsuzluk hissedebilirsin.",
        "ters_gelecek": "Gelecekte aradaki kırgınlıkları onararak o mutlu tabloyu yeniden kuracaksınız."
    },
    "KUPALARIN VALESİ (PAGE OF CUPS)": {
        "duz_gecmis": "Geçmişte romantik bir teklif, sürpriz bir mesaj veya saf bir duygusal haber alınmış.",
        "duz_simdi": "Şu an kalbin kıpır kıpır; yaratıcı sezgiler ve sürpriz duygusal teklifler kapında.",
        "duz_gelecek": "Gelecekte seni çok mutlu edecek tatlı sürprizler ve saf ilişkiler gelişecek.",
        "ters_gecmis": "Geçmişte duygusal hayal kırıklıkları veya çocukça tripler yaşanmış.",
        "ters_simdi": "Şu an duygusal olarak aşırı alıngan veya gerçekçi olmayan beklentiler içindesin.",
        "ters_gelecek": "Gelecekte duygularını daha olgun bir şekilde ifade etmeyi öğreneceksin."
    },
    "KUPALARIN ŞÖVALYESİ (KNIGHT OF CUPS)": {
        "duz_gecmis": "Geçmişte romantik, nazik, teklifkar ve aşık bir şövalye hayatına girmiş.",
        "duz_simdi": "Şu an romantizmin, tekliflerin ve kalbinin sesini dinlemenin en yoğun olduğu zamandasın.",
        "duz_gelecek": "Gelecekte kalbini çalacak çok özel bir teklif ya da romantik bir gelişme yaşanacak.",
        "ters_gecmis": "Geçmişte hayal kırıklığı yaratan, tutarsız veya aldatıcı romantik yaklaşımlar olmuş.",
        "ters_simdi": "Şu an duygusal dalgalanmalar yaşıyor, ne istediğini bilmez bir haldesindir.",
        "ters_gelecek": "Gelecekte hayalî aşklardan arınarak gerçekçi ve dürüst bağlar kuracaksın."
    },
    "KUPALARIN KRALİÇESİ (QUEEN OF CUPS)": {
        "duz_gecmis": "Geçmişte şefkatli, sezgisel, empati yeteneği yüksek ve koruyucu bir kadın figürü hayatında olmuş.",
        "duz_simdi": "Şu an kalbinin sesini dinleyen, empatik, etrafına şifa ve sevgi dağıtan bir konumdasın.",
        "duz_gelecek": "Gelecekte duygusal zekân sayesinde ilişkilerde krizleri ustalıkla çözeceksin.",
        _ters_gecmis: "Geçmişte aşırı duygusallık, alınganlık ve kendini kurban psikolojisine sokma durumu olmuş.",
        "ters_simdi": "Şu an duygusal olarak tükenmiş, kendi sınırlarını koruyamaz halde hissedebilirsin.",
        "ters_gelecek": "Gelecekte içsel şefkati başkalarından önce kendine göstermeyi öğreneceksin."
    },
    "KUPALARIN KRALI (KING OF CUPS)": {
        "duz_gecmis": "Geçmişte duygularını kontrol edebilen, bilge, anlayışlı ve merhametli bir rehberle karşılaşmışsın.",
        "duz_simdi": "Şu an duygularınla mantığını muazzam bir dengede tutuyor, sakin ve şefkatli bir duruş sergiliyorsun.",
        "duz_gelecek": "Gelecekte kriz anlarında bile soğukkanlılığın ve merhametinle örnek gösterileceksin.",
        "ters_gecmis": "Geçmişte duygularını bastıran, manipülatif veya soğuk kalpli bir yaklaşım görülmüş.",
        "ters_simdi": "Şu an duygusal patlamalar yaşayabilir ya da hislerini tamamen kapatmış olablirsin.",
        "ters_gelecek": "Gelecekte duygusal dengeni yeniden bularak etrafına güven vereceksin."
    },

    # --- KÜÇÜK ARKANA: KILIÇLAR (SWORDS) ---
    "KILIÇLARIN ASI (ACE OF SWORDS)": {
        "duz_gecmis": "Geçmişte zihinsel bir aydınlanma, netleşme ve keskin bir karar alma anı yaşanmış.",
        "duz_simdi": "Şu an zihnin pırıl pırıl; gerçeği tüm çıplaklığıyla görüyor ve hakikati savunuyorsun.",
        "duz_gelecek": "Gelecekte adalet, netlik ve zihinsel başarı getirecek büyük kararlar alacaksın.",
        "ters_gecmis": "Geçmişte yanlış anlamalar, zihinsel bulanıklıklar ve yanlış kararlar alınmış.",
        "ters_simdi": "Şu an düşüncelerinde dağınıklık var ve gerçeği görmekte zorlanıyorsun.",
        "ters_gelecek": "Gelecekte zihinsel sisler kalkacak ve doğru kararları netlikle vereceksin."
    },
    "KILIÇLARIN İKİLİSİ (TWO OF SWORDS)": {
        "duz_gecmis": "Geçmişte iki seçenek arasında kalmış, karar vermemek için gözlerini gerçeğe kapatmışsın.",
        "duz_simdi": "Şu an zor bir karar vermemek için direniyor, taraflar arasında denge kurmaya çalışıyorsun.",
        "duz_gelecek": "Gelecekte daha fazla kaçamayacağın o yüzleşmeyi yaşayıp karar vereceksin.",
        "ters_gecmis": "Geçmişte gözlerindeki bağ çözülmüş ve zor da olsa bir karar alınmış.",
        "ters_simdi": "Şu an gerçeklerle yüzleşme vakti geldi; kararsızlık artık sana zarar veriyor.",
        "ters_gelecek": "Gelecekte o zorlu seçimi yaparak rahat bir nefes alacaksın."
    },
    "KILIÇLARIN ÜÇLÜSÜ (THREE OF SWORDS)": {
        "duz_gecmis": "Geçmişte büyük bir kalp kırıklığı, ihanet veya acı bir ayrılık yaşanmış.",
        "duz_simdi": "Şu an ruhsal bir acı, hüzün veya kalbi yaralayan bir gerçekle yüzleşiyorsun.",
        "duz_gelecek": "Gelecekte bu acı zamanla hafifleyecek ve yaralarını sarma fırsatı bulacaksın.",
        "ters_gecmis": "Geçmişteki acılar yavaş yavaş sarılmış, affetme süreci başlamış.",
        "ters_simdi": "Şu an eski yaraları kaşıyor, acıyı taze tutmaktan vazgeçmiyorsun.",
        "ters_gelecek": "Gelecekte kalp kırıklıklarını geride bırakıp şifaya kavuşacaksın."
    },
    "KILIÇLARIN DÖRDÜLSÜ (FOUR OF SWORDS)": {
        "duz_gecmis": "Geçmişte derin bir yorgunluk sonrası zihinsel dinlenme ve hastane/şifa molası verilmiş.",
        "duz_simdi": "Şu an dünyadan el etek çekme, zihnini dinlendirme ve kabuğuna çekilip şifa bulma zamanı.",
        "duz_gelecek": "Gelecekte bu dinlenme sana çok iyi gelecek ve yenilenmiş olarak döneceksin.",
        "ters_gecmis": "Geçmişte dinlenmeye vakit bulamadan aşırı stres altında çalışmışsın.",
        "ters_simdi": "Şu an tükenmek üzeresin ama hâlâ dinlenmeyi reddediyorsun.",
        "ters_gelecek": "Gelecekte zorunlu bir mola alarak pilini yeniden dolduracaksın."
    },
    "KILIÇLARIN BEŞLİSİ (FIVE OF SWORDS)": {
        "duz_gecmis": "Geçmişte kazanılan ama kimseyi mutlu etmeyen zehirli bir zafer veya tartışma yaşanmış.",
        "duz_simdi": "Şu an çıkarcı ilişkiler, arkadan iş çevirmeler ve ego savaşlarıyla dolu bir ortamdasın.",
        "duz_gelecek": "Gelecekte bu tür toksik insanlardan uzak durman gerektiğinin farkına varacaksın.",
        "ters_gecmis": "Geçmişte yaşanan haksızlıklar tatlıya bağlanmaya çalışılmış veya barışılmış.",
        "ters_simdi": "Şu an pişmanlık duyduğun bazı tartışmaların ve kırıcı sözlerin etkisindesin.",
        "ters_gelecek": "Gelecekte bu tatsız olayları geride bırakıp yeni bir sayfa açacaksın."
    },
    "KILIÇLARIN ALTILISI (SIX OF SWORDS)": {
        "duz_gecmis": "Geçmişte sorunlu bir yeri arkada bırakıp daha sakin ve güvenli sulara doğru yol almışsın.",
        "duz_simdi": "Şu an zorlukları geride bırakıyor, yavaş yavaş huzura ve sakinliğe doğru ilerliyorsun.",
        "duz_gelecek": "Gelecekte sıkıntılı dönemi tamamen atlatıp mental olarak huzura ereceksin.",
        "ters_gecmis": "Geçmişte sorunlardan kaçmaya çalışmış ama problemleri de beraberinde götürmüşsün.",
        "ters_simdi": "Şu an sıkıntılı süreç uzuyor; gitmek istiyorsun ama geriye dönük engeller var.",
        "ters_gelecek": "Gelecekte o zorlu geçiş sürecini başarıyla tamamlayacaksın."
    },
    "KILIÇLARIN YEDİLİSİ (SEVEN OF SWORDS)": {
        "duz_gecmis": "Geçmişte gizli saklı işler, stratejik hamleler veya kurnazlıklar yapılmış.",
        "duz_simdi": "Şu an etrafında güven sarsıcı durumlar olabilir; kurnazlığa veya stratejiye dikkat etmelisin.",
        "duz_gelecek": "Gelecekte gizli saklı kalan bazı gerçekler gün yüzüne çıkabilir.",
        "ters_gecmis": "Geçmişte yapılan hatalar veya hırsızlıklar ortaya dökülmüş, itiraflar gelmiş.",
        "ters_simdi": "Şu an dürüst olmama lüksün yok; sırların açığa çıkmasından korkuyorsun.",
        "ters_gelecek": "Gelecekte dürüstlüğün en iyi politika olduğunu anlayıp her şeyi açıklayacaksın."
    },
    "KILIÇLARIN SEKİZLİSİ (EIGHT OF SWORDS)": {
        "duz_gecmis": "Geçmişte kendi zihinsel hapishaneni kurmuş, eli kolu bağlı çaresiz bir kurban psikolojisiyle yaşmışsın.",
        "duz_simdi": "Şu an kendini çıkmazda ve kapana kısılmış hissediyorsun ama o ipler aslında o kadar da sıkı değil.",
        "duz_gelecek": "Gelecekte gözlerindeki bağı çözecek ve o zihinsel hapishaneden kendi gücünle çıkıp özgürleşeceksin.",
        "ters_gecmis": "Geçmişte kurban psikolojisinden kurtulmuş, zincirlerini kırarak özgürlüğünü ilan etmişsin.",
        "ters_simdi": "Şu an özgürlüğe doğru ilk adımları atıyor, korkularını yavaş yavaş kırmaya başlıyorsun.",
        "ters_gelecek": "Gelecekte kısıtlamalardan tamamen kurtulup kendi hayatının lideri olacaksın."
    },
    "KILIÇLARIN DOKUZLUSU (NINE OF SWORDS)": {
        "duz_gecmis": "Geçmişte aşırı kuruntular, kabuslar, kaygı ve uykusuz geceler seni yıpratmış.",
        "duz_simdi": "Şu an kafaya taktığın vesveseler ve kaygılar yüzünden huzursuz ve endişelisin.",
        "duz_gelecek": "Gelecekte bu korkuların çoğunun yersiz olduğunu görüp derin bir 'oh' çekeceksin.",
        "ters_gecmis": "Geçmişte anksiyete dönemi geride kalmış, iç huzuru yavaşça sağlanmış.",
        "ters_simdi": "Şu an kaygıların hafiflemeye başlıyor, gizli korkularınla yüzleşiyorsun.",
        "ters_gelecek": "Gelecekte kabusların bittiği, sabahı aydınlık göreceğin bir döneme giriyorsun."
    },
    "KILIÇLARIN ONLUSU (TEN OF SWORDS)": {
        "duz_gecmis": "Geçmişte dip noktayı gördüğün, en ağır ihaneti veya yıkımı yaşayıp dibe vurmuşsun.",
        "duz_simdi": "Şu an 'daha kötü ne olabilir ki' diyeceğin bir bitiş noktasındasın ama en azından dibe vurdun.",
        "duz_gelecek": "Gelecekte bu durumun en dip nokta olduğunu, bundan sonra sadece yukarı çıkabileceğini göreceksin.",
        "ters_gecmis": "Geçmişte felaketten kıl payı kurtulmuş veya yavaş yavaş toparlanmaya başlamışsın.",
        "ters_simdi": "Şu an yaralarını sarmaya ve en kötü günleri geride bırakmaya çalışıyorsun.",
        "ters_gelecek": "Gelecekte bu acı tecrübe sayesinde eskisinden çok daha güçlü ayağa kalkacaksın."
    },
    "KILIÇLARIN VALESİ (PAGE OF SWORDS)": {
        "duz_gecmis": "Geçmişte meraklı, araştırmacı, her şeyi sorgulayan ve tetikte bir tutum sergilenmiş.",
        "duz_simdi": "Şu an gözlem yapıyor, bilgi topluyor ve etrafında dönen olayları dikkatle inceliyorsun.",
        "duz_gelecek": "Gelecekte beklenmedik haberler alacak ve zihinsel olarak zekice hamleler yapacaksın.",
        "ters_gecmis": "Geçmişte patavatsız sözler, dedikodular veya fevri çıkışlar sorun yaratmış.",
        "ters_simdi": "Şu an sivri dilli olmaktan kaçınmalı, fevri açıklamalar yapmamalısın.",
        "ters_gelecek": "Gelecekte iletişimde daha yapıcı ve sakin bir üslup benimseyeceksin."
    },
    "KILIÇLARIN ŞÖVALYESİ (KNIGHT OF SWORDS)": {
        "duz_gecmis": "Geçmişte hızla hareket eden, aceleci, keskin kararlar alan ve hedefine odaklanan biri olmuş.",
        "duz_simdi": "Şu an fırtına gibi esiyor, zihnindeki planları hızla ve hiç durmadan hayata geçirmeye çalışıyorsun.",
        "duz_gelecek": "Gelecekte engelleri fırtına hızıyla aşacağın çok keskin bir mücadele dönemi seni bekliyor.",
        "ters_gecmis": "Geçmişte düşünmeden söylenen sert sözler ve patavatsızlıklar kalpleri kırmış.",
        "ters_simdi": "Şu an agresif ve aceleci tavırların etrafındakileri germesine yol açabilir.",
        "ters_gelecek": "Gelecekte hızını biraz yavaşlatıp stratejik düşünmeyi öğreneceksin."
    },
    "KILIÇLARIN KRALİÇESİ (QUEEN OF SWORDS)": {
        "duz_gecmis": "Geçmişte mantığına öncelik veren, dürüst, keskin zekalı ve sınırları net bir kadın figürü olmuş.",
        "duz_simdi": "Şu an duygulardan ziyade mantıkla hareket ediyor, insanlara net ve mesafeli sınırlar koyuyorsun.",
        "duz_gelecek": "Gelecekte adaleti ve objektifliği elden bırakmadan profesyonel kararlar alacaksın.",
        "ters_gecmis": "Geçmişte aşırı soğuk, eleştirel ve katı kalpli tutumlar yalnızlık getirmiş.",
        "ters_simdi": "Şu an insanlara karşı çok keskin ve kırıcı olmamaya özen göstermelisin.",
        "ters_gelecek": "Gelecekte mantığınla birlikte empati yeteneğini de yeniden harmanlayacaksın."
    },
    "KILIÇLARIN KRALI (KING OF SWORDS)": {
        "duz_gecmis": "Geçmişte entelektüel, adil, hukuki konularda uzman ve tarafsız kararlar alınmış.",
        "duz_simdi": "Şu an mantığın, hukukun ve akılcı stratejilerin hakim olduğu bir karar verme aşamasındasın.",
        "duz_gelecek": "Gelecekte akılcı ve otoriter yapın sayesinde büyük krizleri profesyonellikle çözeceksin.",
        "ters_gecmis": "Geçmişte aşırı despot, adaletsiz veya manipülatif zihinsel baskılar kurulmuş.",
        "ters_simdi": "Şu an olaylara çok katı ve entelektüel bir kibirle yaklaşıyor olabilirsiz.",
        "ters_gelecek": "Gelecekte daha esnek ve adil bir bakış açısı geliştireceksin."
    },

    # --- KÜÇÜK ARKANA: TILSIMLAR / PENTAGRAMLAR (PENTACLES) ---
    "TILSIMLARIN ASI (ACE OF PENTACLES)": {
        "duz_gecmis": "Geçmişte maddi anlamda yepyeni bir fırsat, iş teklifi veya bolluk kapısı aralanmış.",
        "duz_simdi": "Şu an eline somut bir fırsat geçiyor; finansal ya da kariyer anlamında harika bir başlangıçtasın.",
        "duz_gelecek": "Gelecekte yatırımlarının meyvesini alacak, kalıcı ve kazançlı bir döneme gireceksin.",
        "ters_gecmis": "Geçmişte kaçan maddi fırsatlar veya bütçe açıkları can sıkmış.",
        "ters_simdi": "Şu an finansal konularda temkinli olmalı, fırsatları elinden kaçırmamalısın.",
        "ters_gelecek": "Gelecekte bütçeni doğru yöneterek maddi güvenliğini yeniden inşa edeceksin."
    },
    "TILSIMLARIN İKİLİSİ (TWO OF PENTACLES)": {
        "duz_gecmis": "Geçmişte hayatın koşturmacası içinde iki işi veya bütçeyi dengelemeye çalışmışsın.",
        "duz_simdi": "Şu an hayatındaki birden fazla sorumluluğu jonglör gibi dengede tutmaya çalışıyorsun.",
        "duz_gelecek": "Gelecekte bu esneklik yeteneğin sayesinde maddi ve manevi dengeyi kuracaksın.",
        "ters_gecmis": "Geçmişte dengeler şaşmış, borçlar ve işler birbirine girmiş.",
        "ters_simdi": "Şu an finansal veya zamansal olarak aşırı bunalmış, kontrolü kaybetmek üzeresin.",
        "ters_gelecek": "Gelecekte önceliklerini yeniden belirleyerek bu dağınıklığı toparlayacaksın."
    },
    "TILSIMLARIN ÜÇLÜSÜ (THREE OF PENTACLES)": {
        "duz_gecmis": "Geçmişte takım çalışmasıyla, ustalıkla ve ortaklaşa harika bir iş ortaya konmuş.",
        "duz_simdi": "Şu an projelerinde başkalarıyla işbirliği yapıyor, emeklerinin takdir edildiği bir yerdesin.",
        "duz_gelecek": "Gelecekte kariyerinde terfi, ustalık belgesi veya ortak projelerle büyük başarılar kazanacaksın.",
        "ters_gecmis": "Geçmişte uyumsuz ekip arkadaşları ve kalitesiz işler yüzünden sorunlar çıkmış.",
        "ters_simdi": "Şu an iş yerinde iletişim eksikliği ve takım çalışmasının bozulması seni zorlayabilir.",
        "ters_gelecek": "Gelecekte uyumlu işbirlikleri kurarak projeni başarıyla tamamlayacaksın."
    },
    "TILSIMLARIN DÖRDÜLSÜ (FOUR OF PENTACLES)": {
        "duz_gecmis": "Geçmişte parasını ve pozisyonunu sıkıca elinde tutmuş, risk almaktan kaçınmışsın.",
        "duz_simdi": "Şu an elindekileri kaybetme korkusuyla cimrilik yapıyor, konfor alanına sıkıca tutunuyorsun.",
        "duz_gelecek": "Gelecekte bu maddi güven sağlasa da ilişkilerde izolasyon yaratabilir, esnemelisin.",
        "ters_gecmis": "Geçmişte ani para harcamaları veya maddi kayıplar yaşanmış.",
        "ters_simdi": "Şu an paradan veya kontrolcülükten vazgeçmeye başladığın bir esneme dönemindesin.",
        "ters_gelecek": "Gelecekte cimrilik kalkanını indirerek hayatın akışına güveneceksin."
    },
    "TILSIMLARIN BEŞLİSİ (FIVE OF PENTACLES)": {
        "duz_gecmis": "Geçmişte maddi sıkıntılar, yalnızlık, kriz veya sağlık sorunlarıyla dolu zorlu bir soğukluk yaşanmış.",
        "duz_simdi": "Şu an yokluk psikolojisinde hissediyor, dışlanmış veya maddi darlıkta kalmış gibi hissedebilirsin.",
        "duz_gelecek": "Gelecekte bu zorlu kriz dönemi geride kalacak ve yardım eli uzanacak.",
        "ters_gecmis": "Geçmişte maddi krizler yavaş yavaş atlatılmış, yardımlar alınmış.",
        "ters_simdi": "Şu an en kötü günlerin geride kalmaya başladığı, toparlanma evresindesin.",
        "ters_gelecek": "Gelecekte ekonomik ve ruhsal olarak yeniden güvenli bir yuvaya kavuşacaksın."
    },
    "TILSIMLARIN ALTILISI (SIX OF PENTACLES)": {
        "duz_gecmis": "Geçmişte hem maddi yardımda bulunmuşsun hem de hak ettiğin desteği görmüşsün (verme-alma dengesi).",
        "duz_simdi": "Şu an cömertlik, hayır işleri ya da hak ettiğin finansal desteği alma zamanındasın.",
        "duz_gelecek": "Gelecekte verme-alma dengesinin adil olduğu huzurlu bir maddi düzen kuracaksın.",
        "ters_gecmis": "Geçmişte adaletsiz para ilişkileri veya borç-alacak sorunları yaşanmış.",
        "ters_simdi": "Şu an maddi konularda manipülasyona veya karşılıksız fedakarlıklara dikkat etmelisin.",
        "ters_gelecek": "Gelecekte finansal ilişkilerinde daha adil ve net sınır çizeceksin."
    },
    "TILSIMLARIN YEDİLİSİ (SEVEN OF PENTACLES)": {
        "duz_gecmis": "Geçmişte uzun vadeli yatırımlar yapmış ve sabırla ekdiklerinin büyümesini beklemişsin.",
        "duz_simdi": "Şu an 'Acaba değdi mi?' diye durup yaptıklarını değerlendiriyor, sabırlı bir hasat bekliyorsun.",
        "duz_gelecek": "Gelecekte sabrının karşılığını fazlasıyla alacak, ektiğin tohumların meyvesini yiyeceksin.",
        "ters_gecmis": "Geçmişte sabırsızlık yüzünden erken vazgeçilen projeler hayal kırıklığı yaratmış.",
        "ters_simdi": "Şu an emeklerinin boşa gittiğini düşünerek karamsarlığa kapılabilirsin.",
        "ters_gelecek": "Gelecekte biraz daha sabırlı olmanın ne kadar doğru olduğunu göreceksin."
    },
    "TILSIMLARIN SEKİZLİSİ (EIGHT OF PENTACLES)": {
        "duz_gecmis": "Geçmişte büyük bir özveriyle çalışmış, zanaatini geliştirerek emek vermiştin.",
        "duz_simdi": "Şu an işine odaklandığın, ince eleyip sık dokuyarak kaliteli eserler çıkardığın bir çalışma dönemindesin.",
        "duz_gelecek": "Gelecekte bu çalışkanlığın ve ustalığın kariyerinde seni zirveye taşıyacak.",
        "ters_gecmis": "Geçmişte özensiz çalışmalar, odak eksikliği ve kalitesiz işler sorun yaratmış.",
        "ters_simdi": "Şu an işinden sıkılmış, detaylarda boğuluyor veya kaliteden ödün veriyor olabilirsin.",
        "ters_gelecek": "Gelecekte odağını yeniden toplayarak işine olan sevgini tazeleyeceksin."
    },
    "TILSIMLARIN DOKUZLUSU (NINE OF PENTACLES)": {
        "duz_gecmis": "Geçmişte kendi ayakları üstünde duran, maddi bağımsızlığını ve konforunu ilan etmiş bir kadın/kişi profili var.",
        "duz_simdi": "Şu an lüksün, huzurun, finansal bağımsızlığın ve kendi emeğinin tadını çıkarıyorsun.",
        "duz_gelecek": "Gelecekte kimseye muhtaç olmadan kendi bahçenin meyvelerini keyifle yiyeceksin.",
        "ters_gecmis": "Geçmişte maddi bağımlılıklar veya yanlış yatırımlar konforu sarsmış.",
        "ters_simdi": "Şu an dışarıdan her şey iyi görünse de yalnızlık hissi veya maddi kaygı yaşayabilirsin.",
        "ters_gelecek": "Gelecekte öz değerini yeniden hatırlayarak refahını artıracaksın."
    },
    "TILSIMLARIN ONLUSU (TEN OF PENTACLES)": {
        "duz_gecmis": "Geçmişte kalıcı aile mirası, köklü aile şirketleri ve uzun vadeli maddi refah kurulmuş.",
        "duz_simdi": "Şu an yuvanın huzuru, aile desteği, mülk edinme ve finansal istikrarın en güçlü anındasın.",
        "duz_gelecek": "Gelecekte nesiller boyu sürecek maddi ve manevi kalıcı başarılar, miraslar seni bekliyor.",
        "ters_gecmis": "Geçmişte aile içi miras kavgaları veya maddi iflaslar yaşanmış.",
        "ters_simdi": "Şu an aile bağları ile maddi sorumluluklar arasında bazı anlaşmazlıklar çıkabilir.",
        "ters_gelecek": "Gelecekte aile içi ortak değerleri yeniden inşa ederek huzuru bulacaksın."
    },
    "TILSIMLARIN VALESİ (PAGE OF PENTACLES)": {
        "duz_gecmis": "Geçmişte yeni bir eğitim, iş teklifi veya somut bir para haberi müjdelenmiş.",
        "duz_simdi": "Şu an somut adımlar atmaya, yeni bir beceri öğrenmeye ve pratik planlar yapmaya hazırsın.",
        "duz_gelecek": "Gelecekte kariyerinde veya eğitiminde seni sevindirecek somut bir teklif alacaksın.",
        "ters_gecmis": "Geçmişte tembellik, parayı yanlış yönetme veya fırsatları elden kaçırma olmuş.",
        "ters_simdi": "Şu an gerçekçi olmayan hayaller peşinde koşup pratik adımları ihmal ediyorsun.",
        "ters_gelecek": "Gelecekte ayakları yere basan planlarla yeniden yükselişe geçeceksin."
    },
    "TILSIMLARIN ŞÖVALYESİ (KNIGHT OF PENTACLES)": {
        "duz_gecmis": "Geçmişte yavaş ama emin adımlarla, sabırla ve sorumluluk bilinciyle çalışılmış.",
        "duz_simdi": "Şu an acele etmeden, işini garantiye alarak sabırlı ve istikrarlı bir ilerleme kaydediyorsun.",
        "duz_gelecek": "Gelecekte bu disiplinli ve yavaş ama sağlam adımlar sayesinde hedefine kesinlikle ulaşacaksın.",
        "ters_gecmis": "Geçmişte aşırı inatçılık, hantallık ve işlerin durma noktasına gelmesi yaşanmış.",
        "ters_simdi": "Şu an tembellik, motivasyon düşüklüğü veya her şeyi çok fazla erteleme eğilimindesin.",
        "ters_gelecek": "Gelecekte üzerindeki o hantallığı atarak rutinini yeniden canlandıracaksın."
    },
    "TILSIMLARIN KRALİÇESİ (QUEEN OF PENTACLES)": {
        "duz_gecmis": "Geçmişte bereketli, eli açık, evine ve konforuna düşkün, üretken bir figür etkili olmuş.",
        "duz_simdi": "Şu an pratik, güvenilir, etrafındakileri besleyen ve finansal güvenliği sağlayan bir konumdasın.",
        "duz_gelecek": "Gelecekte maddiyatta ve ev hayatında büyük bir refah, güven ve huzur dönemi seni bekliyor.",
        "ters_gecmis": "Geçmişte maddi kaybetme korkusu, cimrilik veya aşırı madde odaklılık sorun yaratmış.",
        "ters_simdi": "Şu an öz bakımını ihmal edip sadece başkalarının maddi sorunlarıyla ilgileniyor olabilirsin.",
        "ters_gelecek": "Gelecekte hem kendi konforunu hem de maddesel dengeni yeniden kuracaksın."
    },
    "TILSIMLARIN KRALI (KING OF PENTACLES)": {
        "duz_gecmis": "Geçmişte finansal imparatorluk kurmuş, başarılı iş insanı vizyonuyla sağlam yatırımlar yapılmış.",
        "duz_simdi": "Şu an maddi gücün zirvesindesin; güvenilir, zengin, tecrübeli ve somut sonuçlar üretiyorsun.",
        "duz_gelecek": "Gelecekte iş ve para piyasalarında adından söz ettirecek kalıcı bir servet ve konuma geleceksin.",
        "ters_gecmis": "Geçmişte maddi hırs uğruna insanları ezen, rüşvetçi veya katı tutumlar sergilenmiş.",
        "ters_simdi": "Şu an maddi riskler alırken aşırı katı davranıyor veya parayı kontrol etmekte zorlanıyorsun.",
        "ters_gelecek": "Gelecekte finansal gücünü doğru yatırımlarla çok daha güvenli bir boyuta taşıyacaksın."
    }
}
    }
}

if "adim" not in st.session_state:
  st.session_state.adim = "giriş"

# --- 1. GİRİŞ SAYFASI ---
if st.session_state.adim == "giriş":
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.markdown(
        "<h1 style='text-align: center;'>Tarot Bakımı 💌</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #fef08a;'>Kaderinin"
        " fısıltılarını birlikte dinleyelim</p>",
        unsafe_allow_html=True,
    )

    isim = st.text_input("İsmin:")
    dogum_tarihi = st.date_input(
        "Doğum Tarihin:",
        min_value=datetime.date(1940, 1, 1),
        max_value=datetime.date.today(),
        value=datetime.date(2000, 1, 1),
    )

    medeni_durum = st.selectbox(
        "Kalp Durumun:",
        [
            "Bekar",
            "İlişkisi Var",
            "Evli",
            "Flörtleşmekte",
            "Yeni ayrılmış",
            "Boşanmış",
        ],
    )

    is_durumu = st.selectbox(
        "Çalışma Durumun:", ["Çalışıyor", "Çalışmıyor", "Öğrenci"]
    )

    if st.button("Kart Seçim Ekranına Geç 🩵"):
      bugun = datetime.date.today()
      yas = (
          bugun.year
          - dogum_tarihi.year
          - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
      )

      if isim.strip() == "":
        st.warning("Lütfen ismini bizimle paylaş.")
      elif yas < 14:
        st.error(
            "Sevgili dostum, bu mistik yolculuk için biraz daha büyümeyi"
            " beklemelisin."
        )
      else:
        st.session_state.isim = isim
        st.session_state.burc = burc_hesapla(dogum_tarihi)
        st.session_state.medeni_durum = medeni_durum
        st.session_state.is_durumu = is_durumu
        st.session_state.adim = "secim"
        st.rerun()

# --- 2. KART SEÇİM SAYFASI ---
elif st.session_state.adim == "secim":
  st.markdown(
      f"<h2 style='text-align: center;'>Sevgili {st.session_state.isim}"
      f" ({st.session_state.burc})</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center;'>Aşağıdaki gizemli desteden enerjinin"
      " çektiği <b>tam olarak 3 adet kartı</b> kutucuklarından işaretle:</p>",
      unsafe_allow_html=True,
  )
  st.markdown("---")

  # Destedeki tüm kartları listele
  tum_kart_isimleri = list(tarot_veritabani.keys())

  secilenler_listesi = []
  cols = st.columns(4)

  for idx, kart_adi in enumerate(tum_kart_isimleri):
    col_idx = idx % 4
    with cols[col_idx]:
      st.markdown(
          "<div class='tarot-back'>"
          "<span style='font-size: 20px;'>💎</span>"
          f"<b style='color: #fef08a; font-size: 10px; margin-top: 4px;'>GİZLİ"
          f" KART #{idx+1}</b>"
          "</div>",
          unsafe_allow_html=True,
      )
      # Kullanıcının hangi karta tıkladığını ismen yakalıyoruz
      secildimi = st.checkbox(f"Seç ({idx+1})", key=f"secim_krt_{idx}")
      if secildimi:
        secilenler_listesi.append(kart_adi)

  st.markdown("---")

  if len(secilenler_listesi) > 3:
    st.error("Yalnızca 3 adet kart seçebilirsin! Lütfen seçimi 3'e düşür.")
  elif len(secilenler_listesi) == 3:
    if st.button("Seçtiğim Kartları Aç ve Falımı Gör 🌟"):
      # Sıralama: 1. Seçilen = Geçmiş, 2. Seçilen = Şimdi, 3. Seçilen = Gelecek
      zamanlar = ["gecmis", "simdi", "gelecek"]
      final_fal = []
for i, k_adi in enumerate(secilenler_listesi):
    durum = random.choice(["duz", "ters"])
    zaman_anahtari = zamanlar[i]
    
    # Güvenli kontrol ile KeyError'ü önleme
    try:
        yorum_metni = tarot_veritabani[k_adi][durum][zaman_anahtari]
    except KeyError:
        yorum_metni = f"Bu kart ({k_adi}) için seçilen durumda yorum bulunamadı."
        
    durum_str = "Düz Akış" if durum == "duz" else "Ters Enerji"
    final_fal.append((k_adi, durum_str, yorum_metni, zaman_anahtari))

      st.session_state.gercek_fal = final_fal
      st.session_state.adim = "sonuc"
      st.rerun()
  else:
    st.info(
        f"Şu an {len(secilenler_listesi)} kart seçtin. Falının bakılması için"
        " tam 3 kart işaretlemelisin."
    )

  if st.button("← Başa Dön"):
    st.session_state.adim = "giriş"
    st.rerun()

# --- 3. SONUÇ SAYFASI ---
elif st.session_state.adim == "sonuc":
  col_sol, col_orta, col_sag = st.columns([0.5, 5, 0.5])

  with col_orta:
    st.markdown(
        f"<h2 style='text-align: center;'>⭐ {st.session_state.isim}"
        f" ({st.session_state.burc}) İçin Tarot Rehberliği ⭐</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center; color: #fef08a; font-size: 14px;'>Kalp"
        f" Durumu: {st.session_state.medeni_durum} | Çalışma:"
        f" {st.session_state.is_durumu}</p>",
        unsafe_allow_html=True,
    )
    st.write(
        "Seçtiğin kartların zaman dilimlerine göre özel olarak hazırlanan"
        " analizleri:"
    )
    st.markdown("---")

    basliklar = {
        "gecmis": "GEÇMİŞ (Seni Buraya Getiren Temeller)",
        "simdi": "ŞİMDİ (İçinde Bulunduğun Enerji)",
        "gelecek": "GELECEK (Önündeki Olası Yollar ve Gelişmeler)",
    }

    for k_adi, durum_str, yorum_metni, zaman_anahtari in st.session_state.gercek_fal:
      st.markdown(
          f"<div class='tarot-card-box'>"
          f"<h3>{basliklar[zaman_anahtari]}</h3>"
          f"<p style='color: #fef08a; font-size: 16px; font-weight: 600;'>{k_adi}"
          f" <span style='font-size: 13px; color: #cbd5e1;'>({durum_str})"
          "</span></p>"
          f"<p style='line-height: 1.6;'><b>Analiz:</b> {yorum_metni}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if st.button("Yeni Bir Fal Bak 🫧"):
      st.session_state.adim = "giriş"
      st.rerun()
