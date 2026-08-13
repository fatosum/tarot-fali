
import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Modern Tam Dest Tarot Deneyimi",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Modern, Şık ve Temiz Tasarım (Kart Görselleri için Özel Stiller)
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
.tarot-back {
background: linear-gradient(135deg, #312e81 0%, #1e1b4b 100%);
border: 2px solid #818cf8;
border-radius: 12px;
padding: 15px 10px;
text-align: center;
box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2);
margin-bottom: 5px;
}
h1, h2, h3 { color: #f1f5f9 !important; font-weight: 700; }
p, label, span { color: #cbd5e1 !important; }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 78 Kartlık Tam Tarot Destesi Veritabanı
tum_kartlar = {
    # Majör Arkanalar (22 Kart)
    "Deli (The Fool)": {
        "duz": (
            "Yeni başlangıçlar, masumiyet ve spontanlık.",
            "Hayatında yepyeni bir sayfa açılıyor. İç sesini dinle ve korkusuzca adım at.",
        ),
        "ters": (
            "Pervasızlık, riskleri görmezden gelme.",
            "Düşünmeden attığın adımlar başına bela açabilir, biraz daha temkinli olmalısın.",
        ),
    },
    "Büyücü (The Magician)": {
        "duz": (
            "Yetenek, odaklanma ve potansiyeli gerçeğe dönüştürme.",
            "Elindeki tüm imkanlar lehine çalışıyor. Hedefine ulaşmak için mükemmel bir zaman.",
        ),
        "ters": (
            "Manipülasyon, potansiyeli harcama.",
            "Yeteneklerini yanlış yönlendiriyor ya da çevrendeki kişilerden kandırılma riski taşıyorsun.",
        ),
    },
    "Azize (The High Priestess)": {
        "duz": (
            "Sezgiler, bilinçaltı ve gizli kalmış sırlar.",
            "Mantığını bir kenara bırak ve iç sesine kulak ver. Sezgilerin seni yanıltmayacak.",
        ),
        "ters": (
            "Sezgileri bastırma, iç sesini duyamama.",
            "Kendi iç sesini susturduğun için yanlış kararlar alıyorsun, gerçeklere körsün.",
        ),
    },
    "İmparatoriçe (The Empress)": {
        "duz": (
            "Bereket, yaratıcılık ve doğanın bolluğu.",
            "Emeklerinin karşılığını fazlasıyla alacağın, üretken ve huzurlu bir döneme giriyorsun.",
        ),
        "ters": (
            "Tembellik, üretkenlik tıkanıklığı.",
            "Konfor alanına fazla kapıldın, bu da gelişimini durduruyor ve seni tembelleştiriyor.",
        ),
    },
    "İmparator (The Emperor)": {
        "duz": (
            "Otorite, disiplin ve liderlik.",
            "Hayatının kontrolünü eline alma, kuralları koyma ve liderliği üstlenme zamanı.",
        ),
        "ters": (
            "Aşırı baskı, kontrol kaybı ve despotluk.",
            "Etrafındakilere karşı fazla kuralcı davranıyorsun ya da hayatın kontrolünü tamamen yitiriyorsun.",
        ),
    },
    "Hierofant (The Hierophant)": {
        "duz": (
            "Gelenekler, ruhsal rehberlik ve toplumsal değerler.",
            "Kurallara ve köklü geleneklere bağlı kalmak bu süreçte sana güven verecek.",
        ),
        "ters": (
            "İsyankarlık, dogmalara karşı çıkma.",
            "Toplumsal kalıplara başkaldırıyorsun ancak bu durum seni yalnızlaştırabilir.",
        ),
    },
    "Aşıklar (The Lovers)": {
        "duz": (
            "Uyum, bağlar ve kritik bir karar.",
            "Değerlerinle ilgili önemli bir yol ayrımındasın. Kalbinin sesini dinleyerek seç.",
        ),
        "ters": (
            "Uyumsuzluk ve yanlış tercihler.",
            "İlişkilerinde veya kararlarında uyum kopmuş durumda; yanlış bir yoldasın.",
        ),
    },
    "Savaş Arabası (The Chariot)": {
        "duz": (
            "Zafer, irade gücü ve kararlılık.",
            "Karşına çıkan engelleri azmin sayesinde birer birer aşacaksın.",
        ),
        "ters": (
            "Kontrol kaybı ve yönsüzlük.",
            "Enerjini yanlış yönlendiriyorsun, kontrol elinden kayıp gitmek üzere.",
        ),
    },
    "Adalet (Justice)": {
        "duz": (
            "Adalet, hakkaniyet ve dürüstlük.",
            "Geçmişte yaptığın her şeyin adil karşılığını alacağın bir dönem.",
        ),
        "ters": (
            "Haksızlık ve önyargı.",
            "Durumları tarafsız değerlendiremediğin için haksız duruma düşebilirsin.",
        ),
    },
    "Ermiş (The Hermit)": {
        "duz": (
            "İçsel arayış, yalnızlık ve bilgelik.",
            "Bir süre kabuğuna çekilip kendi iç dünyanı dinlemen gerekiyor.",
        ),
        "ters": (
            "Aşırı izolasyon ve yalnızlık korkusu.",
            "Dünyadan tamamen soyutlandın, bu durum seni depresif bir ruh haline sokuyor.",
        ),
    },
    "Kader Çarkı (Wheel of Fortune)": {
        "duz": (
            "Şans, ani değişimler ve fırsatlar.",
            "Çark senin lehine dönüyor, hayatında sürpriz güzel gelişmeler kapıda.",
        ),
        "ters": (
            "Kötü şans ve değişime direnç.",
            "Şu aralar işler istendiği gibi gitmeyebilir, sabırlı olmalısın.",
        ),
    },
    "Güç (Strength)": {
        "duz": (
            "İçsel güç, cesaret ve sabır.",
            "Zorluklar karşısında dışsal kaba kuvvetle değil, içsel gücünle galip geleceksin.",
        ),
        "ters": (
            "Özgüven eksikliği ve zayıflık hissi.",
            "Kendi gücüne olan inancını yitirmişsin, içindeki potansiyeli küçümsüyorsun.",
        ),
    },
    "Asılı Adam (The Hanged Man)": {
        "duz": (
            "Bakış açısını değiştirme, fedakarlık ve duraklama.",
            "Olaylara farklı bir açıdan bakmayı denemelisin, şu anki duraklama sana iyi gelecek.",
        ),
        "ters": (
            "Boşuna fedakarlık ve zaman kaybı.",
            "Değişmeyecek durumlar için kendini feda ediyorsun, bu sadece seni yıpratır.",
        ),
    },
    "Ölüm (Death)": {
        "duz": (
            "Dönüşüm, bitiş ve yeni bir başlangıç.",
            "Eski bir dönemin kapısı kapanıyor. Bu değişime direnme, yeniliğe yer aç.",
        ),
        "ters": (
            "Değişimden korkma ve geçmişe saplanıp kalma.",
            "Ömrünü tamamlamış şeyleri bırakmamakta inat ediyorsun, bu seni çürütüyor.",
        ),
    },
    "Denge (Temperance)": {
        "duz": (
            "İtidal, uyum, denge ve şifa.",
            "Hayatındaki zıtlıkları uyum içinde harmanlayarak huzuru yakalayacaksın.",
        ),
        "ters": (
            "Dengesizlik ve aşırılıklar.",
            "İfrat ile tefrit arasında gidip geliyorsun, hayatında denge kalmamış.",
        ),
    },
    "Şeytan (The Devil)": {
        "duz": (
            "Bağımlılıklar, takıntılar ve kısıtlanma.",
            "Kendi ellerinle yarattığın toksik alışkanlıkların tutsağı olmuşsun.",
        ),
        "ters": (
            "Zincirleri kırma ve özgürleşme.",
            "Seni aşağı çeken toksik bir bağdan nihayet kurtuluyorsun.",
        ),
    },
    "Kule (The Tower)": {
        "duz": (
            "Ani yıkım ve sarsıcı uyandıran gerçekler.",
            "Sahte temeller üzerine kurduğun yapılar yıkılıyor ama bu özgürleşmen için şart.",
        ),
        "ters": (
            "Felaketten kıl payı kurtulma.",
            "Büyük bir krizin eşiğinden döndün ancak temeldeki sorunları çözmezsen tekrar yaşanacak.",
        ),
    },
    "Yıldız (The Star)": {
        "duz": (
            "Umut, ilham ve şifa.",
            "Fırtınalı günlerin ardından içini aydınlatacak taze bir umut ve huzur doğuyor.",
        ),
        "ters": (
            "Umutsuzluk ve inanç kaybı.",
            "Geleceğe dair inancını yitirmiş gibisin, karanlık düşüncelerden sıyrılmalısın.",
        ),
    },
    "Ay (The Moon)": {
        "duz": (
            "İllüzyonlar, belirsizlik ve derin korkular.",
            "Gördüğün her şey gerçeği yansıtmıyor. Zihnindeki kuruntulara karşı dikkatli ol.",
        ),
        "ters": (
            "Korkuların üstesinden gelme ve sislerin dağılması.",
            "Zihnindeki bulutlar dağılıyor; olayların aslını net bir şekilde görmeye başlıyorsun.",
        ),
    },
    "Güneş (The Sun)": {
        "duz": (
            "Neşe, başarı ve canlılık.",
            "Her şeyin aydınlığa kavuştuğu, enerjinin tavan yaptığı harika bir dönem.",
        ),
        "ters": (
            "Geçici bulutlanma ve ego.",
            "Mutluluk çok yakın ama kendi gururun yüzünden anı kaçırıyorsun.",
        ),
    },
    "Mahkeme (Judgement)": {
        "duz": (
            "Uyanış, hesaplaşma ve ilahi adalet.",
            "Geçmişin muhasebesini yapıp hayatınla ilgili büyük ve hayati bir karar veriyorsun.",
        ),
        "ters": (
            "Şüphe ve suçluluk duygusu.",
            "Kendi kendini suçlayıp duruyorsun, geçmişin hatalarından kopamıyorsun.",
        ),
    },
    "Dünya (The World)": {
        "duz": (
            "Tamamlanma, başarı ve bütünlük.",
            "Uzun bir döngüyü başarıyla kapattın, şimdi hak ettiğin ödülü alma zamanı.",
        ),
        "ters": (
            "Eksik kalan kapanışlar.",
            "Son adıma kadar geldin ama bir şeyler hala eksik kalmış hissediliyor.",
        ),
    },
    # Kupa Serisi (Minör - 14 Kart)
    *(
        (
            f"Kupa {n}",
            {
                "duz": (
                    f"Kupa {n} düz enerjisi: Duygusal denge, ilişkilerde derinleşme ve huzur.",
                    "Kalbinin kapılarını açtığın bu dönemde duygusal tatmin yaşayacaksın.",
                ),
                "ters": (
                    f"Kupa {n} ters enerjisi: Duygusal tıkanıklık veya kırgınlık.",
                    "Beklentilerinin karşılığını alamamak seni biraz üzebilir, içine kapanma.",
                ),
            },
        )
        for n in [
            "Ası",
            "İkilisi",
            "Üçlüsü",
            "Dörtlüsü",
            "Beşlisi",
            "Altılısı",
            "Yedilisi",
            "Sekizlisi",
            "Dokuzlusu",
            "Onlusu",
            "Prens",
            "Şövalye",
            "Kraliçe",
            "Kral",
        ]
    ),
    # Kılıç Serisi (Minör - 14 Kart)
    *(
        (
            f"Kılıç {n}",
            {
                "duz": (
                    f"Kılıç {n} düz enerjisi: Zihinsel netlik, strateji ve mantıklı kararlar.",
                    "Mantığını ön plana koyarak sorunları hızlıca çözeceğin bir döneme giriyorsun.",
                ),
                "ters": (
                    f"Kılıç {n} ters enerjisi: Zihinsel karışıklık, sert sözler ve tartışma.",
                    "Sivri dilli olmaktan kaçınmalısın, yanlış anlaşılmalar yaşanabilir.",
                ),
            },
        )
        for n in [
            "Ası",
            "İkilisi",
            "Üçlüsü",
            "Dörtlüsü",
            "Beşlisi",
            "Altılısı",
            "Yedilisi",
            "Sekizlisi",
            "Dokuzlusu",
            "Onlusu",
            "Prens",
            "Şövalye",
            "Kraliçe",
            "Kral",
        ]
    ),
    # Tılsım / Para Serisi (Minör - 14 Kart)
    *(
        (
            f"Tılsım {n}",
            {
                "duz": (
                    f"Tılsım {n} düz enerjisi: Maddi kazanç, bereket, iş ve kariyer başarısı.",
                    "Finansal konularda yüzünü güldürecek gelişmeler kapıda.",
                ),
                "ters": (
                    f"Tılsım {n} ters enerjisi: Maddi kaygılar ve parasal tıkanıklık.",
                    "Bütçeni idare ederken daha dikkatli olmalı, riskli yatırımlardan kaçınmalısın.",
                ),
            },
        )
        for n in [
            "Ası",
            "İkilisi",
            "Üçlüsü",
            "Dörtlüsü",
            "Beşlisi",
            "Altılısı",
            "Yedilisi",
            "Sekizlisi",
            "Dokuzlusu",
            "Onlusu",
            "Prens",
            "Şövalye",
            "Kraliçe",
            "Kral",
        ]
    ),
    # Asa Serisi (Minör - 14 Kart)
    *(
        (
            f"Asa {n}",
            {
                "duz": (
                    f"Asa {n} düz enerjisi: Tutku, yüksek enerji, yaratıcılık ve eylem.",
                    "Projelerini hayata geçirmek için harika bir motivasyon ve enerji buluyorsun.",
                ),
                "ters": (
                    f"Asa {n} ters enerjisi: Motivasyon düşüklüğü ve enerjinin tükenmesi.",
                    "Üzerindeki ölü toprağını atıp yeniden harekete geçmen biraz zaman alabilir.",
                ),
            },
        )
        for n in [
            "Ası",
            "İkilisi",
            "Üçlüsü",
            "Dörtlüsü",
            "Beşlisi",
            "Altılısı",
            "Yedilisi",
            "Sekizlisi",
            "Dokuzlusu",
            "Onlusu",
            "Prens",
            "Şövalye",
            "Kraliçe",
            "Kral",
        ]
    ),
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
    dogum_tarihi = st.date_input(
        "Doğum Tarihin:",
        min_value=datetime.date(1940, 1, 1),
        max_value=datetime.date.today(),
        value=datetime.date(2000, 1, 1),
    )

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

    medeni_durum = st.selectbox(
        "Medeni Durumun:", ["Bekar", "İlişkisi Var", "Evli", "Karmaşık / Diğer"]
    )

    is_durumu = st.selectbox(
        "İş / Çalışma Durumun:",
        [
            "Çalışıyor / Profesyonel",
            "Öğrenci",
            "Kendi İşinin Sahibi",
            "İş Arıyor / Çalışmıyor",
        ],
    )

    if st.button("Kart Seçim Ekranına Geç"):
      bugun = datetime.date.today()
      yas = (
          bugun.year
          - dogum_tarihi.year
          - ((bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day))
      )

      if isim.strip() == "":
        st.warning("Lütfen adını gir.")
      elif yas < 14:
        st.error(
            "Üzgünüm, 14 yaşından küçüklerin bu uygulamayı kullanması"
            " yasaktır."
        )
      else:
        st.session_state.isim = isim
        st.session_state.burc = burc
        st.session_state.medeni_durum = medeni_durum
        st.session_state.is_durumu = is_durumu
        st.session_state.adim = "secim"
        st.rerun()
  with col3:
    st.image(
        "https://images.unsplash.com/photo-1603217040209-47cad6f9518a?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )

# --- 2. KART SEÇİM SAYFASI (Arkası dönük Tarot Kartı Tasarımıyla) ---
elif st.session_state.adim == "secim":
  st.markdown(
      f"<h2>{st.session_state.isim}, 78 Kartlık Tam Desteden 3 Adet Kart"
      " Seç</h2>",
      unsafe_allow_html=True,
  )
  st.write(
      "Aşağıdaki kapalı tarot kartlarından sezgilerine en çok hitap eden 3"
      " tanesini işaretle:"
  )

  secilenler_kutulari = []
  cols = st.columns(4)

  # 78 kartın tamamını görsel tarot arkası tasarımıyla listeleme
  for idx in range(78):
    col_idx = idx % 4
    with cols[col_idx]:
      st.markdown(
          "<div class='tarot-back'>"
          "<span style='font-size: 24px;'>🔮</span><br>"
          f"<b style='color: #c7d2fe; font-size: 12px;'>Kart #{idx+1}</b>"
          "</div>",
          unsafe_allow_html=True,
      )
      secildimi = st.checkbox(f"Seç ({idx+1})", key=f"kart_{idx}")
      if secildimi:
        secilenler_kutulari.append(idx)

  st.markdown("---")

  if len(secilenler_kutulari) > 3:
    st.error("En fazla 3 kart seçebilirsin! Lütfen seçimi 3'e düşür.")
  elif len(secilenler_kutulari) == 3:
    if st.button("Seçtiğim Kartları Aç ve Falımı Gör"):
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
        f"<h2>✨ {st.session_state.isim} ({st.session_state.burc}) İçin Tarot"
        " Analizi</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='font-size:14px; color:#94a3b8;'>Durum: {st.session_state.medeni_durum}"
        f" | Kariyer: {st.session_state.is_durumu}</p>",
        unsafe_allow_html=True,
    )
    st.write("Seçtiğin kartların yaşamına yansımaları:")
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

      ekstra_yorum = ""
      if i == 1 and st.session_state.medeni_durum == "İlişkisi Var":
        ekstra_yorum = (
            " (Bu enerji ilişkine de doğrudan yansıyor, iletişimine dikkat"
            " et.)"
        )
      elif i == 2 and st.session_state.is_durumu == "Öğrenci":
        ekstra_yorum = (
            " (Gelecekteki bu yönelim eğitim ve kariyer planlarını da etkileyecek.)"
        )

      st.markdown(
          f"<div class='tarot-card-box'>"
          f"<h3>{konumlar[i]}: {k_adi} <span style='font-size:14px; color:#818cf8;'>({durum_str})</span></h3>"
          f"<p><b>Özet:</b> {ozet}</p>"
          f"<p><b>Detay:</b> {derin}{ekstra_yorum}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if st.button("← Ana Sayfaya Dön"):
      st.session_state.adim = "giriş"
      st.rerun()

  with col_sag:
    st.image(
        "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=300&auto=format&fit=crop",
        use_container_width=True,
    )
