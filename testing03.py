from fuzzywuzzy import fuzz
import requests
import json
import time

import questions_sample

questionUrls = {"taurus": "https://gist.githubusercontent.com/Elinate0/b92b7552f1a65bab57b1d70547a0d54a/raw/036bf39011788415da650aa6cd847ad70899948e/Questions.json", "lion": "https://gist.githubusercontent.com/Elinate0/b56313c1f0d9380ae94d4607c80ab061/raw/c37c5e148819be5643a500e5e0039b4da116bdcb/lionQuestions.json", "gemini": "https://gist.githubusercontent.com/Elinate0/04ff455fc78f1eb38dd303a2ca400759/raw/8171078d826350df49ae5e7863bbe0daa9e59729/cancerQuestions.json", "cancer": "https://gist.githubusercontent.com/Elinate0/a1a77e95d87087979d9945185a765f10/raw/27785bb4c3da807eb6c0508c87c2922c17eb72cf/geminiQuestions.json"}


def fetchData(horoscope, type):
    if type == "questions":
        if questionUrls[horoscope]:
            reqUrl = questionUrls[horoscope]
        else:
            reqUrl = False
        if reqUrl:
            request = requests.get(url=reqUrl)
            return request.json()
        else:
            return []
    else:
        if horoscope == "taurus":
            answers = [
                     "Venüs gezegeni boğa burcunun yönetici gezegenidir.", #0
                     "Boğa burcunun sevdiği renkler yeşil ve pembedir.",#1
                     "Boğa burcu sabırlı, düzenli, yardımcı, romantik, özenli ve adanmıştır.",#2
                     "Boğa burcu fazla hoşgörülü, inatçı, tembel ve fazla ihtiyatlıdır.",#3
                     "Boğa burcunun elementi topraktır.",#4
                     "Boğa burcunun niteliği sabittir.",#5
                     "Boğa burcunun uğurlu sayıları 6 ve 4.",#6
                     "Boğa burcunun uğurlu taşları Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşimdir.",#7
                     "Boğa burcunun en sevdiği şeyler; Ziynet eşyaları,Moda,Sürprizlerdir",#8
                     "Boğa burcunun en nefret ettiği şeyler;Değişim,Risk almak,Acele Ettirilmek,Güvencesiz kalmaktır.",#9
                     "Boğa burcu ile en iyi anlaşan burçlar;Başak ve Oğlakdır",#10
                     "Boğa burcu ile anlaşamayan burçlar;Kova, Aslan ve Akreptir.",#11
                     "Boğa burcunun uğurlu günü cumadır. ",#12
                     "Şöhret olmaya en uzak burç olan Boğa’lar, çok çalışmayı sever ve alacakları karşılıktan ziyade elde edecekleri sonuca odaklanırlar. Boğa’lardan iyi aşçı, zanaatkâr, iş adamı, bankacı olur.",#13
                     "Boğa burcu orta boylu, etli, tıknaz hatta göbeklidir. Kol ve bacaklar kısa ve tombuldur.",#14
                     "Kanuni Sultan Süleyman, Kraliçe II. Elizabeth, Cem Yılmaz, Ozan Güven, Tolga Çevik, Robert Pattinson, Megan Fox ve Penelope Cruz boğa burcu olan tanınmış kişilerdir. ",#15
                     "Boğa burcuna sahip olan kişiler 21 Nisan - 20 Mayıs tarihlerinin arasında doğmuş olan kişilerdir."#16
                       ]
        elif horoscope == "lion":
            answers = [
                       "Güneş gezegeni aslan burcunun yönetici gezegenidir.",
                       "Aslan burcunun sevdiği renkler altın sarısıdır.",
                       "Aslan burcu; Hoşgörülü , Yardımsever , Çalışkan ,Azimli,sadık, koruyucu, dobra, eğlencelidir .",
                       "Aslan burcu; Kibirli , Küstah, özensiz, taş kalpli, kıskanç, saldırgandır .",
                       "Aslan  burcunun elementi ateştir.",
                       "Aslan burcunun niteliği sabittir.",
                       "Aslan burcunun uğurlu sayıları 4 ve 5'dir.",
                       "Aslan burcunun uğurlu taşları; Kristal Kuvars, akik, Kehribardır.",
                       "Aslan burcunun en sevdiği şeyler;Eğlence, Enerjik Şeyler , Spor yapmak,Kameralar, şarkı söylemek, yakınlık kurmak, iltifat, güzel kıyafetlerdir.",
                       "Aslan burcunun en nefret ettiği şeyler;Görmezden gelinmek, yavan yemekler, yalnız kalmak, vedalar, kral-kraliçe muamelesi görmemektir.",
                       "Aslan burcu ile en iyi anlaşan burçlar;Yay ve Koçtur",
                       "Aslan burcu ile anlaşamayan burçlar; kova ve boğadır.",
                       "Aslan burcunun uğurlu günü pazardır. ",
                       "Kendilerini yaptıkları işe adayan, sadakat duyguları güçlü olan ve insanları mutlu etmeyi seven Aslan’lar hukukçu ya da aktivist olmaya çok uygundur.",
                       "Boylu poslu, enine boyuna, aslan gibi gösterişli.... ifadesi bu burç insanını iyi tarif eder.Saç,göz,ten rengi açık renk,cilt pembemsi,gözler iri ,yüz büyük ve hatlar köşelidir",
                       "Henry Ford,Madonna,Sezen aksu,Napoleon Bonaparte aslan burcu olan tanınmış kişilerdir. ",
                       "Aslan burcuna sahip olan kişiler 11 Ağustos - 16 Eylül tarihlerinin arasında doğmuş olan kişilerdir."
                        ]
        elif horoscope == "gemini":
            answers = ["Merkür gezegeni ikizler burcunun yönetici gezegenidir.",
                       "ikizler burcunun sevdiği renkler açık yeşil ve sarı.",
                       "İkizler burcu etkileyici, özgün, iş bilen, alımlı, akıllı, maceracıdır.",
                       "İkizler burcu vesveseli, dengesiz, iki yüzlü, yargılayıcı, depresifdir.",
                       "İkizler burcunun elementi havadır.",
                       "İkizler burcunun niteliği değişkendir.",
                       "İkizler burcunun uğurlu sayıları 5 ve 7 dir.",
                       "İkizler burcunun uğurlu taşları  Akuamarin, Akik, Topaz, Sitrin, Turmalindir.",
                       "İkizler burcunun en sevdiği şeyler; Özgürlük,Küçük Hobiler,Kalabalık bir çevre,Yeni bir şey öğrenmedir.",
                       "İkizler burcunun en nefret ettiği şeyler;Yalnızlık,Aşırı sahiplenici kişiler,Telefonunun kurcalanması,Kıskanmak,Bekletilmekdir.",
                       "İkizler burcu ile en iyi anlaşan burçlar; Terazi ve Kovadır",
                       "İkizler burcu ile anlaşamayan burçlar; Başak ve Yaydır.",
                       "İkizler burcunun uğurlu günü çarşambadır. ",
                       "Olaylara farklı açılardan bakabilen İkizler burçları, araştırma, ticaret, iletişim, gazetecilik, eğitim gibi alanlarda çalışmaya uygundur. Rekabetçi yapıları sporda da başarılı olmalarını sağlar.",
                       "İlk akla gelen tipik özellik, incelik, uzunluk ve zayıflıktır. Orta boylu bile olsa kesinlikle zayıftır. Ancak bu zayıflık güçsüzlük demek değildir, aksine kuvvetli ve son derece çeviktir. Kilo almaya uygun olmayan tiplerdir.",
                       "Adile Naşit,Bülent Ersoy, Bob Dylan ikizler burcu olan tanınmış kişilerdir. ",
                       "ikizler burcuna sahip olan kişiler 22 Haziran - 20 Temmuz tarihlerinin arasında doğmuş olan kişilerdir."]
        elif horoscope == "cancer":
            answers = ["Ay gezegeni yengeç burcunun yönetici gezegenidir.",
                       "Yengeç burcunun sevdiği renk beyazdır.",
                       "Yengeç burcu Yardımsever, sabırlı, merhametli, anaç, romantik, yaratıcıdır.",
                       "Yengeç burcu Dedikoducu, burnu havada, ketum, aşırı duyarlı, fazla rekabetçidir.",
                       "Yengeç burcunun elementi sudur.",
                       "Yengeç burcunun niteliği kardinaldir(öncü).",
                       "Yengeç burcunun uğurlu sayıları 2 ve 3'dir.",
                       "Yengeç burcunun uğurlu taşları Akuamarin, Ay taşı, Kuvars kristali, Safir Taşı, Zümrütdür.",
                       "Yengeç burcunun en sevdiği şeyler;Romantizm,Sadakat,Güvenilirlik,Anlayıştır.",
                       "Yengeç burcunun en nefret ettiği şeyler;Duygularıyla alay edilmesi,Ailenin önemsenmemesi,BencillikiEşyalarının izinsiz kullanılmasıdır.",
                       "Yengeç burcu ile en iyi anlaşan burçlar; akrep ve balıktır",
                       "Yengeç burcu ile anlaşamayan burçlar; terazi ve oğlaktır.",
                       "Yengeç burcunun uğurlu günü pazartesidir. ",
                       "Sanatsal vizyonları yüksektir. Kendileri sanatçı olabildikleri gibi sanatı değerlendiren müzecilik, antikacılık, sergi düzenlemesi, editörlük gibi mesleklerde de başarılı olurlar.",
                       "İlk akla gelen tipik özellik,kısa boydur.Dar ve düşük olabilen omuzlar,geniş olabilen basenler,özellikle göbekten kilo alma ihtimali,yuvarlak elmacık kemiklerine doğru genişleyen bir yüz şekli,ay şeklinde kaşlar,badem şeklinde gözler, uzun gür kirpikler yengeç burcunun özelliklerindendir .",
                       "Julio Sezar,Nicola Tesla,Prenses Diana,Tom Cruise,Giorgia Michael yengeç burcu olan tanınmış kişilerdir. ",
                       "Yengeç burcuna sahip olan kişiler 21 Temmuz - 10 Ağustos tarihlerinin arasında doğmuş olan kişilerdir."]
        else:
            answers = []
        return answers

def run(answered, horoscope):
    answers = fetchData(horoscope, "answer")
    questions = fetchData(horoscope, "questions")

    if answered and answered != "first":
        time.sleep(0.80)
        print(answered)
    elif answered != "first":
        print("Anlayamadım")
    time.sleep(0.80)
    print("Seçmiş olduğunuz burç hakkında: \n yönetici gezegeni, \n sevdiği renkleri, \n olumlu yönlerini, \n olumsuz yönlerini, \n elementini, \n nitelikleri, \n uğurlu sayısı, \n uğurlu taşı, \n sevdiği şeyler, \n sevmediği şeyler,"
      "\nkonuları içeren sorular sorabilirsiniz.")
    time.sleep(0.80)
    soru = input("Soru: ")

    for i in range(len(questions)):
        if fuzz.token_set_ratio(questions[i], soru.lower()) >= 91:
            time.sleep(0.80)
            print("İncelenen soru sayısı: "+str(i))
            if i > 454 and i <= 514:
                run(answers[16], horoscope)
                time.sleep(0.80)
            if i > 436 and i <= 454:
                run(answers[15], horoscope)
                time.sleep(0.80)
            if i > 396 and i <= 436:
                run(answers[14], horoscope)
                time.sleep(0.80)
            if i > 370 and i <= 396:
                run(answers[13], horoscope)
                time.sleep(0.80)
            if i > 334 and i <= 370:
                run(answers[12], horoscope)
                time.sleep(0.80)
            if i > 310 and i <= 334:
                run(answers[11], horoscope)
                time.sleep(0.80)
            if i > 261 and i <= 310:
                run(answers[10], horoscope)
                time.sleep(0.80)
            if i > 201 and i <= 261:
                run(answers[9], horoscope)
                time.sleep(0.80)
                break
            if i > 165 and i <= 201:
                run(answers[8], horoscope)
                time.sleep(0.80)
                break
            elif i > 141 and i <= 165:
                run(answers[7], horoscope)
                time.sleep(0.80)
                break
            elif i > 105 and i <= 141:
                run(answers[6], horoscope)
                time.sleep(0.80)
                break
            elif i > 89 and i <= 105:
                run(answers[5], horoscope)
                time.sleep(0.80)
                break
            elif i > 75 and i <= 89:
                run(answers[4], horoscope)
                time.sleep(0.80)
                break
            elif i > 45 and i <= 75:
                run(answers[3], horoscope)
                time.sleep(0.80)
                break
            elif i > 31 and i <= 45:
                run(answers[2], horoscope)
                time.sleep(0.80)
                break
            elif i > 10 and i <= 31:
                run(answers[1], horoscope)
                time.sleep(0.80)
                break
            elif i <= 10:
                run(answers[0], horoscope)
                time.sleep(0.80)
                break
            elif i >= 515:
                run(False, horoscope)
                time.sleep(0.80)
                break
        elif i >= len(questions)-1:
            time.sleep(0.80)
            run(False, horoscope)
            break
