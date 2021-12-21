import time

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

def forLoop():
    for x in range(1, 4):
        time.sleep(1)
        print("Menüye dönülüyor: {}\n".format(x))

