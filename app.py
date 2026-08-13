import random
import time

isim = input("falına bakılacak kişi ismin ne?: ")
print(f"\n {isim}, kolektif enerjiye bağlanılıyor...")
time.sleep(2)
# geniş ve dürüst bir tarot destesi 
destem = {
    # Major Arcana
    "Deli": "Yeni bir bodoslama dalış, sonu belirsiz.",
    "Büyücü": "Elindeki imkanları abartıyorsun, ortada devasa bir şey yok.",
    "Azize": "İç sesin 'kaç' diyor ama sen diretiyorsun.",
    "İmparatoriçe": "Keyfin yerinde ama tembelliğe vurdun.",
    "İmparator": "Aşırı otorite taslıyorsun, kimse çekmek zorunda değil.",
    "Hierofant": "Sistemden dışarı çıkmaya cesaretin yok.",
    "Aşıklar": "Kritik bir seçim yapacaksın, muhtemelen yanlış olanı.",
    "Araba": "Hızla gidiyorsun ama frenlerin patlak.",
    "Güç": "Sabrın taştı taşacak, ortalık karışacak.",
    "Ermiş": "Kendi kendine trip atıp kabuğuna çekilmişsin.",
    "Kader Çarkı": "Yine aynı döngüye girdin, tebrikler.",
    "Adalet": "Hak ettiğin neyse o geliyor, şikayet etme.",
    "Asılı Adam": "Hiçbir yere varamıyorsun çünkü inatla kıpırdamıyorsun.",
    "Ölüm": "Eski defterler zorla kapanıyor, ağlamanın lüzumu yok.",
    "Denge": "İğne uyu üzerinde dengede durmaya çalışıyorsun, yazık.",
    "Şeytan": "Kendi ellerinle bağlandığın toksik alışkanlıklar.",
    "Kule": "Bütün planların başına yıkılacak, geçmiş olsun.",
    "Yıldız": "Ufukta hafif bir ışık var ama umut bağlamaya değmez.",
    "Ay": "Paranoya ve kuruntu sezinliyorum, hepsi kafanda.",
    "Güneş": "Her şey yolunda gibi görünecek ama nazara geleceksin.",
    "Mahkeme": "Geçmişteki hataların hesabını ödeme vakti.",
    "Dünya": "Döngüyü bitirdin ama başladığın yere geri döndün.",

    # Kupa Serisi
    "Kupa Ası": "Duygusal bir patlama yaşayacaksın ama altı boş çıkacak.",
    "Kupa İkilisi": "Karşılıklı boş yapma seansı.",
    "Kupa Üçlüsü": "Gereksiz bir kutlama veya kalabalık.",
    "Kupa Dörtlüsü": "Önüne sunulanı beğenmeyip burun kıvırıyorsun.",
    "Kupa Beşlisi": "Dökülen süte ağlamaya devam ediyorsun.",
    "Kupa Altılısı": "Geçmişteki nostaljik bataklığında boğuluyorsun.",
    "Kupa Yedilisi": "Hayal alemindesin, uyanınca çarpılacaksın.",
    "Kupa Sekizlisi": "Kaçıp gitmek istiyorsun ama cesaretin yok.",
    "Kupa Dokuzlusu": "Bencilce bir mutluluk, kimsenin umrunda değil.",
    "Kupa Onlusu": "Reklamlardaki gibi sahte bir aile tablosu.",
    "Kupa Prensi": "Aşırı sulugöz ve alıngan bir dönem.",
    "Kupa Şövalyesi": "Prens olduğunu sanan ama yalan söyleyen biri.",
    "Kupa Kraliçesi": "Sürekli dert dinlemekten içi kurumuş biri.",
    "Kupa Kralı": "Duygularını bastıran ama içten içe bitik bir tip.",

    # Kılıç Serisi
    "Kılıç Ası": "Keskin bir fikir ama başa bela olacak.",
    "Kılıç İkilisi": "Gözünü kapatmışsın, gerçekleri görmek istemiyorsun.",
    "Kılıç Üçlüsü": "Kalp kırıklığı ve net acı gerçekler.",
    "Kılıç Dörtlüsü": "Tükenmişlik sendromu, kafayı yemek üzeresin.",
    "Kılıç Beşlisi": "Kazandığını sandığın ama herkesi kaybettiğin bir kavga.",
    "Kılıç Altılısı": "Zoraki bir kaçış, arkana bakmadan gidiyorsun.",
    "Kılıç Yedilisi": "Üç kağıtçılık ve sinsilik peşindesin.",
    "Kılıç Sekizlisi": "Kendi ördüğün ağlara kendin takılmışsın.",
    "Kılıç Dokuzlusu": "Gece yarısı 'acaba' diye düşünmekten uykuların kaçmış.",
    "Kılıç Onlusu": "Sırtından bıçaklandın, oyun bitti.",
    "Kılıç Prensi": "Her şeye laf sokan sinir bozucu bir tip.",
    "Kılıç Şövalyesi": "Paldır küldür kavgaya dalan aceleci biri.",
    "Kılıç Kraliçesi": "Kimseye acımayan, buz gibi bir mantık.",
    "Kılıç Kralı": "Fazla mantıktan ruhunu kaybetmiş bir otorite.",

    # Değnek Serisi
    "Değnek Ası": "Büyük bir hevesle başlayıp yarım bırakacağın bir iş.",
    "Değnek İkilisi": "Yolun başındasın ama nereye gideceğini bilmiyorsun.",
    "Değnek Üçlüsü": "Bekliyorsun ama gelecek olan kargo bile gecikecek.",
    "Değnek Dörtlüsü": "Geçici bir huzur, hemen bozulacak.",
    "Değnek Beşlisi": "Ortada hiçbir şey yokken çıkan saçma bir tartışma.",
    "Değnek Altılısı": "Erken gelen bir zafer sarhoşluğu, duvara toslayacaksın.",
    "Değnek Yedilisi": "Tek başına herkese karşı piyon gibi savunma yapıyorsun.",
    "Değnek Sekizlisi": "Her şey üst üste geliyor, hızına yetişemiyorsun.",
    "Değnek Dokuzlusu": "Yaralı bereli ama hala 'bana bir şey olmaz' diyorsun.",
    "Değnek Onlusu": "Kaldıramayacağın yükün altına kendi isteğinle girmişsin.",
    "Değnek Prensi": "Yerinde duramayan ama boş gezen bir enerji.",
    "Değnek Şövalyesi": "Gaza gelip her şeyi yüzüne gözüne bulaştıracaksın.",
    "Değnek Kraliçesi": "Ben bilirimci, ortalığı ayağa kaldıran bir karakter.",
    "Değnek Kralı": "Liderlik taslayan ama içeride batmış bir vizyon.",

    # Tılsım Serisi
    "Tılsım Ası": "Küçük bir para girişi olacak, hemen harcayacaksın.",
    "Tılsım İkilisi": "İki parasal iş arasında bocalayıp duruyorsun.",
    "Tılsım Üçlüsü": "Ortak iş yapıyorsunuz ama herkes birbirini kazıklıyor.",
    "Tılsım Dörtlüsü": "Cimriliğin bu kadarı fazla, mezara mı götüreceksin?",
    "Tılsım Beşlisi": "Kuruşsuz ve desteksiz kaldığın soğuk bir dönem.",
    "Tılsım Altılısı": "Sadaka veya borç alıp verme dengesi.",
    "Tılsım Yedilisi": "Ektiğin biçtiğin yok, öylece tarlaya bakıyorsun.",
    "Tılsım Sekizlisi": "Amelenin önde gideni gibi sabahlara kadar çalışıyorsun.",
    "Tılsım Dokuzlusu": "Tek başına keyif yapıyorsun ama yalnızsın.",
    "Tılsım Onlusu": "Aile parası veya miras konulu gerginlikler.",
    "Tılsım Prensi": "Parayı bulacağını sanıp 5 kuruş harcayan stajyer.",
    "Tılsım Şövalyesi": "Ağır vites ama en azından güvenilir bir ilerleyiş.",
    "Tılsım Kraliçesi": "Konforuna düşkün, lüks sevdalısı bir tip.",
    "Tılsım Kralı": "Para bende patron benim diyen ego tavan."
}

# aynı desteden dürüstçe 3 kart çekelim
secilenler = random.sample(list(destem.items()), 3)

print(f"\n--- {isim} için dürüst bir açılım ---")
print(f"GEÇMİŞ : {secilenler[0][0]} -> {secilenler[O][1]}")
print(f"ŞİMDİ : {secilenler[1][0]}-> {secilenler [1][1]}")
print(f"GELECEK : {secilenler[2][0]}-> {secilenler[2][1]}")
print("\--- Evrenin özeti : Kartlar bol, gerçekler acı! ---")
    
    
    
