import random
import streamlit as st
import time

st.set_page_config(page_title="Mistik Tarot & Gizli Kader Odası", page_icon="🕯️", layout="centered")

# Mistik Gotik Tasarım
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background: linear-gradient(135deg, #050208 0%, #1a0b2e 100%);
color: #d1c4e9;
font-family: 'Georgia', serif;
}
.mystic-box {
background-color: rgba(25, 15, 40, 0.7);
border: 1px solid #4a2882;
padding: 25px;
border-radius: 15px;
margin-bottom: 20px;
box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}
h1, h2, h3 { color: #d4af37 !important; text-shadow: 2px 2px 4px #000; }
em { color: #9575cd; font-style: italic; }
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ----------------- KART KÜTÜPHANESİ (DETAYLANDIRILMIŞ) -----------------
# Her kart için: (Kısa Açıklama, Derin Analiz, Gizli Mesaj)
kartlar = {
    "Deli": ("Bilinmeyene atılan pervasız bir adım.", "Sınırların ötesine geçiyorsun. Ancak bu adım, uçurumun kenarında dans etmek gibidir. Kaosu kucaklamaya hazırsan evren seni koruyacaktır.", "Gözlerini kapat ve güven. Düşsen bile kanatlanacaksın."),
    "Büyücü": ("İradenin madde üzerindeki mutlak hakimiyeti.", "Elindeki araçlar senin zihnin ve yeteneklerin. Şu an evrenle işbirliği yapıyorsun; düşüncelerin gerçeğe dönüşmek için can atıyor.", "Odaklan. Dağınık enerji, potansiyelini öldürür."),
    "Azize": ("Perdenin ardındaki sırlar ve içsel sessizlik.", "Dış dünya gürültülü, ama senin iç sesin sessiz bir kuyu gibi derin. Sezgilerin sana yalan söylemez; mantığını bir kenara bırak ve hislerine güven.", "Sırrını kimseye söyleme, sadece hisset."),
    "İmparatoriçe": ("Doğanın bereketli ve vahşi kucaklayışı.", "Yaratıcılığın zirvesindesin. Tohumlar filizleniyor, ancak bu bereket emek ve sabır ister. Toprak ana senin arkanda.", "Kendine şefkat göster, hayatının meyvelerini toplamaya başla."),
    "İmparator": ("Disiplin, yapı ve değişmez otorite.", "Kaosun ortasında dik durman gereken bir an. Kurallarını kendin koymalısın. Zayıflığa yer yok, ama zalimliğe de gerek yok.", "Sınırlarını çiz ve onları koru."),
    "Şeytan": ("Kendi ellerinle yarattığın bağımlılıklar.", "Zincirlerini kendin taktın ve anahtarı elinde tutuyorsun. Korkuların veya tutkuların seni köleleştirmiş. Bu bir uyarıdır.", "Karanlıktan korkma, içindeki gölgeyi tanı ve serbest bırak."),
    "Kule": ("Sarsıcı bir uyanış ve ani yıkım.", "Sahte temeller üzerine kurduğun ne varsa yıkılacak. Bu acı verici görünse de, özgürleşmen için gereken tek yol bu.", "Yıkıntıların arasından yeni bir sen doğacak. Kabullen."),
    "Ay": ("İlüzyonların sisli, tekinsiz suları.", "Gördüğün hiçbir şeye tam inanma. Zihnin sana oyunlar oynuyor, korkuların gerçeği çarpıtıyor. Bulanık sular durulana kadar bekle.", "Gerçeğin yüzünü görmek için biraz daha derine dal."),
    "Güneş": ("Mutlak hakikat ve yüksek enerji.", "Karanlık dağılıyor. Başarı, neşe ve aydınlanma kapında. Kendini saklamana gerek yok, parlamanın zamanı geldi.", "Işığını başkalarının karanlığını aydınlatmak için kullan."),
    "Ölüm": ("Bir döngünün sonu, yeni bir başlangıç.", "Hayatındaki bir şeyin veya birinin artık miadı doldu. Onu uğurlamaktan korkma; boşalan yer yeni bir enerjiyle dolacak.", "Eski derini soyun, yeni kimliğine hazır ol."),
}

# --- OTURUM VE ARAYÜZ ---
if "fal_basladi" not in st.session_state: st.session_state.fal_basladi = False

if not st.session_state.fal_basladi:
    st.title("🕯️ Mistik Kader Odası")
    isim = st.text_input("Ruh Adın:")
    burc = st.selectbox("Burcun:", ["Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak", "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"])
    if st.button("Kaderini Çöz"):
        st.session_state.isim, st.session_state.burc = isim, burc
        st.session_state.fal_basladi = True
        st.rerun()
else:
    st.write(f"Hoş geldin, {st.session_state.isim}. {st.session_state.burc} burcunun gizemli enerjisi kartlara yansıyor...")
    
    secilen_kartlar = random.sample(list(kartlar.items()), 3)
    konumlar = ["GEÇMİŞ (Tohumun atıldığı yer)", "ŞİMDİ (Meydana gelen fırtına)", "GELECEK (Beklenen sonuç)"]
    
    for i in range(3):
        kart_adi, (kisa, derin, mesaj) = secilen_kartlar[i]
        st.markdown(f"<div class='mystic-box'><h3>{konumlar[i]}: {kart_adi}</h3><p><b>Özet:</b> {kisa}</p><p><b>Detaylı Analiz:</b> {derin}</p><p><em>🔮 Gizli Mesaj: {mesaj}</em></p></div>", unsafe_allow_html=True)
    
    if st.button("Kaderi Yeniden Çiz"):
        st.rerun()
