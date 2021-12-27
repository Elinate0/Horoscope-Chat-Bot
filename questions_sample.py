import time
prjName = 'Setenay:'
baseQuestionsTaurus = ["1- Boğa burcunun yönetici gezegeni nedir?",
                       "2- Boğa burcunun sevdiği renkler nelerdir?",
                       "3- Boğa burcunun olumlu özellikleri nelerdir ?",
                       "4- Boğa burcunun olumsuz özellikleri nelerdir ?",
                       "5- Boğa burcunun elementi nedir ?",
                       "6- Boğa burcunun şanslı sayısı nedir ?",
                       "7- Boğa burcnun uğurlu taşı nedir ?",
                       "8- Boğa burcunun sevdiği şeyler nelerdir ?",
                       "9- Boğa burcunun nefret ettiği şeyler ?",
                       "10-Boğa burcunun fiziksel görünümü nedir ?"]

baseAnswersTaurus = ["Venüs gezegeni boğa burcunun yönetici gezegenidir.",
                     "Boğa burcunun sevdiği renkler yeşil ve pembedir.",
                     "Boğa burcu sabırlı, düzenli, yardımcı, romantik, özenli ve adanmıştır.",
                     "Boğa burcu fazla hoşgörülü, inatçı, tembel ve fazal ihtiyatlıdır.",
                     "Boğa burcunun elementi topraktır.",
                     "Boğa burcunun uğurlu sayıları 6 ve 4.",
                     "Boğa burcunun uğurlu taşları Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşimdir.",
                     "Boğa burcunun en sevdiği şeyler; Ziynet eşyaları,Moda,Sürprizlerdir",
                     "Boğa burcunun en nefret ettiği şeyler;Değişim,Risk almak,Acele Ettirilmek,Güvencesiz kalmaktır.",
                     "Boğa burcu orta boylu, etli, tıknaz hatta göbeklidir. Kol ve bacaklar kısa ve tombuldur."]

baseQuestionsGemini = ["1- İkizler burcunun yönetici gezegeni nedir?",
                       "2- İkizler burcunun sevdiği renkler nelerdir?",
                       "3- İkizler burcunun olumlu özellikleri nelerdir ?",
                       "4- İkizler burcunun olumsuz özellikleri nelerdir ?",
                       "5- İkizler burcunun elementi nedir ?",
                       "6- İkizler burcunun şanslı sayısı nedir ?",
                       "7- İkizler burcnun uğurlu taşı nedir ?",
                       "8- İkizler burcunun sevdiği şeyler nelerdir ?",
                       "9- İkizler burcunun nefret ettiği şeyler ?",
                       "10-İkizler burcunun fiziksel görünümü nedir ?"]

baseAnswersGemini = ["Merkür gezegeni ikizler burcunun yönetici gezegenidir.",
					 "ikizler burcunun sevdiği renkler açık yeşil ve sarı.",
					 "İkizler burcu etkileyici, özgün, iş bilen, alımlı, akıllı, maceracıdır.",
					 "İkizler burcu vesveseli, dengesiz, iki yüzlü, yargılayıcı, depresifdir.",
					 "İkizler burcunun elementi havadır.",
					 "İkizler burcunun uğurlu sayıları 5 ve 7 dir.",
					 "İkizler burcunun uğurlu taşları  Akuamarin, Akik, Topaz, Sitrin, Turmalindir.",
					 "İkizler burcunun en sevdiği şeyler; Özgürlük,Küçük Hobiler,Kalabalık bir çevre,Yeni bir şey öğrenmedir.",
					 "İkizler burcunun en nefret ettiği şeyler;Yalnızlık,Aşırı sahiplenici kişiler,Telefonunun kurcalanması,Kıskanmak,Bekletilmekdir.",
					 "İlk akla gelen tipik özellik, incelik, uzunluk ve zayıflıktır. Orta boylu bile olsa kesinlikle zayıftır. Ancak bu zayıflık güçsüzlük demek değildir, aksine kuvvetli ve son derece çeviktir. Kilo almaya uygun olmayan tiplerdir."]

baseQuestionsLeo =[ "1- Aslan burcunun yönetici gezegeni nedir?",
                    "2- Aslan burcunun sevdiği renkler nelerdir ?",
                    "3- Aslan burcunun olumlu özellikleri nelerdir ?",
                    "4- Aslan burcunun olumsuz özellikleri nelerdir ?",
                    "5- Aslan burcunun elementi nedir ?",
                    "6- Aslan burcunun şanslı sayısı nedir ?",
                    "7- Aslan burcnun uğurlu taşı nedir ?",
                    "8- Aslan burcunun sevdiği şeyler nelerdir ?",
                    "9- Aslan burcunun nefret ettiği şeyler ?",
                    "10-Aslan burcunun fiziksel görünümü nedir ?"]

baseAnswersLeo = [ "Güneş gezegeni aslan burcunun yönetici gezegenidir.",
                   "Aslan burcunun sevdiği renkler altın sarısıdır.",
                   "Aslan burcu; Hoşgörülü , Yardımsever , Çalışkan ,Azimli,sadık, koruyucu, dobra, eğlencelidir .",
                   "Aslan burcu; Kibirli , Küstah, özensiz, taş kalpli, kıskanç, saldırgandır .",
                   "Aslan  burcunun elementi ateştir.",
                   "Aslan burcunun uğurlu sayıları 4 ve 5'dir.",
                   "Aslan burcunun uğurlu taşları; Kristal Kuvars, akik, Kehribardır.",
                   "Aslan burcunun en sevdiği şeyler;Eğlence, Enerjik Şeyler , Spor yapmak,Kameralar, şarkı söylemek, yakınlık kurmak, iltifat, güzel kıyafetlerdir.",
                   "Aslan burcunun en nefret ettiği şeyler;Görmezden gelinmek, yavan yemekler, yalnız kalmak, vedalar, kral-kraliçe muamelesi görmemektir.",
                   "Boylu poslu, enine boyuna, aslan gibi gösterişli.... ifadesi bu burç insanını iyi tarif eder.Saç,göz,ten rengi açık renk,cilt pembemsi,gözler iri ,yüz büyük ve hatlar köşelidir"]

baseQuestionsCancer =[ "1- Yengeç burcunun yönetici gezegeni nedir?",
                    "2- Yengeç burcunun sevdiği renkler nelerdir ?",
                    "3- Yengeç burcunun olumlu özellikleri nelerdir ?",
                    "4- Yengeç burcunun olumsuz özellikleri nelerdir ?",
                    "5- Yengeç burcunun elementi nedir ?",
                    "6- Yengeç burcunun şanslı sayısı nedir ?",
                    "7- Yengeç burcnun uğurlu taşı nedir ?",
                    "8- Yengeç burcunun sevdiği şeyler nelerdir ?",
                    "9- Yengeç burcunun nefret ettiği şeyler ?",
                    "10-Yengeç burcunun fiziksel görünümü nedir ?"]
baseAnswersCancer = ["Ay gezegeni yengeç burcunun yönetici gezegenidir.",
                  "Yengeç burcunun sevdiği renk beyazdır.",
                  "Yengeç burcu Yardımsever, sabırlı, merhametli, anaç, romantik, yaratıcıdır.",
                  "Yengeç burcu Dedikoducu, burnu havada, ketum, aşırı duyarlı, fazla rekabetçidir.",
                  "Yengeç burcunun elementi sudur.",
                  "Yengeç burcunun uğurlu sayıları 2 ve 3'dir.",
				  "Yengeç burcunun uğurlu taşları Akuamarin, Ay taşı, Kuvars kristali, Safir Taşı, Zümrütdür.",
                  "Yengeç burcunun en sevdiği şeyler;Romantizm,Sadakat,Güvenilirlik,Anlayıştır.",
                  "Yengeç burcunun en nefret ettiği şeyler;Duygularıyla alay edilmesi,Ailenin önemsenmemesi,BencillikiEşyalarının izinsiz kullanılmasıdır.",
				  "İlk akla gelen tipik özellik,kısa boydur.Dar ve düşük olabilen omuzlar,geniş olabilen basenler,özellikle göbekten kilo alma ihtimali,yuvarlak elmacık kemiklerine doğru genişleyen bir yüz şekli,ay şeklinde kaşlar,badem şeklinde gözler, uzun gür kirpikler yengeç burcunun özelliklerindendir ."]


def taurus():
    """Boğa burcu hakkında genel bilgiler burada tutulmakta"""
    bull_general = "Sembolü: Boğa \n Elementi: Toprak \n Niteliği: Sabit \n Yönetici gezegeni: Venüs (güzelliğin ve aşkın gezegeni) \n Renk: Yeşil ve pembe" \
               "Uğurlu sayılar: 6, 4 \n Uğurlu taşları: Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşim " \
               "\n Olumlu özellikleri: Sabırlı, düzenli, yardımcı, romantik, özenli ve adanmış" \
               "\n Olumsuz özellikleri: Fazla hoşgörülü, inatçı, tembel, fazla ihtiyatlı" \
               "\n En sevdiği şeyler: Fotoğraf, dağlar, güzel müzik, gurme yemek, yemek pişirmek, bahçecilik, romans ve kaliteli giysiler" \
               "\n Nefret ettiği şeyler: Acele ettirilmek, parayı israf etmek, kirli şeyler, oteller, ani değişiklikler, engeller ve güvensizlik " \
                "\n"
    print(bull_general)
    mainMenu()

def leo():
    """Aslan burcu hakkında genel bilgiler burada tutulmakta"""
    lion_general =  "Sembolü: Aslan \n Elementi: Ateş \n Niteliği: Sabit \n Yönetici Gezegeni: Güneş \n Renk: Altın Sarısı" \
                    "Uğurlu Sayılar : 5,4 \n Uğurlu Taşlar: Kristal Kuvars, akik, Kehribar \n  " \
                    "\n Olumlu Özellikleri :Lider Kişilik, Hoşgörü , Yardımseverlik , Çalışkanlık ,Azimlilik,sadık, koruyucu, dobra, eğlenceli" \
                    " \n Olumsuz Özellikleri: Kibirli , Küstah, özensiz, taş kalpli, kıskanç, saldırgan" \
                    "\n En Sevdiği Şeyler: Eğlence, Enerjik Şeyler , Spor yapmak,Kameralar, şarkı söylemek, yakınlık kurmak, iltifat, güzel kıyafetler,"\
                    "\n Nefret Ettiği Şeyler:Görmezden gelinmek, yavan yemekler, yalnız kalmak, vedalar, kral-kraliçe muamelesi görmemek "
    print(lion_general)
    mainMenu()

def cancer():
    """Yengeç burcu hakkında bilgiler burada tutulmakta"""
    cancer_general = " Sembolü: Yengeç \n Elementi: Su \n Niteliği: Kardinal(öncü) \n Yönetici gezegeni: Ay (duyguları ve ruhsal durumları yöneten gök cismi) \n Renk: Beyaz" \
                "Uğurlu sayılar: 2, 3 \n Uğurlu taşları: Akuamarin, Ay taşı, Kuvars kristali, Safir Taşı, Zümrüt" \
                "\n Olumlu özellikleri: Yardımsever, sabırlı, merhametli, anaç, romantik, yaratıcı" \
                "\n Olumsuz özellikleri: Dedikoducu, burnu havada, ketum, aşırı duyarlı, fazla rekabetçi" \
                "\n En sevdiği şeyler: Gurme yemekler, salon sporları, ev partileri, çocuklar, müze ve sanat galeriler, evde yapılan hobiler, denize girmek, sevdiklerine yardım etmek" \
                "\n Nefret ettiği şeyler: Pejmürde giysiler, uluorta konuşmak, acele ettirilmek, yabancı insanlar, özel hayatını anlatmak"
    print(cancer_general)
    mainMenu()

def gemini():
    """İkizler burcu hakkında genel bilgiler burada tutulmakta"""
    gemini_general = " Sembolü: İkizler \n Elementi: Hava \n Niteliği: Değişken \n Yönetici gezegeni: Merkür (iletişim ve haberleşmenin gezegeni) \n Renk: Açık yeşil, sarı" \
                 "Uğurlu sayılar: 5, 7 \n Uğurlu taşları: Akuamarin, Akik, Topaz, Sitrin, Turmalin" \
                 "\n Olumlu özellikleri: Etkileyici, özgün, iş bilen, alımlı, akıllı, maceracı" \
                 "\n Olumsuz özellikleri: Vesveseli, dengesiz, iki yüzlü, yargılayıcı, depresif" \
                 "\n En sevdiği şeyler: Müzik, kitaplar, dergiler, sohbet etmek, kısa gezintiler" \
                 "\n Nefret ettiği şeyler: Yalnız olmak, sınırlandırılmak, tekrar ve rutin, dar görüşlü insanlar, geleneksel moda, otorite figürleri, sessizlik"
    print(gemini_general)
    mainMenu()

def forLoop():
    """ "This is the final count down" adlı şarkıdan aklınıza gelsin """
    print("Menüye dönmek için kalan süre")
    for number in range(3, 0,-1):
        time.sleep(1)
        print("{}".format(number))

def baseQuestionsShow(bqs,bas):
    """Burçlar hakkında 10 soru buradan ekrana yazdırılıyor bqs: base question selection(ana soru seçimi), bas: base answer selection"""
    print("{} Burcun hakkındaki sorular bunlar: ".format(prjName))
    for word in bqs:
        time.sleep(0.50)
        print(word)
    time.sleep(0.80)
    print("{} Hangi soruyu seçmek istersin? ".format(prjName))
    userInput = input("User: ")
    horoscopeQuestion(bas,userInput)

def horoscopeQuestion(bq,inp):
    """Sorulan 10 soru hakkında cevap seçimi"""
    if inp == "1":
        print(bq[0])
    elif inp == "2":
        print(bq[1])
    elif inp == "3":
        print(bq[2])
    elif inp == "4":
        print(bq[3])
    elif inp == "5":
        print(bq[4])
    elif inp == "6":
        print(bq[5])
    elif inp == "7":
        print(bq[6])
    elif inp == "8":
        print(bq[7])
    elif inp == "9":
        print(bq[8])
    elif inp == "10":
        print(bq[9])
    time.sleep(3)
    mainMenu()
    forLoop()


def mainMenu():
    """Menü kontrol"""
    print("{} Menüye dönmek istersen evet yaz".format(prjName))
    userInput =input("Kullanıcı: ")
    if userInput.lower() == "evet":
        return
    if userInput.lower() == "hayır":
        pass
    else:
        print("{} Programı bitirmek istediğine emin misin ?".format(prjName))
        userInput =input("Kullanıcı: ")
        if userInput.lower() == "evet":
            print("{} Üzücü :'( görüşmek üzere...".format(prjName))
            quit()
