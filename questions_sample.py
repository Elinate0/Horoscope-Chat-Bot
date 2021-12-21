import time
baseQuestionsTaurus = {"1- Boğa burcunun yönetici gezegeni nedir?": "Venüs gezegeni boğa burcunun yönetici gezegenidir.",
                       "2- Boğa burcunun sevdiği renkler nelerdir?": "Boğa burcunun sevdiği renkler yeşil ve pembedir.",
                       "3- Boğa burcunun olumlu özellikleri nelerdir?":"Boğa burcu sabırlı, düzenli, yardımcı, romantik, özenli ve adanmıştır.",
                       "4- Boğa burcunun olumsuz özellikleri nelerdir?": "Boğa burcu fazla hoşgörülü, inatçı, tembel ve fazal ihtiyatlıdır.",
                       "5- Boğa burcunun sevdiği aktiviteler nelerdir?": "Müzik dinlemek, yemek pişirmek, bahçıvanlık ve spor yapmaktır.",
                       "6- Boğa burcunun sevmediği durumlar nelerdir?": "Boğa burcu acele ettirilmeyi, paranın israf edilmesini ve ani değişiklikleri sevmemektedir.",}

def taurus():
    bull_general = "Sembolü: Boğa \n Elementi: Toprak \n Niteliği: Sabit \n Yönetici gezegeni: Venüs (güzelliğin ve aşkın gezegeni) \n Renk: Yeşil ve pembe" \
               "Uğurlu sayılar: 6, 4 \n Uğurlu taşları: Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşim " \
               "\n Olumlu özellikleri: Sabırlı, düzenli, yardımcı, romantik, özenli ve adanmış" \
               "\n Olumsuz özellikleri: Fazla hoşgörülü, inatçı, tembel, fazla ihtiyatlı" \
               "\n En sevdiği şeyler: Fotoğraf, dağlar, güzel müzik, gurme yemek, yemek pişirmek, bahçecilik, romans ve kaliteli giysiler" \
               "\n Nefret ettiği şeyler: Acele ettirilmek, parayı israf etmek, kirli şeyler, oteller, ani değişiklikler, engeller ve güvensizlik " \
                "\n Menüye dönülüyor" \
                "\n"
    print(bull_general)
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
    for x in range(1, 4):
        time.sleep(1)
        print("Menüye dönülüyor: {}\n".format(x))

def baseQuestionsShow(inp,bqt):
    for word in bqt.keys():
        print(word)
    print("Hangi soruyu seçmek istersin? ")
    userInput = input("User: ")
    horoscopeQuestion(,userInput)

def horoscopeQuestion(bq,inp):
    if inp == "1":
        print(bq.)
    elif inp == "2":
        print(bq.get("2- Boğa burcunun sevdiği renkler nelerdir?"))
    elif inp == "3":
        print(bq.get("3- Boğa burcunun olumlu özellikleri nelerdir?"))
    elif inp == "4":
        print(bq.get("4- Boğa burcunun olumsuz özellikleri nelerdir?"))

