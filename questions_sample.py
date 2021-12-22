import time
prjName = 'Project X:'
baseQuestionsTaurus = ["1- Boğa burcunun yönetici gezegeni nedir?",
                       "2- Boğa burcunun sevdiği renkler nelerdir?"]

baseAnswersTaurus = ["Venüs gezegeni boğa burcunun yönetici gezegenidir.",
                     "Boğa burcunun sevdiği renkler yeşil ve pembedir."]
def taurus():
    bull_general = "Sembolü: Boğa \n Elementi: Toprak \n Niteliği: Sabit \n Yönetici gezegeni: Venüs (güzelliğin ve aşkın gezegeni) \n Renk: Yeşil ve pembe" \
               "Uğurlu sayılar: 6, 4 \n Uğurlu taşları: Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşim " \
               "\n Olumlu özellikleri: Sabırlı, düzenli, yardımcı, romantik, özenli ve adanmış" \
               "\n Olumsuz özellikleri: Fazla hoşgörülü, inatçı, tembel, fazla ihtiyatlı" \
               "\n En sevdiği şeyler: Fotoğraf, dağlar, güzel müzik, gurme yemek, yemek pişirmek, bahçecilik, romans ve kaliteli giysiler" \
               "\n Nefret ettiği şeyler: Acele ettirilmek, parayı israf etmek, kirli şeyler, oteller, ani değişiklikler, engeller ve güvensizlik " \
                "\n"
    print(bull_general)
    print("{} Menüye dönmek ister misin?".format(prjName))
    forLoop()

def leo():
    lion_general =  "Sembolü: Aslan \n Elementi: Ateş \n Niteliği: Sabit \n Yönetici Gezegeni: Güneş \n Renk: Altın Sarısı" \
                    "Uğurlu Sayılar : 5,4 \n Uğurlu Taşlar: Kristal Kuvars, akik, Kehribar \n  " \
                    "\n Olumlu Özellikleri :Lider Kişilik, Hoşgörü , Yardımseverlik , Çalışkanlık ,Azimlilik,sadık, koruyucu, dobra, eğlenceli" \
                    " \n Olumsuz Özellikleri: Kibirli , Küstah, özensiz, taş kalpli, kıskanç, saldırgan" \
                    "\n En Sevdiği Şeyler: Eğlence, Enerjik Şeyler , Spor yapmak,Kameralar, şarkı söylemek, yakınlık kurmak, iltifat, güzel kıyafetler,"\
                    "\n Nefret Ettiği Şeyler:Görmezden gelinmek, yavan yemekler, yalnız kalmak, vedalar, kral-kraliçe muamelesi görmemek "
    print(lion_general)
    forLoop()

def cancer():
    cancer_general = " Sembolü: Yengeç \n Elementi: Su \n Niteliği: Kardinal(öncü) \n Yönetici gezegeni: Ay (duyguları ve ruhsal durumları yöneten gök cismi) \n Renk: Beyaz" \
                "Uğurlu sayılar: 2, 3 \n Uğurlu taşları: Akuamarin, Ay taşı, Kuvars kristali, Safir Taşı, Zümrüt" \
                "\n Olumlu özellikleri: Yardımsever, sabırlı, merhametli, anaç, romantik, yaratıcı" \
                "\n Olumsuz özellikleri: Dedikoducu, burnu havada, ketum, aşırı duyarlı, fazla rekabetçi" \
                "\n En sevdiği şeyler: Gurme yemekler, salon sporları, ev partileri, çocuklar, müze ve sanat galeriler, evde yapılan hobiler, denize girmek, sevdiklerine yardım etmek" \
                "\n Nefret ettiği şeyler: Pejmürde giysiler, uluorta konuşmak, acele ettirilmek, yabancı insanlar, özel hayatını anlatmak"
    print(cancer_general)

def gemini():
    gemini_general = " Sembolü: İkizler \n Elementi: Hava \n Niteliği: Değişken \n Yönetici gezegeni: Merkür (iletişim ve haberleşmenin gezegeni) \n Renk: Açık yeşil, sarı" \
                 "Uğurlu sayılar: 5, 7 \n Uğurlu taşları: Akuamarin, Akik, Topaz, Sitrin, Turmalin" \
                 "\n Olumlu özellikleri: Etkileyici, özgün, iş bilen, alımlı, akıllı, maceracı" \
                 "\n Olumsuz özellikleri: Vesveseli, dengesiz, iki yüzlü, yargılayıcı, depresif" \
                 "\n En sevdiği şeyler: Müzik, kitaplar, dergiler, sohbet etmek, kısa gezintiler" \
                 "\n Nefret ettiği şeyler: Yalnız olmak, sınırlandırılmak, tekrar ve rutin, dar görüşlü insanlar, geleneksel moda, otorite figürleri, sessizlik"
    print(gemini_general)

def forLoop():
    print("Menüye dönmek için kalan süre")
    for number in range(3, 0,-1):
        time.sleep(1)
        print("{}".format(number))

def baseQuestionsShow(bqt):
    print("{} Burcun hakkındaki sorular bunlar: ".format(prjName))
    for word in bqt:
        time.sleep(0.50)
        print(word)
    time.sleep(0.80)
    print("{} Hangi soruyu seçmek istersin? ".format(prjName))
    userInput = input("User: ")
    horoscopeQuestion(baseAnswersTaurus,userInput)

def horoscopeQuestion(bq,inp):
    if inp == "1":
        print(bq[0])
    elif inp == "2":
        print(bq[1])
    time.sleep(3)
    forLoop()
