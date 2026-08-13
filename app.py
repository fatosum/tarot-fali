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
/* Ana uygulama arka planı: Derin gece mavisi, beyaz dalgalı tül hissi ve gold parıltılar */
[data-testid="stAppViewContainer"] > .main {
background: 
    radial-gradient(circle at 50% 30%, rgba(255, 255, 255, 0.07) 0%, transparent 60%),
    linear-gradient(135deg, #0b0714 0%, #161026 50%, #08040d 100%);
color: #f3f4f6;
font-family: 'Cinzel', 'Inter', serif;
background-attachment: fixed;
}

/* Sayfa başlıkları ve yazı zarifliği */
h1, h2, h3 { 
color: #fef08a !important; 
font-family: 'Cinzel', serif; 
text-shadow: 0 2px 10px rgba(255, 215, 0, 0.2);
}
p, label, span { color: #e2e8f0 !important; }

/* Buton tasarımı */
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

/* Tarot kart sonuç kutusu */
.tarot-card-box {
background: rgba(22, 14, 38, 0.85);
border: 1px solid rgba(197, 155, 39, 0.4);
padding: 24px;
border-radius: 16px;
margin-bottom: 20px;
backdrop-filter: blur(16px);
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
}

/* SEÇİM EKRANI İÇİN KARTLARIN ARKA YÜZÜ: Tül, gold yıldız ve işlemeli estetik */
.tarot-back {
background: 
    radial-gradient(circle at 50% 50%, rgba(255, 215, 0, 0.15) 0%, transparent 70%),
    linear-gradient(135deg, #12091f 0%, #221438 50%, #12091f 100%);
border: 2px solid #dfb135;
border-radius: 14px;
width: 100%;
height: 170px;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
text-align: center;
box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), inset 0 0 18px rgba(212, 175, 55, 0.3);
margin-bottom: 8px;
transition: all 0.3s ease;
position: relative;
}

.tarot-back:hover {
transform: translateY(-6px);
border-color: #ffe875;
box-shadow: 0 12px 30px rgba(212, 175, 55, 0.5), inset 0 0 25px rgba(255, 232, 117, 0.5);
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
# Mistik ama fazlasıyla gerçekçi tarot destesi sözlüğü (Düz ve Ters anlamlarıyla)
tum_kartlar = {
    # --- BÜYÜK ARKANA ---
    "Deli (The Fool)": {
        "duz": (
            "Yeni bir bodoslama dalış, sonu belirsiz.",
            "Yeni bir döneme balıklama atlıyorsun ama sonu nereye varacak, meçhul.",
        ),
        "ters": (
            "Ayağını taşa takıp düşeceksin ama hala 'aslında uçuyordum' diye kendini kandıracaksın.",
            "Pervasızlığın başına bela açmak üzere, biraz etrafına bak.",
        ),
    },
    "Büyücü (The Magician)": {
        "duz": (
            "Elindeki imkanları abartıyorsun, ortada devasa bir şey yok.",
            "Sahip olduğun yetenekleri olduğundan büyük görüyorsun, yere biraz sağlam bas.",
        ),
        "ters": (
            "Dolandırıcı kılıklı bir tip seni parmağında oynatacak, ruhun duymayacak.",
            "Hileye ve manipülasyona karşı gözünü dört aç.",
        ),
    },
    "Azize (The High Priestess)": {
        "duz": (
            "İç sesin 'kaç' diyor ama sen diretiyorsun.",
            "Sezgilerin bas bas bağırıyor ama sen mantığını susturmaya çalışıyorsun.",
        ),
        "ters": (
            "Sırların ayağına dolaşacak, halı altına süpürdüğün ne varsa yüzüne patlayacak.",
            "Gizli saklı işlerin sonu maalesef felaket.",
        ),
    },
    "İmparatoriçe (The Empress)": {
        "duz": (
            "Keyfin yerinde ama tembelliğe vurdun.",
            "Rahatlık batıyor diyemeyiz ama bu şekerleme dönemi fazla uzadı.",
        ),
        "ters": (
            "Üretkenlik sıfır, kendine acımaktan bir baltaya sap olamayacaksın.",
            "Kendini saldın, biraz toparlanma vakti.",
        ),
    },
    "İmparator (The Emperor)": {
        "duz": (
            "Aşırı otorite taslıyorsun, kimse çekmek zorunda değil.",
            "Her şeyi ben bilirim havaları etrafındakileri çileden çıkarıyor.",
        ),
        "ters": (
            "O kurduğun krallık başına yıkılacak, boyun eğmek zorunda kalacaksın.",
            "Kontrolü kaybettin, şimdi kuralları başkaları koyuyor.",
        ),
    },
    "Hierofant (The Hierophant)": {
        "duz": (
            "Sistemden dışarı çıkmaya cesaretin yok.",
            "Geleneklerin ve kuralların kölesi olmuşsun, farklı bir şey denemeye korkuyorsun.",
        ),
        "ters": (
            "Çakma gurulara inanıp elinde avucunda ne varsa kaptıracaksın.",
            "Sorgulamadan inandığın her şey elinde patlayacak.",
        ),
    },
    "Aşıklar (The Lovers)": {
        "duz": (
            "Kritik bir seçim yapacaksın, muhtemelen yanlış olanı.",
            "Kalbinle mantığın savaş halinde ama yanlışa meyil var.",
        ),
        "ters": (
            "Yanlış insana kalbini kaptırıp enkazdan çıkamayacaksın.",
            "Uyumsuz bir ilişkiye veya karara körü körüne bağlanmışsın.",
        ),
    },
    "Savaş Arabası (The Chariot)": {
        "duz": (
            "Hızla gidiyorsun ama frenlerin patlak.",
            "Katarak ilerliyorsun ama sonu duvara toslamak olacak.",
        ),
        "ters": (
            "Kontrolü tamamen kaybedip duvara balıklama toslayacaksın.",
            "Direksiyon elinden kaydı, geçmiş olsun.",
        ),
    },
    "Güç (Strength)": {
        "duz": (
            "Sabrın taştı taşacak, ortalık karışacak.",
            "İçindeki öfkeyi zor zapt ediyorsun, fena patlayacaksın.",
        ),
        "ters": (
            "İçindeki canavar seni yiyecek, sinirden kendi saçını yolacaksın.",
            "Özgüven tavan ama altı bomboş, sabrın tükendi.",
        ),
    },
    "Ermiş (The Hermit)": {
        "duz": (
            "Kendi kendine trip atıp kabuğuna çekilmişsin.",
            "Dünyayla iletişimi kestin, mağaranda tek başına oturuyorsun.",
        ),
        "ters": (
            "Yalnızlıktan duvara konuşmaya başlayacaksın, kimse seni takmıyor.",
            "Aşırı izolasyon kafayı yedirecek, dışarı çık.",
        ),
    },
    "Kader Çarkı (Wheel of Fortune)": {
        "duz": (
            "Yine aynı döngüye girdin, tebrikler.",
            "Aynı hatayı tekrar yapmayı nasıl başarıyorsun cidden tebrikler.",
        ),
        "ters": (
            "Şansın döndü sanma, daha da dibe battın. Geçmiş olsun.",
            "Kader çarkı bu kez tersine ezerek geçiyor.",
        ),
    },
    "Adalet (Justice)": {
        "duz": (
            "Hak ettiğin neyse o geliyor, şikayet etme.",
            "Ne ektiysen onu biçiyorsun, şimdi ağlamak yok.",
        ),
        "ters": (
            "Torpil arıyorsun ama adalet duvarı kafana yıkılacak.",
            "Haksızlığın tescillenecek, kaçışın yok.",
        ),
    },
    "Asılı Adam (The Hanged Man)": {
        "duz": (
            "Hiçbir yere varamıyorsun çünkü inatla kıpırdamıyorsun.",
            "Kendi ellerinle kendini askıya aldın, bekleyip duruyorsun.",
        ),
        "ters": (
            "Boşuna kurbanı oynamaya kalkma, o ipe kendi boynunu kendin geçirdin.",
            "Gereksiz bir diretme, ne çektiysen kendi inatçılığından.",
        ),
    },
    "Ölüm (Death)": {
        "duz": (
            "Eski defterler zorla kapanıyor, ağlamanın lüzumu yok.",
            "Bitti dediysek bitti, arkasından helva yemesi kaldı.",
        ),
        "ters": (
            "Ölmüş bitmiş ilişkiyi diriltmeye çalışıp mezar kazıyorsun.",
            "Zombileşmiş alışkanlıkları canlandırma çaban hüsranla bitecek.",
        ),
    },
    "Denge (Temperance)": {
        "duz": (
            "İğne ucu üzerinde dengede durmaya çalışıyorsun, yazık.",
            "Her an düşecekmiş gibi titrek bir denge halindesin.",
        ),
        "ters": (
            "Aşırılıklarınla dibi göreceksin, orta yolu bulmak ne kelime.",
            "Dengeyi tamamen kaybettin, uçurumun kenarındasın.",
        ),
    },
    "Şeytan (The Devil)": {
        "duz": (
            "Kendi ellerinle bağlandığın toksik alışkanlıklar.",
            "Bağımlısı olduğun ne varsa seni bitiriyor ama bırakmaya niyetin yok.",
        ),
        "ters": (
            "O zincirler bir kopacak ama sen de paramparça olacaksın.",
            "Krizli bir kopuş, canın çok yanacak.",
        ),
    },
    "Kule (The Tower)": {
        "duz": (
            "Bütün planların başına yıkılacak, geçmiş olsun.",
            "Evdeki hesap çarşıya uymadı, bina komple çöktü.",
        ),
        "ters": (
            "Yıkım kaçınılmazdı, şimdi enkazı tek tek sen toplayacaksın.",
            "Beterin beteri varmış, enkaz altından çıkmak uzun sürecek.",
        ),
    },
    "Yıldız (The Star)": {
        "duz": (
            "Ufukta hafif bir ışık var ama umut bağlamaya değmez.",
            "Boş bir umudun peşinden koşturup duruyorsun.",
        ),
        "ters": (
            "Hayal kırıklığından gözyaşın kurumayacak, umut tüccarlarına para kaptırma.",
            "Yıldızın kaydı, hayaller suya düştü.",
        ),
    },
    "Ay (The Moon)": {
        "duz": (
            "Paranoya ve kuruntu sezinliyorum, hepsi kafanda.",
            "Karanlıkta kendi gölgenden korkuyorsun, ortada bir şey yok.",
        ),
        "ters": (
            "Korkularından kaçarken daha büyük bir kabusun içine düşeceksin.",
            "Sisler dağılıyor ama gördüğün manzara hiç hoşuna gitmeyecek.",
        ),
    },
    "Güneş (The Sun)": {
        "duz": (
            "Her şey yolunda gibi görünecek ama nazara geleceksin.",
            "Çok gülmenin sonu ağlamaktır derler, dikkat et.",
        ),
        "ters": (
            "Sahte gülümsemeler maskesi düşecek, gerçeklerle yüzleşeceksin.",
            "Bulutlar güneşi kapattı, neşen kursağında kalacak.",
        ),
    },
    "Mahkeme (Judgement)": {
        "duz": (
            "Geçmişteki hataların hesabını ödeme vakti.",
            "Geçmişin faturaları tek tek önüne konuluyor.",
        ),
        "ters": (
            "Suçu başkalarına atmayı kes, ayna karşısına geçip kendine bak.",
            "Yargı kapıda ama sen hala bahaneler üretiyorsun.",
        ),
    },
    "Dünya (The World)": {
        "duz": (
            "Döngüyü bitirdin ama başladığın yere geri döndün.",
            "Büyük bir işi bitirdin ama eline koca bir sıfır kaldı.",
        ),
        "ters": (
            "Son adıma kadar gelip çuvallayacaksın, emeğine yazık oldu.",
            "Merasuma iki adım kala ayağın takıldı, yazık.",
        ),
    },

    # --- KUPA SERİSİ ---
    "Kupa Ası": {
        "duz": "Duygusal bir patlama yaşayacaksın ama altı boş çıkacak.",
        "ters": "Kalbin kurumuş, kimseye zırnık sevgi veremiyorsun.",
    },
    "Kupa İkilisi": {
        "duz": "Karşılıklı boş yapma seansı.",
        "ters": "Karşılıklı ihanet ve entrika çarkı.",
    },
    "Kupa Üçlüsü": {
        "duz": "Gereksiz bir kutlama veya kalabalık.",
        "ters": "Dedikodu kazanı kaynıyor, arkandan kuyu kazıyorlar.",
    },
    "Kupa Dörtlüsü": {
        "duz": "Önüne sunulanı beğenmeyip burun kıvırıyorsun.",
        "ters": "Depresyondan uyanıp hayata sövmeye başladın.",
    },
    "Kupa Beşlisi": {
        "duz": "Dökülen süte ağlamaya devam ediyorsun.",
        "ters": "Kendi hatalarını başkasına yıkıp mağduru oynuyorsun.",
    },
    "Kupa Altılısı": {
        "duz": "Geçmişteki nostaljik bataklığında boğuluyorsun.",
        "ters": "Eskileri unutamayıp bugünü de mahvediyorsun.",
    },
    "Kupa Yedilisi": {
        "duz": "Hayal alemindesin, uyanınca çarpılacaksın.",
        "ters": "Gerçeklerle yüzleşme vakti, rüya bitti horlama sesi geldi.",
    },
    "Kupa Sekizlisi": {
        "duz": "Kaçıp gitmek istiyorsun ama cesaretin yok.",
        "ters": "Kaçamadın, kalıp o dırdırı çekmek zorundasın.",
    },
    "Kupa Dokuzlusu": {
        "duz": "Bencilce bir mutluluk, kimsenin umrunda değil.",
        "ters": "Sahip olduğun her şeyi burnundan getirecekler.",
    },
    "Kupa Onlusu": {
        "duz": "Reklamlardaki gibi sahte bir aile tablosu.",
        "ters": "Evdeki hesap çarşıya uymadı, kriz kapıda.",
    },
    "Kupa Prensi": {
        "duz": "Aşırı sulugöz ve alıngan bir dönem.",
        "ters": "Şımarıklığınla herkesi çileden çıkarıyorsun.",
    },
    "Kupa Şövalyesi": {
        "duz": "Prens olduğunu sanan ama yalan söyleyen biri.",
        "ters": "Yalancının mumu yatsıya kadar bile yanmadı.",
    },
    "Kupa Kraliçesi": {
        "duz": "Sürekli dert dinlemekten içi kurumuş biri.",
        "ters": "Manipülatif gözyaşlarıyla herkesi boğuyorsun.",
    },
    "Kupa Kralı": {
        "duz": "Duygularını bastıran ama içten içe bitik bir tip.",
        "ters": "Öfke patlaması yaşayıp etrafı kırıp dökeceksin.",
    },

    # --- KILIÇ SERİSİ ---
    "Kılıç Ası": {
        "duz": "Keskin bir fikir ama başa bela olacak.",
        "ters": "Yanlış anlaşılan bir laf yüzünden ortalık karışacak.",
    },
    "Kılıç İkilisi": {
        "duz": "Gözünü kapatmışsın, gerçekleri görmek istemiyorsun.",
        "ters": "Göz bandı düştü, acı gerçekler yüzüne tokat gibi çarpacak.",
    },
    "Kılıç Üçlüsü": {
        "duz": "Kalp kırıklığı ve net acı gerçekler.",
        "ters": "O acıyı içine atıp kinleneceksin, intikam vakti.",
    },
    "Kılıç Dörtlüsü": {
        "duz": "Tükenmişlik sendromu, kafayı yemek üzeresin.",
        "ters": "Dinlenmek yok, zorla koşturacaklar.",
    },
    "Kılıç Beşlisi": {
        "duz": "Kazandığını sandığın ama herkesi kaybettiğin bir kavga.",
        "ters": "Rezil olduğunla kalacaksın, ortada zafer falan yok.",
    },
    "Kılıç Altılısı": {
        "duz": "Zoraki bir kaçış, arkana bakmadan gidiyorsun.",
        "ters": "Kaçış bitti, sorunlar peşinden koşarak geldi.",
    },
    "Kılıç Yedilisi": {
        "duz": "Üç kağıtçılık ve sinsilik peşindesin.",
        "ters": "Planın elinde patladı, foyan meydana çıkıyor.",
    },
    "Kılıç Sekizlisi": {
        "duz": "Kendi ördüğün ağlara kendin takılmışsın.",
        "ters": "Çıkış yolu buldun ama kafayı da sıyırdın.",
    },
    "Kılıç Dokuzlusu": {
        "duz": "Gece yarısı 'acaba' diye düşünmekten uykuların kaçmış.",
        "ters": "Paranoyalarından arınacaksın ama çok geç olacak.",
    },
    "Kılıç Onlusu": {
        "duz": "Sırtından bıçaklandın, oyun bitti.",
        "ters": "Öldün derken canına okumaya devam edecekler.",
    },
    "Kılıç Prensi": {
        "duz": "Her şeye laf sokan sinir bozucu bir tip.",
        "ters": "Dedikoduların başına bela olacak.",
    },
    "Kılıç Şövalyesi": {
        "duz": "Paldır küldür kavgaya dalan aceleci biri.",
        "ters": "Gözü dönmüşlükten kendi ayağına sıkacaksın.",
    },
    "Kılıç Kraliçesi": {
        "duz": "Kimseye acımayan, buz gibi bir mantık.",
        "ters": "Soğuk tavırlarınla herkesi kaçıracaksın.",
    },
    "Kılıç Kralı": {
        "duz": "Fazla mantıktan ruhunu kaybetmiş bir otorite.",
        "ters": "Diktatörlük taslarken yalnız kalacaksın.",
    },

    # --- DEĞNEK SERİSİ ---
    "Değnek Ası": {
        "duz": "Büyük bir hevesle başlayıp yarım bırakacağın bir iş.",
        "ters": "Enerjin sıfır, ateşi yakamadan sönüp gideceksin.",
    },
    "Değnek İkilisi": {
        "duz": "Yolun başındasın ama nereye gideceğini bilmiyorsun.",
        "ters": "Kararsızlıktan yerinde saymaktan küf tutacaksın.",
    },
    "Değnek Üçlüsü": {
        "duz": "Bekliyorsun ama gelecek olan kargo bile gecikecek.",
        "ters": "Beklenen gemi battı, limanı da su bastı.",
    },
    "Değnek Dörtlüsü": {
        "duz": "Geçici bir huzur, hemen bozulacak.",
        "ters": "Davetin tadı kaçtı, herkes birbirine girdi.",
    },
    "Değnek Beşlisi": {
        "duz": "Ortada hiçbir şey yokken çıkan saçma bir tartışma.",
        "ters": "Kavga büyüdü, altından kalkamayacaksın.",
    },
    "Değnek Altılısı": {
        "duz": "Erken gelen bir zafer sarhoşluğu, duvara toslayacaksın.",
        "ters": "Alkışlayanlar ilk fırsatta seni satacak.",
    },
    "Değnek Yedilisi": {
        "duz": "Tek başına herkese karşı piyon gibi savunma yapıyorsun.",
        "ters": "Savunma hattın çöktü, havlu atıyorsun.",
    },
    "Değnek Sekizlisi": {
        "duz": "Her şey üst üste geliyor, hızına yetişemiyorsun.",
        "ters": "İşler sarpa sardı, hız kazası yaptın.",
    },
    "Değnek Dokuzlusu": {
        "duz": "Yaralı bereli ama hala 'bana bir şey olmaz' diyorsun.",
        "ters": "Artık dayanamıyorsun, pes bayrağını çekeceksin.",
    },
    "Değnek Onlusu": {
        "duz": "Kaldıramayacağın yükün altına kendi isteğinle girmişsin.",
        "ters": "O yük altında ezileceksin, yardım edenin de olmayacak.",
    },
    "Değnek Prensi": {
        "duz": "Yerinde duramayan ama boş gezen bir enerji.",
        "ters": "Daldan dala atlarken hiçbir şey beceremeyeceksin.",
    },
    "Değnek Şövalyesi": {
        "duz": "Gaza gelip her şeyi yüzüne gözüne bulaştıracaksın.",
        "ters": "Trafik kazası gibi bir hata, aceleden battın.",
    },
    "Değnek Kraliçesi": {
        "duz": "Ben bilirimci, ortalığı ayağa kaldıran bir karakter.",
        "ters": "Hükümdarlığın bitti, otoriten sarsıldı.",
    },
    "Değnek Kralı": {
        "duz": "Liderlik taslayan ama içeride batmış bir vizyon.",
        "ters": "Planlar suya düştü, foyan meydana çıktı.",
    },

    # --- TILSIM SERİSİ ---
    "Tılsım Ası": {
        "duz": "Küçük bir para girişi olacak, hemen harcayacaksın.",
        "ters": "Para eline geçmeden eridi gitti, geçmiş olsun.",
    },
    "Tılsım İkilisi": {
        "duz": "İki parasal iş arasında bocalayıp duruyorsun.",
        "ters": "Borç bataklığında jonglörlük yapmaya çalışıyorsun.",
    },
    "Tılsım Üçlüsü": {
        "duz": "Ortak iş yapıyorsunuz ama herkes birbirini kazıklıyor.",
        "ters": "Ekip ruhu sıfır, herkes kendi derdinde.",
    },
    "Tılsım Dörtlüsü": {
        "duz": "Cimriliğin bu kadarı fazla, mezara mı götüreceksin?",
        "ters": "Parayı saçtın, şimdi kara kara düşünüyorsun.",
    },
    "Tılsım Beşlisi": {
        "duz": "Kuruşsuz ve desteksiz kaldığın soğuk bir dönem.",
        "ters": "Durumun kötüydü, şimdi tamamen dibi boyladın.",
    },
    "Tılsım Altılısı": {
        "duz": "Sadaka veya borç alıp verme dengesi.",
        "ters": "Borç verdiklerini bir daha göremeyeceksin.",
    },
    "Tılsım Yedilisi": {
        "duz": "Ektiğin biçtiğin yok, öylece tarlaya bakıyorsun.",
        "ters": "Emeğin boşa gitti, ne ekersen biçemedin.",
    },
    "Tılsım Sekizlisi": {
        "duz": "Amelenin önde gideni gibi sabahlara kadar çalışıyorsun.",
        "ters": "Karın tok sırtımız pek ama emeğinin karşılığı sıfır.",
    },
    "Tılsım Dokuzlusu": {
        "duz": "Tek başına keyif yapıyorsun ama yalnızsın.",
        "ters": "Malın mülkün var ama huzurun yok, lüks içinde mutsuzluk.",
    },
    "Tılsım Onlusu": {
        "duz": "Aile parası veya miras konulu gerginlikler.",
        "ters": "Miras kavgası yüzünden mahkemelik olacaksınız.",
    },
    "Tılsım Prensi": {
        "duz": "Parayı bulacağını sanıp 5 kuruş harcayan stajyer.",
        "ters": "Tembellikten parayı da işi de kaybettin.",
    },
    "Tılsım Şövalyesi": {
        "duz": "Ağır vites ama en azından güvenilir bir ilerleyiş.",
        "ters": "Zaten yavaştین, şimdi tamamen durdun.",
    },
    "Tılsım Kraliçesi": {
        "duz": "Konforuna düşkün, lüks sevdalısı bir tip.",
        "ters": "Kredi kartı borçları dağ gibi yığıldı.",
    },
    "Tılsım Kralı": {
        "duz": "Para bende patron benim diyen ego tavan.",
        "ters": "Batık imparatorluğun başında tek başına kralcılık oynuyorsun.",
    },
}

if "adim" not in st.session_state:
  st.session_state.adim = "giriş"

# --- 1. GİRİŞ SAYFASI ---
if st.session_state.adim == "giriş":
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.markdown(
        "<h1 style='text-align: center;'> Tarot Bakımı💌</h1>",
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
      f"<h2 style='text-align: center;'>Hoş geldin sevgili {st.session_state.isim}"
      f" ({st.session_state.burc} Burcu)</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center;'>Aşağıdaki 78 gizemli karttan sezgilerinin"
      " seni çektiği <b>3 adet kartı</b> tül işlemeli arka yüzlerinden"
      " seç:</p>",
      unsafe_allow_html=True,
  )
  st.markdown("---")

  secilenler_kutulari = []
  cols = st.columns(4)

  for idx in range(78):
    col_idx = idx % 4
    with cols[col_idx]:
      st.markdown(
          "<div class='tarot-back'>"
          "<span style='font-size: 24px;'>💎</span>"
          f"<b style='color: #fef08a; font-size: 11px; margin-top: 6px;'>GİZLİ"
          f" KART #{idx+1}</b>"
          "</div>",
          unsafe_allow_html=True,
      )
      secildimi = st.checkbox(f"Seç ({idx+1})", key=f"kart_{idx}")
      if secildimi:
        secilenler_kutulari.append(idx)

  st.markdown("---")

  if len(secilenler_kutulari) > 3:
    st.error("Yalnızca 3 adet kart seçebilirsin, canımın içi.")
  elif len(secilenler_kutulari) == 3:
    if st.button("Seçtiğim Kartları Aç ve Falımı Gör 🌟"):
      secilenler_keys = random.sample(list(tum_kartlar.keys()), 3)
      sabit_fal = []
      for k in secilenler_keys:
        durum = random.choice(["duz", "ters"])
        # Handle cases where dictionary format might be a tuple or string
        val = tum_kartlar[k][durum]
        if isinstance(val, tuple):
          ozet, derin = val
        else:
          ozet, derin = val, val
        sabit_fal.append((k, durum, (ozet, derin)))
      st.session_state.sabit_fal = sabit_fal
      st.session_state.adim = "sonuc"
      st.rerun()
  else:
    st.info(
        f"Şu an {len(secilenler_kutulari)} kart seçtin. Toplam 3 kart seçmelisin."
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
        f" Durumu: {st.session_state.medeni_durum} | Durum:"
        f" {st.session_state.is_durumu}</p>",
        unsafe_allow_html=True,
    )
    st.write("Seçtiğin kartların ruhuna fısıldadıkları:")
    st.markdown("---")

    konumlar = [
        "GEÇMİŞ (Seni Buraya Getiren Temeller)",
        "ŞİMDİ (İçinde Bulunduğun Enerji)",
        "GELECEK (Önündeki Olası Yollar)",
    ]

    for i, (k_adi, durum, (ozet, derin)) in enumerate(
        st.session_state.sabit_fal
    ):
      durum_str = "Düz Akış" if durum == "duz" else "Ters Enerji"

      ekstra_yorum = ""
      if i == 1 and st.session_state.is_durumu == "Çalışmıyor":
        ekstra_yorum = (
            " (Şu an çalışmıyor olman, enerjini toparlaman ve kendine"
            " odaklanman için harika bir dönem.)"
        )
      elif i == 2 and st.session_state.is_durumu == "Öğrenci":
        ekstra_yorum = (
            " (Önümüzdeki dönemde öğrenim ve kişisel gelişim alanında karşına"
            " çok şanslı kapılar açılacak.)"
        )

      st.markdown(
          f"<div class='tarot-card-box'>"
          f"<h3>{konumlar[i]}</h3>"
          f"<p style='color: #fef08a; font-size: 16px; font-weight: 600;'>{k_adi}"
          f" <span style='font-size: 13px; color: #cbd5e1;'>({durum_str})"
          "</span></p>"
          f"<p><b>Özet:</b> {ozet}</p>"
          f"<p><b>Derin Yorum:</b> {derin}{ekstra_yorum}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if st.button("Yeni Bir Fal Bak 🫧"):
      st.session_state.adim = "giriş"
      st.rerun()
