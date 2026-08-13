import random
import streamlit as st
import time

st.set_page_config(
    page_title="En Dürüst Tarot ve Burç Falı",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Şık ve modern bir arayüz için CSS stilleri
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background-color: #0e1117;
}
h1, h2, h3, .stMarkdown, p, label {
color: #FFFFFF !important;
font-family: 'Georgia', serif;
}
.stButton>button {
width: 100%;
background-color: #6c5ce7;
color: white;
border-radius: 10px;
font-size: 18px;
height: 50px;
border: none;
}
.stButton>button:hover {
background-color: #a29bfe;
color: black;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Oturum durumu kontrolü (Sayfaları ayırmak için)
if "fal_goster" not in st.session_state:
  st.session_state.fal_goster = False

# ----------------- 1. BÖLÜM: GİRİŞ EKRANI -----------------
if not st.session_state.fal_goster:
  st.title("🔮 En Dürüst Tarot ve Burç Falı")
  st.write(
      "Kartlar bol, burçlar bahane, yapay zeka seninle! Seni tanımamızla"
      " başlayalım."
  )

  with st.form("kullanici_formu"):
    isim = st.text_input("Adın ne?")
    yas = st.number_input("Yaşın kaç?", min_value=1, max_value=120, value=20)
    burc = st.selectbox(
        "Burcun ne?",
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

    submitted = st.form_submit_button("Kolektif Enerjiye Bağlan ve Falıma Bak")

    if submitted:
      if isim.strip() == "":
        st.warning("Lütfen önce adını yaz.")
      else:
        st.session_state.isim = isim
        st.session_state.yas = yas
        st.session_state.burc = burc
        st.session_state.fal_goster = True
        st.rerun()

# ----------------- 2. BÖLÜM: FAL VE SONUÇ EKRANI -----------------
else:
  # Bilgileri oturumdan alalım
  isim = st.session_state.isim
  yas = st.session_state.yas
  burc = st.session_state.burc

  # Burçlara özel dengeli analizler
  burc_yorumları = {
      "Koç": (
          "Öncü ve cesursun, ancak bazen aceleciliğin sabrını zorlayabiliyor."
      ),
      "Boğa": (
          "Sadık ve güvenilirensin, konforuna düşkünlüğün bazen değişime"
          " direnmeni sağlıyor."
      ),
      "İkizler": (
          "Zeki ve iletişimcisin, zihnindeki hızlı değişimler bazen karar"
          " vermeni güçleştiriyor."
      ),
      "Yengeç": (
          "Sezgisel ve şefkatlisin, korumacı yapın bazen seni duygusal bir"
          " kabuğa hapsediyor."
      ),
      "Aslan": (
          "Karizmatik ve yaratıcısın, takdir edilme ihtiyacın bazen enerjini"
          " dışarıya bağlıyor."
      ),
      "Başak": (
          "Detaycı ve çalışkansın, mükemmeliyetçiliğin bazen kendine yük"
          " olabiliyor."
      ),
      "Terazi": (
          "Adaletli ve uyumlusun, denge arayışın bazen kendi isteklerini"
          " ertelemenize neden oluyor."
      ),
      "Akrep": (
          "Tutkulu ve derinliklisin, gizemli yapın bazen çevrenle arana mesafe"
          " koyabiliyor."
      ),
      "Yay": (
          "Özgürlüğüne düşkün ve iyimsersin, keşfetme arzun bazen detayları"
          " gözden kaçırmana sebep oluyor."
      ),
      "Oğlak": (
          "Disiplinli ve azimlisin, hedeflerine odaklanırken bazen anı"
          " yaşamayı unutabiliyorsun."
      ),
      "Kova": (
          "Yenilikçi ve özgünsün, sıra dışı fikirlerin bazen çevren tarafından"
          " anlaşılamayabiliyor."
      ),
      "Balık": (
          "Empati yeteneği yüksek ve hayalperestsin, duygusallığın bazen"
          " gerçeklerden uzaklaşmanı sağlıyor."
      ),
  }

  # Kartlara özel olası burç eşleştirmeleri
  kart_burcları = {
      "Deli": "Kova veya Koç",
      "Büyücü": "İkizler veya Akrep",
      "Azize": "Balık veya Yengeç",
      "İmparatoriçe": "Boğa veya Terazi",
      "İmparator": "Koç veya Oğlak",
      "Hierofant": "Boğa",
      "Aşıklar": "İkizler",
      "Araba": "Koç",
      "Güç": "Aslan",
      "Ermiş": "Başak",
      "Kader Çarkı": "Yay",
      "Adalet": "Terazi",
      "Asılı Adam": "Balık",
      "Ölüm": "Akrep",
      "Denge": "Terazi",
      "Şeytan": "Oğlak veya Akrep",
      "Kule": "Koç veya Akrep",
      "Yıldız": "Kova",
      "Ay": "Balık",
      "Güneş": "Aslan",
      "Mahkeme": "Oğlak",
      "Dünya": "Boğa",
      "Kupa Ası": "Yengeç",
      "Kupa İkilisi": "Terazi",
      "Kupa Üçlüsü": "İkizler",
      "Kupa Dörtlüsü": "Yengeç",
      "Kupa Beşlisi": "Balık",
      "Kupa Altılısı": "Yengeç",
      "Kupa Yedilisi": "Balık",
      "Kupa Sekizlisi": "Yay",
      "Kupa Dokuzlusu": "Boğa",
      "Kupa Onlusu": "Yengeç",
      "Kupa Prensi": "Balık",
      "Kupa Şövalyesi": "İkizler veya Akrep",
      "Kupa Kraliçesi": "Yengeç",
      "Kupa Kralı": "Akrep",
      "Kılıç Ası": "Kova",
      "Kılıç İkilisi": "Terazi",
      "Kılıç Üçlüsü": "İkizler",
      "Kılıç Dörtlüsü": "Başak",
      "Kılıç Beşlisi": "Koç",
      "Kılıç Altılısı": "Kova",
      "Kılıç Yedilisi": "İkizler",
      "Kılıç Sekizlisi": "Başak",
      "Kılıç Dokuzlusu": "Yengeç",
      "Kılıç Onlusu": "Oğlak",
      "Kılıç Prensi": "İkizler",
      "Kılıç Şövalyesi": "Koç",
      "Kılıç Kraliçesi": "Başak",
      "Kılıç Kralı": "Oğlak",
      "Değnek Ası": "Yay",
      "Değnek İkilisi": "Koç",
      "Değnek Üçlüsü": "Yay",
      "Değnek Dörtlüsü": "Aslan",
      "Değnek Beşlisi": "Koç",
      "Değnek Altılısı": "Aslan",
      "Değnek Yedilisi": "Aslan",
      "Değnek Sekizlisi": "Yay",
      "Değnek Dokuzlusu": "Oğlak",
      "Değnek Onlusu": "Oğlak",
      "Değnek Prensi": "Yay",
      "Değnek Şövalyesi": "Yay",
      "Değnek Kraliçesi": "Aslan",
      "Değnek Kralı": "Aslan",
      "Tılsım Ası": "Boğa",
      "Tılsım İkilisi": "İkizler",
      "Tılsım Üçlüsü": "Oğlak",
      "Tılsım Dörtlüsü": "Boğa",
      "Tılsım Beşlisi": "Oğlak",
      "Tılsım Altılısı": "Boğa",
      "Tılsım Yedilisi": "Başak",
      "Tılsım Sekizlisi": "Başak",
      "Tılsım Dokuzlusu": "Boğa",
      "Tılsım Onlusu": "Oğlak",
      "Tılsım Prensi": "Başak",
      "Tılsım Şövalyesi": "Boğa",
      "Tılsım Kraliçesi": "Boğa",
      "Tılsım Kralı": "Oğlak",
  }

  destem = {
      "Deli": "Yeni bir bodoslama dalış yaptın, sonu belirsiz.",
      "Büyücü": "Elindeki imkanları abartıyorsun, ortada devasa bir şey yok.",
      "Azize": "İç sesin 'kaç' diyor ama sen diretiyorsun.",
      "İmparatoriçe": "Keyfin yerinde ama tembelliğe vurdun.",
      "İmparator": "Aşırı otorite taslıyorsun, kimse çekmek zorunda değil.",
      "Hierofant": "Sistemden dışarı çıkmaya cesaretin yok.",
      "Aşıklar": "Kritik bir seçim yaptın, muhtemelen yanlış olanı.",
      "Araba": "Hızla gidiyorsun ama frenlerin patlak.",
      "Güç": "Sabrın taştı taşacak, ortalık karışacak.",
      "Ermiş": "Kendi kendine trip atıp kabuğuna çekilmişsin.",
      "Kader Çarkı": "Yine aynı döngüye girdin, tebrikler.",
      "Adalet": "Hak ettiğin neyse o geliyor, şikayet etme.",
      "Asılı Adam": "Hiçbir yere varamıyorsun çünkü inatla kıpırdamıyorsun.",
      "Ölüm": "Eski defterler zorla kapanıyor, ağlamanın lüzumu yok.",
      "Denge": "İğne ucu üzerinde dengede durmaya çalışıyorsun.",
      "Şeytan": "Kendi ellerinle bağlandığın toksik alışkanlıklar.",
      "Kule": "Bütün planların başına yıkılacak, geçmiş olsun.",
      "Yıldız": "Ufukta hafif bir ışık var ama umut bağlamaya değmez.",
      "Ay": "Paranoya ve kuruntu sezinliyorum, hepsi kafanda.",
      "Güneş": "Her şey yolunda gibi görünecek ama nazara geleceksin.",
      "Mahkeme": "Geçmişteki hataların hesabını ödeme vakti.",
      "Dünya": "Döngüyü bitirdin ama başladığın yere geri döndün.",
      "Kupa Ası": "Duygusal bir patlama yaşayacaksın ama altı boş çıkacak.",
      "Kupa İkilisi": "Karşılıklı boş yapma seansındasın.",
      "Kupa Üçlüsü": "Gereksiz bir kutlama veya kalabalığın ortasındasın.",
      "Kupa Dörtlüsü": "Önüne sunulanı beğenmeyip burun kıvırıyorsun.",
      "Kupa Beşlisi": "Dökülen süte ağlamaya devam ediyorsun.",
      "Kupa Altılısı": "Geçmişteki nostaljik bataklığında boğuluyorsun.",
      "Kupa Yedilisi": "Hayal alemindesin, uyanınca çarpılacaksın.",
      "Kupa Sekizlisi": "Kaçıp gitmek istiyorsun ama cesaretin yok.",
      "Kupa Dokuzlusu": "Bencilce bir mutluluk peşindesin, kimsenin umrunda değil.",
      "Kupa Onlusu": "Reklamlardaki gibi sahte bir aile tablosundasın.",
      "Kupa Prensi": "Aşırı sulugöz ve alıngan bir döneme giriyorsun.",
      "Kupa Şövalyesi": "Sana yalan söyleyen biriyle sınanacaksın.",
      "Kupa Kraliçesi": "Sürekli dert dinlemekten içini kurutacak biriyle uğraşacaksın.",
      "Kupa Kralı": "Duygularını bastıran ama içten içe bitik birine dönüşüyorsun.",
      "Kılıç Ası": "Keskin bir fikir buldun ama başa bela olacak.",
      "Kılıç İkilisi": "Gözünü kapatmışsın, gerçekleri görmek istemiyorsun.",
      "Kılıç Üçlüsü": "Net bir kalp kırıklığı ve acı gerçeklerle yüzleşiyorsun.",
      "Kılıç Dörtlüsü": "Tükenmişlik sendromundasın, kafayı yemek üzeresin.",
      "Kılıç Beşlisi": "Kazandığını sandığın ama herkesi kaybettiğin bir kavgadasın.",
      "Kılıç Altılısı": "Zoraki bir kaçış içindesin, arkana bakmadan gidiyorsun.",
      "Kılıç Yedilisi": "Üç kağıtçılık ve sinsilik peşindesin.",
      "Kılıç Sekizlisi": "Kendi ördüğün ağlara kendin takılmışsın.",
      "Kılıç Dokuzlusu": "Gece yarısı 'acaba' diye düşünmekten uykuların kaçmış.",
      "Kılıç Onlusu": "Sırtından bıçaklandın, oyun bitti.",
      "Kılıç Prensi": "Her şeye laf sokan biriyle başın belaya girecek.",
      "Kılıç Şövalyesi": "Paldır küldür kavgaya dalan aceleci birine dönüşeceksin.",
      "Kılıç Kraliçesi": "Kimseye acımayan, buz gibi bir mantıkla hareket edeceksin.",
      "Kılıç Kralı": "Fazla mantıktan ruhunu kaybetmiş birine dönüşeceksin.",
      "Değnek Ası": "Büyük bir hevesle başlayıp yarım bırakacağın bir iş seni bekliyor.",
      "Değnek İkilisi": "Yolun başındasın ama nereye gideceğini bilmiyorsun.",
      "Değnek Üçlüsü": "Bekliyorsun ama gelecek olan kargo bile gecikecek.",
      "Değnek Dörtlüsü": "Geçici bir huzurdesin, hemen bozulacak.",
      "Değnek Beşlisi": (
          "Ortada hiçbir şey yokken çıkan saçma bir tartışmanın içindesin."
      ),
      "Değnek Altılısı": (
          "Erken gelen bir zafer sarhoşluğundasın, duvara toslayacaksın."
      ),
      "Değnek Yedilisi": (
          "Tek başına herkese karşı piyon gibi savunma yapıyorsun."
      ),
      "Değnek Sekizlisi": "Her şey üst üste geliyor, hızına yetişemiyorsun.",
      "Değnek Dokuzlusu": (
          "Yaralı berelisin ama hala 'bana bir şey olmaz' diyorsun."
      ),
      "Değnek Onlusu": (
          "Kaldıramayacağın yükün altına kendi isteğinle girmişsin."
      ),
      "Değnek Prensi": "Yerinde duramayan ama boş gezen bir enerjin var.",
      "Değnek Şövalyesi": "Gaza gelip her şeyi yüzüne gözüne bulaştıracaksın.",
      "Değnek Kraliçesi": (
          "Ben bilirimci, ortalığı ayağa kaldıran bir karaktere bürüneceksin."
      ),
      "Değnek Kralı": "Liderlik taslayan ama içeride batmış bir vizyondasın.",
      "Tılsım Ası": "Küçük bir para girişi olacak, hemen harcayacaksın.",
      "Tılsım İkilisi": "İki parasal iş arasında bocalayıp duruyorsun.",
      "Tılsım Üçlüsü": "Ortak iş yapıyorsun ama herkes birbirini kazıklıyor.",
      "Tılsım Dörtlüsü": "Cimriliğin bu kadarı fazla, mezara mı götüreceksin?",
      "Tılsım Beşlisi": "Kuruşsuz ve desteksiz kaldığın soğuk bir dönemdesin.",
      "Tılsım Altılısı": "Sadaka veya borç alıp verme dengesindesin.",
      "Tılsım Yedilisi": "Ektiğin biçtiğin yok, öylece tarlaya bakıyorsun.",
      "Tılsım Sekizlisi": "Sabahlara kadar amele gibi çalışıyorsun.",
      "Tılsım Dokuzlusu": "Tek başına keyif yapıyorsun ama yalnızsın.",
      "Tılsım Onlusu": "Aile parası veya miras konulu gerginlikler yaşayacaksın.",
      "Tılsım Prensi": "Parayı bulacağını sanıp 5 kuruş harcayan birine dönüşeceksin.",
      "Tılsım Şövalyesi": "Ağır vites ama güvenilir bir ilerleyiştesin.",
      "Tılsım Kraliçesi": "Konforuna düşkün, lüks sevdalısı bir hayat yaşayacaksın.",
      "Tılsım Kralı": "Para bende patron benim diyen bir ego patlaması yaşayacaksın.",
  }

  with st.spinner(f"{isim}, evrenin derinliklerinden kartlar seçiliyor..."):
    time.sleep(1.5)

  secilenler = random.sample(list(destem.items()), 3)

  # Gelecek kartı ve +1 bonus mantığı
  gelecek_kart_adi = secilenler[2][0]
  gelecek_metin = secilenler[2][1]
  ilgili_burc = kart_burcları.get(gelecek_kart_adi, "Gizemli bir")

  if (
      "biri" in gelecek_metin
      or "tip" in gelecek_metin
      or "karakter" in gelecek_metin
  ):
    kalanlar = [k for k in destem.items() if k[0] != gelecek_kart_adi]
    ek_kart = random.choice(kalanlar)
    gelecek_aciklama = f"{gelecek_metin} *(Olası Burcu: {ilgili_burc} biri)* | Bonus Olay: {ek_kart[0]} -> {ek_kart[1]}"
  else:
    gelecek_aciklama = f"{gelecek_metin} *(Olası Burç Enerjisi: {ilgili_burc})*"

  # Yapay Zeka Tarzı Bütünleşik Sentez Algoritmasi
  gecmis_k, gecmis_v = secilenler[0]
  simdi_k, simdi_v = secilenler[1]
  gelecek_k = secilenler[2][0]

  yapay_zeka_sentezi = (
      f"Genel enerji akışını analiz ettiğimde {isim}; geçmişte"
      f" **{gecmis_k}** kartının getirdiği etkilerle {gecmis_v.lower()}"
      f" yaşayarak bazı sınavlardan geçmis görünüyorsun. Şu an ise"
      f" **{simdi_k}** enerjisiyle {simdi_v.lower()} bu durumu toparlamaya ve"
      f" dengeyi bulmaya çalışıyorsun. Ancak dikkat etmelisin; önümüzdeki"
      f" süreçte **{gelecek_k}** kartının işaret ettiği gibi, temkinli olmazsan"
      f" benzer döngülerle tekrar sarsılabilirsin. {burc} burcunun"
      f" özellikleriyle ({burc_yorumları[burc]}) bu süreci lehine çevirmek"
      f" tamamen senin elinde."
  )

  # Şık Sonuç Ekranı Tasarımı
  st.balloons()
  st.markdown(
      f"<h2 style='text-align: center; color: #a29bfe;'>✨ {isim}"
      f" ({yas}, {burc}) İçin Yapay Zeka Fal Odası ✨</h2>",
      unsafe_allow_html=True,
  )

  st.markdown("---")

  st.markdown(f"🌟 **Kişilik & Burç Analizin:** {burc_yorumları[burc]}")

  st.markdown("### 🤖 Yapay Zeka Bütünleşik Fal Sentezi:")
  st.success(yapay_zeka_sentezi)

  st.markdown("### 🎴 Seçilen Kartların Detayları:")
  st.info(
      f"**GEÇMİŞ ({gecmis_k}):** {gecmis_v} *(Olası Burç:"
      f" {kart_burcları.get(gecmis_k, 'Değişken')})*"
  )
  st.warning(
      f"**ŞİMDİ ({simdi_k}):** {simdi_v} *(Olası Burç:"
      f" {kart_burcları.get(simdi_k, 'Değişken')})*"
  )
  st.error(f"**GELECEK ({gelecek_k}):** {gelecek_aciklama}")

  st.markdown("---")

  # Geri dönüp tekrar fal bakma butonu
  if st.button("🔄 Yeni Bir Fal Bak"):
    st.session_state.fal_goster = False
    st.rerun()
