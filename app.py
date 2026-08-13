import random
import streamlit as st

st.set_page_config(
    page_title="Modern Tarot Deneyimi",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Modern, Şık ve Temiz Tasarım
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
color: #f8fafc;
font-family: 'Inter', sans-serif;
}
.stButton>button {
width: 100%;
background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
color: #ffffff;
border-radius: 10px;
font-size: 16px;
height: 48px;
border: none;
font-weight: 600;
box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
transition: all 0.3s ease;
}
.stButton>button:hover {
background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%);
box-shadow: 0 6px 16px rgba(99, 102, 241, 0.5);
}
.tarot-card-box {
background: rgba(30, 27, 75, 0.6);
border: 1px solid rgba(129, 140, 248, 0.2);
padding: 24px;
border-radius: 16px;
margin-bottom: 20px;
backdrop-filter: blur(10px);
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
h1, h2, h3 { color: #f1f5f9 !important; font-weight: 700; }
p, label, span { color: #cbd5e1 !important; }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 72 Kartlık Genişletilmiş Örnek Veritabanı (Düz ve Ters Anlamlar)
tum_kartlar = {
    "Deli": {
        "duz": (
            "Yeni başlangıçlar, masumiyet ve spontanlık.",
            "Hayatında yepyeni bir sayfa açılıyor. İç sesini dinle ve korkusuzca adım at.",
        ),
        "ters": (
            "Pervasızlık, riskleri görmezden gelme.",
            "Düşünmeden attığın adımlar başına bela açabilir, biraz daha temkinli olmalısın.",
        ),
    },
    "Büyücü": {
        "duz": (
            "Yetenek, odaklanma ve potansiyeli gerçeğe dönüştürme.",
            "Elindeki tüm imkanlar lehine çalışıyor. Hedefine ulaşmak için mükemmel bir zaman.",
        ),
        "ters": (
            "Manipülasyon, potansiyeli harcama.",
            "Yeteneklerini yanlış yönlendiriyor ya da çevrendeki kişilerden kandırılma riski taşıyorsun.",
        ),
    },
    "Azize": {
        "duz": (
            "Sezgiler, bilinçaltı ve gizli kalmış sırlar.",
            "Mantığını bir kenara bırak ve iç sesine kulak ver. Sezgilerin seni yanıltmayacak.",
        ),
        "ters": (
            "Sezgileri bastırma, iç sesini duyamama.",
            "Kendi iç sesini susturduğun için yanlış kararlar alıyorsun, gerçeklere körsün.",
        ),
    },
    "İmparatoriçe": {
        "duz": (
            "Bereket, yaratıcılık ve doğanın bolluğu.",
            "Emeklerinin karşılığını fazlasıyla alacağın, üretken ve huzurlu bir döneme giriyorsun.",
        ),
        "ters": (
            "Tembellik, üretkenlik tıkanıklığı.",
            "Konfor alanına fazla kapıldın, bu da gelişimini durduruyor ve seni tembelleştiriyor.",
        ),
    },
    "İmparator": {
        "duz": (
            "Otorite, disiplin ve liderlik.",
            "Hayatının kontrolünü eline alma, kuralları koyma ve liderliği üstlenme zamanı.",
        ),
        "ters": (
            "Aşırı baskı, kontrol kaybı ve despotluk.",
            "Etrafındakilere karşı fazla kuralcı davranıyorsun ya da hayatın kontrolünü tamamen yitiriyorsun.",
        ),
    },
    "Aşıklar": {
        "duz": (
            "Uyum, bağlar ve kritik bir karar.",
            "Değerlerinle ilgili önemli bir yol ayrımındasın. Kalbinin sesini dinleyerek seç.",
        ),
        "ters": (
            "Uyumsuzluk, yanlış tercihler ve içsel çatışma.",
            "İlişkilerinde veya kararlarında uyum kopmuş durumda; yanlış bir yoldasın.",
        ),
    },
    "Ölüm": {
        "duz": (
            "Dönüşüm, bitiş ve yeni bir başlangıç.",
            "Eski bir dönemin kapısı kapanıyor. Bu değişime direnme, yeniliğe yer aç.",
        ),
        "ters": (
            "Değişimden korkma, geçmişe saplanıp kalma.",
            "Ömrünü tamamlamış şeyleri bırakmamakta inat ediyorsun, bu seni çürütüyor.",
        ),
    },
    "Yıldız": {
        "duz": (
            "Umut, ilham ve şifa.",
            "Fırtınalı günlerin ardından içini aydınlatacak taze bir umut ve huzur doğuyor.",
        ),
        "ters": (
            "Umutsuzluk, inanç kaybı.",
            "Geleceğe dair inancını yitirmiş gibisin, karanlık düşüncelerden sıyrılmalısın.",
        ),
    },
    "Kule": {
        "duz": (
            "Ani yıkım ve sarsıcı uyandıran gerçekler.",
            "Sahte temeller üzerine kurduğun yapılar yıkılıyor ama bu özgürleşmen için şart.",
        ),
        "ters": (
            "Felaketten kıl payı kurtulma, erteleme.",
            "Büyük bir krizin eşiğinden döndün ancak temeldeki sorunları çözmezsen tekrar yaşanacak.",
        ),
    },
    "Ay": {
        "duz": (
            "İllüzyonlar, belirsizlik ve derin korkular.",
            "Gördüğün her şey gerçeği yansıtmıyor. Zihnindeki kuruntulara karşı dikkatli ol.",
        ),
        "ters": (
            "Korkuların üstesinden gelme, sislerin dağılması.",
            "Zihnindeki bulutlar dağılıyor; olayların aslını net bir şekilde görmeye başlıyorsun.",
        ),
    },
    "Güneş": {
        "duz": (
            "Neşe, başarı ve canlılık.",
            "Her şeyin aydınlığa kavuştuğu, enerjinin tavan yaptığı harika bir dönem.",
        ),
        "ters": (
            "Geçici bulutlanma, ego.",
            "Mutluluk çok yakın ama kendi gururun yüzünden anı kaçırıyorsun.",
        ),
    },
    "Dünya": {
        "duz": (
            "Tamamlanma, başarı ve bütünlük.",
            "Uzun bir döngüyü başarıyla kapattın, şimdi hak ettiğin ödülü alma zamanı.",
        ),
        "ters": (
            "Eksik kalan kapanışlar.",
            "Son adıma kadar geldin ama bir şeyler hala eksik kalmış hissediliyor.",
        ),
    },
}

# Oturum yönetimi
if "adim" not in st.session_state:
  st.session_state.adim = "giriş"

# --- 1. GİRİŞ SAYFASI ---
if st.session_state.adim == "giriş":
  col1, col2, col3 = st.columns([1, 2, 1])
  with col1:
    st.image(
        "https://images.unsplash.com/photo-1514539079130-25950c84af65?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )
  with col2:
    st.markdown(
        "<h1 style='text-align: center;'>Tarot Deneyimi</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>Kaderini kendi ellerinle seç</p>",
        unsafe_allow_html=True,
    )

    isim = st.text_input("Adın:")
    burc = st.selectbox(
        "Burcun:",
        [
            "Koç",
            "Boğa",
            "İkizler",
            "Yengeç",
            "Aslan",
            "Başak",
            "Terazi",
            "Akrep",
            "Yay",
            "Oğlak",
            "Kova",
            "Balık",
        ],
    )

    if st.button("Kart Seçim Ekranına Geç"):
      if isim.strip() == "":
        st.warning("Lütfen adını gir.")
      else:
        st.session_state.isim = isim
        st.session_state.burc = burc
        st.session_state.adim = "secim"
        st.rerun()
  with col3:
    st.image(
        "https://images.unsplash.com/photo-1603217040209-47cad6f9518a?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )

# --- 2. KART SEÇİM SAYFASI (Kullanıcının kart seçtiği ekran) ---
elif st.session_state.adim == "secim":
  st.markdown(
      f"<h2>{st.session_state.isim}, desteden 3 adet kart seç</h2>",
      unsafe_allow_html=True,
  )
  st.write(
      "Aşağıdaki kapalı kartlar arasından sezgilerine güvenerek 3 tanesini"
      " işaretle:"
  )

  # 12 tane kapalı kart seçeneği oluşturalım
  secilenler = []
  cols = st.columns(4)

  # Kullanıcının çoklu seçim yapabilmesi için checkbox'lar koyuyoruz
  secim_havuzu = [f"Kart #{i+1}" for i in range(12)]

  secilenler_kutulari = []
  for idx, kart_isim in enumerate(secim_havuzu):
    col_idx = idx % 4
    with cols[col_idx]:
      # Kart arkası görseli gibi şık bir kutu
      st.markdown(
          "<div"
          " style='background:#312e81;padding:20px;text-align:center;border-radius:10px;margin-bottom:10px;border:1px"
          " solid #6366f1;'>🎴 <b>Kapalı Kart</b></div>",
          unsafe_allow_html=True,
      )
      secildimi = st.checkbox(f"Seç ({kart_isim})", key=f"kart_{idx}")
      if secildimi:
        secilenler_kutulari.append(kart_isim)

  st.markdown("---")

  if len(secilenler_kutulari) > 3:
    st.error("En fazla 3 kart seçebilirsin! Lütfen seçimi 3'e düşür.")
  elif len(secilenler_kutulari) == 3:
    if st.button("Seçtiğim Kartları Aç ve Falımı Gör"):
      # Sistem arkada rastgele kartları ve durumlarını atar
      secilenler_keys = random.sample(list(tum_kartlar.keys()), 3)
      sabit_fal = []
      for k in secilenler_keys:
        durum = random.choice(["duz", "ters"])
        sabit_fal.append((k, durum, tum_kartlar[k][durum]))
      st.session_state.sabit_fal = sabit_fal
      st.session_state.adim = "sonuc"
      st.rerun()
  else:
    st.info(
        f"Şu an {len(secilenler_kutulari)} kart seçtin. Lütfen toplam 3 kart"
        " seç."
    )

  if st.button("← Ana Sayfaya Dön"):
    st.session_state.adim = "giriş"
    st.rerun()

# --- 3. SONUÇ SAYFASI ---
elif st.session_state.adim == "sonuc":
  col_sol, col_orta, col_sag = st.columns([1, 4, 1])

  with col_sol:
    st.image(
        "https://images.unsplash.com/photo-1635850452968-3d6067db8a99?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )

  with col_orta:
    st.markdown(
        f"<h2>✨ {st.session_state.isim} ({st.session_state.burc}) İçin Seçtiğin"
        " Kartlar</h2>",
        unsafe_allow_html=True,
    )
    st.write("Seçtiğin kartların enerjine göre açılımı:")
    st.markdown("---")

    konumlar = [
        "GEÇMİŞ (Temeller)",
        "ŞİMDİ (Mevcut Enerji)",
        "GELECEK (Olası Yön)",
    ]

    for i, (k_adi, durum, (ozet, derin)) in enumerate(
        st.session_state.sabit_fal
    ):
      durum_str = "Düz" if durum == "duz" else "Ters"
      st.markdown(
          f"<div class='tarot-card-box'>"
          f"<h3>{konumlar[i]}: {k_adi} <span style='font-size:14px; color:#818cf8;'>({durum_str})</span></h3>"
          f"<p><b>Özet:</b> {ozet}</p>"
          f"<p><b>Detay:</b> {derin}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    # Ana Sayfaya Dönüş Butonu
    if st.button("← Ana Sayfaya Dön"):
      st.session_state.adim = "giriş"
      st.rerun()

  with col_sag:
    st.image(
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )
