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


# Zaman bağlamlarına göre zenginleştirilmiş ve doğrulanmış tarot veritabanı
tum_kartlar = {
    "Deli (The Fool)": {
        "duz": {
            "gecmis": (
                "Geçmişte mantığını bir kenara bırakıp tamamen sezgilerinle"
                " ya da fevri bir kararla yepyeni bir yola, bilinmeze doğru"
                " adım atmışsın."
            ),
            "simdi": (
                "Şu an hayatında büyük bir risk alma eşiğindesin; önünü tam"
                " olarak göremiyorsun ama içindeki macera isteği baskın"
                " geliyor."
            ),
            "gelecek": (
                "Gelecekte seni hazırlıksız yakalayacak ani bir değişim ve"
                " risksiz adım atman gereken yepyeni bir başlangıç bekliyor,"
                " dikkatli olmalısın."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişteki pervasız ve düşüncesiz hareketlerin başına"
                " merdiven altı işler ve gereksiz riskler açmış."
            ),
            "simdi": (
                "Şu sıralar ayağını taşa takıp düşmek üzeresin ama hala"
                " kendini her şeyin yolunda olduğuna dair kandırmaya"
                " çalışıyorsun."
            ),
            "gelecek": (
                "Gelecekte aşırı aceleciliğin ve tedbirsizliğin yüzünden"
                " zarara uğrayabilir, plansızlığın kurbanı olabilirsin."
            ),
        },
    },
    "Büyücü (The Magician)": {
        "duz": {
            "gecmis": (
                "Geçmişte elindeki tüm imkanları ve becerileri ustalıkla"
                " kullanarak çevrendeki durumları kendi lehine çevirmeyi"
                " başarmışsın."
            ),
            "simdi": (
                "Şu an elinde güçlü kozlar var, iletişim yeteneğini ve zekanı"
                " kullanarak krizleri yönetebilecek güçtesin."
            ),
            "gelecek": (
                "Gelecekte yaratıcılığın sayesinde önüne çıkacak fırsatları"
                " en iyi şekilde yönlendirecek ve projelerini gerçeğe"
                " dönüştüreceksin."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte etrafındaki insanları manipüle etmiş ya da hileli"
                " yollarla kısa süreli çıkarlar elde etmeye çalışmışsın."
            ),
            "simdi": (
                "Şu an etrafında seni kandırmaya çalışan, sahte vaatlerle"
                " parmağında oynatmak isteyen manipülatif kişilere karşı"
                " uyanık olmalısın."
            ),
            "gelecek": (
                "Gelecekte güvenilmez niyetlerle yaklaşan kişilerin kurduğu"
                " tuzaklara düşmemek için gözünü dört açman gerekecek."
            ),
        },
    },
    "Mahkeme (Judgement)": {
        "duz": {
            "gecmis": (
                "Geçmişte verdiğin kararların ve yaptığın seçimlerin"
                " sonuçlarıyla yüzleştiğin köklü bir hesaplaşma dönemi"
                " yaşamışsın."
            ),
            "simdi": (
                "Şu an geçmişin faturaları birer birer önüne konuluyor; ne"
                " ektiysen onu biçtiğin, adaletin yerini bulduğu bir"
                " dönemdesin."
            ),
            "gelecek": (
                "Gelecekte uzun süredir ardında bıraktığını sandığın eski"
                " meseleler nihai bir karara bağlanacak ve tertemiz bir"
                " sayfaya geçeceksin."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte hatalarını kabul etmekten kaçınmış, sorumluluk"
                " almaktan sürekli kaçarak kaçak oynamışsın."
            ),
            "simdi": (
                "Şu an öz eleştiri yapmaktan uzak duruyor, sorumluluğu hep"
                " başkalarına yıkarak kendi gerçeğini örtbas etmeye"
                " çalışıyorsun."
            ),
            "gelecek": (
                "Gelecekte kaçınılmaz yüzleşmeleri daha fazla erteleyemeyecek"
                " ve gerçeğin duvarına sert bir şekilde çarpacaksın."
            ),
        },
    },
    "Kupa Altılısı": {
        "duz": {
            "gecmis": (
                "Geçmişteki güzel anılar, eski dostluklar ve çocuksu saf"
                " duygular hafızanda derin izler bırakmış."
            ),
            "simdi": (
                "Şu an geçmişin nostaljik rüzgarlarına kapılmış, eski günlerin"
                " huzurunu bugünde aramaktasın."
            ),
            "gelecek": (
                "Gelecekte geçmişten gelen bir kişi, eski bir olay veya"
                " anılar yeniden kapını çalarak karşına çıkacak; bu durum seni"
                " duygusal bir muhasebeye götürecek."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte yaşadığın olumsuz olaylara ve eski travmalara takılı"
                " kalıp ilerlemeni kendi ellerinle engellemişsin."
            ),
            "simdi": (
                "Şu an geçmişin o nostaljik ama boğucu bataklığında"
                " debeleniyor, dünü bırakamadığın için bugünü kaçırıyorsun."
            ),
            "gelecek": (
                "Gelecekte geçmişin gölgesinden kurtulamazsan, sürekli geriye"
                " bakmaktan önündeki yeni mutluluk fırsatlarını"
                " göremeyeceksin."
            ),
        },
    },
}

# Rastgele kart havuzunu doldurmak için örnek ek kartlar (Zaman bağlamlarıyla)
diger_kartlar = [
    (
        "Kılıç Üçlüsü",
        {
            "gecmis": "Geçmişte aldığın ani bir haber veya derin bir kalp kırıklığı ruhunda cicat bırakmış.",
            "simdi": "Şu an ruhsal olarak yıpratıcı bir gerçekle yüzleşiyor ve acı çekiyorsun.",
            "gelecek": (
                "Gelecekte seni üzebilecek bazı gerçekler açığa çıkabilir,"
                " ancak bu acı seni olgunlaştıracak."
            ),
        },
    ),
    (
        "Kader Çarkı",
        {
            "gecmis": "Geçmişte hayatının akışını değiştiren ani ve beklenmedik dönemeçlerden geçtin.",
            "simdi": "Şu an hayatında ilahi bir döngünün ve kaderin getirdiği değişimlerin merkezindesin.",
            "gelecek": (
                "Gelecekte rüzgarın yönü tamamen lehine dönecek ve yeni bir"
                " şans kapısı aralanacak."
            ),
        },
    ),
    (
        "Güneş (The Sun)",
        {
            "gecmis": "Geçmişte büyük bir ferahlama, aydınlanma ve mutluluk dönemi yaşamışsın.",
            "simdi": "Şu an enerjin yüksek, her şey yolunda görünüyor ve içini ısıtan bir dönemeçtesin.",
            "gelecek": (
                "Gelecekte başarı, neşe ve huzur dolu günler seni bekliyor,"
                " karanlıklar tamamen geride kalacak."
            ),
        },
    ),
    (
        "Kule (The Tower)",
        {
            "gecmis": "Geçmişte ani bir krizle kurduğun tüm düzen alt üst olmuş, büyük bir sarsıntı yaşamışsın.",
            "simdi": "Şu an hayatında bazı yapı taşları yerinden oynuyor, beklenmedik değişimlerle sınanıyorsun.",
            "gelecek": (
                "Gelecekte yanlış temeller üzerine kurduğun her şey yıkılacak"
                " ki daha sağlam bir yapı inşa edebilesin."
            ),
        },
    ),
    (
        "Aşıklar (The Lovers)",
        {
            "gecmis": "Geçmişte hayatını kökten etkileyen kritik bir ilişki veya değer seçimi yapmak zorunda kalmışsın.",
            "simdi": "Şu an kalbinle mantığın arasında sıkışıp kaldığın önemli bir karar aşamasındasın.",
            "gelecek": (
                "Gelecekte hayatının yönünü belirleyecek kalıcı bir ortaklık"
                " veya ilişki kararı alacaksın."
            ),
        },
    ),
]

for kart_adi, anlambilim in diger_kartlar:
  if kart_adi not in tum_kartlar:
    tum_kartlar[kart_adi] = {
        "duz": anlambilim,
        "ters": {
            "gecmis": f"Geçmişte {kart_adi} enerjisinin ters etkisiyle yanlış yönlendirilmişsin.",
            "simdi": f"Şu an {kart_adi} kartının ters açılımı tıkanıklıklara ve zorluklara işaret ediyor.",
            "gelecek": f"Gelecekte bu enerjinin ters dönmesiyle bazı engelleri aşmak için ekstra çaba sarf etmen gerekecek.",
        },
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
      f"<h2 style='text-align: center;'>Hoş geldin sevgili {st.session_state.isim}"
      f" ({st.session_state.burc} Burcu)</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center;'>Aşağıdaki 12 gizemli karttan sezgilerinin"
      " seni çektiği <b>tam olarak 3 adet kartı</b> işaretle:</p>",
      unsafe_allow_html=True,
  )
  st.markdown("---")

  secilenler_kutulari = []
  cols = st.columns(4)

  # 12 kartlık sabit bir havuz gösterelim ki kullanıcı kendi kartlarını net seçebilsin
  havuz_kartlari = list(tum_kartlar.keys())[:12]

  secimler = {}
  for idx, kart_ismi in enumerate(havuz_kartlari):
    col_idx = idx % 4
    with cols[col_idx]:
      st.markdown(
          "<div class='tarot-back'>"
          "<span style='font-size: 24px;'>💎</span>"
          f"<b style='color: #fef08a; font-size: 11px; margin-top: 6px;'>KART"
          f" #{idx+1}</b>"
          "</div>",
          unsafe_allow_html=True,
      )
      secildimi = st.checkbox(f"Seç #{idx+1}", key=f"kart_sec_{idx}")
      if secildimi:
        secilenler_kutulari.append(kart_ismi)

  st.markdown("---")

  if len(secilenler_kutulari) > 3:
    st.error(
        "Yalnızca 3 adet kart seçebilirsin! Lütfen seçimini 3 karta düşür."
    )
  elif len(secilenler_kutulari) == 3:
    if st.button("Seçtiğim Kartları Aç ve Falımı Gör 🌟"):
      # Kullanıcının seçtiği 3 kartı sırasıyla GEÇMİŞ, ŞİMDİ, GELECEK olarak atayalım
      secilen_fal = []
      zaman_dilimleri = ["gecmis", "simdi", "gelecek"]

      for i, k_adi in enumerate(secilenler_kutulari):
        durum = random.choice(["duz", "ters"])
        zaman = zaman_dilimleri[i]
        detay = tum_kartlar[k_adi][durum][zaman]
        durum_metni = "Düz Akış" if durum == "duz" else "Ters Enerji"
        secilen_fal.append((k_adi, durum_metni, detay, zaman))

      st.session_state.gercek_fal = secilen_fal
      st.session_state.adim = "sonuc"
      st.rerun()
  else:
    st.info(
        f"Şu an {len(secilenler_kutulari)} kart seçtin. Lütfen tam 3 kart"
        " işaretle."
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
    st.write("Seçtiğin kartların zaman akışına göre derinlemesine analizi:")
    st.markdown("---")

    basliklar = {
        "gecmis": "GEÇMİŞ (Seni Buraya Getiren Temeller)",
        "simdi": "ŞİMDİ (İçinde Bulunduğun Enerji)",
        "gelecek": "GELECEK (Önündeki Olası Yollar ve Gelişmeler)",
    }

    for k_adi, durum_metni, detay, zaman in st.session_state.gercek_fal:
      st.markdown(
          f"<div class='tarot-card-box'>"
          f"<h3>{basliklar[zaman]}</h3>"
          f"<p style='color: #fef08a; font-size: 16px; font-weight: 600;'>{k_adi}"
          f" <span style='font-size: 13px; color: #cbd5e1;'>({durum_metni})"
          "</span></p>"
          f"<p><b>Yorum:</b> {detay}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if st.button("Yeni Bir Fal Bak 🫧"):
      st.session_state.adim = "giriş"
      st.rerun()
