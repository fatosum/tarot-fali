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
# Tarot 78 Kart Detaylı Zaman Anlam Sözlüğü
tarot_veritabani = {
    1: {
        "isim": "DELİ (THE FOOL)",
        "duz_gecmis": "Geçmişte yeni başlangıçlara, masumiyete ve bilinmeyene doğru özgürce ve korkusuzca attığın saf adımlar seni bu noktaya getirdi.",
        "duz_simdi": "Şu an hayatında sıfırdan bir yola çıkma, iç sesine uyarak büyük bir risk alma ve spontan yaşama enerjisindesin.",
        "duz_gelecek": "Gelecekte karşına yepyeni bir macera ve saf inançla atılacağın tertemiz bir sayfa açılacak.",
        "ters_gecmis": "Geçmişteki pervasız, düşüncesiz ve riskleri hesapsızca alan hareketlerin başına bazı talihsizlikler açmış.",
        "ters_simdi": "Şu sıralar ayağını taşa takıp düşmek üzeresin; körü körüne aldığın riskler seni tehlikeli bir yola sokuyor.",
        "ters_gelecek": "Gelecekte aşırı aceleciliğin ve tedbirsizliğin yüzünden aptalca hatalar yapma riskin var, dikkatli olmalısın."
    },
    2: {
        "isim": "BÜYÜCÜ (THE MAGICIAN)",
        "duz_gecmis": "Geçmişte elindeki tüm imkanları, iradeyi ve becerileri ustalıkla kullanarak çevreni ve şartları kendi lehine dönüştürmüşsün.",
        "duz_simdi": "Şu an elinde çok güçlü kozlar var; yaratıcılığın ve zekanla her türlü zorluğun üstesinden gelebilecek güçtesin.",
        "duz_gelecek": "Gelecekte becerilerin sayesinde niyet ettiğin tüm projeleri gerçeğe dönüştürecek ve hedeflerini tezahür ettireceksin.",
        "ters_gecmis": "Geçmişte yeteneklerini yanlış yönlendirmiş, hileli yollara sapmış ya da manipülasyonlarla kısa vadeli çıkarlar aramışsın.",
        "ters_simdi": "Şu an çevrende seni sahte vaatlerle kandırmaya çalışan, parmağında oynatmak isteyen manipülatif enerjiler ve insanlar var.",
        "ters_gelecek": "Gelecekte kötü niyetli kişilerin kurabileceği tuzaklara ve potansiyelini harcama tehlikesine karşı uyanık olmalısın."
    },
    3: {
        "isim": "AZİZE (THE HIGH PRIESTESS)",
        "duz_gecmis": "Geçmişte iç sesine kulak verdiğin, sırları sezdiğin ve dış dünyadan uzaklaşıp tamamen kendi iç bilgeligine sığındığın bir dönem geçirdin.",
        "duz_simdi": "Şu an mantığından ziyade içgüdülerinin ve sezgilerinin rehberliğine ihtiyacın var; olayların arkasındaki gizli gerçekler saklı duruyor.",
        "duz_gelecek": "Gelecekte bugüne kadar saklı kalmış bazı sırlar ve hakikatler önüne serilecek, sezgilerin seni asla yanıltmayacak.",
        "ters_gecmis": "Geçmişte sezgilerini görmezden gelip tamamen dış etkenlerle hareket ettiğin için yanılgılara ve güvensizliklere sürüklenmişsin.",
        "ters_simdi": "Şu sıralar iç sesine kulak tıkayıp yüzeysel kararlar alıyor, etrafındaki dedikodulardan ve asılsız kuruntulardan etkileniyorsun.",
        "ters_gelecek": "Gelecekte sezgisel kopukluklar ve sinsi planlar yüzünden yanlış anlamalar ve güven sarsılmaları yaşayabilirsin."
    },
    4: {
        "isim": "İMPARATORİÇE (THE EMPRESS)",
        "duz_gecmis": "Geçmişte bolluk, bereket, anaç şefkat ve doğanın iyileştirici enerjisiyle beslenerek ruhsal ve maddesel olarak büyümüşsün.",
        "duz_simdi": "Şu an hayatında üretkenliğin, yaratıcılığın ve huzurlu bir yuva ortamının tadını çıkardığın bereketli bir dönemdesin.",
        "duz_gelecek": "Gelecekte emeklerinin karşılığını fazlasıyla alacağın, maddi ve manevi bolluk dolu, huzurlu günler seni bekliyor.",
        "ters_gecmis": "Geçmişte kıtlık bilinci, yaratıcı tıkanıklıklar veya aşırı boğucu, baskıcı ilişkiler yüzünden enerjin tüketilmiş.",
        "ters_simdi": "Şu an kendine ve etrafındakilere yeterince özen göstermiyor, tembellik veya aşırı sahiplenici tavırlar yüzünden tıkanmalar yaşıyorsun.",
        "ters_gelecek": "Gelecekte verimsizlik, maddi/manevi kıtlık hissi ve bakımsızlıktan kaynaklanan sorunlarla yüzleşmen gerekebilir."
    },
    5: {
        "isim": "İMPARATOR (THE EMPEROR)",
        "duz_gecmis": "Geçmişte hayatına sağlam bir düzen kurmuş, disiplinli ve koruyucu bir otorite figürü olarak kararlar almışsın.",
        "duz_simdi": "Şu an otoriteni kurma, kuralları belirleme ve hayatını tamamen mantıksal bir disiplin altına alma zorunluluğundasın.",
        "duz_gelecek": "Gelecekte işlerini tamamen rayına oturtacağın, güçlü pozisyonlar elde edeceğin ve sağlam temeller kuracağın bir dönem geliyor.",
        "ters_gecmis": "Geçmişte aşırı baskıcı, zorba veya kontrolcüm tutumların çevrendeki insanlarla çatışmalara yol açmış.",
        "ters_simdi": "Şu an ya hayatındaki otorite figürlerinin baskısıyla eziliyor ya da kendi diktatörce tavırlarınla çevreni boğuyorsun.",
        "ters_gelecek": "Gelecekte kuralların yıkılması, disiplinsizlik ve gücü kötüye kullanmaktan doğan büyük krizlerle karşılaşabilirsin."
    },
    6: {
        "isim": "HİEROFANT (THE HIEROPHANT)",
        "duz_gecmis": "Geçmişte geleneksel değerlere bağlı kalmış, ruhsal rehberlerden feyz almış ve toplumsal kurallara uyum sağlamışsın.",
        "duz_simdi": "Şu an doğru bildiğin inanç sistemleri, evlilik/ortaklık kuralları veya toplumsal kalıplar içinde hareket etme durumundasın.",
        "duz_gelecek": "Gelecekte resmi anlaşmalar, evlilikler veya kurumsal ve ruhsal rehberlik alacağın güvenli bağlar karşına çıkacak.",
        "ters_gecmis": "Geçmişte toplumsal dogmalara körü körüne uymuş ya da tam tersi geleneklere başkaldırarak hatalar yapmışsın.",
        "ters_simdi": "Şu an ikiyüzlü durumlardan, etrafındaki sahte akıl hocalarından ve yanıltıcı inançlardan uzak durmalısın.",
        "ters_gelecek": "Gelecekte dogmaların yıkılması, yanlış yönlendirmeler ve inanç çatışmaları nedeniyle zorlanabilirsin."
    },
    7: {
        "isim": "AŞIKLAR (THE LOVERS)",
        "duz_gecmis": "Geçmişte hayatını kökten etkileyen derin bir aşk yaşamış ya da değerlerinle ilgili çok kritik bir seçim yapmışsın.",
        "duz_simdi": "Şu an kalbinle mantığın arasında kaldığın önemli bir karar eşiğindesin; ruh eşi enerjisi veya uyumlu ortaklıklar gündemde.",
        "duz_gelecek": "Gelecekte hayatının akışını güzelleştirecek kalıcı bir ilişki, ortaklık veya doğru bir değer seçimi seni bekliyor.",
        "ters_gecmis": "Geçmişte yapılan yanlış tercihler, değer çatışmaları ve uyumsuz ilişkiler büyük hayal kırıklıkları yaratmış.",
        "ters_simdi": "Şu an ilişkilerde güvensizlik, yanlış kararlar alma korkusu ve taraflar arasında ciddi bir uyumsuzluk hüküm sürüyor.",
        "ters_gelecek": "Gelecekte yaşanabilecek değer çatışmaları ve yanlış ortaklık kararları ayrılıkları beraberinde getirebilir."
    },
    8: {
        "isim": "SAVAŞ ARABASI (THE CHARIOT)",
        "duz_gecmis": "Geçmişte irade gücünü sonuna kadar kullanarak tüm engelleri devirmiş ve hedefine zaferle ulaşmışsın.",
        "duz_simdi": "Şu an dizginleri eline alma, kararlılıkla hedefine odaklanma ve karşına çıkan engelleri hızla aşma vaktindesin.",
        "duz_gelecek": "Gelecekte zafer, seyahatler ve kariyerinde atacağın hızlı ve başarılı adımlarla zirveye çıkacaksın.",
        "ters_gecmis": "Geçmişte kontrolü kaybetmiş, agresif tutumlar yüzünden projelerini ve yolunu yüzüstü bırakmışsın.",
        "ters_simdi": "Şu an hayatın kontrolü elinden kaçıyor; yanlış yöne ilerliyor ve engeller karşısında eziliyorsun.",
        "ters_gelecek": "Gelecekte irade zayıflığı, savrulmalar ve yanlış hedef seçimi nedeniyle büyük bir duraklama yaşayabilirsin."
    },
    9: {
        "isim": "GÜÇ (STRENGTH)",
        "duz_gecmis": "Geçmişte içsel gücünü, sabrını ve merhametini kullanarak en vahşi zorlukları bile zarafetle dize getirmişsin.",
        "duz_simdi": "Şu an dürtülerini kontrol altında tutma, sakinliğini koruma ve içindeki o devasa cesareti ortaya koyma zamanı.",
        "duz_gelecek": "Gelecekte sabrının ve metanetinin ödülünü alacak, tüm korkularını cesaretle alt edeceksin.",
        "ters_gecmis": "Geçmişte özgüven eksikliği yaşamış, içsel zayıflıkların yüzünden dürtülerine yenik düşmüşsün.",
        "ters_simdi": "Şu sıralar sabırsızlık, öfke patlamaları ve özgüven zedelenmesiyle baş etmeye çalışıyorsun.",
        "ters_gelecek": "Gelecekte içsel kontrolü kaybetmekten ötürü fevri reaksiyonlar verebilir, zorluklar karşısında çabuk pes edebilirsin."
    },
    10: {
        "isim": "ERMİŞ (THE HERMIT)",
        "duz_gecmis": "Geçmişte kalabalıklardan uzaklaşıp iç gözlem yapmış, kendi iç sesini dinleyerek derin bir bilgelik kazanmışsın.",
        "duz_simdi": "Şu an biraz yalnız kalmaya, dünyaişlerinden el etek çekip ruhsal bir aydınlanma ve arayış yaşamaya ihtiyacın var.",
        "duz_gelecek": "Gelecekte hayatına ışık tutacak doğru yolu kendi iç dünyanda bulacak ve krizleri akılla çözeceksin.",
        "ters_gecmis": "Geçmişte aşırı yalnızlaşma ve toplumdan tamamen kopma hali seni depresif bir döngüye sokmuş.",
        "ters_simdi": "Şu an insanlardan kaçıyor, yalnızlığı yanlış yorumlayarak içsel bir karanlığa gömülüyorsun.",
        "ters_gelecek": "Gelecekte kibirli bir bilgelik taslama ya da tamamen dış dünyadan soyutlanıp yalnız kalma riski var."
    },
    11: {
        "isim": "KADER ÇARKI (WHEEL OF FORTUNE)",
        "duz_gecmis": "Geçmişte hayatının akışını tamamen değiştiren ani, ilahi ve şans dolu döngülerden geçip kazançlı çıkmışsın.",
        "duz_simdi": "Şu an kaderin rüzgarı senin lehine esiyor; ani fırsatlara ve hayatındaki dönüm noktalarına açık olmalısın.",
        "duz_gelecek": "Gelecekte şans kapıları ardına kadar açılacak, ilahi adalet yerini bulacak ve çark senin için dönecek.",
        "ters_gecmis": "Geçmişte şanssızlık döngülerine kapılmış, ardı arkasına gelen olumsuzluklar karşısında çaresiz kalmışsın.",
        "ters_simdi": "Şu an rüzgar tersine esiyor gibi hissedebilirsin; değişime direnç göstermek işleri daha da sarpa sardırıyor.",
        "ters_gelecek": "Gelecekte kontrol dışı aksilikler ve kötüye giden şans döngüleriyle sınanabilirsin, esnek olmalısın."
    },
    12: {
        "isim": "ADALET (JUSTICE)",
        "duz_gecmis": "Geçmişte hakkaniyetli kararlar almış, karma yasasıyla yüzleşmiş ve hukuki/resmi işlerini dengeye oturtmuşsun.",
        "duz_simdi": "Şu an dürüstlükten şaşmama, tarafsız olma ve hayatındaki teraziyi tam merkeze koyma zamanındasın.",
        "duz_gelecek": "Gelecekte devam eden mahkeme veya resmi süreçler lehine sonuçlanacak, hak ettiğin değeri bulacaksın.",
        "ters_gecmis": "Geçmişte yapılan adaletsizlikler, sorumluluktan kaçma çabaları ve önyargılı tutumlar karmik sorunlar yaratmış.",
        "ters_simdi": "Şu an hayatında haksızlığa uğradığını hissedebilir ya da kendi hatalarının sorumluluğunu almaktan kaçınıyor olabilirsin.",
        "ters_gelecek": "Gelecekte adaletsiz durumlar, dürüstlükten uzaklaşma nedeniyle yaşanacak cezalandırıcı karma süreçleri kapıda."
    },
    13: {
        "isim": "ASILI ADAM (THE HANGED MAN)",
        "duz_gecmis": "Geçmişte işlerin askıya alındığı zorunlu bir bekleme dönemi yaşamış, bu sayede bakış açını kökten değiştirmişsin.",
        "duz_simdi": "Şu an ellerin kolların bağlı gibi hissedebilirsin; ancak bu durum olaylara teslim olup farklı bir açıdan bakabilmen için bir fırsattır.",
        "duz_gelecek": "Gelecekte bugüne kadar inatla göremediğin gerçekleri fark edecek ve kilitli kapıların fedakarlıkla açıldığını göreceksin.",
        "ters_gecmis": "Geçmişte boşuna kürek çekmiş, gereksiz fedakarlıklar yaparak kendini kurban psikolojisine kaptırmışsın.",
        "ters_simdi": "Şu an inat uğruna zamana karşı direniyor, hiçbir yere varmayan bir bekleyişin içinde tüketiliyorsun.",
        "ters_gelecek": "Gelecekte kurban psikolojisi ve gereksiz fedakarlıklar yüzünden zaman kaybettiğini fark edip hüsrana uğrayabilirsin."
    },
    14: {
        "isim": "ÖLÜM (DEATH)",
        "duz_gecmis": "Geçmişte hayatında misyonunu tamamlamış köhne bir dönemi arkanda bırakarak tamamen kabuk değiştirmişsin.",
        "duz_simdi": "Şu an hayatında kaçınılmaz bir bitiş ve yepyeni bir başlangıcın eşiğindesin; eski olanı korkusuzca serbest bırakmalısın.",
        "duz_gelecek": "Gelecekte köklü bir dönüşüm yaşayacak, hayatında küllerinden yeniden doğacağın taze bir sayfa açacaksın.",
        "ters_gecmis": "Geçmişte bitmesi gereken ilişkilere veya durumlara hastalıklı bir şekilde tutunarak değişime direnç göstermişsin.",
        "ters_simdi": "Şu an korkuların yüzünden hayatındaki kaçınılmaz sonları kabullenmekten kaçınıyor, zorla süreci uzatmaya çalışıyorsun.",
        "ters_gelecek": "Gelecekte değişime direnmenin getirdiği acı ve geçmişe takılı kalma hali ilerlemeni tamamen engelleyebilir."
    },
    15: {
        "isim": "DENGE (TEMPERANCE)",
        "duz_gecmis": "Geçmişte zıtlıkları uyumla harmanlamış, sabırla hareket ederek ruhsal ve bedensel bir şifa süreci atlatmışsın.",
        "duz_simdi": "Şu an hayatında orta yolu bulma, ılımlı olma, acele etmeden her şeyi dengede tutma zamanındasın.",
        "duz_gelecek": "Gelecekte içsel huzuru yakalayacağın, taşların yerine oturduğu ve şifa bulacağın sakin bir dönem seni bekliyor.",
        "ters_gecmis": "Geçmişteki aşırılıklar, sabırsızlıklar ve dengesiz davranışlar hayatının akışını alt üst etmiş.",
        "ters_simdi": "Şu an her şey aşırı uçlarda yaşanıyor; ne dengen kalmış ne de sabrın, içsel bir kaosla boğuşuyorsun.",
        "ters_gelecek": "Gelecekte uyumsuzluklar, aşırılıklar ve sabırsızlık yüzünden hayatının kontrolden çıktığını görebilirsin."
    },
    16: {
        "isim": "ŞEYTAN (THE DEVIL)",
        "duz_gecmis": "Geçmişte toksik bağların, materyalist arzuların veya kötü alışkanlıkların esiri olub kısıtlanmışlık hissetmişsin.",
        "duz_simdi": "Şu an seni aşağı çeken toksik ilişkilere, bağımlılıklara ve prangalarına karşı uyanık olman gerekiyor.",
        "duz_gelecek": "Gelecekte hırsın kurbanı olmamak ve yanlış arzulara kapılmamak için güçlü bir irade göstermen şart.",
        "ters_gecmis": "Geçmişte hayatını zindan eden o kalın zincirleri kırıp atmayı ve toksik bağlardan kurtulmayı başarmışsın.",
        "ters_simdi": "Şu an farkındalık kazanıyor, seni kısıtlayan tüm kalıplardan ve zararlı alışkanlıklardan özgürleşiyorsun.",
        "ters_gelecek": "Gelecekte tam bir özgürlük hissiyle eski karanlık bağlarını tamamen geride bırakacak ve rahata ereceksin."
    },
    17: {
        "isim": "KULE (THE TOWER)",
        "duz_gecmis": "Geçmişte ani bir şokla sahte temeller üzerine kurulu hayatın ve düzenin tamamen yıkılıp yerle bir olmuş.",
        "duz_simdi": "Şu an hayatında sarsıcı gerçeklerin ortaya döküldüğü ve taşların yerinden oynadığı uyanış sürecindesin.",
        "duz_gelecek": "Gelecekte seni şoke edecek ani değişimler kapıda; ancak bu yıkım daha sağlam bir temel kurman için şart.",
        "ters_gecmis": "Geçmişte büyük bir felaketten veya yıkımdan kıl payı kurtulmuş ya da yaklaşan krizi görmezden gelmişsin.",
        "ters_simdi": "Şu an kaçınılmaz bir yıkımı ertelemeye çalışıyor, çürümüş yapıyı ayakta tutmak için boşuna çabalıyorsun.",
        "ters_gelecek": "Gelecekte bastırdığın krizler daha büyük bir patlamayla önüne gelebilir, artık kaçışın olmayacak."
    },
    18: {
        "isim": "YILDIZ (THE STAR)",
        "duz_gecmis": "Geçmişte fırtınalı günlerin ardından derin bir şifa bulmuş, umudunu ve geleceğe inancını yeniden tazelemişsin.",
        "duz_simdi": "Şu an içini huzur dolduran, ilham veren ve hayallerine göz kırpan saf bir umut dönemindesin.",
        "duz_gelecek": "Gelecekte şansın döneceği, dileklerinin gerçeğe dönüşeceği ve ruhsal dinginliğe ereceğin parlak bir gelecek seni bekliyor.",
        "ters_gecmis": "Geçmişte umutsuzluk, hayal kırıklığı ve inanç kaybı yüzünden karanlığa gömülmüşsün.",
        "ters_simdi": "Şu an özgüvenin zedelenmiş durumda, geleceğe dair inancını kaybetmiş ve karamsarlık içinde kıvranıyorsun.",
        "ters_gelecek": "Gelecekte optimizmin azalması ve yanlış hayaller peşinde koşturulması nedeniyle hayal kırıklığı yaşama riskin var."
    },
    19: {
        "isim": "AY (THE MOON)",
        "duz_gecmis": "Geçmişte illüzyonlar, saklı düşmanlıklar, belirsizlikler ve yoğun korkularla dolu sisli bir yoldan geçmişsin.",
        "duz_simdi": "Şu an ortalık sisli; gerçekler ile yalanlar birbirine karışmış durumda, içindeki korkularınla yüzleşiyorsun.",
        "duz_gelecek": "Gelecekte gizli saklı kalmış bazı konular açığa çıkacak; yanıldığın noktaları fark edip aydınlanacaksın.",
        "ters_gecmis": "Geçmişte içsel korkularını yenmeyi başarmış, sis perdesini aralayarak gerçeği gün yüzüne çıkarmışsın.",
        "ters_simdi": "Şu an kuruntularından sıyrılıyor, bilinmezliklerin dağıldığı ve netleşmeye başladığın bir merhaledesin.",
        "ters_gelecek": "Gelecekte karanlıkta kalan endişelerin son bulacak, hakikat en saf haliyle önüne serecektir."
    },
    20: {
        "isim": "GÜNEŞ (THE SUN)",
        "duz_gecmis": "Geçmişte hayatının en parlak, neşeli, başarılı ve aydınlık dönemlerinden birini gururla yaşamışsın.",
        "duz_simdi": "Şu an enerjinin zirvesindesin; her şey yolunda gidiyor, yüzünü güldürecek sıcak gelişmelerle dolusun.",
        "duz_gelecek": "Gelecekte saf mutluluk, büyük başarılar, canlılık ve karanlıkların tamamen bittiği güneşli günler seni bekliyor.",
        "ters_gecmis": "Geçmişte başarıya çok yaklaşmışken yaşanan geçici bulutlanmalar veya gölgelenmeler neşeni kaçırmış.",
        "ters_simdi": "Şu an içindeki neşe biraz sönük; her şey yolunda görünse de içinde tatmin etmeyen ufak bulutlar var.",
        "ters_gelecek": "Gelecekte beklenen mutluluğun biraz gecikmesi veya başarıya giden yolda ufak aksiliklerin çıkması muhtemeldir."
    },
    21: {
        "isim": "MAHKEME (JUDGEMENT)",
        "duz_gecmis": "Geçmişte verdiğin kararların sonuçlarıyla yüzleştiğin, köklü bir ilahi hesaplaşma ve uyanış dönemi geçirmişsin.",
        "duz_simdi": "Şu an geçmişin faturaları önünе konuluyor; ne ektiysen onu biçtiğin, hayatına çeki düzen verme vaktindesin.",
        "duz_gelecek": "Gelecekte eski meseleler nihai bir karara bağlanacak ve tertemiz, suçsuz bir sayfayla yola devam edeceksin.",
        "ters_gecmis": "Geçmişteki hatalarını kabul etmekten kaçınmış, sorumluluk almaktan sürekli kaçarak kaçak oynamışsın.",
        "ters_simdi": "Şu an öz eleştiri yapmaktan uzak duruyor, suçluluk psikolojisiyle ya da kararsızlıkla kıvranıyorsun.",
        "ters_gelecek": "Gelecekte yüzleşmeleri ertelemenin bedelini ağır ödeyebilir, pişmanlıklardan ders çıkaramayabilirsin."
    },
    22: {
        "isim": "DÜNYA (THE WORLD)",
        "duz_gecmis": "Geçmişte büyük bir döngüyü başarıyla tamamlamış, tüm emeklerini taçlandırarak bütünlüğe ulaşmışsın.",
        "duz_simdi": "Şu an bir devrin kapandığı, mutlu sonların ve büyük bir tatminin yaşandığı harika bir doruk noktasındasın.",
        "duz_gelecek": "Gelecekte hedeflerine tamamen ulaşacak, kutlamalar yapacak ve hayatında yepyeni, büyük bir dönemin kapısını aralayacaksın.",
        "ters_gecmis": "Geçmişte hedefe çok yaklaşıp son anda yarım kalan işler ve kapanmayan kapılar yüzünden tatminsizlik yaşamışsın.",
        "ters_simdi": "Şu an projelerini sonlandırmakta zorlanıyor, eksiklik hissiyatıyla tatmine ulaşamıyorsun.",
        "ters_gelecek": "Gelecekte son adımı atamamak ve döngüyü tamamlayamamak nedeniyle ufak hayal kırıklıkları yaşayabilirsin."
    },
    23: {
        "isim": "KUPA ASI (ACE OF CUPS)",
        "duz_gecmis": "Geçmişte duygusal anlamda kalbini açtığın, taşmalar yaratan yepyeni bir ilişki veya sevgi döngüsü başlatmışsın.",
        "duz_simdi": "Şu an kalbin sevgiyle dolu; yeni bir aşka ya da derin duygusal tatminlere kucak açtığın bir dönemdesin.",
        "duz_gelecek": "Gelecekte duygusal hayatını şifalandıracak, kalbini ısıtacak çok taze ve mutlu bir ilişki fırsatı karşına çıkacak.",
        "ters_gecmis": "Geçmişte duygusal tıkanıklıklar, kırık kalpler veya sevgisizlik hissi seni oldukça yıpratmış.",
        "ters_simdi": "Şu an duygularını bastırıyor, sevgini göstermekte zorlanıyor ve içsel bir kuruluk ya da alınganlık yaşıyorsun.",
        "ters_gelecek": "Gelecekte yaşanabilecek duygusal hayal kırıklıklarına ve kalp kırıcı yanlış anlamalara karşı dikkatli olmalısın."
    },
    24: {
        "isim": "KUPA İKİLİSİ (TWO OF CUPS)",
        "duz_gecmis": "Geçmişte ruh eşi enerjisinde, karşılıklı çekim ve uyum barındıran çok özel bir ortaklık veya bağ kurmuşsun.",
        "duz_simdi": "Şu an hayatında karşılıklı sevgi, saygı ve uyumun hakim olduğu harika bir ikili ilişki veya bağ yaşıyorsun.",
        "duz_gelecek": "Gelecekte kalıcı bir birlikteliğe dönüşebilecek güçlü bir ortaklık ya da yeni bir aşk bağı kapını çalacak.",
        "ters_gecmis": "Geçmişteki ilişkilerde yaşanan iletişim kopuklukları ve uyuşmazlıklar ortak bağları zedelemiş.",
        "ters_simdi": "Şu an karşındaki kişiyle frekanslarınız tutmuyor; yanlış anlamalar ve denge sarsılması gündemde.",
        "ters_gelecek": "Gelecekte aradaki bağların kopma noktasına gelebileceği dengesizlikler ve ortaklık krizleri yaşanabilir."
    },
    25: {
        "isim": "KUPA ÜÇLÜSÜ (THREE OF CUPS)",
        "duz_gecmis": "Geçmişte dostlarınla bir araya geldiğin, başarıları neşeyle kutladığın ve sosyal bağları güçlendirdiğin anlar olmuş.",
        "duz_simdi": "Şu an etrafında seni seven insanlarla kutlamalar yapıyor, neşeli buluşmalarla enerjini yükseltiyorsun.",
        "duz_gelecek": "Gelecekte mutluluğunu paylaşacağın harika sosyal etkinlikler, düğünler veya kutlama ortamları seni bekliyor.",
        "ters_gecmis": "Geçmişte sosyal çevrede yaşanan dedikodular, dışlanmalar veya aşırıya kaçan eğlenceler sorun yaratmış.",
        "ters_simdi": "Şu an çevrendeki insanlarla arana mesafe koyuyor ya da sahte dostlukların kurbanı oluyorsun.",
        "ters_gelecek": "Gelecekte aşırı sosyalleşmenin getirdiği yorgunluklar veya dedikodu krizleriyle karşılaşabilirsin."
    },
    26: {
        "isim": "KUPA DÖRTLÜSÜ (FOUR OF CUPS)",
        "duz_gecmis": "Geçmişte önüne sunulan fırsatları görmezden gelip içsel bir tatminsizlik ve dalgınlık içinde kalmışsın.",
        "duz_simdi": "Şu an her şey önünde durmasına rağmen mutsuz ve ilgisiz hissediyorsun; sunulan şansları elinin tersiyle itiyorsun.",
        "duz_gelecek": "Gelecekte bu apatik durumdan sıyrılmak için yeni bir bakış açısı kazanman gereken bir dönem gelecek.",
        "ters_gecmis": "Geçmişteki durgunluk halinden kurtulup yeniden hayata motive olmaya başladığın adımlar atmışsın.",
        "ters_simdi": "Şu an kabuğundan çıkıyor, çevrendeki fırsatları fark etmeye ve uyanmaya başlıyorsun.",
        "ters_gelecek": "Gelecekte durgunluğun sona ereceği, içsel motivasyonunun hızla artacağı taze bir dönem seni bekliyor."
    },
    27: {
        "isim": "KUPA BEŞLİSİ (FIVE OF CUPS)",
        "duz_gecmis": "Geçmişte yaşanan kayıplara ve dökülen sütlere odaklanarak kendini uzun süre yas ve pişmanlık içinde bırakmışsın.",
        "duz_simdi": "Şu an elinde kalan güzellikleri görmüyor, sadece kaybettiğin ya da giden şeylerin üzüntüsünü yaşıyorsun.",
        "duz_gelecek": "Gelecekte geçmişin pişmanlıklarını arkada bırakıp kalan değerlerinle yola devam etmeyi öğreneceksin.",
        "ters_gecmis": "Geçmişteki acıları affetmiş ve artık yaralarını sarmaya başlayarak toparlanma evresine girmişsin.",
        "ters_simdi": "Şu an üzüntülerini hafifletiyor, hayata yeniden umutla bakabilmek için içsel bir güç buluyorsun.",
        "ters_gelecek": "Gelecekte tam bir şifa süreci yaşayacak, kaybettiğini sandığın enerjiyi yeniden kazanacaksın."
    },
    28: {
        "isim": "KUPA ALTILISI (SIX OF CUPS)",
        "duz_gecmis": "Geçmişte çocukluk anıları, saf nostalji ve eski güzel günlerin masumluğu hayatında büyük yer kaplamış.",
        "duz_simdi": "Şu an geçmişten gelen tatlı hatıralar, eski dostlar veya saf sevgi bağları hayatını ısıtıyor.",
        "duz_gelecek": "Gelecekte geçmişteki güzel bir anı veya eski bir tanıdık hayatına yeniden neşe getirebilir.",
        "ters_gecmis": "Geçmişe ve eski zamana aşırı takılı kalmak bugünü yaşamanı engellemiş ve seni geride tutmuş.",
        "ters_simdi": "Şu an nostaljinin bataklığından çıkmaya, bugüne ve geleceğe odaklanmaya çalışıyorsun.",
        "ters_gelecek": "Gelecekte geçmişin hayaletlerinden tamamen kurtulup ayakları yere basan kararlar alacaksın."
    },
    29: {
        "isim": "KUPA YEDİLİSİ (SEVEN OF CUPS)",
        "duz_gecmis": "Geçmişte hayaller, illüzyonlar ve önünde duran çok fazla seçenek arasında kafan karışmış ve kararsız kalmışsın.",
        "duz_simdi": "Şu an kafanda binbir türlü hayal var ama hangisinin gerçek olduğunu seçmekte zorlanıyorsun, illüzyonlardasın.",
        "duz_gelecek": "Gelecekte hayaller ile gerçekleri birbirinden ayırman gereken kritik bir elek döneminden geçeceksin.",
        "ters_gecmis": "Geçmişteki hayal perestlikten sıyrılıp net ve gerçekçi kararlar almayı başarmışsın.",
        "ters_simdi": "Şu an sis perdesi aralanıyor; ne istediğini net bir şekilde görüyor ve odaklanıyorsun.",
        "ters_gelecek": "Gelecekte kafa karışıklıkları son bulacak, en doğru ve somut seçimi yapacaksın."
    },
    30: {
        "isim": "KUPA SEKİZLİSİ (EIGHT OF CUPS)",
        "duz_gecmis": "Geçmişte sana artık duygusal olarak yetmeyen, tükenmiş bir durumu veya ortamı arkanda bırakıp yola çıkmışsın.",
        "duz_simdi": "Şu an seni manevi olarak tatmin etmeyen yapıları geride bırakıp daha yüksek bir amaca doğru yürüyorsun.",
        "duz_gelecek": "Gelecekte aradığın huzuru bulmak için mevcut düzenini terk edip uzun ve anlamlı bir yolculuğa çıkacaksın.",
        "ters_gecmis": "Geçmişte gitmekle kalmak arasında kalmış, korkular yüzünden mutsuz bir düzende kalmaya devam etmişsin.",
        "ters_simdi": "Şu an gitme korkusu ile kalma isteği arasında sıkışmış durumdasın; cesaretini toplaman gerekiyor.",
        "ters_gelecek": "Gelecekte ertelediğin o ayrılık adımını nihayet atacak ve kendi yolunu çizeceksin."
    },
    31: {
        "isim": "KUPA DOKUZLUSU (NINE OF CUPS)",
        "duz_gecmis": "Geçmişte dileklerinin gerçekleştiği, içsel tatminin ve mutluluğun zirvesinde keyifli bir dönem geçirmişsin.",
        "duz_simdi": "Şu an her şey dilediğin gibi gidiyor; büyük bir tatmin, huzur ve keyif hali içindesin (Dilek kartı).",
        "duz_gelecek": "Gelecekte uzun süredir istediğin bir arzunun gerçeğe dönüştüğünü görecek ve büyük bir mutluluk yaşayacaksın.",
        "ters_gecmis": "Geçmişte elde ettiğin başarılar seni şımartmış ya da yüzeysel tatminler ruhunu beslememiş.",
        "ters_simdi": "Şu an her şey dışarıdan iyi görünse de içten içe bir eksiklik veya açgözlülük hissi yaşıyorsun.",
        "ters_gelecek": "Gelecekte aşırı beklentiler nedeniyle hayal kırıklığı yaşayabilir ya da mutluluğu yanlış yerlerde arayabilirsin."
    },
    32: {
        "isim": "KUPA ONLUSU (TEN OF CUPS)",
        "duz_gecmis": "Geçmişte mutlu aile ortamı, kalıcı huzur ve sevdiklerinle paylaştığın cennet gibi bir yuva kurmuşsun.",
        "duz_simdi": "Şu an hayatında huzurun, aile içi uyumun ve kalbi dolduran büyük bir mutluluğun tam merkezindesin.",
        "duz_gelecek": "Gelecekte ömür boyu sürecek huzurlu bir yuva, evlilik veya en üst düzeyde duygusal tatmin seni bekliyor.",
        "ters_gecmis": "Geçmişte aile içi huzursuzluklar, evlilik krizleri ve beklenen uyumun sağlanamaması üzüntü yaratmış.",
        "ters_simdi": "Şu an evinde veya yakın ilişkilerinde soğukluklar, anlaşmazlıklar ve huzursuzluklar hakim.",
        "ters_gelecek": "Gelecekte ailevi veya ortaksal ilişkilerde yaşanabilecek kopuklukları onarmak için çaba harcaman gerekecek."
    },
    33: {
        "isim": "KUPA PRENSİ (PAGE OF CUPS)",
        "duz_gecmis": "Geçmişte beklenmedik romantik teklifler, tatlı haberler ve duygusal sürprizler almışsın.",
        "duz_simdi": "Şu an saf duygular, çocuksu bir heyecan ve kalbini tıkırdatacak sürpriz bir teklif kapında.",
        "duz_gelecek": "Gelecekte hayatına neşe katacak taze bir haber veya kalbini heyecanlandıracak tatlı bir gelişme yaşanacak.",
        "ters_gecmis": "Geçmişte aşırı alınganlıklar, çocuksu tavırlar ve asılsız duygusal beklentiler hayal kırıklığı yaratmış.",
        "ters_simdi": "Şu an duygularında çok alıngan, çocuksu ve güven vermeyen bir ruh halindesin.",
        "ters_gelecek": "Gelecekte tutarsız duygusal çıkışlar ve olgunlaşmamış teklifler yüzünden zaman kaybedebilirsin."
    },
    34: {
        "isim": "KUPA ŞÖVALYESİ (KNIGHT OF CUPS)",
        "duz_gecmis": "Geçmişte romantik yaklaşımlar sergilemiş, cazibeli teklifler almış ya da sevginin peşinden koşturmuşsun.",
        "duz_simdi": "Şu an hayatında romantizm, teklifler, cazibe ve duygusal anlamda atılan zarif adımlar ön planda.",
        "duz_gelecek": "Gelecekte beyaz atlı prens/prensas edasıyla hayatına girecek çok romantik ve kalpli bir insanla karşılaşacaksın.",
        "ters_gecmis": "Geçmişte gerçekçi olmayan hayaller peşinden koşturmuş, güven vermeyen vaatlerle kandırılmışsın.",
        "ters_simdi": "Şu an karşındaki kişinin niyetleri belirsiz; romantik görünen ama altı boş vaatlerle karşı karşıyasın.",
        "ters_gelecek": "Gelecekte tutarsız aşaklar ve hayal kırıklığı yaratacak romantik hayal kırıklıkları yaşayabilirsin."
    },
    35: {
        "isim": "KUPA KRALİÇESİ (QUEEN OF CUPS)",
        "duz_gecmis": "Geçmişte çok şefkatli, sezgisel, anlayışlı ve olaylara kalbiyle yaklaşan bir kadın figüründen destek almışsın.",
        "duz_simdi": "Şu an sezgilerinin çok güçlü olduğu, etrafına şefkat dağıttığın ve iç sesinle hareket ettiğin bir dönemdesin.",
        "duz_gelecek": "Gelecekte hayatına şefkatli, duygusal açıdan olgun ve seni derinlemesine anlayan bir kadın figürü dahil olacak.",
        "ters_gecmis": "Geçmişte duygusal istismar, manipülasyon, aşırı alınganlık ve boğucu bir şefkat ortamı seni bunaltmış.",
        "ters_simdi": "Şu an duygusal olarak çok kırılgan ve manipülasyona açık bir ruh halindesin; iç huzurun sarsılmış.",
        "ters_gelecek": "Gelecekte aşırı duygusallık ve alınganlık yüzünden ilişkilerde trajikomik krizler yaşayabilirsin."
    },
    36: {
        "isim": "KUPA KRALI (KING OF CUPS)",
        "duz_gecmis": "Geçmişte duygularını ustalıkla kontrol edebilen, olgun, adil ve merhametli bir liderin desteğini görmüşsün.",
        "duz_simdi": "Şu an mantık ile duygu arasında mükemmel bir denge kurmuş, etrafına güven veren bir bilgesin.",
        "duz_gelecek": "Gelecekte hayatına duygusal olgunluğa erişmiş, seni koruyup kollayacak güçlü bir erkek figürü girecek.",
        "ters_gecmis": "Geçmişte duygu sömürüsü yapan, içten pazarlıklı, soğuk ve öfkesini gizleyen manipülatif erkekler üzmüş.",
        "ters_simdi": "Şu an duygularını bastırıyor ya da öfkeni kontrol etmekte zorlanarak çevrene zarar veriyorsun.",
        "ters_gelecek": "Gelecekte güven sarsacak duygusal manipülasyonlara ve soğuk, mesafeli tutumlara karşı dikkatli olmalısın."
    },
    37: {
        "isim": "KILIÇ ASI (ACE OF SWORDS)",
        "duz_gecmis": "Geçmişte keskin bir zeka patlaması yaşamış, hakikati net bir şekilde görüp yepyeni kararlar almışsın.",
        "duz_simdi": "Şu an zihnin pırıl pırıl; doğruları net görüyor, keskin kararlar almak için en doğru zamandasın.",
        "duz_gelecek": "Gelecekte hakikatin ortaya çıkacağı, zaferle sonuçlanacak hukuki veya zihinsel büyük bir başarı kazanacaksın.",
        "ters_gecmis": "Geçmişte zihinsel bulanıklıklar, yanlış kararlar ve düşünmeden söylenen kırıcı sözler sorun yaratmış.",
        "ters_simdi": "Şu an kafan oldukça karışık; yanlış kararlar almak üzeresin ve mantığın yerine önyargılarla hareket ediyorsun.",
        "ters_gelecek": "Gelecekte yanlış anlaşılmalar, adaletsiz zihinsel kararlar ve iletişim kazaları yaşanabilir."
    },
    38: {
        "isim": "KILIÇ İKİLİSİ (TWO OF SWORDS)",
        "duz_gecmis": "Geçmişte iki seçenek arasında kalmış, gözlerini gerçeğe kapatarak karar vermeyi bilinçli olarak ertelemişsin.",
        "duz_simdi": "Şu an büyük bir ikilemdesin; taraflardan birini seçmemek için gerçeği görmezden geliyorsun.",
        "duz_gelecek": "Gelecekte artık kaçamayacağın zorunlu bir karar almak ve gözlerindeki bandı çıkarmak zorunda kalacaksın.",
        "ters_gecmis": "Geçmişte o zorlu kararı nihayet almış ve gerçekle yüzleşerek kördüğümü çözmüşsün.",
        "ters_simdi": "Şu an kararsızlık perdesi aralanıyor; istemesen de gerçeklerle yüzleşmek zorunda kaldığın bir antasın.",
        "ters_gelecek": "Gelecekte uzun süredir ertelenen o kritik karar netleşecek ve rahat bir nefes alacaksın."
    },
    39: {
        "isim": "KILIÇ ÜÇLÜSÜ (THREE OF SWORDS)",
        "duz_gecmis": "Geçmişte derin bir kalp kırıklığı, acı haber veya sarsıcı bir ihanetle büyük bir hüsran yaşamışsın.",
        "duz_simdi": "Şu an kalbin sızlıyor; aldığın acı bir haber veya hayal kırıklığı ruhunu derinden yaralamış durumda.",
        "duz_gelecek": "Gelecekte bu acı dönemi geride bırakıp yaralarını sarmaya başlayacağın bir şifa evresi seni bekliyor.",
        "ters_gecmis": "Geçmişteki acıları affetmeye ve kalbindeki o derin yaraları yavaş yavaş kapatmaya başlamışsın.",
        "ters_simdi": "Şu an iyileşme sürecindesin; acı hafifliyor ancak izleri hala taze.",
        "ters_gelecek": "Gelecekte tamamen bağışlama ve geçmişin acı yüklerinden arınarak özgürleşme zamanı gelecek."
    },
    40: {
        "isim": "KILIÇ DÖRTLÜSÜ (FOUR OF SWORDS)",
        "duz_gecmis": "Geçmişte yaşadığın yoğun stresin ardından derin bir zihinsel mola vermiş, hastane veya dinlenme dönemi geçirmişsin.",
        "duz_simdi": "Şu an acilen dinlenmeye, dünyadan el etek çekip zihnini tamamen sessizliğe gömmeye ihtiyacın var.",
        "duz_gelecek": "Gelecekte fırtınalar dinecek ve uzun süreli huzurlu bir dinlenme, meditasyon dönemi seni bekliyor.",
        "ters_gecmis": "Geçmişteki tükenmişlik hali ve zorunlu yatak istirahati enerjini tüketmiş.",
        "ters_simdi": "Şu an aşırı yorgunluktan tükenmek üzeresin ama yine de durmayı reddediyorsun.",
        "ters_gelecek": "Gelecekte dinlenmediğin takdirde vücudun veya zihnin seni durmaya zorlayacak büyük bir çöküş yaşayabilir."
    },
    41: {
        "isim": "KILIÇ BEŞLİSİ (FIVE OF SWORDS)",
        "duz_gecmis": "Geçmişte ego savaşlarının olduğu, kazandığını sandığın ama aslında herkesi kaybettiğin kirli bir mücadele yaşamışsın.",
        "duz_simdi": "Şu an çevrendeki insanlarla gereksiz bir güç ve ego savaşı içine giriyorsun; bu kavganın galibi olmayacak.",
        "duz_gelecek": "Gelecekte hırs uğruna kıracağın kalplerin ve çıkacak çatışmaların pişmanlığını yaşayabilirsin.",
        "ters_gecmis": "Geçmişteki kavgaları geride bırakmış, barışma ve uzlaşı yollarını arayarak meseleyi tatlıya bağlamışsın.",
        "ters_simdi": "Şu an düşmanca tutumları bitirip uzlaşma sağlamak için masaya oturma vaktindesin.",
        "ters_gelecek": "Gelecekte eski kavgalar son bulacak, taraflar arasındaki gerginlik yerini yumuşamaya bırakacak."
    },
    42: {
        "isim": "KILIÇ ALTILISI (SIX OF SWORDS)",
        "duz_gecmis": "Geçmişte sıkıntılı, fırtınalı bir süreci geride bırakıp daha sakin ve güvenli sulara doğru yol almışsın.",
        "duz_simdi": "Şu an sorunlu ortamları arkanda bırakıyor, yavaş ama emin adımlarla huzurlu bir geleceğe doğru ilerliyorsun.",
        "duz_gelecek": "Gelecekte tüm dertlerini geride bırakacağın huzurlu bir seyahat veya yeni bir yaşam alanı seni bekliyor.",
        "ters_gecmis": "Geçmişte sorunlardan kaçmaya çalışmış ancak sırtındaki yükleri ve problemleri de beraberinde taşımışsın.",
        "ters_simdi": "Şu an kaçmak istediğin sorunlar peşini bırakmıyor; yüklerin hala çok ağır.",
        "ters_gelecek": "Gelecekte köklü çözümler bulmadan yapacağın kaçışların işe yaramayacağını fark edeceksin."
    },
    43: {
        "isim": "KILIÇ YEDİLİSİ (SEVEN OF SWORDS)",
        "duz_gecmis": "Geçmişte gizli saklı işler çevrilmiş, kurnazlıklar yapılmış veya bir şeylerden stratejik olarak kaçılmış.",
        "duz_simdi": "Şu an etrafında dönen dolaplara, gizli saklı işlere ve kurnaz insanlara karşı çok dikkatli olmalısın.",
        "duz_gelecek": "Gelecekte stratejik hamleler yapman gerekecek ya da sakladığın sırlar gün yüzüne çıkma tehlikesi yaşayacak.",
        "ters_gecmis": "Geçmişte yapılan gizli işler ifşa olmuş, kurnazlık yapanlar suçüstü yakalanmış.",
        "ters_simdi": "Şu an sırların ortaya döküldüğü, dürüstlüğün kazandığı bir yüzleşme anındasın.",
        "ters_gelecek": "Gelecekte giz saklamanın imkansız olduğunu anlayacak ve her şeyi açık oynamaya başlayacaksın."
    },
    44: {
        "isim": "KILIÇ SEKİZLİSİ (EIGHT OF SWORDS)",
        "duz_gecmis": "Geçmişte kendi kendini kısıtlamış, elin kolun bağlıymış gibi hissederek çaresizlik psikolojisine kapılmışsın.",
        "duz_simdi": "Şu an çıkış yolu olmadığını düşünüyorsun ama bu kısıtlamaların çoğu kendi zihninde kurduğun kuruntulardan ibaret.",
        "duz_gelecek": "Gelecekte gözlerindeki bağı çözüp etrafındaki ip bağlarını kopararak özgürlüğüne kavuşacaksın.",
        "ters_gecmis": "Geçmişteki çaresizlik zincirlerini kırmış, korkularını yenerek yeniden ayağa kalkmışsın.",
        "ters_simdi": "Şu an özgürleşme yolunda çok güçlü adımlar atıyorsun; kısıtlamalardan sıyrılıyorsun.",
        "ters_gelecek": "Gelecekte tüm engelleri arkanda bırakacak, kendi hayatının kontrolünü tamamen eline alacaksın."
    },
    45: {
        "isim": "KILIÇ DOKUZLUSU (NINE OF SWORDS)",
        "duz_gecmis": "Geçmişte kabuslar, aşırı kaygılar ve uykusuz gecelerle geçen çok yıpratıcı bir kaygı dönemi yaşamışsın.",
        "duz_simdi": "Şu an kafana taktığın kuruntular ve endişeler yüzünden geceleri uyuyamaz haldesin, strese yeniliyorsun.",
        "duz_gelecek": "Gelecekte bu yersiz endişelerin kuruntu olduğunu anlayacak ve derin bir rahatlama yaşayacaksın.",
        "ters_gecmis": "Geçmişteki korkular ve kabuslar hafiflemiş, şifa bulma süreci yavaş yavaş başlamış.",
        "ters_simdi": "Şu an kaygıların azalıyor; gizli korkularını gün ışığına çıkarıp rahatlamaya başlıyorsun.",
        "ters_gelecek": "Gelecekte zihinsel yüklerden tamamen arınacak, kafandaki kara bulutları dağıtacaksın."
    },
    46: {
        "isim": "KILIÇ ONLUSU (TEN OF SWORDS)",
        "duz_gecmis": "Geçmişte en dip noktayı görmüş, sırtından bıçaklanmış ve tükenişin acısını sonuna kadar hissetmişsin.",
        "duz_simdi": "Şu an her şeyin bittiğini sandığın en zorlu ve yorucu bir kriz noktasındasın, ama buradan başka düşecek yer yok.",
        "duz_gelecek": "Gelecekte en dipten ayağa kalkacak, yaralarını sarıp yepyeni bir sabaha uyanacaksın.",
        "ters_gecmis": "Geçmişteki büyük felaket atlatılmış, en kötü günlerin geride kaldığı bir iyileşme süreci başlamış.",
        "ters_simdi": "Şu an krizin en şiddetli anı geçiyor; toparlanma ve yeniden doğuş için ilk adımları atıyorsun.",
        "ters_gelecek": "Gelecekte tamamen şifa bulacak, eski acıları tarihe gömerek güçlü bir şekilde yeniden başlayacaksın."
    },
    47: {
        "isim": "KILIÇ PRENSİ (PAGE OF SWORDS)",
        "duz_gecmis": "Geçmişte etrafı tetikte gözlemlemiş, dedikodular almış ve keskin sözler sarf etmişsin.",
        "duz_simdi": "Şu an bilgi topluyor, etraftaki gelişmeleri yakından takip ediyor ve çok eleştirel bir gözle bakıyorsun.",
        "duz_gelecek": "Gelecekte beklenmedik keskin haberler alacak ve zihinsel olarak hazır olman gereken durumlarla karşılaşacaksın.",
        "ters_gecmis": "Geçmişte düşüncesizce sarf edilen kırıcı sözler ve yersiz şüpheler tartışmalara yol açmış.",
        "ters_simdi": "Şu an dedikodulara kulak asıyor, düşünmeden konuşarak insanları kırıyorsun.",
        "ters_gelecek": "Gelecekte fevri ve patavatsızca söylenen sözlerin yaratacağı dezavantajları toplamak zorunda kalabilirsin."
    },
    48: {
        "isim": "KILIÇ ŞÖVALYESİ (KNIGHT OF SWORDS)",
        "duz_gecmis": "Geçmişte çok hızlı, hırslı, fevri ve gözü kara bir şekilde hedeflerinin üzerine yürümüşsün.",
        "duz_simdi": "Şu an fırtınalar estiriyor, mantığınla ve hızınla engelleri parçalayarak ilerlemek istiyorsun.",
        "duz_gelecek": "Gelecekte hayatına çok hızlı gelişmeler, ani kararlar ve büyük bir koşturmaca hakim olacak.",
        "ters_gecmis": "Geçmişteki aşırı acelecilik ve düşüncesiz hamleler büyük hatalara ve kazalara yol açmış.",
        "ters_simdi": "Şu an kafana esenin peşinden düşünmeden koşuyor, etrafı kırıp geçiriyorsun.",
        "ters_gelecek": "Gelecekte aceleciliğin ve fevriliğin yüzünden telafisi güç zihinsel hatalar yapabilirsin."
    },
    49: {
        "isim": "KILIÇ KRALİÇESİ (QUEEN OF SWORDS)",
        "duz_gecmis": "Geçmişte mantıklı, dürüst, analitik, net ve duygularından ziyade adaleti savunan bir kadın figürüyle karşılaşmışsın.",
        "duz_simdi": "Şu an duygularını bir kenara bırakmış, tamamen mantığınla hareket ediyor ve araya net mesafeler koyuyorsun.",
        "duz_gelecek": "Gelecekte hayatına akıllı, dürüst ama bir o kadar da mesafeli ve net kuralları olan bir kadın girecek.",
        "ters_gecmis": "Geçmişte katı kalplilik, aşırı soğukluk, iğneleyici ve kırıcı bir dil çevreni uzaklaştırmış.",
        "ters_simdi": "Şu an etrafındakilere karşı çok soğuk, yargılayıcı ve eleştirelsin; empatiyi unutmuşsun.",
        "ters_gelecek": "Gelecekte yalnızlaşmaya yol açabilecek katı ve acımasız eleştirilerden kaçınmalısın."
    },
    50: {
        "isim": "KILIÇ KRALI (KING OF SWORDS)",
        "duz_gecmis": "Geçmişte son derece adil, entelektüel, mantıklı ve otoriter bir erkek figüründen akıl almışsın.",
        "duz_simdi": "Şu an olaylara tamamen tarafsız, analitik ve bir hakim edasıyla yaklaşma zorunluluğundasın.",
        "duz_gelecek": "Gelecekte hayatında mantığın, yasanın ve entelektüel gücün hakim olduğu profesyonel bir süreç başlayacak.",
        "ters_gecmis": "Geçmişte zorbalık yapan, insanları acımasızca eleştiren ve manipülatif akıllar veren bir otorite seni ezmiş.",
        "ters_simdi": "Şu an gücünü yanlış kullanıyor, zekanı başkalarını ezmek veya baskı kurmak için harcıyorsun.",
        "ters_gelecek": "Gelecekte adaletsiz ve katı tutumlar sergileyen kibirli insanlarla çatışmalar yaşayabilirsin."
    },
    51: {
        "isim": "DEĞNEK ASI (ACE OF WANDS)",
        "duz_gecmis": "Geçmişte hayatına büyük bir tutku, yüksek bir enerji ve yaratıcı yeni bir kıvılcım dahil olmuş.",
        "duz_simdi": "Şu an enerjin tavan yapmış durumda; yeni bir projeye başlamak için harika bir tutku ve ilham içindesin.",
        "duz_gelecek": "Gelecekte hayatını ateşleyecek muazzam bir fırsat, yeni bir iş veya tutku dolu bir başlangıç kapıda.",
        "ters_gecmis": "Geçmişte enerji düşüklüğü, ertelenen projeler ve sönen hevesler hayal kırıklığı yaratmış.",
        "ters_simdi": "Şu an motivasyonun çok düşük; başlamak istediğin şeyler sürekli erteleniyor ve enerjin blokeli.",
        "ters_gelecek": "Gelecekte yanlış yönlendirilen enerjiler ve kaçan fırsatlar yüzünden tatminsizlik yaşayabilirsin."
    },
    52: {
        "isim": "DEĞNEK İKİLİSİ (TWO OF WANDS)",
        "duz_gecmis": "Geçmişte geleceğe dair büyük planlar yapmış, dünya haritasını önüne sererek stratejik adımlar tasarlamışsın.",
        "duz_simdi": "Şu an bir yol ayrımındasın; ya mevcut yerinde kalacaksın ya da vizyonunu genişletip büyük bir adım atacaksın.",
        "duz_gelecek": "Gelecekte uluslararası işler, seyahatler ve uzun vadeli vizyoner planların meyvesini vermeye başlayacak.",
        "ters_gecmis": "Geçmişte vizyonsuzluk, risk alamama ve konfor alanından çıkmama korkusu seni kısıtlamış.",
        "ters_simdi": "Şu an ne yapacağını bilemez haldesin; planların askıda kalmış ve cesaret edemiyorsun.",
        "ters_gelecek": "Gelecekte cesaretsizlik ve yanlış planlamalar yüzünden büyük fırsatları başkalarına kaptırabilirsin."
    },
    53: {
        "isim": "DEĞNEK ÜÇLÜSÜ (THREE OF WANDS)",
        "duz_gecmis": "Geçmişte attığın tohumların ve yatırımların ilk meyvelerini toplamaya başladığın genişleme dönemi olmuş.",
        "duz_simdi": "Şu an ufka bakıyorsun; beklediğin gemiler limana yaklaşmaya başlıyor, işlerin büyüyor.",
        "duz_gelecek": "Gelecekte ticari başarılar, uzak yoldan gelecek güzel haberler ve beklenen gelişmeler gerçeğe dönüşecek.",
        "ters_gecmis": "Geçmişte beklenenlerin gecikmesi ve yatırımların karşılıksız kalması hayal kırıklığı yaratmış.",
        "ters_simdi": "Şu an işlerin beklediğin hızda ilerlemediğini görüyor ve sabırsızlanıyorsun.",
        "ters_gelecek": "Gelecekte lojistik veya zamanlama hataları yüzünden ufak aksaklıklar yaşayabilirsin."
    },
    54: {
        "isim": "DEĞNEK DÖRTLÜSÜ (FOUR OF WANDS)",
        "duz_gecmis": "Geçmişte düğünler, kutlamalar, ev kurma veya başarıyı sevdiklerinle kutladığın harika bir yuva ortamı olmuş.",
        "duz_simdi": "Şu an hayatında huzurun, istikrarın ve kutlama yapmaya değer mutlu bir dönemin tadını çıkarıyorsun.",
        "duz_gelecek": "Gelecekte evlilik, nişan, eve taşınma veya büyük bir başarı kutlaması seni bekliyor.",
        "ters_gecmis": "Geçmişte aile içi gerginlikler, kutlamaların ertelenmesi veya yuva içindeki uyumsuzluklar üzmüş.",
        "ters_simdi": "Şu an ev ortamında veya yakın çevrende huzursuzluklar ve geçici gerginlikler var.",
        "ters_gelecek": "Gelecekte planlanan kutlama veya evlilik gibi organizasyonlarda ufak pürüzler çıkabilir."
    },
    55: {
        "isim": "DEĞNEK BEŞLİSİ (FIVE OF WANDS)",
        "duz_gecmis": "Geçmişte fikir çatışmalarının, rekabetin ve herkesin kendi sesini duyurmaya çalıştığı arbedeli bir ortam yaşanmış.",
        "duz_simdi": "Şu an çevrende seninle aynı fikirde olmayan insanlarla sürekli bir sürtüşme ve rekabet halindesin.",
        "duz_gelecek": "Gelecekte önüne çıkacak zorlu rakiplerle mücadele etmen gereken hareketli bir süreç seni bekliyor.",
        "ters_gecmis": "Geçmişteki kavgalar ve rekabet ortamı yerini uzlaşmaya ve ortak akla bırakmış.",
        "ters_simdi": "Şu an tartışmalardan kaçınıyor, kaosu bitirmek için yapıcı adımlar atıyorsun.",
        "ters_gelecek": "Gelecekte anlamsız tartışmalar son bulacak, sular durulacak ve ortak paydada buluşulacak."
    },
    56: {
        "isim": "DEĞNEK ALTILISI (SIX OF WANDS)",
        "duz_gecmis": "Geçmişte büyük bir zafer kazanmış, halkın takdirini toplamış ve başarıyla gurur duyduğun bir an yaşamışsın.",
        "duz_simdi": "Şu an başarılarının kutlandığı, herkesin gözünün üstünde olduğu parlayan bir zafer dönemindesin.",
        "duz_gelecek": "Gelecekte projelerin büyük ödüller alacak, adından övgüyle söz ettirecek harika bir zafer seni bekliyor.",
        "ters_gecmis": "Geçmişte başarısızlık hissi, takdir görmeme ve zaferin son anda elden kayması üzüntü yaratmış.",
        "ters_simdi": "Şu an emeklerinin karşılığını yeterince alamadığını düşünüyor, takdir edilmemekten yakınıyorsun.",
        "ters_gelecek": "Gelecekte gizli kıskançlıklara ve başarıya giden yolda engellemelere karşı uyanık olmalısın."
    },
    57: {
        "isim": "DEĞNEK YEDİLİSİ (SEVEN OF WANDS)",
        "duz_gecmis": "Geçmişte haklarını, pozisyonunu ve inandığın değerleri tek başına büyük bir dirençle savunmuşsun.",
        "duz_simdi": "Şu an etrafından gelen baskılara ve eleştirilere karşı kendi kaleni korumak için direnmek zorundasın.",
        "duz_gelecek": "Gelecekte pozisyonunu korumak adına vereceğin bu haklı mücadeleden galip çıkacaksın.",
        "ters_gecmis": "Geçmişte baskılar karşısında pes etmiş, savunmasız kalarak köşeye sıkışmışsın.",
        "ters_simdi": "Şu an üst üste gelen baskılar altında eziliyor, artık direnecek gücü kendinde bulamıyorsun.",
        "ters_gelecek": "Gelecekte tükenmişlik yaşayabilir, haklı olduğun bir davada sırf yorgunluktan dolayı geri adım atabilirsin."
    },
    58: {
        "isim": "DEĞNEK SEKİZLİSİ (EIGHT OF WANDS)",
        "duz_gecmis": "Geçmişte hayatına ani gelişmeler, hızlı haberler, seyahatler ve ardı arkasına gelen fırsatlar akın etmiş.",
        "duz_simdi": "Şu an olaylar çok hızlı gelişiyor; hızına yetişmekte zorlanacağın müthiş bir hareketlilik var.",
        "duz_gelecek": "Gelecekte çok hızlı haberler, ani seyahat kararları ve sürpriz gelişmeler kapını çalacak.",
        "ters_gecmis": "Geçmişteki gecikmeler, yanlış yönlendirilen enerjiler ve askıya alınan seyahatler sinir bozmuş.",
        "ters_simdi": "Şu an işler tıkandığı için beklemek zorunda kalıyor, hızın kesilmesinden sıkılıyorsun.",
        "ters_gelecek": "Gelecekte planlarda yaşanacak ani aksaklıklar ve bürokratik gecikmeler seni yavaşlatabilir."
    },
    59: {
        "isim": "DEĞNEK DOKUZLUSU (NINE OF WANDS)",
        "duz_gecmis": "Geçmişte çok yıpratıcı süreçlerden geçmiş, yaralı ama hala ayakta kalarak son bir direniş sergilemişsin.",
        "duz_simdi": "Şu an yorgunsun ama tetiktesin; gelebilecek son darbelere karşı savunma pozisyonunu bozmuyorluktasın.",
        "duz_gelecek": "Gelecekte maratonun son metresindesin; biraz daha sabredersen bu savaşı tamamen kazanacaksın.",
        "ters_gecmis": "Geçmişteki aşırı güvensizlik ve paranoyak savunma halleri seni fazlasıyla yormuş.",
        "ters_simdi": "Şu an artık savunma yapamayacak kadar tükenmiş durumdasın; duvarlarını indirmek üzeresin.",
        "ters_gelecek": "Gelecekte direnç göstermeyi bırakıp teslim olacağın, yorgunluğun zirve yapacağı bir an gelebilir."
    },
    60: {
        "isim": "DEĞNEK ONLUSU (TEN OF WANDS)",
        "duz_gecmis": "Geçmişte her sorumluluğu tek başına sırtlanmış, taşıyamayacağın kadar büyük yükler altına girmişsin.",
        "duz_simdi": "Şu an omuzlarındaki yükler seni ezmek üzere; her şeyi tek başına sırtlamaktan tükenmiş haldesin.",
        "duz_gelecek": "Gelecekte bu ağır sorumlulukları bitirip finiş çizgisine ulaşacaksın ama sonrasında acilen dinlenmen gerekecek.",
        "ters_gecmis": "Geçmişte binen o ağır yüklerden kurtulmuş, sorumlulukları başkalarıyla paylaşarak rahatlamışsın.",
        "ters_simdi": "Şu an sırtındaki küfeyi hafifletmeye, gereksiz yükleri birer birer atmaya çalışıyorsun.",
        "ters_gelecek": "Gelecekte yüklerin hafifleyeceği ve hayatının nefes alabileceği çok rahat bir döneme gireceksin."
    },
    61: {
        "isim": "DEĞNEK PRENSİ (PAGE OF WANDS)",
        "duz_gecmis": "Geçmişte heyecanlı haberler almış, macera dolu fikirlere atılmış ve gençsel bir enerjiyle hareket etmişsin.",
        "duz_simdi": "Şu an yeni bir macera için sabırsızlanıyor, öğrenmeye ve keşfetmeye son derece açık bir ruh halindesin.",
        "duz_gelecek": "Gelecekte hayatına renk katacak sürpriz bir haber, seyahat veya genç dinamik biri girecek.",
        "ters_gecmis": "Geçmişte sabırsızlık, dağınıklık ve başlanan işlerin yarım bırakılması kötü sonuçlar doğurmuş.",
        "ters_simdi": "Şu an odaklanmakta zorlanıyor, daldan dala atlıyor ve sabırsız tavırlar sergiliyorsun.",
        "ters_gelecek": "Gelecekte tutarsız hevesler ve yarım kalan projeler yüzünden vakit kaybedebilirsin."
    },
    62: {
        "isim": "DEĞNEK ŞÖVALYESİ (KNIGHT OF WANDS)",
        "duz_gecmis": "Geçmişte tutkularının peşinden korkusuzca koşturmuş, seyahatler etmiş ve ateşli kararlar almışsın.",
        "duz_simdi": "Şu an macera peşinde koşuyor, enerjik, tutkulu ve durdurulamaz bir hızla hareket ediyorsun.",
        "duz_gelecek": "Gelecekte ani seyahatler, tutkulu aşklar ve arkana bakmadan atılacağın heyecanlı maceralar seni bekliyor.",
        "ters_gecmis": "Geçmişteki aşırı fevrilik, sabırsızlık ve çabuk sönen ateşler büyük pişmanlıklar bırakmış.",
        "ters_simdi": "Şu an çok aceleci, patavatsız ve düşünmeden hareket eden bir enerjiye sahipsin.",
        "ters_gelecek": "Gelecekte çabuk parlayıp çabuk sönen tutkular yüzünden yanlış adımlar atabilirsin."
    },
    63: {
        "isim": "DEĞNEK KRALİÇESİ (QUEEN OF WANDS)",
        "duz_gecmis": "Geçmişte son derece bağımsız, enerjik, çekici, sıcakkanlı ve etrafına ışık saçan bir kadın figürüyle etkileşime girmişsin.",
        "duz_simdi": "Şu an özgüvenin tavan yapmış durumda; karizmanla herkesi etkiliyor ve işlerini tutkuyla yönetiyorsun.",
        "duz_gelecek": "Gelecekte hayatına ilham veren, lider ruhlu, sosyal ve sıcakkanlı güçlü bir kadın dahil olacak.",
        "ters_gecmis": "Geçmişte aşırı kıskançlık, domine etme çabası ve bencil tutumlar ilişkileri zedelemiş.",
        "ters_simdi": "Şu an egonun kurbanı olabilir, başkalarını küçümseyen baskıcı tavırlar sergileyebilirsin.",
        "ters_gelecek": "Gelecekte kıskançlık krizlerine ve aşırı otoriter yaklaşımlardan doğan çatışmalara dikkat etmelisin."
    },
    64: {
        "isim": "DEĞNEK KRALI (KING OF WANDS)",
        "duz_gecmis": "Geçmişte vizyoner, büyük liderlik vasıfları olan, ilham veren ve işleri büyüten bir erkek figüründen destek almışsın.",
        "duz_simdi": "Şu an büyük projelerin liderliğini üstleniyor, karizmanla kitleleri peşinden sürükleyecek güçtesin.",
        "duz_gelecek": "Gelecekte iş dünyasında veya kendi hayatında çok büyük başarılar elde edeceğin liderlik pozisyonuna geleceksin.",
        "ters_gecmis": "Geçmişte sabırsız, buyurgan, bencil ve kendi bildiğini okuyan zorba bir lider yüzünden zorluklar yaşanmış.",
        "ters_simdi": "Şu an çevrendekileri dinlemiyor, fazla baskıcı ve dayatmacı bir tutum sergiliyorsun.",
        "ters_gelecek": "Gelecekte dik başlılık ve fevri yönetim tarzı yüzünden destek kaybedebilirsin."
    },
    65: {
        "isim": "TILSIM ASI (ACE OF PENTACLES)",
        "duz_gecmis": "Geçmişte somut, maddi anlamda çok değerli bir fırsat, iş teklifi veya finansal başlangıç yakalamışsın.",
        "duz_simdi": "Şu an eline parayla, iş kurmayla veya yatırımla ilgili çok somut ve şanslı bir fırsat geçiyor.",
        "duz_gelecek": "Gelecekte maddi refahı artıracak, uzun vadeli sağlam temelli kazanç kapıları ardına kadar açılacak.",
        "ters_gecmis": "Geçmişte kaçan maddi fırsatlar, para kaybetme riskleri ve yanlış yatırımlar zarar vermiştir.",
        "ters_simdi": "Şu an maddi konularda sıkışıklıklar yaşıyor, elindeki finansal fırsatları değerlendiremiyorsun.",
        "ters_gelecek": "Gelecekte yanlış bütçe yönetimi veya kaçırılan iş teklifleri yüzünden parasal riskler doğabilir."
    },
    66: {
        "isim": "TILSIM İKİLİSİ (TWO OF PENTACLES)",
        "duz_gecmis": "Geçmişte hayatın getirdiği maddi ve manevi sorumlulukları hokkabaz gibi dengede tutmak için büyük çaba harcamışsın.",
        "duz_simdi": "Şu an bütçeyi, işleri ve hayatın koşturmacasını aynı anda dengede tutmaya çalışarak hokkabazlık yapıyorsun.",
        "duz_gelecek": "Gelecekte esnek olman gereken değişken finansal şartlar ve para akışını dengelemen gereken durumlar olacak.",
        "ters_gecmis": "Geçmişteki maddi dengesizlikler, borçlar ve kontrolden çıkan bütçe krizlere yol açmış.",
        "ters_simdi": "Şu an finansal dengen tamamen şaşmış durumda; borçlar ve harcamalar birbirine girmiş.",
        "ters_gelecek": "Gelecekte parasal konularda aşırı savurganlık veya dengesizlik yüzünden büyük sıkıntılar kapıda olabilir."
    },
    67: {
        "isim": "TILSIM ÜÇLÜSÜ (THREE OF PENTACLES)",
        "duz_gecmis": "Geçmişte takım çalışması yaparak, başkalarıyla uyumlu ortak emekler vererek usta işi bir projeye imza atmışsın.",
        "duz_simdi": "Şu an iş yerinde veya projelerde ekip ruhuyla hareket ediyor, ortak emeklerin karşılığını almak için çalışıyorsun.",
        "duz_gelecek": "Gelecekte kariyerinde ustalığını kanıtlayacağın, takdir göreceğin kurumsal ve ortaklı projeler seni bekliyor.",
        "ters_gecmis": "Geçmişte ekip içi uyumsuzluklar, kalitesiz işler ve sorumluluk almayan ortaklar projeyi baltalamış.",
        "ters_simdi": "Şu an iş arkadaşlarınla uyum sağlayamıyor, ortak çalışmalarda ciddi iletişim kopuklukları yaşıyorsun.",
        "ters_gelecek": "Gelecekte ekip içi çatışmalar ve kalitesiz iş teslimleri kariyerini olumsuz etkileyebilir."
    },
    68: {
        "isim": "TILSIM DÖRTLÜSÜ (FOUR OF PENTACLES)",
        "duz_gecmis": "Geçmişte paraya, mülke veya mevcut konuma aşırı bağlanmış, cimrilik sınırında güvenlikçi politikalar izlemişsin.",
        "duz_simdi": "Şu an elindekileri kaybetme korkusuyla sıkı sıkıya tutunuyor, para harcamaktan kaçınıyor ve fazlasıyla kontrolcüsün.",
        "duz_gelecek": "Gelecekte maddi güvenceni sağlama alacaksın ancak bu aşırı tutucu tavır sosyal ilişkilerini zedeleyebilir.",
        "ters_gecmis": "Geçmişteki para korkularını aşmış, parayı serbest bırakarak daha cömert ve rahat bir tutum benimsemişsin.",
        "ters_simdi": "Şu an para saçmaya, kontrolsüz harcamalar yapmaya ya da elindekileri kaybetmeye başlıyorsun.",
        "ters_gelecek": "Gelecekte maddi açıdan savurganlıklar yüzünden ani borçlanma riskleriyle karşılaşabilirsin."
    },
    69: {
        "isim": "TILSIM BEŞLİSİ (FIVE OF PENTACLES)",
        "duz_gecmis": "Geçmişte maddi sıkıntılar, yoksulluk psikolojisi, yalnızlık ve soğuk dış etkenler yüzünden çok zor günlerden geçmişsin.",
        "duz_simdi": "Şu an kendini maddi ve manevi anlamda yapayalnız, desteksiz ve krizde hissediyor olabilirsin.",
        "duz_gelecek": "Gelecekte bu maddi/manevi kriz aşılacak ancak yaşadığın bu zor deneyim sana çok şey öğretecek.",
        "ters_gecmis": "Geçmişteki o yokluk ve kriz döneminden çıkılmış, yardımların gelmesiyle yaralar sarılmaya başlanmış.",
        "ters_simdi": "Şu an krizin en karanlık yeri geride kalıyor; yavaş yavaş toparlanma ve şifa bulma ışığı görünüyor.",
        "ters_gelecek": "Gelecekte maddi yardımlar ve doğru destekler sayesinde finansal istikrara yeniden kavuşacaksın."
    },
    70: {
        "isim": "TILSIM ALTILISI (SIX OF PENTACLES)",
        "duz_gecmis": "Geçmişte cömertlik yapmış, ihtiyacı olana yardım etmiş ya da hak ettiğin maddi desteği başkalarından görmüşsün.",
        "duz_simdi": "Şu an gelir-gider dengesinde adil bir paylaşım içindesin; hem alıyor hem de hak edenlere veriyorsun.",
        "duz_gelecek": "Gelecekte beklediğin maddi yardımlar, burslar veya hak ettiğin finansal destekler cömertçe sana sunulacak.",
        "ters_gecmis": "Geçmişte karşılıksız yardımlar suistimal edilmiş, borç alıp verme dengesi bozulduğu için sorunlar çıkmış.",
        "ters_simdi": "Şu an ya paranı kötü niyetli kişilere kaptırıyor ya da hak ettiğin desteği alamıyorsun.",
        "ters_gelecek": "Gelecekte borç ilişkilerinde yaşanabilecek haksızlıklara ve parasal suiistimallere dikkat etmelisin."
    },
    71: {
        "isim": "TILSIM YEDİLİSİ (SEVEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte ektiğin tohumların ve yaptığın yatırımların büyümesini sabırla ve uzun süre bekleyerek izlemişsin.",
        "duz_simdi": "Şu an yaptıklarının meyve verip vermediğini sorguluyor, sabırla hasat zamanını bekliyorsun.",
        "duz_gelecek": "Gelecekte uzun vadeli emeklerinin karşılığını nihayet maddi ve somut olarak almaya başlayacaksın.",
        "ters_gecmis": "Geçmişte sabırsızlık gösterilmiş, verilen emeğin karşılığı alınamadan projeler yarıda bırakılmış.",
        "ters_simdi": "Şu an harcadığın emeklerin boşa gittiğini düşünerek büyük bir sabırsızlık ve hayal kırıklığı yaşıyorsun.",
        "ters_gelecek": "Gelecekte yanlış yatırımlar ve sabırsızlık yüzünden verdiğin emeklerin karşılığını alamama riski var."
    },
    72: {
        "isim": "TILSIM SEKİZLİSİ (EIGHT OF PENTACLES)",
        "duz_gecmis": "Geçmişte işine dört elle sarılmış, el becerini ve ustalığını geliştirmek için azimle çalışmışsın.",
        "duz_simdi": "Şu an ince işçilik gerektiren projelerle uğraşıyor, detaylara odaklanarak mesleğinde ustalaşıyorsun.",
        "duz_gelecek": "Gelecekte iş disiplinin sayesinde kariyerinde aranan usta bir isim olacak ve emeğinin karşılığını alacaksın.",
        "ters_gecmis": "Geçmişte kalitesiz işler yapılmış, tembellik ve motivasyon eksikliği başarıyı engellemiş.",
        "ters_simdi": "Şu an işine odaklanamıyor, rutin işlerten sıkılıyor ve kaliteden ödün veriyorsun.",
        "ters_gelecek": "Gelecekte iş disiplinsizliği ve odaklanma sorunları yüzünden kariyerinde geride kalabilirsin."
    },
    73: {
        "isim": "TILSIM DOKUZLUSU (NINE OF PENTACLES)",
        "duz_gecmis": "Geçmişte bağımsızlığını ilan etmiş, finansal özgürlüğünü kazanarak lüks ve konfor içinde keyifli bir hayat kurmuşsun.",
        "duz_simdi": "Şu an kendi ayakları üzerinde duran, zenginliğin, lüksün ve kendi emeğinin tadını çıkaran huzurlu bir konumdasın.",
        "duz_gelecek": "Gelecekte maddi özgürlüğün zirvesinde, keyif dolu, konforlu ve kimseye muhtaç olmadığın bir hayat seni bekliyor.",
        "ters_gecmis": "Geçmişte maddi kayıplar yaşanmış, sahte lüks yaşamlar yüzünden borç batağına sürüklenilmiş.",
        "ters_simdi": "Şu an dışarıdan iyi görünsen de içten içe finansal güvencesizlik ve maddi kayıp korkusu yaşıyorsun.",
        "ters_gelecek": "Gelecekte aşırı masraflar ve sahte gösterişler yüzünden parasal sıkıntılar kapını çalabilir."
    },
    74: {
        "isim": "TILSIM ONLUSU (TEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte aile serveti, kalıcı refah, mülk edinme ve nesiller boyu sürecek maddi bir miras kurulmuş.",
        "duz_simdi": "Şu an aile içinde büyük bir maddi refah, mülk sahipliği ve kalıcı güvence altındasın.",
        "duz_gelecek": "Gelecekte tapu, miras, aile şirketi veya ömür boyu sürecek kalıcı bir maddi zenginlik seni bekliyor.",
        "ters_gecmis": "Geçmişte miras kavgaları, aile içi maddi krizler ve iflas durumları büyük yıkımlar yaratmış.",
        "ters_simdi": "Şu an aile içinde para yüzünden büyük sürtüşmeler ve maddi krizler yaşanıyor.",
        "ters_gelecek": "Gelecekte ailevi mülk anlaşmazlıkları ve ortak paralarda yaşanacak kayıplara karşı uyanık olmalısın."
    },
    75: {
        "isim": "TILSIM PRENSİ (PAGE OF PENTACLES)",
        "duz_gecmis": "Geçmişte eğitim, kariyer veya somut bir para haberi almış, pratik adımlar atmak için dersine çalışmışsın.",
        "duz_simdi": "Şu an yeni bir eğitim, iş teklifi veya somut bir yatırım fırsatını öğrenmek ve hayata geçirmek üzeresin.",
        "duz_gelecek": "Gelecekte kariyerinde veya maddi hayatında çok somut ve umut vad eden fırsat haberi alacaksın.",
        "ters_gecmis": "Geçmişte tembellik, hedefsizlik ve pratikten uzak hayaller yüzünden fırsatlar kaçmış.",
        "ters_simdi": "Şu an odak eksikliğin var; dersine çalışmıyor, fırsatları elinin tersiyle itiyorsun.",
        "ters_gelecek": "Gelecekte tembellik ve hedefsizlik yüzünden maddi anlamda geride kalabilirsin."
    },
    76: {
        "isim": "TILSIM ŞÖVALYESİ (KNIGHT OF PENTACLES)",
        "duz_gecmis": "Geçmişte yavaş ama yavaş olduğu kadar emin, güvenilir ve istikrarlı adımlarla hedeflerine yürümüşsün.",
        "duz_simdi": "Şu an işleri ağırta alıyor ama çok sağlam yapıyorsun; rutine sadık kalmak en güvenli yoldur.",
        "duz_gelecek": "Gelecekte istikrarlı ve güvenilir çalışmalarının meyvesini garantici bir şekilde toplayacaksın.",
        "ters_gecmis": "Geçmişte aşırı rutine bağlanmak, tembellik, duraklama dönemi ve işlerin hiç ilerlememesi can sıkmış.",
        "ters_simdi": "Şu an işler tamamen durma noktasında; aşırı inatçı ve hantalsın, hiçbir adım atmıyorsun.",
        "ters_gelecek": "Gelecekte değişime direnç göstermek ve hantallık yüzünden fırsatları kaçırabilirsin."
    },
    77: {
        "isim": "TILSIM KRALİÇESİ (QUEEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte ayakları yere basan, güvenilir, bereketli, doğayı seven ve evini koruyan çok anaç/başarılı bir kadın figürüyle karşılaşmışsın.",
        "duz_simdi": "Şu an maddi ve manevi olarak oldukça güvenli, bereketli ve etrafına kol kanat geren bir pozisyondasın.",
        "duz_gelecek": "Gelecekte hayatına maddi açıdan güçlü, eli açık, güvenilir ve huzur veren bir kadın dahil olacak.",
        "ters_gecmis": "Geçmişte aşırı maddi hırslar, materyalizm, evine ve paraya aşırı bağımlı kaprisli tutumlar huzursuzluk yaratmış.",
        "ters_simdi": "Şu an paraya veya maddiyata çok fazla odaklanmış, ruhsal olarak kendini güvensiz hissediyorsun.",
        "ters_gelecek": "Gelecekte maddi kaygıların esiri olmamak ve cimrilik tuzaklarına düşmemek için dikkatli olmalısın."
    },
    78: {
        "isim": "TILSIM KRALI (KING OF PENTACLES)",
        "duz_gecmis": "Geçmişte iş dünyasında çok zengin, başarılı, güvenilir ve imparatorluk kurmuş bir erkek figüründen büyük destek almışsın.",
        "duz_simdi": "Şu an finansal imparatorluğunu kurma, parasal konularda tam yetki sahibi olma ve güven verme zamanındasın.",
        "duz_gelecek": "Gelecekte işinde zirveye çıkacağın, maddi zenginliğe ve büyük bir finansal güvenceye ulaşacağın bir dönem seni bekliyor.",
        "ters_gecmis": "Geçmişte açgözlülük, riskli yatırımlar, parayı kötü kullanan ve güven sarsan zorba zenginler zarar vermiş.",
        "ters_simdi": "Şu an maddi konularda aşırı risk alıyor ya da parayı her şeyin üstünde tutarak hata yapıyorsun.",
        "ters_gelecek": "Gelecekte yanlış yatırımlar ve açgözlülük yüzünden büyük maddi risklerle karşılaşabilirsin."
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
