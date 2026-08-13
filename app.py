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


# Her kartın zaman akışına (Geçmiş, Şimdi, Gelecek) tam oturan detaylı veritabanı
tarot_veritabani = {
    "Deli (The Fool)": {
        "duz": {
            "gecmis": (
                "Geçmişte mantığını bir kenara bırakarak tamamen iç sesinle ve"
                " saf bir cesaretle bilinmeyene doğru ani bir adım"
                " atmışsın."
            ),
            "simdi": (
                "Şu an hayatında sıfırdan başlamak istediğin, büyük bir risk"
                " barındıran ancak sana heyecan veren bir dönemeçtesin."
            ),
            "gelecek": (
                "Gelecekte karşına ani ve yepyeni bir macera çıkacak;"
                " hazırlıksız yakalanabilirsin ancak bu değişim sana özgürlük"
                " getirecek."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişteki fevri, düşüncesiz ve aşırı riskli hareketlerin yüzünden"
                " bazı kayıplar yaşamış ve acemilikler çekmişsin."
            ),
            "simdi": (
                "Şu sıralar pervasızca adımlar atıyor, tehlikeli bir yolda"
                " uyarıları dikkate almadan ilerlemeye çalışıyorsun."
            ),
            "gelecek": (
                "Gelecekte tedbirsizliğin ve plansızlığın başına bela"
                " açabilir; ayağını taşa takıp düşmemek için temkinli"
                " olmalısın."
            ),
        },
    },
    "Büyücü (The Magician)": {
        "duz": {
            "gecmis": (
                "Geçmişte elindeki tüm imkanları, zekanı ve iletişim"
                " yeteneklerini ustaca kullanarak krizleri kendi lehine"
                " çevirmeyi başarmışsın."
            ),
            "simdi": (
                "Şu an elinde güçlü kozlar var; neyi nasıl ifade edeceğini"
                " biliyor, iradenle çevrendeki olayları yönlendiriyorsun."
            ),
            "gelecek": (
                "Gelecekte yeteneklerini konuşturacağın büyük fırsatlar"
                " ellerinde olacak, hayata geçirmek istediğin projeleri"
                " başarıyla gerçeğe dönüştüreceksin."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte potansiyelini yanlış yönlendirmiş ya da bazı"
                " manipülatif ve hileli yollara sapmışsın."
            ),
            "simdi": (
                "Şu an etrafında seni kandırmaya çalışan, sahte vaatlerle"
                " kafanı bulandıran çıkarcı kişilere karşı uyanık olman"
                " gerekiyor."
            ),
            "gelecek": (
                "Gelecekte yaşanabilecek dolandırıcılık veya kötü niyetli"
                " yönlendirmelere karşı gözünü dört açmazsan zarara"
                " uğrayabilirsin."
            ),
        },
    },
    "Mahkeme (Judgement)": {
        "duz": {
            "gecmis": (
                "Geçmişte verdiğin kararların sonuçlarıyla yüzleştiğin, geçmiş"
                " defterlerin kapandığı köklü bir hesaplaşma dönemi"
                " atlatmışsın."
            ),
            "simdi": (
                "Şu an geçmişin faturalarının önüne konulduğu, ne ektiysen onu"
                " biçtiğin ve ilahi adaletin tecelli ettiği bir süreçtesin."
            ),
            "gelecek": (
                "Gelecekte uzun süredir seni bağlayan eski bir mesele nihai"
                " bir sonuca kavuşacak ve karmik olarak tertemiz bir sayfaya"
                " adım atacaksın."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte hatalarını kabul etmekten kaçınmış, sorumluluk almayı"
                " reddederek gerçeği hep halı altına süpürmüşsün."
            ),
            "simdi": (
                "Şu an öz eleştiri yapmaktan uzak duruyor, suçu sürekli"
                " başkalarına atarak gerçeklerle yüzleşmekten kaçıyorsun."
            ),
            "gelecek": (
                "Gelecekte kaçınılmaz yüzleşmeleri daha fazla erteleyemeyecek"
                " ve yaptığın hataların gerçeğiyle sert bir şekilde"
                " karşılaşacaksın."
            ),
        },
    },
    "Kupa Altılısı": {
        "duz": {
            "gecmis": (
                "Geçmişteki tatlı anılar, eski dostluklar ve saf duygular"
                " hafızanda ve kalbinde derin izler bırakmış."
            ),
            "simdi": (
                "Şu an geçmişin nostaljik rüzgarlarının etkisi altında kalmış,"
                " eski günlerin sıcaklığını arıyorsun."
            ),
            "gelecek": (
                "Gelecekte geçmişten gelen bir kişi, eski bir hatıra veya"
                " çocuklukla ilgili bir konu yeniden karşına çıkacak ve seni"
                " duygusal bir yolculuğa çıkaracak."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte yaşanan eski travmalara, kapanmamış defterlere ve"
                " eskide kalmış olaylara aşırı takılıp kalmışsın."
            ),
            "simdi": (
                "Şu an geçmişin o nostaljik ama bir o kadar da boğucu"
                " bataklığında debeleniyor, dünü bırakamadığın için bugünü"
                " kaçırıyorsun."
            ),
            "gelecek": (
                "Gelecekte geçmişin hayaletlerinden ve eski takıntılarından"
                " kurtulamazsan, önündeki yeni ve taze mutlulukları asla"
                " göremeyeceksin."
            ),
        },
    },
    "Kılıç Üçlüsü": {
        "duz": {
            "gecmis": (
                "Geçmişte kalbini derinden yaralayan ani bir ayrılık, hayal"
                " kırıklığı veya acı bir gerçekle sınanmışsın."
            ),
            "simdi": (
                "Şu an ruhsal olarak zorlayıcı, hüzünlü ve insanı sorgulatan"
                " acı bir gerçeğin tam ortasından geçiyorsun."
            ),
            "gelecek": (
                "Gelecekte seni duygusal anlamda sarsabilecek bazı gerçekler"
                " gün yüzüne çıkacak, ancak bu acı zamanla ruhunu"
                " güçlendirecek."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte yaşadığın kalp kırıklıklarını içine atıp kinlenmiş,"
                " acıyı kabullenmek yerine bastırmayı seçmişsin."
            ),
            "simdi": (
                "Şu an içindeki acıyı ve kırgınlığı iyileştirmeye çalışıyor,"
                " yavaş yavaş toparlanma evresine giriyorsun."
            ),
            "gelecek": (
                "Gelecekte eski yaraların kabuk bağlamaya başlayacak ve uzun"
                " süredir çektiğin o zihinsel ızdıraptan nihayet"
                " kurtulacaksın."
            ),
        },
    },
    "Kader Çarkı": {
        "duz": {
            "gecmis": (
                "Geçmişte hayatının akışını tamamen değiştiren ani fırsatlar ve"
                " kaderin getirdiği dönemeçler yaşanmış."
            ),
            "simdi": (
                "Şu an hayatında büyük bir döngünün değişim aşamasındasın;"
                " rüzgarın yönü senin lehine dönmeye başlıyor."
            ),
            "gelecek": (
                "Gelecekte şans kapıları ardına kadar açılacak, işler"
                " beklemediğin kadar hızlı ve hayırlı bir şekilde lehinize"
                " ilerleyecek."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte üst üste gelen şanssızlıklar ve ters giden olaylar"
                " yüzünden sürekli aynı kısır döngüye hapsolmuşsun."
            ),
            "simdi": (
                "Şu an işlerin sarp sarıldığı, kaderin adeta sana karşı"
                " çalıştığını hissettiğin sıkıntılı bir döngüdesin."
            ),
            "gelecek": (
                "Gelecekte işlerin rast gitmesi için biraz daha sabırlı"
                " olman gerekecek; aksi halde aynı hataları tekrarlayıp"
                " zorlanabilirsin."
            ),
        },
    },
    "Güneş (The Sun)": {
        "duz": {
            "gecmis": (
                "Geçmişte hayatının en parlak, en neşeli ve her şeyin tıkırında"
                " gittiği aydınlık bir dönem yaşamışsın."
            ),
            "simdi": (
                "Şu an enerjinin yüksek olduğu, içini ısıtan, umut dolu ve"
                " sorunların çözüldüğü bir zaman dilimindesin."
            ),
            "gelecek": (
                "Gelecekte başarı, kutlama, bolluk ve mutluluk dolu günler"
                " seni bekliyor; tüm bulutlar dağılacak."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte mutluluğu yakaladığını sandığın anlarda ufak da"
                " olsa bazı gölgeler ve hayal kırıklıkları yaşamışsın."
            ),
            "simdi": (
                "Şu an neşen kursağında kalmış gibi hissedebilirsin, işler"
                " beklediğin kadar parlak ve coşkulu ilerlemiyor."
            ),
            "gelecek": (
                "Gelecekte geçici bazı bulutlanmalar ve nazar durumları"
                " olabileceği için aşırı iyimserlikten kaçınmanda fayda var."
            ),
        },
    },
    "Kule (The Tower)": {
        "duz": {
            "gecmis": (
                "Geçmişte ani bir olayla güvenli sandığın tüm kaleler başına"
                " yıkılmış, büyük ve sarsıcı bir değişim yaşamışsın."
            ),
            "simdi": (
                "Şu an hayatındaki yanlış temellerin çatırtıyla döküldüğü, her"
                " şeyin bir anda altüst olduğu kaos dolu bir süreçtesin."
            ),
            "gelecek": (
                "Gelecekte sarsıcı ama bir o kadar gerekli bir yıkım yaşanacak"
                " ki bu sayede sahte olan her şey arınacak ve yerine daha"
                " sağlamı kurulacak."
            ),
        },
        "ters": {
            "gecmis": (
                "Geçmişte büyük bir felaketin kıyısından dönmüş ya da"
                " yıkımı ertelemek için çok büyük çabalar harcamışsın."
            ),
            "simdi": (
                "Şu an yaklaşan krizleri görmezden gelmeye çalışıyor, çöküşü"
                " engellemek için pamuk ipliğine tutunuyorsun."
            ),
            "gelecek": (
                "Gelecekte kaçınılmaz olan o değişim sarsıntısı küçük çaplı"
                " da olsa kapını çalacak, artık eskisi gibi devam edemeyeceğini"
                " anlayacaksın."
            ),
        },
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
        yorum_metni = tarot_veritabani[k_adi][durum][zaman_anahtari]
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
