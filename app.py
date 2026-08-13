import datetime
import random
import streamlit as st

st.set_page_config(
    page_title="Mistik Tarot Deneyimi",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Gönderdiğin görsellere ve mistik konsepte uygun yumuşak, lüks ve modern tasarım
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background: linear-gradient(135deg, #090d16 0%, #171c28 50%, #0f172a 100%);
color: #f1f5f9;
font-family: 'Inter', sans-serif;
}
.stButton>button {
width: 100%;
background: linear-gradient(135deg, #d4af37 0%, #aa771c 100%);
color: #ffffff;
border-radius: 12px;
font-size: 16px;
height: 50px;
border: none;
font-weight: 600;
box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
transition: all 0.3s ease;
}
.stButton>button:hover {
background: linear-gradient(135deg, #e6c555 0%, #d4af37 100%);
box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
}
.tarot-card-box {
background: rgba(23, 28, 40, 0.7);
border: 1px solid rgba(212, 175, 55, 0.3);
padding: 24px;
border-radius: 16px;
margin-bottom: 20px;
backdrop-filter: blur(12px);
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
/* Dikey ve Dikdörtgen Tarot Kartı Arkası Tasarımı */
.tarot-back {
background: linear-gradient(145deg, #1a2234 0%, #0f172a 100%);
border: 2px solid #d4af37;
border-radius: 10px;
width: 100%;
height: 110px;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
text-align: center;
box-shadow: 0 4px 15px rgba(212, 175, 55, 0.15);
margin-bottom: 8px;
transition: transform 0.2s ease;
}
.tarot-back:hover {
transform: translateY(-3px);
border-color: #f3e5ab;
}
h1, h2, h3 { color: #fdfbf7 !important; font-weight: 600; }
p, label, span { color: #cbd5e1 !important; }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Doğum tarihine göre otomatik burç hesaplama fonksiyonu
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


# 78 Kartlık Tam Tarot Destesi Veritabanı
tum_kartlar = {
    # Majör Arkanalar (22 Kart)
    "Deli (The Fool)": {
        "duz": (
            "Yeni başlangıçlar, saf bir heyecan ve akışa güvenmek.",
            "Hayatında yepyeni, tertemiz bir sayfa açılıyor. İçindeki coşkuya kulak ver ve cesurca adım at.",
        ),
        "ters": (
            "Pervasızlık veya nereye gittiğini bilememe.",
            "Küçük bir durup düşünmekte fayda var; acele kararlar seni yorabilir.",
        ),
    },
    "Büyücü (The Magician)": {
        "duz": (
            "Yeteneklerini konuşturma, yaratıcılık ve imkanları hayata geçirme.",
            "Şu an ellerindeki güç ve potansiyel muazzam. İstediğin her şeyi gerçeğe dönüştürebilirsin.",
        ),
        "ters": (
            "Potansiyeli harcama veya odak dağılması.",
            "Enerjini çok fazla noktaya dağıtıyorsun; odağını tek bir yere toplamak mucizeler yaratacaktır.",
        ),
    },
    "Azize (The High Priestess)": {
        "duz": (
            "Derin sezgiler, sırlar ve içsel rehberlik.",
            "Mantığından ziyade kalbinin ve hislerinin fısıltılarına kulak ver. İç sesin seni asla yanıltmaz.",
        ),
        "ters": (
            "İç sesini bastırma, huzursuzluk.",
            "Kendi sezgilerini görmezden geldiğin için kararsızlık yaşıyorsun.",
        ),
    },
    "İmparatoriçe (The Empress)": {
        "duz": (
            "Bereket, bolluk, şefkat ve üretkenlik.",
            "Emeklerinin karşılığını fazlasıyla alacağın, adeta çiçek açacağın huzurlu bir döneme giriyorsun.",
        ),
        "ters": (
            "Üretkenlikte duraksama veya aşırı düşkünlük.",
            "Kendini biraz ihmal etmiş olabilirsin; önce kendi ruhunu beslemelisin.",
        ),
    },
    "İmparator (The Emperor)": {
        "duz": (
            "Otorite, düzen kurma ve hayatın dizginlerini ele alma.",
            "Hayatında kuralları yeniden yazma, kendi liderliğini ilan etme ve sağlam temeller atma zamanı.",
        ),
        "ters": (
            "Aşırı kontrolcülük veya esneklik eksikliği.",
            "Her şeyi kontrol etmeye çalışmak seni yıpratabilir, akışa biraz alan tanımalısın.",
        ),
    },
    "Hierofant (The Hierophant)": {
        "duz": (
            "Manevi rehberlik, gelenekler ve güven.",
            "Köklü değerler ve güvendiğin kişilerden alacağın tavsiyeler bu süreçte yolunu aydınlatacak.",
        ),
        "ters": (
            "Kalıplara sığmama, isyankar hissetme.",
            "Sana dayatılan eski kuralları sorguluyor ve kendi yolunu çizmek istiyorsun.",
        ),
    },
    "Aşıklar (The Lovers)": {
        "duz": (
            "Kalpten gelen bağlar, uyum ve kritik bir seçim.",
            "Değerlerinle ilgili kalbinin sesini dinleyeceğin tatlı bir yol ayrımındasın.",
        ),
        "ters": (
            "Uyumsuzluk veya yanlış anlaşılmalar.",
            "İlişkilerinde veya kararlarında dengeyi bulmakta zorlanabilirsin, sabırlı ol.",
        ),
    },
    "Savaş Arabası (The Chariot)": {
        "duz": (
            "Zafer, irade gücü ve kararlılıkla ilerleme.",
            "Karşına çıkan engelleri azmin ve inancın sayesinde birer birer geride bırakıyorsun.",
        ),
        "ters": (
            "Kontrolü kaybetme hissi veya yönsüzlük.",
            "Aynı anda çok fazla şeye yetişmeye çalışmak enerjini tüketebilir.",
        ),
    },
    "Adalet (Justice)": {
        "duz": (
            "Adalet, dürüstlük ve hak ettiğini bulma.",
            "Geçmişte gösterdiğin her çabanın, ektiğin her tohumun adil karşılığını alıyorsun.",
        ),
        "ters": (
            "Haksızlığa uğramışlık hissi veya önyargı.",
            "Olaylara karşı biraz daha tarafsız ve esnek bakmaya çalışmalısın.",
        ),
    },
    "Ermiş (The Hermit)": {
        "duz": (
            "İçsel yolculuk, huzurlu yalnızlık ve bilgelik.",
            "Bir süre kalabalıklarca uzaklaşıp kendi iç sesini dinlemek ruhuna çok iyi gelecek.",
        ),
        "ters": (
            "Aşırı kapanma veya dış dünyadan kopma.",
            "Yalnızlığı abartıp sevdiklerini dışlıyor olabilirsin, dengeyi koru.",
        ),
    },
    "Kader Çarkı (Wheel of Fortune)": {
        "duz": (
            "Şansın dönmesi, sürpriz gelişmeler ve ilahi akış.",
            "Kader çarkı senin lehinə dönüyor; hayatında çok keyifli ve şanslı bir rüzgar esmeye başlıyor.",
        ),
        "ters": (
            "Geçici aksilikler veya değişime direnç.",
            "Her şeyin anında olmasını istemek yerine, zamanın akışına güvenmelisin.",
        ),
    },
    "Güç (Strength)": {
        "duz": (
            "İçsel cesaret, şefkat ve nazik bir güç.",
            "Zorlukları kaba kuvvetle değil, kalbindeki asalet ve sabırla kolayca aşacaksın.",
        ),
        "ters": (
            "Özgüven dalgalanmaları veya içsel yorgunluk.",
            "Kendi gücünü küçümseme; içindeki ışık eskisinden daha parlak.",
        ),
    },
    "Asılı Adam (The Hanged Man)": {
        "duz": (
            "Bakış açısını değiştirme, durup dinlenme ve teslimiyet.",
            "Olayları kafanda tersine çevirip bambaşka bir gözle göreceğin aydınlatıcı bir mola.",
        ),
        "ters": (
            "Boşuna kürek çekme hissi veya direniş.",
            "Değiştiremeyeceğin şeyler için kendini yıpratmayı bırakmalısın.",
        ),
    },
    "Ölüm (Death)": {
        "duz": (
            "Kökten dönüşüm, kapanan eski defterler ve taze başlangıçlar.",
            "Ömrünü tamamlamış bir döneme harika bir veda ediyorsun. Yeniliğe yer aç.",
        ),
        "ters": (
            "Geçmişe tutunma korkusu.",
            "Gitmesine izin vermen gereken kişileri veya alışkanlıkları hala tutuyorsun.",
        ),
    },
    "Denge (Temperance)": {
        "duz": (
            "Uyum, huzur, şifa ve orta yolu bulma.",
            "Hayatındaki zıtlıkları kusursuz bir uyumla harmanlayıp içsel huzuru yakalıyorsun.",
        ),
        "ters": (
            "Aşırılıklar ve dengeyi kaybetme.",
            "Hayatında küçük pürüzler varsa, acele etmeden sakinleşmeyi dene.",
        ),
    },
    "Şeytan (The Devil)": {
        "duz": (
            "Takıntılar, toksik alışkanlıklar veya kısıtlanmışlık.",
            "Kendi ellerinle yarattığın kuruntuların veya alışkanlıkların tutsağı olmaktan vazgeç.",
        ),
        "ters": (
            "Zincirleri kırma ve özgürlüğe kavuşma.",
            "Seni aşağı çeken ağır bir yükten veya bağımlılıktan nihayet sıyrılıyorsun.",
        ),
    },
    "Kule (The Tower)": {
        "duz": (
            "Ani ve sarsıcı farkındalıklar, eski yapıların yıkılışı.",
            "Beklenmedik ama seni sahte durumlardan kurtaracak özgürleştirici bir değişim.",
        ),
        "ters": (
            "Küçük bir krizden kıl payı kurtulma.",
            "Atlatılan bir badirenin ardından derin bir nefes alacaksın.",
        ),
    },
    "Yıldız (The Star)": {
        "duz": (
            "Umut, ilham, şifa ve parlak bir gelecek.",
            "Karanlık günlerin ardından içini ısıtacak taze bir umut ve mucizeler dönemi başlıyor.",
        ),
        "ters": (
            "Geçici umutsuzluk hissi.",
            "Hayata olan inancını tazelemek için kendine biraz zaman tanımalısın.",
        ),
    },
    "Ay (The Moon)": {
        "duz": (
            "Sezgiler, rüyalar ve sisli, belirsiz durumlar.",
            "Gördüğün ya da duyduğun her şey ilk başta algıladığın gibi olmayabilir, sezgilerine güven.",
        ),
        "ters": (
            "Korkuların dağılması ve gerçeklerin ortaya çıkışı.",
            "Zihnindeki bulutlar yavaş yavaş aralanıyor, her şey netleşiyor.",
        ),
    },
    "Güneş (The Sun)": {
        "duz": (
            "Neşe, başarı, canlılık ve saf mutluluk.",
            "Her şeyinyle aydınlığa kavuştuğun, yüzünün güleceği harika bir dönem seni bekliyor.",
        ),
        "ters": (
            "Bulutlu ama geçici bir neşesizlik.",
            "Mutluluk çok yakın, sadece içindeki neşeyi dışarı çıkarmana engel olan şeyleri bırak.",
        ),
    },
    "Mahkeme (Judgement)": {
        "duz": (
            "İçsel uyanış, öz eleştiri ve hayatınla ilgili büyük bir hamle.",
            "Geçmişin muhasebesini yapıp seni ileri taşıyacak tertemiz bir sayfa seçiyorsun.",
        ),
        "ters": (
            "Geçmişteki pişmanlıklara takılı kalma.",
            "Artık kendini suçlamayı bırakıp önстере bakma zamanı.",
        ),
    },
    "Dünya (The World)": {
        "duz": (
            "Tamamlanma, kutlama, başarı ve bütünlük.",
            "Uzun soluklu bir dönemi muazzam bir başarıyla taçlandırıyor, yeni bir çembere adım atıyorsun.",
        ),
        "ters": (
            "Son adreste ufak bir gecikme.",
            "Çok az kaldı, sabrının karşılığını almak üzeresin.",
        ),
    },
}

# Minör Arkanaları Güvenli Ekleme
minor_seriler = ["Kupa", "Kılıç", "Tılsım", "Asa"]
minör_kartlar = [
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

for seri in minor_seriler:
  for kart in minör_kartlar:
    isim_key = f"{seri} {kart}"
    tum_kartlar[isim_key] = {
        "duz": (
            f"{isim_key} düz enerjisi: Akışta huzur ve uyumlu gelişmeler.",
            "Hayatının bu alanında beklediğin dengeli ve tatlı akış seni buluyor.",
        ),
        "ters": (
            f"{isim_key} ters enerjisi: Ufak aksaklıklar veya içsel yavaşlama.",
            "Acele etmek yerine biraz dinlenmek ve akışı izlemek sana iyi gelecektir.",
        ),
    }

# Oturum yönetimi
if "adim" not in st.session_state:
  st.session_state.adim = "giriş"

# --- 1. GİRİŞ SAYFASI ---
if st.session_state.adim == "giriş":
  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    st.markdown(
        "<h1 style='text-align: center;'>✨ Mistik Tarot Deneyimi ✨</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #d4af37;'>Kaderinin"
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
        ["Bekar & Özgür", "İlişkisi Var / Kalbi Dolu", "Evli", "Karmaşık / Akışta"],
    )

    # İstediğin net ve kısa iş durumu seçenekleri
    is_durumu = st.selectbox(
        "Çalışma Durumun:", ["Çalışıyor", "Çalışmıyor", "Öğrenci"]
    )

    if st.button("Kart Seçim Ekranına Geç ✨"):
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
        # Burcu doğum tarihinden otomatik hesaplıyoruz
        st.session_state.burc = burc_hesapla(dogum_tarihi)
        st.session_state.medeni_durum = medeni_durum
        st.session_state.is_durumu = is_durumu
        st.session_state.adim = "secim"
        st.rerun()

# --- 2. KART SEÇİM SAYFASI (Dikdörtgen, Dikey Tarot Kartları) ---
elif st.session_state.adim == "secim":
  st.markdown(
      f"<h2>Hoş geldin sevgili {st.session_state.isim} ({st.session_state.burc"
      " Burcu})</h2>",
      unsafe_allow_html=True,
  )
  st.write(
      "Aşağıdaki 78 gizemli karttan sezgilerinin seni çektiği **3 adet"
      " kartı** dikey olarak seç ve derinlere inelim:"
  )

  secilenler_kutulari = []
  cols = st.columns(4)

  for idx in range(78):
    col_idx = idx % 4
    with cols[col_idx]:
      # Dikdörtgen, dikey ve estetik tarot kartı arkası görünümü
      st.markdown(
          "<div class='tarot-back'>"
          "<span style='font-size: 20px;'>✨</span>"
          f"<b style='color: #f3e5ab; font-size: 11px; margin-top: 5px;'>Kart"
          f" #{idx+1}</b>"
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
        sabit_fal.append((k, durum, tum_kartlar[k][durum]))
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
        f"<h2 style='text-align: center;'>✨ {st.session_state.isim}"
        f" ({st.session_state.burc}) İçin Tarot Rehberliği ✨</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center; color: #d4af37; font-size: 14px;'>Kalp"
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

      # Yumuşak ve kişiselleştirilmiş dokunuşlar
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
          f"<p style='color: #f3e5ab; font-size: 16px; font-weight: 600;'>{k_adi}"
          f" <span style='font-size: 13px; color: #94a3b8;'>({durum_str})"
          "</span></p>"
          f"<p><b>Özet:</b> {ozet}</p>"
          f"<p><b>Derin Yorum:</b> {derin}{ekstra_yorum}</p>"
          f"</div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if st.button("Yeni Bir Fal Bak ✨"):
      st.session_state.adim = "giriş"
      st.rerun()
