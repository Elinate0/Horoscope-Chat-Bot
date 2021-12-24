from fuzzywuzzy import fuzz
baseQuestionsTaurus = ["boğa burcunun yönetici gezegeni nedir?",#0 Yönetici gezegen başlangıç
                       "boğa burcunun gezegeni nedir?",
                       "boğa burcu hangi gezegenindir?",
                       "boğa burcu hangi yönetici gezegeninindir?",
                       "boğa burcu nedir gezegeni?",
                       "boğa burcunun nedir gezegeni?",
                       "boğa burcu gezegeni hangisidir?",
                       "boğa burcu gezegeni nedir?",
                       "boğa burcu hangi gezegene aittir?",
                       "boğa burcu hangi yönetici gezegene aittir?",
                       "boğa burcu hangi yönetici gezegenine aittir?", #10 Yönetici gezegen bitiş
                       "boğa burcu rengi nedir?", #11 Renkler başlangıç
                       "boğa burcunun rengi nelerdir?",
                       "boğa burcunun sevdiği renkler nelerdir?",
                       "boğa burcu renkleri nelerdir?",
                       "boğa burcu hangi renklerden hoşlanır?",
                       "boğa burcunun rengi nedir?",
                       "boğa burcunun hoşlandığı renkler nelerdir?",
                       "boğa burcunun beğendiği renk nedir?",
                       "boğa burcunun beğendiği renkler nedir?",
                       "boğa burcunun beğnediği renkler nelerdir?",
                       "boğa burcunun beğendiği renk hangisidir?",
                       "boğa burcunun beğendiği renkler hangileridir?",
                       "boğa burcunun rengi hangisidir?",
                       "boğa burcu nedir rengi?",
                       "boğa burcunun nedir rengi?",
                       "boğa burcunun nedir renkleri",
                       "boğa burcu hangi renkten hoşlanır?",
                       "boğa burcunun sevdiği renk nedir?",
                       "boğa burcunun sevdiği renk hangisidir?",
                       "boğa burcunun sevdiği renkler hangisidir?",
                       "boğa burcunun sevdiği renkler hangileridir?", #31 Renkler bitiş
                       "boğa burcunun olumlu özellikleri nelerdir?", #32 Olumlu özellikler başlangıcı
                       "boğa burcu olumlu özellikleri nedir?",
                       "boğa burcu olumlu özelliği nedir?",
                       "boğa burcunun olumlu özellikleri hangileridir?",
                       "boğa burcunun olumlu yönleri nedir?",
                       "boğa burcunun olumlu yönleri nelerdir?",
                       "boğa burcu olumlu yönleri nedir?",
                       "boğa burcunun olumlu yönü nedir?",
                       "boğa burcu olumlu yönü nedir?",
                       "boğa burcunun olumlu yönü nelerdir?",
                       "boğa burcu nedir olumlu özelliği?",
                       "boğa burcu nedir olumlu özellikleri?",
                       "boğa burcu nedir olumlu yönleri?",
                       "boğa burcu nelerdir olumlu yönleri?", #45 olumlu özellikler bitiş
                       "boğa burcunun olumsuz özellikleri nelerdir?", #46 olumsuz özellikler başlangıç
                       "boğa burcu olumsuz özellikleri nedir?",
                       "boğa burcu olumsuz özelliği nedir?",
                       "boğa burcunun olumsuz özellikleri hangileridir?",
                       "boğa burcunun olumsuz yönleri nedir?",
                       "boğa burcunun olumsuz yönleri nelerdir?",
                       "boğa burcu olumsuz yönleri nedir?",
                       "boğa burcunun olumsuz yönü nedir?",
                       "boğa burcu olumsuz yönü nedir?",
                       "boğa burcunun olumsuz yönü nelerdir?",
                       "boğa burcu nedir olumsuz özelliği?",
                       "boğa burcu nedir olumsuz özellikleri?",
                       "boğa burcu nedir olumsuz yönleri?",
                       "boğa burcu nelerdir olumsuz yönleri?", #59 Olumsuz özellikler bitiş
                       "boğa burcu elementi nedir?", #60 Elementi özellikler başlangıç
                       "boğa burcu elementleri nelerdir?",
                       "boğa burcunun elementleri nelerdir?",
                       "boğa burcunun elementi nedir?",
                       "boğa burcu elementi hangisidir",
                       "boğa burcu elementleri hangisidir?",
                       "boğa burcunun elementi hangisidir?",
                       "boğa burcunun nedir elementi?",
                       "boğa burcu nedir elementi?",
                       "boğa burcu nelerdir elementleri?", #69 Elementi bitiş
                       "boğa burcunun niteliği nedir?", #70 Nitelik başlangıç
                       "boğa burcunun nitelikleri nedir?",
                       "boğa burcu niteliği nedir?",
                       "boğa burcu nitelikleri nelerdir?",
                       "boğa burcu nitelileri nedir?",
                       "boğa burcu niteliği nelerdir",
                       "boğa burcunun nitelikleri nelerdir?",
                       "boğa burcunun niteliği nelerdir?",
                       "boğa burcu nedir niteliği?",
                       "boğa burcu nedir nitelikleri?",
                       "boğa burcu nelerdir nitelikleri?",
                       "boğa burcu nelerdir niteliği?",
                       "boğa burcunun nedir niteliği?",
                       "boğa burcunun nelerdir niteliği?",
                       "boğa burcunun nedir nitelikleri?",
                       "boğa burcunun nelerdir nitelikleri?", #85 Nitelik bitiş
                       "boğa burcu uğurlu sayısı nedir?", #86 Uğurlu sayı başlangıç
                       "boğa burcu uğurlu sayısı nelerdir?",
                       "boğa burcu uğurlu sayıları nedir?",
                       "boğa burcu uğurlu sayıları nelerdir?",
                       "boğa burcu sayısı nedir?",
                       "boğa burcu sayısı nelerdir?",
                       "boğa burcu sayıları nedir?",
                       "boğa burcu sayıları nelerdir?",
                       "boğa burcu şanslı sayısı nedir?",
                       "boğa burcu şanslı sayısı nelerdir?",
                       "boğa burcu şanslı sayıları nedir?",
                       "boğa burcu şanslı sayıları nelerdir?",
                       "boğa burcunun uğurlu sayısı nedir?",
                       "boğa burcunun uğurlu sayısı nelerdir?",
                       "boğa burcunun uğurlu sayıları nedir?",
                       "boğa burcunun uğurlu sayıları nelerdir?",
                       "boğa burcunun sayısı nedir?",
                       "boğa burcunun sayısı nelerdir?",
                       "boğa burcunun sayıları nedir?",
                       "boğa burcunun sayıları nelerdir?",
                       "boğa burcunun şanslı sayısı nedir?",
                       "boğa burcunun şanslı sayısı nelerdir?",
                       "boğa burcunun şanslı sayıları nedir?",
                       "boğa burcunun şanslı sayıları nelerdir?",
                       "boğa burcu nedir şanslı sayısı?",
                       "boğa burcu nedir şanslı sayıları?",
                       "boğa burcunun nedir şanslı sayısı?",
                       "boğa burcunun nedir şanslı sayıları?",
                       "boğa burcu nedir sayısı?",
                       "boğa burcu nedir sayıları?",
                       "boğa burcunun nedir sayısı?",
                       "boğa burcunun nedir sayıları?",
                       "boğa burcu nedir uğurlu sayısı?",
                       "boğa burcu nedir uğurlu sayıları?",
                       "boğa burcunun nedir uğurlu sayısı?",
                       "boğa burcunun nedir uğurlu sayıları?", #121 Uğurlu sayı bitiş
                       "boğa burcu uğurlu taşı nedir?", #122 Uğurlu sayı başlangıç
                       "boğa burcu uğurlu taşı nelerdir?",
                       "boğa burcu uğurlu taşları nedir?",
                       "boğa burcu uğurlu taşları nelerdir?",
                       "boğa burcu taşı nedir?",
                       "boğa burcu taşı nelerdir?",
                       "boğa burcu taşları nedir?",
                       "boğa burcu taşları nelerdir?",
                       "boğa burcunun uğurlu taşı nedir?",
                       "boğa burcunun uğurlu taşı nelerdir?",
                       "boğa burcunun uğurlu taşları nedir?",
                       "boğa burcunun uğurlu taşları nelerdir?",
                       "boğa burcunun taşı nedir?",
                       "boğa burcunun taşı nelerdir?",
                       "boğa burcunun taşları nedir?",
                       "boğa burcunun taşları nelerdir?",
                       "boğa burcu nedir uğurlu taşı?",
                       "boğa burcu nedir uğurlu taşları?",
                       "boğa burcu nedir taşı?",
                       "boğa burcu nedir taşları?",
                       "boğa burcunun nedir uğurlu taşı?",
                       "boğa burcunun nedir uğurlu taşları?",
                       "boğa burcunun nedir taşı?",
                       "boğa burcunun nedir taşları?", #145 uğurlu taş bitiş
                       "boğa burcu en sevdiği şeyler nedir?", #146 Sevdiği şeyler başlangıç
                       "boğa burcu en sevdiği şeyler nelerdir?",
                       "boğa burcu en sevdiği şey nedir?",
                       "boğa burcu en sevdiği şey nelerdir?",
                       "boğa burcu sevdiği şeyler nedir?",
                       "boğa burcu sevdiği şeyler nelerdir?",
                       "boğa burcu sevdiği şey nedir?",
                       "boğa burcu sevdiği şey nelerdir?",
                       "boğa burcu hoşlandığı şeyler nedir?",
                       "boğa burcu hoşlandığı şeyler nelerdir?",
                       "boğa burcu hoşlandığı şey nedir?",
                       "boğa burcu hoşlandığı şey nelerdir?",
                       "boğa burcunun en sevdiği şeyler nedir?",
                       "boğa burcunun en sevdiği şeyler nelerdir?",
                       "boğa burcunun en sevdiği şey nedir?",
                       "boğa burcunun en sevdiği şey nelerdir?",
                       "boğa burcunun sevdiği şeyler nedir?",
                       "boğa burcunun sevdiği şeyler nelerdir?",
                       "boğa burcunun sevdiği şey nedir?",
                       "boğa burcunun sevdiği şey nelerdir?",
                       "boğa burcunun hoşlandığı şeyler nedir?",
                       "boğa burcunun hoşlandığı şeyler nelerdir?",
                       "boğa burcunun hoşlandığı şey nedir?",
                       "boğa burcunun hoşlandığı şey nelerdir?",
                       "boğa burcu nedir en sevdiği şey?",
                       "boğa burcu nedir en sevdiği şeyler?",
                       "boğa burcu nedir sevdiği şey?",
                       "boğa burcu nedir sevdiği şeyler?",
                       "boğa burcu nedir hoşlandığı şey?",
                       "boğa burcu nedir hoşlandığı şeyler?",
                       "boğa burcunun nedir en sevdiği şey?",
                       "boğa burcunun nedir en sevdiği şeyler?",
                       "boğa burcunun nedir sevdiği şey?",
                       "boğa burcunun nedir sevdiği şeyler?",
                       "boğa burcunun nedir hoşlandığı şey?",
                       "boğa burcunun nedir hoşlandığı şeyler?",#181 Hoşlandığı şeyler bitiş
                       "boğa burcu nefret ettiği şey nedir?", #182 Hoşlanmadığı şeyler başlangıç
                       "boğa burcu nefret ettiği şey nelerdir?",
                       "boğa burcu nefret ettiği şeyler nedir?",
                       "boğa burcu nefret ettiği şeyler nelerdir?",
                       "boğa burcu sevmediği şey nedir?",
                       "boğa burcu sevmediği şey nelerdir?",
                       "boğa burcu sevmediği şeyler nedir?",
                       "boğa burcu sevmediği şeyler nelerdir?",
                       "boğa burcu hoşlanmadığı şey nedir?",
                       "boğa burcu hoşlanmadığı şey nelerdir?",
                       "boğa burcu hoşlanmadığı şeyler nedir?",
                       "boğa burcu hoşlanmadığı şeyler nelerdir?",
                       "boğa burcunun nefret ettiği şey nedir?",
                       "boğa burcunun nefret ettiği şey nelerdir?",
                       "boğa burcunun nefret ettiği şeyler nedir?",
                       "boğa burcunun nefret ettiği şeyler nelerdir?",
                       "boğa burcunun sevmediği şey nedir?",
                       "boğa burcunun sevmediği şey nelerdir?",
                       "boğa burcunun sevmediği şeyler nedir?",
                       "boğa burcunun sevmediği şeyler nelerdir?",
                       "boğa burcunun hoşlanmadığı şey nedir?",
                       "boğa burcunun hoşlanmadığı şey nelerdir?",
                       "boğa burcunun hoşlanmadığı şeyler nedir?",
                       "boğa burcunun hoşlanmadığı şeyler nelerdir?",
                       "boğa burcu en nefret ettiği şey nedir?",
                       "boğa burcu en nefret ettiği şey nelerdir?",
                       "boğa burcu en nefret ettiği şeyler nedir?",
                       "boğa burcu en nefret ettiği şeyler nelerdir?",
                       "boğa burcu en sevmediği şey nedir?",
                       "boğa burcu en sevmediği şey nelerdir?",
                       "boğa burcu en sevmediği şeyler nedir?",
                       "boğa burcu en sevmediği şeyler nelerdir?",
                       "boğa burcu en hoşlanmadığı şey nedir?",
                       "boğa burcu en hoşlanmadığı şey nelerdir?",
                       "boğa burcu en hoşlanmadığı şeyler nedir?",
                       "boğa burcu en hoşlanmadığı şeyler nelerdir?",
                       "boğa burcunun en nefret ettiği şey nedir?",
                       "boğa burcunun en nefret ettiği şey nelerdir?",
                       "boğa burcunun en nefret ettiği şeyler nedir?",
                       "boğa burcunun en nefret ettiği şeyler nelerdir?",
                       "boğa burcunun en sevmediği şey nedir?",
                       "boğa burcunun en sevmediği şey nelerdir?",
                       "boğa burcunun en sevmediği şeyler nedir?",
                       "boğa burcunun en sevmediği şeyler nelerdir?",
                       "boğa burcunun en hoşlanmadığı şey nedir?",
                       "boğa burcunun en hoşlanmadığı şey nelerdir?",
                       "boğa burcunun en hoşlanmadığı şeyler nedir?",
                       "boğa burcunun en hoşlanmadığı şeyler nelerdir?",
                       "boğa burcu nedir sevmediği şeyler?",
                       "boğa burcu nedir sevmediği şey?",
                       "boğa burcu nedir nefret ettiği şey?",
                       "boğa burcu nedir nefret ettiği şeyler?",
                       "boğa burcu nedir hoşlanmadığı şey?",
                       "boğa burcu nedir hoşlanmadığı şeyler?",
                       "boğa burcu nedir en sevmediği şeyler?",
                       "boğa burcu nedir en sevmediği şey?",
                       "boğa burcu nedir en nefret ettiği şey?",
                       "boğa burcu nedir en nefret ettiği şeyler?",
                       "boğa burcu nedir en hoşlanmadığı şey?",
                       "boğa burcu nedir en hoşlanmadığı şeyler?"] #241 Hoşlanmadığı şeyler bitiş




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
c = input(": ")

def testfunc(a):
    test = False
    while test == False:
        number = a
        if fuzz.token_sort_ratio(baseQuestionsTaurus[number], c)  >= 80:
            test = True
            print(a)
            print(fuzz.token_sort_ratio(baseQuestionsTaurus[64], c))
            print(fuzz.token_sort_ratio(baseQuestionsTaurus[6], c))
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








        else:
            a+=1

testfunc(0)

