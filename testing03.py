from fuzzywuzzy import fuzz
import requests

resp = requests.get(url="https://gist.githubusercontent.com/Elinate0/b92b7552f1a65bab57b1d70547a0d54a/raw/79e8280fc3316ba112563a4f29102ba994d1e0d9/Questions.json")
baseQuestionsTaurus = resp.json()



baseAnswersTaurus = ["Venüs gezegeni boğa burcunun yönetici gezegenidir.", #0
                     "Boğa burcunun sevdiği renkler yeşil ve pembedir.",#1
                     "Boğa burcu sabırlı, düzenli, yardımcı, romantik, özenli ve adanmıştır.",#2
                     "Boğa burcu fazla hoşgörülü, inatçı, tembel ve fazal ihtiyatlıdır.",#3
                     "Boğa burcunun elementi topraktır.",#4
                     "Boğa burcunun niteliği sabittir.",#5
                     "Boğa burcunun uğurlu sayıları 6 ve 4.",#6
                     "Boğa burcunun uğurlu taşları Turkuaz taşı, Topaz taşı, Pembe Kuvars, Safir ve Yeşimdir.",#7
                     "Boğa burcunun en sevdiği şeyler; Ziynet eşyaları,Moda,Sürprizlerdir",#8
                     "Boğa burcunun en nefret ettiği şeyler;Değişim,Risk almak,Acele Ettirilmek,Güvencesiz kalmaktır.",]#9
print("Seçmiş olduğunuz burç hakkında: \n yönetici gezegeni, \n sevdiği renkleri, \n olumlu yönlerini, \n olumsuz yönlerini, \n elementini, \n nitelikleri, \n uğurlu sayısı, \n uğurlu taşı, \n sevdiği şeyler, \n sevmediği şeyler,"
      "\nkonuları içeren sorular sorabilirsiniz.")
c = input("Soru: ")

def testfunc(a):
    test = False
    while test == False:
        number = a
        if fuzz.token_set_ratio(baseQuestionsTaurus[number], c.lower())  >= 91:
            test = True
            print("İncelenen soru sayısı: "+str(a))
            if a > 181 and a <= 241:
                print(baseAnswersTaurus[9])
            elif a > 145 and a <= 181:
                print(baseAnswersTaurus[8])
            elif a > 121 and a <= 145:
                print(baseAnswersTaurus[7])
            elif a > 85 and a <= 121:
                print(baseAnswersTaurus[6])
            elif a > 69 and a <= 85:
                print(baseAnswersTaurus[5])
            elif a > 59 and a <= 69:
                print(baseAnswersTaurus[4])
            elif a > 45 and a <= 59:
                print(baseAnswersTaurus[3])
            elif a > 31 and a <= 45:
                print(baseAnswersTaurus[2])
            elif a > 10 and a <= 31:
                print(baseAnswersTaurus[1])
            elif a <= 10:
                print(baseAnswersTaurus[0])
        elif test == False:
            a+=1
        elif number == 242:
            print("Söylediğinizi anlayamıyorum.")
            quit()


testfunc(0)

