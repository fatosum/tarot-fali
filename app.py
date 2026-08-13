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
        "duz_gecmis": "Geçmişte iç sesine kulak verdiğin, sırları sezdiğin ve dış dünyadan uzaklaşıp tamamen kendi iç bilgeliğine sığındığın bir dönem geçirdin.",
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
        "ters_gecmis": "Geçmişte aşırı baskıcı, zorba veya kontrolcü tutumların çevrendeki insanlarla çatışmalara yol açmış.",
        "ters_simdi": "Şu an ya hayatındaki otorite figürlerinin baskısıyla eziliyor ya da kendi diktatörce tavırlarınla çevreni boğuyorsun.",
        "ters_gelecek": "Gelecekte kuralların yıkılması, disiplinsizlik ve gücü kötüye kullanmaktan doğan büyük krizlerle karşılaşabilirsin."
    },
    6: {
        "isim": "HİEROFANT (THE HIEROPHANT)",
        "duz_gecmis": "Geçmişte geleneksel değerlere bağlı kalmış, ruhsal rehberlerden feyz almış ve toplumsal kurallara uyum sağlamışsın.",
        "duz_simdi": "Şu an doğru bildiğin inanç sistemine, toplumsal normlara ve kurallara bağlı kalman gereken bir süreçtesin.",
        "duz_gelecek": "Gelecekte resmi bir anlaşma, evlilik veya topluluk içinde saygınlık kazandıracak kurumsal bir yapıya adım atacaksın.",
        "ters_gecmis": "Geçmişte körü körüne dayatılan kurallara isyan etmiş ya da yanlış dogmalardan dolayı zarar görmüşsün.",
        "ters_simdi": "Şu sıralar gelenekleri yıkma, toplumsal baskılara karşı çıkma veya yanlış bir inanç sisteminin kurbanı olma eğilimindesin.",
        "ters_gelecek": "Gelecekte dogmatik düşünceler yüzünden çevrenle ters düşebilir, yanlış yönlendirilmiş kurallarla kısıtlanabilirsin."
    },
    7: {
        "isim": "AŞIKLAR (THE LOVERS)",
        "duz_gecmis": "Geçmişte hayatını kökten değiştiren önemli bir ilişki ya da değerler arasında kritik bir seçim yapmışsın.",
        "duz_simdi": "Şu an kalbinle mantığın arasında kaldığın bir karar aşamasındasın veya hayatında derin bir uyum/bağlantı var.",
        "duz_gelecek": "Gelecekte hayatının yönünü belirleyecek kalıcı bir ortaklık, aşk veya ruhsal bir bütünleşme seni bekliyor.",
        "ters_gecmis": "Geçmişte yanlış bir seçim yapmış, kalbini kırmış ya da ilişkilerde uyumsuzluklar ve değer çatışmaları yaşamışsın.",
        "ters_simdi": "Şu an kararsızlıklar, yanlış ilişkiler veya içsel değerlerinle çelişen bir seçim yapma baskısı altındasın.",
        "ters_gelecek": "Gelecekte yanlış ortaklıklar, güvensizlikler veya yanlış tercihlerden ötürü pişmanlıklar kapını çalabilir."
    },
    8: {
        "isim": "SAVAŞ ARABASI (THE CHARIOT)",
        "duz_gecmis": "Geçmişte büyük bir irade ve kararlılık göstererek tüm engelleri aşmış, hedefine zaferle ulaşmışsın.",
        "duz_simdi": "Şu an hayatının dizginlerini eline alma, odaklanma ve rakiplerine karşı kararlı bir zafer kazanma zamanındasın.",
        "duz_gelecek": "Gelecekte seyahatler, büyük başarılar ve hayatının kontrolünü tamamen ele alacağın parlak bir dönem seni bekliyor.",
        "ters_gecmis": "Geçmişte kontrolü kaybetmiş, yönsüz kalmış ya da aceleci hırslar yüzünden yolda kalmışsın.",
        "ters_simdi": "Şu sıralar olaylar kontrolden çıkıyor; acelecilik ve yönsüzlük yüzünden nereye koştuğunu bilemez haldesin.",
        "ters_gelecek": "Gelecekte yön bilmezlik, disiplinsizlik ve kontrolsüz güç kullanımı büyük kazalara veya başarısızlıklara yol açabilir."
    },
    9: {
        "isim": "GÜÇ (STRENGTH)",
        "duz_gecmis": "Geçmişte içsel cesaretin, sabırlı tavrın ve şefkatinle en zorlu tutkuları ve korkuları bile sakinleştirmeyi başarmışsın.",
        "duz_simdi": "Şu an kaba kuvvetle değil, tamamen özgüven, sabır ve tatlı dille üstesinden gelebileceğin bir sınavdasın.",
        "duz_gelecek": "Gelecekte içsel gücünü tam anlamıyla keşfedecek, her türlü zorluğu zarif ve dirençli duruşunla alt edeceksin.",
        "ters_gecmis": "Geçmişte özgüven eksikliği yaşamış, içindeki öfkeyi bastıramamış ya da zayıflık hissine yenik düşmüşsün.",
        "ters_simdi": "Şu an enerjinin tükendiğini hissediyor, sabırsızlık ve içsel korkular yüzünden kendine olan inancını yitiriyorsun.",
        "ters_gelecek": "Gelecekte sabırsızlık, özgüven kaybı ve dürtüleri kontrol edememekten kaynaklanan pişmanlıklar yaşayabilirsin."
    },
    10: {
        "isim": "ERMİŞ (THE HERMIT)",
        "duz_gecmis": "Geçmişte kalabalıklardan uzaklaşıp kendi içine dönmüş, ruhsal bir arayışa girerek derin bir bilgelik kazanmışsın.",
        "duz_simdi": "Şu an dış dünyayı sessize alıp kendi iç sesine kulak vermen, yalnızlaşarak hayatını ve yolunu sorgulaman gereken bir dönemdesin.",
        "duz_gelecek": "Gelecekte aradığın aydınlanmaya ulaşacak, kendi iç ışığınla başkalarına da yol gösterecek bir olgunluğa erişeceksin.",
        "ters_gecmis": "Geçmişte aşırı izolasyon yaşamış, dünyadan kopmuş ya da yalnızlık korkusuyla yanlış ortamlara sığınmışsın.",
        "ters_simdi": "Şu sıralar çevrenden tamamen kopuk, depresif bir yalnızlık içinde kaybolmuş veya iç sesini duyamaz haldesin.",
        "ters_gelecek": "Gelecekte aşırı yalnızlık, paranoya veya insanlardan tamamen kopmaktan ötürü yaşanacak yabancılaşma tehlikesi var."
    },
    11: {
        "isim": "KADER ÇARKI (WHEEL OF FORTUNE)",
        "duz_gecmis": "Geçmişte hayatında ani ve dönüştürücü döngüler yaşamış, kaderin sana sunduğu sürpriz fırsatları yakalamışsın.",
        "duz_simdi": "Şu an çarkın senin lehine döndüğü, şansın ve ilahi zamanlamanın hayatında aktif rol oynadığı bir dönüm noktasındasın.",
        "duz_gelecek": "Gelecekte hayatında yepyeni bir döngü başlayacak; şans kapını çalacak ve işler lehine hızla değişecek.",
        "ters_gecmis": "Geçmişte talihsizlikler silsilesi yaşamış, kötü bir zamanlamanın kurbanı olmuş ve kontrol dışı olaylarla sarsılmışsın.",
        "ters_simdi": "Şu sıralar işlerin ters gittiğini, şansın senden yana olmadığını hissediyor ve döngüyü kırmakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte kötü alışkanlıkları devam ettirdiğin sürece aynı kısır döngüleri tekrar yaşama riskin yüksek."
    },
    12: {
        "isim": "ADALET (JUSTICE)",
        "duz_gecmis": "Geçmişte verdiğin tüm kararlarda dürüstlüğü, hakkaniyeti ve sorumluluk bilincini ön planda tutmuşsun.",
        "duz_simdi": "Şu an hayatında dengeyi kurma, adil olma ve geçmişteki eylemlerinin sonuçlarıyla yüzleşme zamanındasın.",
        "duz_gelecek": "Gelecekte hukuki veya resmi konularda hak ettiğin adaleti bulacak, temiz ve dengeli bir sayfa açacaksın.",
        "ters_gecmis": "Geçmişte adaletsizliğe uğramış ya da haksız kararlar alarak başkalarının hakkına girmişsin.",
        "ters_simdi": "Şu sıralar hayatında büyük bir dengesizlik var; adaletsiz durumlarla karşılaşıyor ve sorumluluklardan kaçıyorsun.",
        "ters_gelecek": "Gelecekte dürüstlükten uzaklaşmanın bedelini ödeyebilir, mahkemelik veya adaletsiz krizlerle boğuşabilirsin."
    },
    13: {
        "isim": "ASILMIŞ ADAM (THE HANGED MAN)",
        "duz_gecmis": "Geçmişte olaylara bakış açını tamamen değiştirmek için fedakarlıkta bulunmuş ve bir duraklama dönemi yaşamışsın.",
        "duz_simdi": "Şu an elinin kolunun bağlı olduğunu düşündüğün, olayları akışına bırakıp teslim olman gereken bir askıda kalma sürecindesin.",
        "duz_gelecek": "Gelecekte yaşadığın bu fedakarlıklar ve bakış açısı değişimi sayesinde olayları çok daha farklı ve aydınlanmış göreceksin.",
        "ters_gecmis": "Geçmişte gereksiz kurbanlar vermiş, kendini boşuna feda etmiş ve çıkmaz sokaklarda vakit kaybetmişsin.",
        "ters_simdi": "Şu sıralar direndiğin için acı çekiyorsun; kurban psikolojisinden çıkamıyor ve olaylara körü körüne diretiyorsun.",
        "ters_gelecek": "Gelecekte zaman kaybı, boşuna yapılmış fedakarlıklar ve inatçılık yüzünden hayal kırıklığı yaşayabilirsin."
    },
    14: {
        "isim": "ÖLÜM (DEATH)",
        "duz_gecmis": "Geçmişte senin için artık işlevini yitirmiş eski bir dönemi, alışkanlığı ya da ilişkiyi geride bırakıp kökten bir dönüşüm yaşamışsın.",
        "duz_simdi": "Şu an eski olanın bitmesi ve yerini yepyeni bir şeye bırakması için acı ama gerekli bir bitiş/kabulleniş sürecindesin.",
        "duz_gelecek": "Gelecekte küllerinden yeniden doğacağın, seni özgürleştirecek devrim niteliğinde bir değişim ve yenilenme kapıda.",
        "ters_gecmis": "Geçmişte bitmesi gereken şeylere sıkıca tutunmuş, değişime direnerek süreci kendi adına kabusa çevirmişsin.",
        "ters_simdi": "Şu sıralar değişimden korkuyor, geçmişin hayaletlerini ve ölmüş ilişkileri canlandırmaya çalışarak direniyorsun.",
        "ters_gelecek": "Gelecekte değişime direnmenin getirdiği ağır durgunluk ve tıkanıklıklar hayatını zorlaştırmaya devam edebilir."
    },
    15: {
        "isim": "DENGE (TEMPERANCE)",
        "duz_gecmis": "Geçmişte zıtlıkları uyum içinde harmanlamış, sabırlı ve ılımlı adımlarla içsel huzuru yakalamışsın.",
        "duz_simdi": "Şu an hayatında şifa bulma, aşırılıklardan kaçınma ve her şeyi dengeleme safhasındasın.",
        "duz_gelecek": "Gelecekte sabrının ve uyumlu tavrının meyvesini alacak, huzurlu ve dengeli bir döneme kavuşacaksın.",
        "ters_gecmis": "Geçmişte aşırılıklara kaçmış, sabırsız davranmış ve hayatındaki dengeyi tamamen altüst etmişsin.",
        "ters_simdi": "Şu sıralar içsel huzurun bozulmuş durumda; uçlarda yaşıyor, sabırsızlık ve uyumsuzlukla mücadele ediyorsun.",
        "ters_gelecek": "Gelecekte aşırılıklar, dengesiz ilişkiler ve sabırsızlık yüzünden büyük iç çatışmalar yaşayabilirsin."
    },
    16: {
        "isim": "ŞEYTAN (THE DEVIL)",
        "duz_gecmis": "Geçmişte toksik bağımlılıklara, maddiyata veya seni esir alan sağlıksız tutkulara kapılmış, bunlarla sınanmışsın.",
        "duz_simdi": "Şu an seni kısıtlayan, kendi ellerinle yarattığın zincirleri ve toksik bağları fark etmen gereken bir yüzleşme anındasın.",
        "duz_gelecek": "Gelecekte bu karanlık bağımlılıklardan tamamen özgürleşecek ve kendi gücünü eline alacaksın.",
        "ters_gecmis": "Geçmişte zincirlerini kırmayı başarmış, toksik bir durumdan veya manipülatif bir kişiden kurtulmuşsun.",
        "ters_simdi": "Şu sıralar zincirlerini koparmak üzere büyük bir farkındalık yaşıyor ya da bağımlılıklarınla mücadele ediyorsun.",
        "ters_gelecek": "Gelecekte yanlış arzulara tekrar kapılma tehlikesi var; kendi içindeki karanlıkla yüzleşmen şart."
    },
    17: {
        "isim": "YIKILAN KULE (THE TOWER)",
        "duz_gecmis": "Geçmişte yalan temeller üzerine kurulu her şeyin ani bir darbeyle yıkıldığı büyük bir şok ve kriz dönemi atlatmışsın.",
        "duz_simdi": "Şu an hayatında taş üstünde taş bırakmayan ani bir sarsıntı, gerçeklerin ortaya dökülmesiyle yaşanan büyük bir uyanıştasın.",
        "duz_gelecek": "Gelecekte çürümüş yapılar tamamen yıkılacak ve yerini çok daha sağlam, gerçekçi bir düzene bırakacak.",
        "ters_gecmis": "Geçmişte felaketin eşiğinden kıl payı dönmüş ya da büyük bir yıkımı ertelemek için çaba sarf etmişsin.",
        "ters_simdi": "Şu sıralar yaklaşan bir fırtınanın korkusunu yaşıyor ya da kaçınılmaz bir yıkımı engellemeye çalışıyorsun.",
        "ters_gelecek": "Gelecekte ertelediğin o büyük patlama veya kriz kaçınılmaz olarak kapını çalabilir, hazırlıklı olmalısın."
    },
    18: {
        "isim": "YILDIZ (THE STAR)",
        "duz_gecmis": "Geçmişte yaşadığın onca karanlık ve fırtınanın ardından derin bir şifa bulmuş, umutla yeniden dolmuşsun.",
        "duz_simdi": "Şu an geleceğe dair inancının tazelendiği, ilahi bir koruma altında olduğun ve ilham dolu bir huzur dönemindesin.",
        "duz_gelecek": "Gelecekte hayallerinin gerçeğe dönüştüğü, parlak, şanslı ve ruhsal olarak tatmin edici günler seni bekliyor.",
        "ters_gecmis": "Geçmişte umutsuzluğa kapılmış, inancını yitirmiş ve geleceğe dair karanlık senaryolar kurmuşsun.",
        "ters_simdi": "Şu sıralar motivasyonun düşük; kendine olan inancını yitiriyor ve hayallerinin gerçekleşmeyeceğine inanıyorsun.",
        "ters_gelecek": "Gelecekte karamsarlık ve fırsatları görememek yüzünden elindeki güzel şansları tepebilirsin."
    },
    19: {
        "isim": "AY (THE MOON)",
        "duz_gecmis": "Geçmişte korkularla, kuruntularla ve arkandan dönen sinsi işlerle, belirsizliklerle dolu kaygılı bir dönem geçirmişsin.",
        "duz_simdi": "Şu an ortalığın sisli olduğu, hiçbir şeyin göründüğü gibi çıkmayabileceği, sezgilerine güvenmen gereken bir illüzyon sürecindesin.",
        "duz_gelecek": "Gelecekte tüm sırlar açığa çıkacak, sis perdesi aralanacak ve korkularının aslında sadece birer kuruntu olduğunu göreceksin.",
        "ters_gecmis": "Geçmişte korkularının üzerine gitmiş, kuruntuları yenmiş ve karanlık bir sis perdesini arkanda bırakmışsın.",
        "ters_simdi": "Şu sıralar zihnindeki kaygılar ve paranoyalar azalmaya başlıyor, gerçeklerle yüzleşmeye başlıyorsun.",
        "ters_gelecek": "Gelecekte zihinsel karmaşa ve gizli düşmanlıkların etkisi tamamen dağılacak, aydınlığa çıkacaksın."
    },
    20: {
        "isim": "GÜNEŞ (THE SUN)",
        "duz_gecmis": "Geçmişte neşe, başarı, canlılık ve her türlü engeli aşarak büyük bir mutluluk yakaladığın harika bir dönem yaşamışsın.",
        "duz_simdi": "Şu an hayatında her şeyin yolunda gittiği, enerjinin, neşenin ve başarıların dorukta olduğu muazzam bir aydınlıktasın.",
        "duz_gelecek": "Gelecekte seni adeta güneş gibi parlatacak, tüm üzüntüleri unutturacak büyük başarılar ve mutluluklar var.",
        "ters_gecmis": "Geçmişte geçici mutsuzluklar, neşenin sönmesi veya başarıların gölgelenmesi gibi durumlar yaşamışsın.",
        "ters_simdi": "Şu an içindeki neşe biraz sönük kalmış olabilir; olayların olumsuz yönlerine odaklanarak ışığını kapatıyorsun.",
        "ters_gelecek": "Gelecekte geçici engeller neşeni biraz gölgeleyebilir ancak bu durum uzun sürmeyecek, sabırlı olmalısın."
    },
    21: {
        "isim": "MAHKEME (JUDGEMENT)",
        "duz_gecmis": "Geçmişte hayatınla ilgili büyük bir muhasebe yapmış, eski hatalardan ders çıkarıp adeta yeniden doğmuşsun.",
        "duz_simdi": "Şu an hayatının çağrısına kulak verme, geçmişin hesaplarını kapatma ve ilahi bir uyanış yaşama zamanındasın.",
        "duz_gelecek": "Gelecekte hak ettiğin ödülü alacağın, hayatında yepyeni ve tertemiz bir kulvara geçeceğin ilahi bir karar anı seni bekliyor.",
        "ters_gecmis": "Geçmişte hatalarını kabul etmekten kaçınmış, suçluluk duygularına takılıp kalmış ve kararları ertelemişsin.",
        "ters_simdi": "Şu sıralar öz eleştiri yapmaktan kaçınıyor, geçmişin pişmanlıklarıyla kendini hırpalıyor ve kararsızlık yaşıyorsun.",
        "ters_gelecek": "Gelecekte kaçındığın yüzleşmeler ve bitmeyen pişmanlıklar karşına tekrar çıkabilir, hesaplaşma zamanı."
    },
    22: {
        "isim": "DÜNYA (THE WORLD)",
        "duz_gecmis": "Geçmişte uzun soluklu bir yolculuğu, projeyi veya hayat evresini büyük bir başarı ve bütünlükle tamamlamışsın.",
        "duz_simdi": "Şu an büyük bir çemberin tamamlandığı, huzurun, tatminin ve adeta zirvede hissetmenin tadını çıkardığın muhteşem bir andasın.",
        "duz_gelecek": "Gelecekte tüm hedeflerine ulaşacak, hayatının en büyük başarılarından birini kutlayarak taçlandırılacaksın.",
        "ters_gecmis": "Geçmişte bir şeyleri yarım bırakmış, tam hedefe ulaşacakken son anda engellerle karşılaşmışsın.",
        "ters_simdi": "Şu sıralar bir şeyleri bitirmekte zorlanıyor, son adımı atamadığın için bir tıkanıklık hissi yaşıyorsun.",
        "ters_gelecek": "Gelecekte eksik kalan işler tamamlanana kadar küçük gecikmeler yaşayabilirsin, pes etmemelisin."
    },
    23: {
        "isim": "ASA ASI (ACE OF WANDS)",
        "duz_gecmis": "Geçmişte içini kıpır kıpır eden harika bir ilham, yaratıcı kıvılcım ve yeni bir tutku dalgası yakalamışsın.",
        "duz_simdi": "Şu an elinde müthiş bir yaratıcı enerji ve eyleme geçme isteği var; fırsatları değerlendirmek için harika bir gündesin.",
        "duz_gelecek": "Gelecekte hayatında büyük bir heyecan yaratacak yepyeni bir girişim veya tutkulu bir proje kapını çalacak.",
        "ters_gecmis": "Geçmişte enerjin düşükmüş, yaratıcı tıkanıklıklar yaşamış ve hevesin kursağında kalmış.",
        "ters_simdi": "Şu sıralar motivasyon eksikliği ve yanlış adımlar yüzünden içindeki o coşkulu ateşi yakmakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte ertelenen projeler ve sönen hevesler yüzünden hayal kırıklığı yaşama riskin var."
    },
    24: {
        "isim": "ASA İKİLİSİ (TWO OF WANDS)",
        "duz_gecmis": "Geçmişte geleceğe dair stratejik planlar yapmış, atacağın büyük adımlar için dünyayı ve seçenekleri masaya yatırmışsın.",
        "duz_simdi": "Şu an konfor alanından çıkıp çıkmama kararı aldığın, geleceğini şekillendirecek stratejik bir yol ayrımındasın.",
        "duz_gelecek": "Gelecekte ortaklıklar kurarak ya da yeni ufuklara yelken açarak uzun vadeli planlarını hayata geçireceksin.",
        "ters_gecmis": "Geçmişte yanlış planlamalar yapmış, kararsızlıklar yüzünden elindeki fırsatları ertelemişsin.",
        "ters_simdi": "Şu sıralar geleceğe dair belirsizlikler seni korkutuyor, risk almaktan çekindiğin için yerinde sayıyorsun.",
        "ters_gelecek": "Gelecekte cesaretsizlik ve yanlış stratejiler yüzünden atıl kalma ve pişmanlık yaşama ihtimalin var."
    },
    25: {
        "isim": "ASA ÜÇLÜSÜ (THREE OF WANDS)",
        "duz_gecmis": "Geçmişte attığın tohumların ilk meyvelerini toplamış, ufka umutla bakarak beklediğin adımların sonuçlarını almışsın.",
        "duz_simdi": "Şu an yaptıklarının sonuçlarını beklediğin, vizyonunu genişleterek yeni seyahatler veya girişimler planladığın bir dönemdesin.",
        "duz_gelecek": "Gelecekte işlerinin büyüyeceği, ticari veya kişisel anlamda yeni ufuklara açılacağın çok verimli günler seni bekliyor.",
        "ters_gecmis": "Geçmişte beklentilerin boşa çıkmış, yatırımlarından veya projelerinden umduğun geri dönüşü alamamışsın.",
        "ters_simdi": "Şu sıralar sabırsızlık ve geciken haberler yüzünden hayal kırıklığı yaşıyor, işlerin yavaşlığından yakınıyorsun.",
        "ters_gelecek": "Gelecekte yanlış yönlendirilmiş yatırımlar veya planlardaki aksamalar canını sıkabilir."
    },
    26: {
        "isim": "ASA DÖRTLÜSÜ (FOUR OF WANDS)",
        "duz_gecmis": "Geçmişte evlilik, nişan, kutlama veya huzurlu bir yuva kurma gibi çok mutlu ve coşkulu bir etkinlik yaşamışsın.",
        "duz_simdi": "Şu an sevdiklerinle birlikte kutlama yaptığın, huzurlu, güvenli ve mutlu bir yuva ortamının tadını çıkarıyorsun.",
        "duz_gelecek": "Gelecekte seni ve sevdiklerini bir araya getirecek mutlu bir yuva, düğün veya büyük bir kutlama var.",
        "ters_gecmis": "Geçmişte aile içinde huzursuzluklar, iptal edilen kutlamalar veya yuva kurma yolunda engeller çıkmış.",
        "ters_simdi": "Şu sıralar ev veya aile ortamında geçici gerginlikler yaşanıyor, uyumu yakalamakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte ailevi anlaşmazlıklar veya kutlamalarda çıkabilecek pürüzler neşeni biraz gölgeleyebilir."
    },
    27: {
        "isim": "ASA BEŞLİSİ (FIVE OF WANDS)",
        "duz_gecmis": "Geçmişte fikir ayrılıkları, rekabet ortamı ve kimin haklı olduğunu kanıtlamaya çalıştığın çekişmeli bir mücadele vermişsin.",
        "duz_simdi": "Şu an etrafındaki insanlarla çıkar çatışmaları, fikir uyuşmazlıkları ve yoğun bir rekabet ortamı içindesin.",
        "duz_gelecek": "Gelecekte seni zorlayacak tartışmalar ve güç savaşlarıyla karşılaşabilirsin, sabırlı olmalısın.",
        "ters_gecmis": "Geçmişte gereksiz kavgalardan kaçınmış, tartışmaları ustalıkla bastırıp uzlaşma sağlamışsın.",
        "ters_simdi": "Şu sıralar çatışmaları yatıştırmaya çalışıyor, kaosu bitirmek için ortak bir yol bulmaya çabalıyorsun.",
        "ters_gelecek": "Gelecekte inatlaşmaları bir kenara bırakıp uzlaşmayı seçtiğin sürece krizleri rahatça atlatacaksın."
    },
    28: {
        "isim": "ASA ALTILISI (SIX OF WANDS)",
        "duz_gecmis": "Geçmişte büyük bir başarı elde etmiş, rakiplerini geride bırakarak zafer çelengini gururla taşımışsın.",
        "duz_simdi": "Şu an emeklerinin takdir edildiği, başarılarının kutlandığı ve haklı bir gurur yaşadığın parlak bir dönemdesin.",
        "duz_gelecek": "Gelecekte adını duyuracağın büyük bir başarı, terfi veya toplumsal bir zafer seni bekliyor.",
        "ters_gecmis": "Geçmişte başarıya çok yaklaşmışken destek görmemiş, zaferin elinden kayıp gittiğini görmüşsün.",
        "ters_simdi": "Şu sıralar hak ettiğin değeri görmediğini düşünüyor, takdir edilmemekten dolayı bir özgüven sarsıntısı yaşıyorsun.",
        "ters_gelecek": "Gelecekte kibirli tavırlar veya yanlış adımlar yüzünden kazanılmış zaferleri kaybetme riski doğabilir."
    },
    29: {
        "isim": "ASA YEDİLİSİ (SEVEN OF WANDS)",
        "duz_gecmis": "Geçmişte haklarını, pozisyonunu ve sevdiklerini korumak için tek başına büyük bir direniş göstermişsin.",
        "duz_simdi": "Şu an etrafından gelen eleştirilere ve baskılara karşı kendi alanını ve doğrularını savunma mücadelesindesin.",
        "duz_gelecek": "Gelecekte rakiplerine karşı dik durmaya devam edecek ve zorluklar karşısında pozisyonunu korumayı başaracaksın.",
        "ters_gecmis": "Geçmişte baskılara boyun eğmiş, savunmasız kalmış ve haklarını yeterince koruyamamışsın.",
        "ters_simdi": "Şu sıralar tükenmiş hissediyorsun; herkes sana yükleniyor gibi geliyor ve savunma yapmakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte aşırı baskı altında ezilmemek için sınırlarını daha net çizmeyi öğrenmen gerekecek."
    },
    30: {
        "isim": "ASA SEKİZLİSİ (EIGHT OF WANDS)",
        "duz_gecmis": "Geçmişte hayatında her şeyin çok hızlı geliştiği, sürpriz haberler aldığın ve seyahatlerle dolu bir dönem yaşamışsın.",
        "duz_simdi": "Şu an olayların inanılmaz bir hız kazandığı, ardı ardına haberler aldığın ve kararların hızla alındığı bir süreçtesin.",
        "duz_gelecek": "Gelecekte beklenmedik gelişmeler, ani seyahatler ve müjdeli haberler kapını hızla çalacak.",
        "ters_gecmis": "Geçmişte işler sarpa sarmış, beklediğin haberler gecikmiş ve planların askıya alınmış.",
        "ters_simdi": "Şu sıralar iletişimde kopukluklar, yanlış anlamalar ve işlerin yavaşlamasından duyulan bir sabırsızlık var.",
        "ters_gelecek": "Gelecekte acelecilik yüzünden yapılan hatalar ve yanlış zamanlanmış hamleler projelerini aksatabilir."
    },
    31: {
        "isim": "ASA DOKUZLUSU (NINE OF WANDS)",
        "duz_gecmis": "Geçmişte yaşadığın onca zorluk ve mücadele seni yormuş ama aynı zamanda son derece tetikte ve dayanıklı yapmış.",
        "duz_simdi": "Şu an son bir engelin kaldığı, artık yorulduğun ama siper alarak sonuna kadar direnmen gereken bir noktadasın.",
        "duz_gelecek": "Gelecekte son bir kez daha dişini sıkman gerekecek ancak bu direniş seni kalıcı bir zafere götürecek.",
        "ters_gecmis": "Geçmişte paranoyaklaşmış, sürekli saldırı beklemekten dolayı tükenmişlik sendromu yaşamışsın.",
        "ters_simdi": "Şu sıralar aşırı savunmacı ve kuşkucu tavırlar sergiliyor, insanlara karşı güven duvarları örüyorsun.",
        "ters_gelecek": "Gelecekte yersiz korkular ve tükenmişlik yüzünden zaferin eşiğinden dönebilirsin, biraz rahatla."
    },
    32: {
        "isim": "ASA ONLUSU (TEN OF WANDS)",
        "duz_gecmis": "Geçmişte her şeyi tek başına sırtlanmış, aşırı sorumluluklar ve yükler altında ezilmişsin.",
        "duz_simdi": "Şu an omuzlarında dünyanın yükünü taşıyormuş gibi hissediyorsun; artık bazı sorumlulukları bırakma vakti.",
        "duz_gelecek": "Gelecekte bu ağır yüklerin sonuna gelecek, nihayet hafifleyerek ferah bir nefes alacaksın.",
        "ters_gecmis": "Geçmişte bazı yükleri devretmeyi öğrenmiş, sorumlulukları paylaşarak rahatlamışsın.",
        "ters_simdi": "Şu sıralar başkalarının yüklerini de taşıyor ve tükenme noktasına geliyorsun; hayır demeyi öğrenmelisin.",
        "ters_gelecek": "Gelecekte aşırı yüklenmekten kaynaklanan fiziksel ve mental yorgunluklarla yüzleşebilirsin."
    },
    33: {
        "isim": "ASA PRENSİ (PAGE OF WANDS)",
        "duz_gecmis": "Geçmişte yeni fikirlerin peşinden koşan, maceraperest, öğrenmeye aç ve hevesli bir haberci rolü üstlenmişsin.",
        "duz_simdi": "Şu an içindeki coşkuyu ortaya koyacak yeni bir haber, yaratıcı bir fikir veya heyecan verici bir teklif almaktasın.",
        "duz_gelecek": "Gelecekte hayatına renk katacak genç enerjili biri veya yepyeni bir macera teklifi seni bekliyor.",
        "ters_gecmis": "Geçmişte hevesleri çabuk sönen, tutarsız kararlar alan ve odaklanmakta zorlanan biri olmuşsun.",
        "ters_simdi": "Şu sıralar aldığın haberler asılsız çıkabilir veya motivasyonun anlık olarak düşebilir.",
        "ters_gelecek": "Gelecekte aceleci ve tutarsız yaklaşımlar yüzünden başlanan işlerin yarım kalma riski var."
    },
    34: {
        "isim": "ASA ŞÖVALYESİ (KNIGHT OF WANDS)",
        "duz_gecmis": "Geçmişte korkusuzca atıldığın maceralar, seyahatler ve tutkuyla peşinden koştuğun hedefler olmuş.",
        "duz_simdi": "Şu an adeta bir ateş topu gibisin; hızla hareket ediyor, tutkularının peşinden gözü kara koşuyorsun.",
        "duz_gelecek": "Gelecekte ani bir seyahat, tutkulu bir aşk veya macera dolu sürpriz gelişmeler kapını çalacak.",
        "ters_gecmis": "Geçmişte acelecilik ve düşünmeden atılan adımlar yüzünden büyük kazalar ve hayal kırıklıkları yaşamışsın.",
        "ters_simdi": "Şu sıralar sabırsızlığın tavan yapmış durumda; öfkeyle kalkıp zararla oturma riskin çok yüksek.",
        "ters_gelecek": "Gelecekte pervasız ve yıkıcı bir hız yüzünden elindeki fırsatları ziyan edebilirsin."
    },
    35: {
        "isim": "ASA KRALİÇESİ (QUEEN OF WANDS)",
        "duz_gecmis": "Geçmişte karizman, özgüvenin, sıcakkanlılığın ve lider ruhunla çevrene ilham saçmışsın.",
        "duz_simdi": "Şu an son derece çekici, üretken, kendine güvenen ve ne istediğini çok iyi bilen bir duruş sergiliyorsun.",
        "duz_gelecek": "Gelecekte karizman ve liderliğinle projelerin aranan ismi olacak, çevrene ışık saçacaksın.",
        "ters_gecmis": "Geçmişte kıskançlıklar, baskıcı tavırlar veya özgüven problemleri ilişkilerini zedelemiş.",
        "ters_simdi": "Şu sıralar enerjin biraz düşük; manipülatif veya bencil hissedebilir, hırsına yenik düşebilirsin.",
        "ters_gelecek": "Gelecekte otoriteyi yanlış kullanmak ve aşırı ben merkezci olmak çevrendeki insanları uzaklaştırabilir."
    },
    36: {
        "isim": "ASA KRALI (KING OF WANDS)",
        "duz_gecmis": "Geçmişte büyük vizyonlar ortaya koymuş, ilham verici projelere liderlik etmiş ve kararlı bir vizyoner olmuşsun.",
        "duz_simdi": "Şu an işleri yöneten, vizyoner kararlar alan, otoriter ama yapıcı bir lider konumundasın.",
        "duz_gelecek": "Gelecekte büyük bir imparatorluk kuracak güçte projelere liderlik edecek, büyük başarılar elde edeceksin.",
        "ters_gecmis": "Geçmişte zorba, sabırsız ve bencil bir liderlik anlayışı sergileyerek çatışmalara sebep olmuşsun.",
        "ters_simdi": "Şu sıralar çevrendekileri baskı altında tutuyor, kendi bildiğin dışında hiçbir fikre tahammül edemiyorsun.",
        "ters_gelecek": "Gelecekte fevri kararlar ve diktatörce yaklaşımlar kurduğun yapının sarsılmasına neden olabilir."
    },
    37: {
        "isim": "KUPA ASI (ACE OF CUPS)",
        "duz_gecmis": "Geçmişte kalbini açan muazzam bir aşk, ilahi bir sevgi veya duygusal bir taşma dönemi yaşamışsın.",
        "duz_simdi": "Şu an kalbinin pır pır attığı, sevgiye, şefkate ve yeni duygusal başlangıçlara sonuna kadar açık bir dönemdesin.",
        "duz_gelecek": "Gelecekte hayatını güzelleştirecek derin bir aşk, ruhsal tatmin veya mutlu bir haber kapını çalacak.",
        "ters_gecmis": "Geçmişte duygusal tıkanıklıklar yaşamış, kalbini kapatmış ve sevgiyi göstermekte zorlanmışsın.",
        "ters_simdi": "Şu sıralar içsel bir boşluk hissediyor, duygularını bastırıyor veya karşılıksız sevgilerden yoruluyorsun.",
        "ters_gelecek": "Gelecekte duygusal hayal kırıklıkları ve sevgisizlik hissi kalbini bir süre yorabilir."
    },
    38: {
        "isim": "KUPA İKİLİSİ (TWO OF CUPS)",
        "duz_gecmis": "Geçmişte hayatını değiştiren özel bir ortaklık, uyumlu bir ilişki veya ruh eşi bağı kurmuşsun.",
        "duz_simdi": "Şu an biriyle aranızda harika bir uyum, karşılıklı çekim ve kalpten bir anlaşma söz konusu.",
        "duz_gelecek": "Gelecekte uzun soluklu, sevgi dolu bir ilişki veya çok güçlü bir iş ortaklığı seni bekliyor.",
        "ters_gecmis": "Geçmişte ilişkilerde uyumsuzluk, kopukluklar ve karşılıklı yanlış anlamalar yaşanmış.",
        "ters_simdi": "Şu sıralar partnerinle aranızdaki bağda kopukluklar var; dengeyi ve uyumu yeniden kurmanız gerekiyor.",
        "ters_gelecek": "Gelecekte yanlış ortaklıklar veya ilişkilerde bitişler yaşanma ihtimaline karşı dikkatli olmalısın."
    },
    39: {
        "isim": "KUPA ÜÇLÜSÜ (THREE OF CUPS)",
        "duz_gecmis": "Geçmişte dostlarınla bir araya geldiğin, başarıları kutladığın neşeli ve keyifli partiler yaşamışsın.",
        "duz_simdi": "Şu an arkadaşlarınla sosyalleştiğin, kutlamalar yaptığın ve keyifli vakit geçirdiğin neşeli bir dönemdesin.",
        "duz_gelecek": "Gelecekte kutlamalar, düğünler veya dostlarla bir araya gelerek neşe depolayacağın anlar var.",
        "ters_gecmis": "Geçmişte dedikodular, dost kazıkları veya aşırı sosyalleşmekten tükenme durumları yaşanmış.",
        "ters_simdi": "Şu sıralar sosyal çevrende bazı anlaşmazlıklar veya dışlanma hissi gibi durumlar canını sıkabilir.",
        "ters_gelecek": "Gelecekte yanlış dostluklar ve dedikodular huzurunu kaçırabilir, çevrene dikkat etmelisin."
    },
    40: {
        "isim": "KUPA DÖRTLÜSÜ (FOUR OF CUPS)",
        "duz_gecmis": "Geçmişte önüne sunulan fırsatları beğenmemiş, tatminsizlik ve içe kapanıklıkla vakit geçirmişsin.",
        "duz_simdi": "Şu an her şeyim var ama mutsuzum ruh halindesin; önündeki fırsatları görmezden gelerek küskün duruyorsun.",
        "duz_gelecek": "Gelecekte bu apatiden sıyrılacak ve göz ardı ettiğin yeni bir fırsatı nihayet fark edeceksin.",
        "ters_gecmis": "Geçmişte içine kapanık dönemi geride bırakmış, hayata yeniden motive olmayı başarmışsın.",
        "ters_simdi": "Şu sıralar kabuğundan çıkmaya başlıyor, ilgisizliğin yerini yavaş yavaş merak duygusuna bırakıyor.",
        "ters_gelecek": "Gelecekte fırsatları kaçırmamak için biraz daha uyanık olmalı ve hayata küsmemelisin."
    },
    41: {
        "isim": "KUPA BEŞLİSİ (FIVE OF CUPS)",
        "duz_gecmis": "Geçmişte dökülen sütlere ağlamış, kaybettiklerinin yasını tutarak kalbini bir süre üzüntüye teslim etmişsin.",
        "duz_simdi": "Şu an geçmişte kalan hayal kırıklıklarına odaklanmış, elinde kalanları görmezden gelerek hüzün yaşayorsun.",
        "duz_gelecek": "Gelecekte yas döneminin sonuna gelecek ve arkana değil, arkada kalanların dışındaki dolu bardaklara bakacaksın.",
        "ters_gecmis": "Geçmişte yas sürecini tamamlamış, affetmiş ve hayata yeniden umutla bakmaya başlamışsın.",
        "ters_simdi": "Şu sıralar yavaş yavaş üzüntüden sıyrılıyor, geçmişin yükünü hafifleterek kabullenmeye geçiyorsun.",
        "ters_gelecek": "Gelecekte eski defterleri tamamen kapatıp geçmişin acılarından arınarak özgürleşeceksin."
    },
    42: {
        "isim": "KUPA ALTILISI (SIX OF CUPS)",
        "duz_gecmis": "Geçmişte çocukluk anıları, eski dostlar veya nostaljik güzellikler hayatında çok önemli bir yer tutmuş.",
        "duz_simdi": "Şu an geçmişten gelen güzel hatıralar, eski bir tanıdık veya saf bir nostalji rüzgarı esiyor.",
        "duz_gelecek": "Gelecekte geçmişten biriyle yeniden karşılaşabilir ya da hayatına çocuksu bir neşe ve masumiyet dönebilir.",
        "ters_gecmis": "Geçmişe çok fazla takılıp kalmış, bugünü yaşayamayarak nostaljinin esiri olmuşsun.",
        "ters_simdi": "Şu sıralar geçmişteki anılara takılıp kalmaktan anı kaçırıyor veya eski travmaları bugüne taşıyorsun.",
        "ters_gelecek": "Gelecekte geçmişin hayaletlerinden kurtulup geleceğe odaklanman gereken durumlar oluşacak."
    },
    43: {
        "isim": "KUPA YEDİLİSİ (SEVEN OF CUPS)",
        "duz_gecmis": "Geçmişte hayal aleminde yaşamış, gerçekçi olmayan seçenekler ve illüzyonlar arasında kaybolmuşsun.",
        "duz_simdi": "Şu an önünde pek çok seçenek var ama hangisinin gerçek hangisinin hayal olduğunu seçmekte zorlanıyorsun.",
        "duz_gelecek": "Gelecekte hayaller ile gerçekler arasında bir seçim yapacak ve ayakların yere basmaya başlayacak.",
        "ters_gecmis": "Geçmişte hayallerden uyanmış, net ve gerçekçi kararlar alarak odağını bulmuşsun.",
        "ters_simdi": "Şu sıralar illüzyonlar dağılıyor; artık hayalperestlikten çıkıp gerçeklerle yüzleşiyorsun.",
        "ters_gelecek": "Gelecekte yanlış hayallerin peşinden koşarak vakit kaybetmeme bilincine erişeceksin."
    },
    44: {
        "isim": "KUPA SEKİZLİSİ (EIGHT OF CUPS)",
        "duz_gecmis": "Geçmişte artık sana ruhsal olarak yetmeyen bir durumu, ilişkiyi veya ortamı arkanda bırakıp yola çıkmışsın.",
        "duz_simdi": "Şu an seni tatmin etmeyen şeyleri terk ediyor, daha yüksek bir anlam aramak için yola koyuluyorsun.",
        "duz_gelecek": "Gelecekte ruhsal olarak seni beslemeyen her şeyi geride bırakıp yeni bir arayışa ve yolculuğa çıkacaksın.",
        "ters_gecmis": "Geçmişte gitmen gereken yerden ayrılamamış, korku yüzünden mutsuz bir düzende kalmışsın.",
        "ters_simdi": "Şu sıralar gitmekle kalmak arasında sıkışıp kalmışsın; cesaretini toplamakta zorlanıyorsun.",
        "ters_gelecek": "Gelecekte korkuları yenip nihayet sana zarar veren o yapıyı arkanda bırakmayı başaracaksın."
    },
    45: {
        "isim": "KUPA DOKUZLUSU (NINE OF CUPS)",
        "duz_gecmis": "Geçmişte dileklerin kabul olmuş, keyfin, huzurun ve kişisel tatminin doruklarında bir dönem yaşamışsın.",
        "duz_simdi": "Şu an isteklerinin gerçekleştiği, 'dilek kartı' denilen, son derece mutlu ve tatmin dolu bir andasın.",
        "duz_gelecek": "Gelecekte yüzünü güldürecek, kalbini tatmin edecek harika dileklerin gerçeğe dönüştüğünü göreceksin.",
        "ters_gecmis": "Geçmişte doyumsuzluk yaşamış, elde ettiklerinin kıymetini bilemeyerek mutsuzluk üretmişsin.",
        "ters_simdi": "Şu sıralar içsel bir tatminsizlik var; her şeyim var ama sanki eksik bir şeyler var diyorsun.",
        "ters_gelecek": "Gelecekte açgözlülükten kaçındığın sürece sahip olduğun mutluluğun kıymetini daha iyi anlayacaksın."
    },
    46: {
        "isim": "KUPA ONLUSU (TEN OF CUPS)",
        "duz_gecmis": "Geçmişte huzurlu aile ortamı, mutlu bir evlilik ve ruhsal olarak tam bir tatmin bulduğun limana ulaşmışsın.",
        "duz_simdi": "Şu an hayatında her şeyin uyum içinde olduğu, sevdiklerinle birlikte tam anlamıyla cenneti yaşadığın bir dönemdesin.",
        "duz_gelecek": "Gelecekte ömür boyu sürecek mutlu bir aile hayatı, huzur ve kalıcı bir mutluluk seni bekliyor.",
        "ters_gecmis": "Geçmişte aile içi huzursuzluklar, dağılmış yuvalar veya sahte mutluluklar tecrübe edilmiş.",
        "ters_simdi": "Şu sıralar aile veya yakın çevre ilişkilerinde geçici soğukluklar ve uyumsuzluklar yaşanabilir.",
        "ters_gelecek": "Gelecekte evdeki huzuru yeniden tesis etmek için biraz fedakarlık yapman gerekebilir."
    },
    47: {
        "isim": "KUPA PRENSİ (PAGE OF CUPS)",
        "duz_gecmis": "Geçmişte romantik teklifler alan, sanatsal ilhamlarla dolu, hassas ve tatlı dilli biriyle karşılaşmışsın.",
        "duz_simdi": "Şu an kalbini ısıtacak sürpriz bir haber, romantik bir mesaj veya saf bir teklif kapında.",
        "duz_gelecek": "Gelecekte sevindirici sürprizler, duygusal teklifler ve yaratıcı sürpriz gelişmeler seni bekliyor.",
        "ters_gecmis": "Geçmişte aşırı alınganlıklar, duygusal çocukluklar ve hayal kırıklığı yaratan haberler alınmış.",
        "ters_simdi": "Şu sıralar duygusal olarak çok hassassın; en küçük şeylere kırılabilir, gerçekçi olmayan hayaller kurabilirsin.",
        "ters_gelecek": "Gelecekte çocuksu kaprisler ve duygusal taşkınlıklar ilişkilerini kısa süreliğine zedeleyebilir."
    },
    48: {
        "isim": "KUPA ŞÖVALYESİ (KNIGHT OF CUPS)",
        "duz_gecmis": "Geçmişte romantik adımlar atan, kalbini sunan, aşkın peşinden koşan zarif bir aşık profili çizmişsin.",
        "duz_simdi": "Şu an hayatına romantizmin hakim olduğu, tekliflerin ve sevgi gösterilerinin yoğun olduğu bir süreçtesin.",
        "duz_gelecek": "Gelecekte beyaz atlı prens/prensas edasıyla hayatına girecek çok özel bir teklif veya aşık gelebilir.",
        "ters_gecmis": "Geçmişte sahte vaatler veren, duygularıyla oynayan veya gerçeklerden kopuk romantik hayalcilerle karşılaşmışsın.",
        "ters_simdi": "Şu sıralar duygusal konularda hayal kırıklığı yaşama riskin var; vaatlerin altı boş çıkabilir.",
        "ters_gelecek": "Gelecekte güven sarsıcı romantik manipülasyonlara karşı uyanık olman gerekebilir."
    },
    49: {
        "isim": "KUPA KRALİÇESİ (QUEEN OF CUPS)",
        "duz_gecmis": "Geçmişte şefkatli, sezgisel, empati yeteneği yüksek ve etrafındakileri iyileştiren bir anaç sevgi sunmuşsun.",
        "duz_simdi": "Şu an iç sesine tamamen güvenen, son derece şefkatli, merhametli ve duygusal olarak olgun bir duruştasın.",
        "duz_gelecek": "Gelecekte hayatında sana şefkat gösterecek, dertlerini dinleyecek çok güvenilir bir kadın figürü var.",
        "ters_gecmis": "Geçmişte duygusal istismara uğramış, aşırı alınganlıklar ve kurban psikolojisiyle tükenmişsin.",
        "ters_simdi": "Şu sıralar duygusal olarak boğulmuş hissedebilir, kendi kuruntularının kurbanı olabilirsiniz.",
        "ters_gelecek": "Gelecekte aşırı duygusallık ve manipüle edilmeye açık olma durumlarına karşı dikkatli olmalısın."
    },
    50: {
        "isim": "KUPA KRALI (KING OF CUPS)",
        "duz_gecmis": "Geçmişte duygularını mantığıyla dengeleyebilen, bilge, adil ve kriz anlarında sakin kalabilen bir rehber olmuşsun.",
        "duz_simdi": "Şu an duygusal zekanla hareket eden, etrafındakilere huzur ve güven veren bir otorite konumundasın.",
        "duz_gelecek": "Gelecekte sana hem duygusal hem de mantıksal anlamda destek olacak çok olgun bir erkek figürü hayatına girecek.",
        "ters_gecmis": "Geçmişte duygularını bastırmış, içten pazarlıklı veya manipülatif duygusal oyunlar oynamışsın.",
        "ters_simdi": "Şu sıralar duygularını kontrol etmekte zorlanıyor, içsel bir öfke veya soğukluk dalgası yaşıyorsun.",
        "ters_gelecek": "Gelecekte duygusal patlamalar veya sinsi tavırlar sergileyen kişilere karşı temkinli olmalısın."
    },
    51: {
        "isim": "KILIÇ ASI (ACE OF SWORDS)",
        "duz_gecmis": "Geçmişte kafandaki tüm sis perdesini dağıtan, hakikati haykıran ve keskin bir zihinsel uyanış yaşayan adımlar atmışsın.",
        "duz_simdi": "Şu an zihninin berrak olduğu, en doğru kararları vereceğin ve hakikati net bir şekilde göreceğin bir anındasın.",
        "duz_gelecek": "Gelecekte büyük bir zafer, hukuki bir başarı veya zihinsel olarak çığır açacak parlak bir fikir seninle olacak.",
        "ters_gecmis": "Geçmişte yanlış anlaşılmalar, adaletsiz kararlar ve zihinsel bulanıklıklar yüzünden hata yapmışsın.",
        "ters_simdi": "Şu sıralar zihnin çok karışık; keskin kararlar almak yerine yanlış anlamalara açık bir dönemdesin.",
        "ters_gelecek": "Gelecekte yanlış ifade edilen sözler ve keskin dilli eleştiriler ilişkilerini zedeleyebilir."
    },
    52: {
        "isim": "KILIÇ İKİLİSİ (TWO OF SWORDS)",
        "duz_gecmis": "Geçmişte iki seçenek arasında kalıp gözlerini gerçeğe kapatarak taraf seçmeyi reddettiğin bir çıkmaz yaşamışsın.",
        "duz_simdi": "Şu an gerçeklerle yüzleşmekten kaçındığın, zor bir kararı ertelediğin zihinsel bir çıkmazdasın.",
        "duz_gelecek": "Gelecekte o gözlerindeki bağ nihayet çözülecek ve ne kadar kaçarsan kaç o kararı vermek zorunda kalacaksın.",
        "ters_gecmis": "Geçmişte kararsızlığı sonlandırmış, göz bağını çıkarıp zor da olsa bir seçim yapmışsın.",
        "ters_simdi": "Şu sıralar gerçekler yüzüne tokat gibi çarpıyor; daha fazla kaçamayacağın bir karar anına yaklaşıyorsun.",
        "ters_gelecek": "Gelecekte ertelenen yüzleşmeler ve kararlar zihnini bir süre daha meşgul etmeye devam edecek."
    },
    53: {
        "isim": "KILIÇ ÜÇLÜSÜ (THREE OF SWORDS)",
        "duz_gecmis": "Geçmişte kalbini kıran, ihanet, ayrılık veya acı bir gerçekle yüzleşerek derin bir hüzün yaşamışsın.",
        "duz_simdi": "Şu an kalp kırıklığı, yas ve acı veren bir yüzleşmeyle sınandığın kederli bir süreçtesin.",
        "duz_gelecek": "Gelecekte bu acı zamanla hafifleyecek ve o yara yerini derin bir zihinsel olgunluğa bırakacak.",
        "ters_gecmis": "Geçmişteki kalp kırıklıklarını iyileştirmeye başlamış, affetme ve yaraları sarma yoluna girmişsin.",
        "ters_simdi": "Şu sıralar acıyı atlatmaya çalışıyor, içindeki o kırgınlığı geride bırakmak için çaba sarf ediyorsun.",
        "ters_gelecek": "Gelecekte eski acıların tamamen kabuk bağlayacağı ve huzuru bulacağın günler çok yakın."
    },
    54: {
        "isim": "KILIÇ DÖRTLÜSÜ (FOUR OF SWORDS)",
        "duz_gecmis": "Geçmişte yoğun stres ve koşturmacanın ardından hastaneye çekilir gibi derin bir dinlenme ve zihinsel mola almışsın.",
        "duz_simdi": "Şu an her şeyden elini ayağını çekip kafanı dinlemen, şifa bulman ve zihnini sessize alman gereken bir şarj sürecindesin.",
        "duz_gelecek": "Gelecekte bu dinlenme sayesinde çok daha dinç, zinde ve güçlü bir şekilde sahalara geri döneceksin.",
        "ters_gecmis": "Geçmişte dinlenmeyi reddetmiş, tükenmiş bir zihinle çalışmaya devam ederek sağlığını zorlamışsın.",
        "ters_simdi": "Şu sıralar zihinsel yorgunluk hat safhada ama hala durmayı reddediyorsun; biraz yavaşlamalısın.",
        "ters_gelecek": "Gelecekte zorunlu bir mola (hastalık vb.) almamak için şimdiden dinlenmeye özen göstermelisin."
    },
    55: {
        "isim": "KILIÇ BEŞLİSİ (FIVE OF SWORDS)",
        "duz_gecmis": "Geçmişte her ne pahasına olursa olsun kazandığını sandığın ama aslında herkesi kaybettiğin toksik bir kavga yaşamışsın.",
        "duz_simdi": "Şu an çevrende hileli durumların, ego savaşlarının ve kimin haklı olduğunun önemsizleştiği bir kriz var.",
        "duz_gelecek": "Gelecekte bu tarz ucuz zaferlerin ve sinsi çekişmelerin sana hiçbir şey kazandırmadığını fark edeceksin.",
        "ters_gecmis": "Geçmişte haksız bir kavgadan uzaklaşmış, gururlu bir duruşla orayı terk etmeyi seçmişsin.",
        "ters_simdi": "Şu sıralar gerginlikleri bitirme, barış sağlama veya geçmişteki haksızlıkları telafi etme çabasındasın.",
        "ters_gelecek": "Gelecekte ego savaşlarına son vererek daha olgun bir iletişim tarzı benimsemeye başlayacaksın."
    },
    56: {
        "isim": "KILIÇ ALTILISI (SIX OF SWORDS)",
        "duz_gecmis": "Geçmişte arkanda fırtınalar bırakarak daha sakin, huzurlu sulara doğru zorunlu bir yolculuğa çıkmışsın.",
        "duz_simdi": "Şu an sorunlu bir dönemi arkada bırakıp daha sakin, güvenli bir geleceğe doğru ilerleme sürecindesin.",
        "duz_gelecek": "Gelecekte fırtınalar dinecek, sular durulacak ve hayatında çok daha huzurlu bir limana varacaksın.",
        "ters_gecmis": "Geçmişte sorunlardan kaçmaya çalışmış ama sıkıntılı dönemi bir türlü arkanda bırakamamışsın.",
        "ters_simdi": "Şu sıralar geçiş sürecinde pürüzler yaşıyor, sorunları çözmeden kaçmaya çalışmanın bedelini ödüyorsun.",
        "ters_gelecek": "Gelecekte çözülmemiş meseleler tekrar önüne çıkabilir, önce onları temizlemen gerekecek."
    },
    57: {
        "isim": "KILIÇ YEDİLİSİ (SEVEN OF SWORDS)",
        "duz_gecmis": "Geçmişte gizli saklı işler çevirmiş, kurnazlık yapmış ya da bir şeylerden sinsice kaçmak zorunda kalmışsın.",
        "duz_simdi": "Şu an etrafında gizli planlar dönüyor olabilir veya sen sorumluluklardan kaçmak için kurnazca yollar arıyorsun.",
        "duz_gelecek": "Gelecekte arkadan iş çeviren insanlara veya gizli saklı yürütülen projelere karşı uyanık olmalısın.",
        "ters_gecmis": "Geçmişte dürüstlüğü seçmiş, yalanların ve kurnazlıkların ortaya dökülmesiyle dersini almışsın.",
        "ters_simdi": "Şu sıralar vicdan muhasebesi yapıyor, gizlediğin şeylerin yükünden kurtulmak istiyorsun.",
        "ters_gelecek": "Gelecekte dürüst olmayan tutumların başına iş açabileceği için açık oynamakta fayda var."
    },
    58: {
        "isim": "KILIÇ SEKİZLİSİ (EIGHT OF SWORDS)",
        "duz_gecmis": "Geçmişte kendi zihinsel hapishaneni kurmuş, eli kolu bağlı çaresiz bir kurban psikolojisiyle yaşmışsın.",
        "duz_simdi": "Şu an kendini çıkmazda ve kapana kısılmış hissediyorsun ama o ipler aslında o kadar da sıkı değil.",
        "duz_gelecek": "Gelecekte gözlerindeki bağı çözecek ve o zihinsel hapishaneden kendi gücünle çıkıp özgürleşeceksin.",
        "ters_gecmis": "Geçmişte kurban psikolojisinden kurtulmuş, zincirlerini kırarak özgürlüğünü ilan etmişsin.",
        "ters_simdi": "Şu sıralar çaresizlik hissinden yavaş yavaş sıyrılıyor, durumu değiştirebilecek gücü fark ediyorsun.",
        "ters_gelecek": "Gelecekte zihinsel engelleri tamamen yıkarak çok daha özgür kararlar alacaksın."
    },
    59: {
        "isim": "KILIÇ DOKUZLUSU (NINE OF SWORDS)",
        "duz_gecmis": "Geçmişte kabuslar gördüğün, uykusuz geceler geçirdiğin, kaygı ve endişeden zihnini tüketmişsin.",
        "duz_simdi": "Şu an aşırı kaygı, kuruntu ve stres yüzünden geceleri uyuyamadığın zihinsel bir tükenmişliktesin.",
        "duz_gelecek": "Gelecekte bu korkuların çoğunun yersiz olduğunu anlayacak ve derin bir nefes alarak rahatlayacaksın.",
        "ters_gecmis": "Geçmişte kaygılarla baş etmeyi öğrenmiş, zihinsel kabusları geride bırakarak şifa bulmuşsun.",
        "ters_simdi": "Şu sıralar endişelerin yavaş yavaş hafifliyor; fırtınanın en şiddetli anı geride kalıyor.",
        "ters_gelecek": "Gelecekte zihnini kemiren o vesveselerden kurtularak çok daha huzurlu uykular uyuyacaksın."
    },
    60: {
        "isim": "KILIÇ ONLUSU (TEN OF SWORDS)",
        "duz_gecmis": "Geçmişte hayatının en büyük sırt darbesini almış, dibe vurduğun ve her şeyin bittiğini sandığın bir yıkım yaşamışsın.",
        "duz_simdi": "Şu an acı verici bir sonun son aşamasındasın; bundan daha kötü olamaz dediğin bir dip noktasındasın.",
        "duz_gelecek": "Gelecekte bu dip noktası senin için yepyeni bir başlangıç olacak; çünkü daha fazla düşemezsin, yönün yukarı.",
        "ters_gecmis": "Geçmişteki o büyük yıkımın ardından yaralarını sarmış ve yavaş yavaş toparlanmaya başlamışsın.",
        "ters_simdi": "Şu sıralar en kötü günlerin geride kalıyor; felaket senaryoları yerini toparlanmaya bırakıyor.",
        "ters_gelecek": "Gelecekte o enkazdan güçlenerek çıkacak ve hayatını yeniden inşa edeceksin."
    },
    61: {
        "isim": "KILIÇ PRENSİ (PAGE OF SWORDS)",
        "duz_gecmis": "Geçmişte her şeyi sorgulayan, araştırmacı, dedikoduları toplayan ama biraz da sivri dilli biriyle karşılaşmışsın.",
        "duz_simdi": "Şu an etrafı gözlemleyen, meraklı, her şeyi didik didik eden ve keskin sözler sarf eden bir zihin yapısındasın.",
        "duz_gelecek": "Gelecekte beklenmedik haberler alacak, arkandan dönen bazı dedikoduları öğreneceksin.",
        "ters_gecmis": "Geçmişte düşünmeden konuşmuş, sivri dilin yüzünden insanları kırmış ve yanlış bilgiler yaymışsın.",
        "ters_simdi": "Şu sıralar dedikodulara ve asılsız bilgilere karşı dikkatli olmalı, dilinin kemiğine kulak vermelisin.",
        "ters_gelecek": "Gelecekte fevri ve patavatsız açıklamalar yapmaktan kaçınman gereken durumlar oluşabilir."
    },
    62: {
        "isim": "KILIÇ ŞÖVALYESİ (KNIGHT OF SWORDS)",
        "duz_gecmis": "Geçmişte fırtına gibi estiren, zekasıyla ve hırsıyla hedeflerine doğru koşan keskin bir mücadele vermişsin.",
        "duz_simdi": "Şu an inanılmaz hızlı, aceleci, mantığınla hareket eden ve engelleri bıçak gibi kesip atan bir enerjidesin.",
        "duz_gelecek": "Gelecekte ani bir mücadele, hızlı kararlar ve zihinsel olarak çok yoğun bir koşturmaca seni bekliyor.",
        "ters_gecmis": "Geçmişte düşüncesizce ve saldırgan bir üslupla hareket ederek etrafındaki herkesi kırmışsın.",
        "ters_simdi": "Şu sıralar çok sert ve agresif çıkışlar yapıyorsun; sakinleşmezsen bu öfke sana zarar verecek.",
        "ters_gelecek": "Gelecekte fevri ve yıkıcı tartışmalardan kaçınman gerektiğini acı bir tecrübeyle anlayabilirsin."
    },
    63: {
        "isim": "KILIÇ KRALİÇESİ (QUEEN OF SWORDS)",
        "duz_gecmis": "Geçmişte duygulardan ziyade mantığı, adaleti ve dürüstlüğü ön planda tutan keskin kararlar almışsın.",
        "duz_simdi": "Şu an olaylara son derece objektif, mantıklı, net ve tarafsız bir gözle yaklaşıyorsun.",
        "duz_gelecek": "Gelecekte hayatında sana net kurallar koyacak, duygusallığa yer vermeyen ama adil bir kadın figürü olacak.",
        "ters_gecmis": "Geçmişte aşırı soğuk, eleştirel, kırıcı ve buz gibi mesafeli tavırlar sergilemişsin.",
        "ters_simdi": "Şu sıralar çok yargılayıcı ve acımasız olabiliyorsun; insanlara karşı empatiyi unutmaman gerekiyor.",
        "ters_gelecek": "Gelecekte yalnızlaşmamak için keskin eleştirilerini biraz yumuşatman gerekebilir."
    },
    64: {
        "isim": "KILIÇ KRALI (KING OF SWORDS)",
        "duz_gecmis": "Geçmişte entelektüel zekasıyla yasaları koruyan, son derece adil, stratejik ve mantıksal bir otorite kurmuşsun.",
        "duz_simdi": "Şu an mantığın, hukukun ve stratejik zekanın emirdesin; duygulara yer vermeden analitik kararlar alıyorsun.",
        "duz_gelecek": "Gelecekte hukuki veya resmi konularda çok güçlü, mantıklı ve adil bir destek göreceksin.",
        "ters_gecmis": "Geçmişte adaleti kendi çıkarları doğrultusunda kullanan, manipülatif ve katı bir zihniyet hakim olmuş.",
        "ters_simdi": "Şu sıralar aşırı kuralcı, inatçı ve duygusuz kararlarla çevrendekileri bunaltıyorsun.",
        "ters_gelecek": "Gelecekte otorite figürleriyle yaşanabilecek zihinsel çatışmalara ve katı kurallara karşı dikkatli ol."
    },
    65: {
        "isim": "TABAK/TOPRAK ASI (ACE OF PENTACLES)",
        "duz_gecmis": "Geçmişte maddi ve somut anlamda çok sağlam bir fırsat yakalamış, yeni bir yatırım veya işe adım atmışsın.",
        "duz_simdi": "Şu an elinde para, iş, sağlık veya kariyer anlamında çok somut ve bereketli bir fırsat duruyor.",
        "duz_gelecek": "Gelecekte maddi refah getirecek, uzun vadeli ve kalıcı temelleri olan harika bir başlangıç seni bekliyor.",
        "ters_gecmis": "Geçmişte kaçırılan maddi fırsatlar, kötü yatırımlar veya finansal sıkıntılar yaşanmış.",
        "ters_simdi": "Şu sıralar maddi konularda temkinli olmalısın; fırsat gibi görünen bazı tuzaklar para kaybına yol açabilir.",
        "ters_gelecek": "Gelecekte bütçe dengeni sarsacak harcamalardan ve riskli finansal hamlelerden kaçınmalısın."
    },
    66: {
        "isim": "TABAK/TOPRAK İKİLİSİ (TWO OF PENTACLES)",
        "duz_gecmis": "Geçmişte bütçeyi denkleştirmek, iki işi birden idare etmek ve hayatın akışında hokkabazlık yapmak zorunda kalmışsın.",
        "duz_simdi": "Şu an hayatındaki birden fazla sorumluluğu veya finansal kalemi dengelemeye çalıştığın esnek bir dönemdesin.",
        "duz_gelecek": "Gelecekte hayatın temposuna ayak uydurmayı öğrenecek ve ekonomik dengeni sağlamayı başaracaksın.",
        "ters_gecmis": "Geçmişte dengeler altüst olmuş, borçlar birikmiş ve hayatın yönetimi kontrolden çıkmış.",
        "ters_simdi": "Şu sıralar ekonomik olarak zorlanıyor, ödemeleri denkleştirmekte büyük bir karmaşa yaşıyorsun.",
        "ters_gelecek": "Gelecekte finansal dalgalanmalara karşı daha disiplinli bir bütçe planlaması yapman şart."
    },
    67: {
        "isim": "TABAK/TOPRAK ÜÇLÜSÜ (THREE OF PENTACLES)",
        "duz_gecmis": "Geçmişte ekip çalışmasıyla harika bir iş çıkarılmış, usta ellerden çıkan projeler takdir edilmiş.",
        "duz_simdi": "Şu an iş yerinde veya bir projede ortaklaşa çalışarak emeklerinin karşılığını aldığın verimli bir süreçtesin.",
        "duz_gelecek": "Gelecekte kariyerinde terfi alacağın, uzmanlığının tescilleneceği ve takdir göreceğin günler çok yakın.",
        "ters_gecmis": "Geçmişte ekip içinde uyumsuzluklar, iş bilmezlikler ve projelerin aksaması gibi sorunlar yaşanmış.",
        "ters_simdi": "Şu sıralar iş arkadaşlarınla uyum sorunu yaşıyor, ortak projelerde fikir ayrılıklarıyla boğuşuyorsun.",
        "ters_gelecek": "Gelecekte profesyonel hayatta daha uyumlu çalışmayı öğrenmediğin sürece ilerlemekte zorlanabilirsin."
    },
    68: {
        "isim": "TABAK/TOPRAK DÖRTLÜSÜ (FOUR OF PENTACLES)",
        "duz_gecmis": "Geçmişte maddiyata ve güvenliğe aşırı derecede bağlanmış, elindekileri sıkı sıkı tutarak risk almaktan kaçınmışsın.",
        "duz_simdi": "Şu an para, mal veya ilişkiler konusunda son derece tutucu, cimri ve kontrolcü bir duruş sergiliyorsun.",
        "duz_gelecek": "Gelecekte bu katı tutumundan vazgeçmediğin sürece bolluk enerjisinin akışını tıkama riskin var.",
        "ters_gecmis": "Geçmişte parasal konularda esnemeyi öğrenmiş, elindekileri paylaşarak rahatlamışsın.",
        "ters_simdi": "Şu sıralar para harcama korkusundan veya kaybetme endişesinden yavaş yavaş arınmaya başlıyorsun.",
        "ters_gelecek": "Gelecekte cimriliği bırakıp hayatın akışına güvenmeyi seçtiğin an bolluk sana da gelecektir."
    },
    69: {
        "isim": "TABAK/TOPRAK BEŞLİSİ (FIVE OF PENTACLES)",
        "duz_gecmis": "Geçmişte maddi ve manevi yokluk, yalnızlık, kriz veya sağlık sorunlarıyla sınandığın zorlu bir kış dönemi atlatmışsın.",
        "duz_simdi": "Şu an kendini dışlanmış, parasız, desteksiz ve adeta karanlıkta kalmış hissettiğin bir yoksulluk/kriz sürecindesin.",
        "duz_gelecek": "Gelecekte bu zorluklar geride kalacak; yardım eli uzatılacak ve sıcak bir yuvaya kavuşacaksın.",
        "ters_gecmis": "Geçmişteki o yoksulluk ve yalnızlık dönemi yavaş yavaş bitmiş, yardımlar sayesinde toparlanmışsın.",
        "ters_simdi": "Şu sıralar en kötü kriz atlatılıyor; tünelin ucundaki ışığı görmeye başladığın bir iyileşme anındasın.",
        "ters_gelecek": "Gelecekte maddi ve manevi kayıpların telafi edileceği çok daha güvenli bir döneme giriyorsun."
    },
    70: {
        "isim": "TABAK/TOPRAK ALTILISI (SIX OF PENTACLES)",
        "duz_gecmis": "Geçmişte ya başkalarına cömertçe yardım etmiş ya da zor anında hak ettiğin desteği ve sadakayı görmüşsün.",
        "duz_simdi": "Şu an hayatında dengeli bir verme-alma ilişkisi var; maddi veya manevi destek alışverişi içindesin.",
        "duz_gelecek": "Gelecekte parasal konularda rahatlayacağın, hak ettiğin finansal desteği veya yardımı bulacağın günler var.",
        "ters_gecmis": "Geçmişte adaletsiz yardımlar, borç batağı veya karşılıklı çıkara dayalı ilişkiler yaşanmış.",
        "ters_simdi": "Şu sıralar maddi yardımlarda veya borç alıp verme süreçlerinde dengesizlikler yaşayabilirsin.",
        "ters_gelecek": "Gelecekte finansal konularda kimseye kefil olmamaya ve dengesiz para ilişkilerinden kaçınmaya dikkat et."
    },
    71: {
        "isim": "TABAK/TOPRAK YEDİLİSİ (SEVEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte ektiğin tohumların büyümesini sabırla beklemiş, uzun vadeli yatırımlar için emek harcamışsın.",
        "duz_simdi": "Şu an yaptığın yatırımların ve harcadığın emeklerin meyvesini alıp almayacağını hesapladığın bir bekleme ve değerlendirme aşamasındasın.",
        "duz_gelecek": "Gelecekte sabrının karşılığını fazlasıyla alacak, ürünlerini toplamanın keyfini süreceksin.",
        "ters_gecmis": "Geçmişte sabırsızlık yapmış, ektiğin mahsulü hemen almak isterken boşa kürek çekmişsin.",
        "ters_simdi": "Şu sıralar harcadığın emeklerin karşılığını alamadığını düşünerek hayal kırıklığı ve sabırsızlık yaşıyorsun.",
        "ters_gelecek": "Gelecekte yanlış alanlara yatırım yaptığını fark edebilir veya projeni gözden geçirmek zorunda kalabilirsin."
    },
    72: {
        "isim": "TABAK/TOPRAK SEKİZLİSİ (EIGHT OF PENTACLES)",
        "duz_gecmis": "Geçmişte işine büyük bir titizlikle sarılmış, ustalık kazanmak için saatlerce alın teri dökerek çalışmışsın.",
        "duz_simdi": "Şu an detaylarla uğraştığın, işini mükemmel yapmak için büyük bir özveriyle çalıştığın çıraklıkten ustaçılığa geçiş sürecindesin.",
        "duz_gelecek": "Gelecekte bu yoğun emek ve ustalığın sayesinde kariyerinde aranan bir uzman haline geleceksin.",
        "ters_gecmis": "Geçmişte kalitesiz işler yapmış, detayları önemsemeden aceleye getirerek çalışmışsın.",
        "ters_simdi": "Şu sıralar işine karşı motivasyonun düşük; detaylarda boğuluyor veya ezbere işler yapıyorsun.",
        "ters_gelecek": "Gelecekte iş disiplinine daha çok sarılman gerekecek, aksi takdirde kaliteden ödün verebilirsin."
    },
    73: {
        "isim": "TABAK/TOPRAK DOKUZLUSU (NINE OF PENTACLES)",
        "duz_gecmis": "Geçmişte kendi ayakları üzerinde duran, finansal özgürlüğünü ilan etmiş ve konforlu bir yaşam kurmuşsun.",
        "duz_simdi": "Şu an emeklerinin lüksünü ve konforunu çıkardığın, bağımsız, özgür ve huzurlu bir zenginlik dönemindesin.",
        "duz_gelecek": "Gelecekte maddi ve manevi tüm lükslerin, konforun ve kendi kendine yetmenin gururunu yaşayacaksın.",
        "ters_gecmis": "Geçmişte maddi bağımlılıklar yaşamış, başkalarına muhtaç kalmış veya konfor uğruna özgürlüğünü satmışsın.",
        "ters_simdi": "Şu sıralar finansal konularda geçici darlıklar veya lüks harcamalardan ötürü bütçe sarsıntıları yaşayabilirsin.",
        "ters_gelecek": "Gelecekte kendi öz değerini parasal varlıklarla ölçme yanlışına düşmemeye dikkat etmelisin."
    },
    74: {
        "isim": "TABAK/TOPRAK ONLUSU (TEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte kalıcı bir aile serveti, büyük mülkler ve nesiller boyu sürecek sağlam bir refah temeli atmışsın.",
        "duz_simdi": "Şu an aile bağlarının, mal mülk güvencesinin ve köklü bir aile şirketinin/mirasın getirdiği huzurdasın.",
        "duz_gelecek": "Gelecekte gayrimenkul sahibi olacağın, aile boyu büyük bir refaha ve kalıcı başarılara kavuşacağın bir dönem var.",
        "ters_gecmis": "Geçmişte aile içi miras kavgaları, iflaslar veya maddi temellerin sarsılması gibi büyük krizler yaşanmış.",
        "ters_simdi": "Şu sıralar aile içinde parasal anlaşmazlıklar veya mal mülk paylaşımlarından ötürü gerginlikler var.",
        "ters_gelecek": "Gelecekte finansal temellerini korumak için aile içi yatırımlarda çok daha dikkatli olmalısın."
    },
    75: {
        "isim": "TABAK/TOPRAK PRENSİ (PAGE OF PENTACLES)",
        "duz_gecmis": "Geçmişte yeni bir eğitime başlayan, kariyer planları yapan, çalışkan ve öğrenmeye hevesli biriyle karşılaşmışsın.",
        "duz_simdi": "Şu an somut adımlar atmak için dersine çalışan, yeni bir iş teklifi veya eğitim fırsatı bekleyen bir konumdasın.",
        "duz_gelecek": "Gelecekte kariyerine yön verecek harika bir iş teklifi, burs veya somut bir fırsat kapını çalacak.",
        "ters_gecmis": "Geçmişte tembellik yapmış, fırsatları elinin tersiyle itmiş ve çalışma disiplininden yoksun kalmışsın.",
        "ters_simdi": "Şu sıralar odaklanma sorunu yaşıyor, somut adımlar atmak yerine hayallerle vakit kaybediyorsun.",
        "ters_gelecek": "Gelecekte tembellik ve disiplinsizlik yüzünden kaçan fırsatlar sonradan pişmanlık yaratabilir."
    },
    76: {
        "isim": "TABAK/TOPRAK ŞÖVALYESİ (KNIGHT OF PENTACLES)",
        "duz_gecmis": "Geçmişte yavaş ama emin adımlarla ilerleyen, sorumluluk sahibi, güvenilir ve işini asla yarım bırakmayan biri olmuşsun.",
        "duz_simdi": "Şu an yavaş ama çok sağlam adımlarla ilerliyor, sabırla ve inatla işini sonuna kadar götürüyorsun.",
        "duz_gelecek": "Gelecekte istikrarlı ve güvenilir adımların sayesinde işlerini başarıyla sonuca ulaştıracaksın.",
        "ters_gecmis": "Geçmişte aşırı inatçılık, hantallık ve rutine saplanıp kalmak projelerin yavaşlamasına yol açmış.",
        "ters_simdi": "Şu sıralar işler adeta yerinde sayıyor; inatçılığın ve esnek olmaman yüzünden ilerleme kaydedemiyorsun.",
        "ters_gelecek": "Gelecekte aşırı tutuculuk ve hantallıktan kaçınarak biraz daha esnek olman gerekebilir."
    },
    77: {
        "isim": "TABAK/TOPRAK KRALİÇESİ (QUEEN OF PENTACLES)",
        "duz_gecmis": "Geçmişte doğayı seven, bereketli, çevresindekileri besleyip kollayan, maddiyatta usta bir anne figürü olmuşsun.",
        "duz_simdi": "Şu an elindekileri en iyi şekilde değerlendiren, güven veren, yuvasına ve işine çok düşkün bir konumdasın.",
        "duz_gelecek": "Gelecekte maddi ve manevi bolluk içinde yaşayacağın, konforlu ve güvenli bir düzen seni bekliyor.",
        "ters_gecmis": "Geçmişte aşırı maddiyata düşkünlük, cimrilik veya evine/işine yabancılaşma durumları yaşanmış.",
        "ters_simdi": "Şu sıralar kendine ve çevrene yeterince özen göstermiyor, maddi kaygılarla huzurunu kaçırıyorsun.",
        "ters_gelecek": "Gelecekte maddiyata aşırı odaklanıp maneviyatı ihmal etmemeye özen göstermelisin."
    },
    78: {
        "isim": "TABAK/TOPRAK KRALI (KING OF PENTACLES)",
        "duz_gecmis": "Geçmişte büyük bir servet yönetmiş, finansal imparatorluk kurmuş, son derece güvenilir ve cömert bir iş insanı olmuşsun.",
        "duz_simdi": "Şu an maddi gücün zirvesinde, işleri ustalıkla yöneten, güvenilir ve sağlam bir otorite figürüsün.",
        "duz_gelecek": "Gelecekte finansal anlamda tam güvenceye kavuşacağın, büyük yatırımlarla adını duyuracağın bir dönem var.",
        "ters_gecmis": "Geçmişte rüşvet, yolsuzluk, maddi açgözlülük veya iflaslar gibi finansal krizler yaşanmış.",
        "ters_simdi": "Şu sıralar maddi gücünü kötüye kullanan, bencil veya parayı her şeyin üstünde tutan bir yapın var.",
        "ters_gelecek": "Gelecekte parasal konularda aşırı risk almaktan ve açgözlü tavırlardan kesinlikle kaçınmalısın."
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
