from fuzzywuzzy import fuzz
from fuzzywuzzy import process

baseQuestionsTaurus = ["boğa burcunun yönetici gezegeni nedir?", #0
                       "boğa burcu gezegeni nedir?", #1
                       "boğa burcu rengi nedir?", #2
                       "boğa burcunun rengi nelerdir?", #3
                       "boğa burcunun sevdiği renkler nelerdir?", #4
                       "boğa burcu renkleri nelerdir?", #5 #boğa burcu hangi rengi sever ve hangi renkleri sever
                       "boğa burcunun olumlu özellikleri nelerdir?", #6
                       "boğa burcu olumlu özellikleri nedir?", #7
                       "boğa burcu olumlu özelliği nedir?", #8
                       "boğa burcunun olumsuz özellikleri nelerdir?", #9
                       "boğa burcu olumsuz özellikleri nedir?", #10
                       "boğa burcu olumsuz özelliği nedir?",] #11

baseAnswersTaurus = ["Venüs gezegeni boğa burcunun yönetici gezegenidir.",
                     "Boğa burcunun sevdiği renkler yeşil ve pembedir.",
                     "Boğa burcu sabırlı, düzenli, yardımcı, romantik, özenli ve adanmıştır.",
                     "Boğa burcu fazla hoşgörülü, inatçı, tembel ve fazal ihtiyatlıdır.",]
c = input(": ")
print(fuzz.partial_ratio(baseQuestionsTaurus[2], c))
print(fuzz.partial_ratio(baseQuestionsTaurus[3], c))
print(fuzz.partial_ratio(baseQuestionsTaurus[4], c))
print(fuzz.partial_ratio(baseQuestionsTaurus[5], c))
print("\n")
print(fuzz.partial_ratio(baseQuestionsTaurus[0], c))
print(fuzz.partial_ratio(baseQuestionsTaurus[1], c))
print("\n")
print(fuzz.token_sort_ratio(baseQuestionsTaurus[2], c))
print(fuzz.token_sort_ratio(baseQuestionsTaurus[3], c))
print(fuzz.token_sort_ratio(baseQuestionsTaurus[4], c))
print(fuzz.token_sort_ratio(baseQuestionsTaurus[5], c))


if fuzz.partial_ratio(baseQuestionsTaurus[0], c) >= 72 or fuzz.partial_ratio(baseQuestionsTaurus[1], c) >= 72:
    print(baseAnswersTaurus[0])
elif fuzz.partial_ratio(baseQuestionsTaurus[2], c) >= 72 or fuzz.partial_ratio(baseQuestionsTaurus[3], c) >= 72\
        or fuzz.partial_ratio(baseQuestionsTaurus[4], c) >= 72 or fuzz.partial_ratio(baseQuestionsTaurus[5], c) >= 72:
    print(baseAnswersTaurus[1])
elif fuzz.partial_ratio(baseQuestionsTaurus[6], c) >= 72 or fuzz.partial_ratio(baseQuestionsTaurus[7], c) >= 72\
        or fuzz.partial_ratio(baseQuestionsTaurus[8], c) >= 72:
    print(baseAnswersTaurus[2])
elif fuzz.partial_ratio(baseQuestionsTaurus[9], c) >= 72 or fuzz.partial_ratio(baseQuestionsTaurus[10], c) >= 72\
        or fuzz.partial_ratio(baseQuestionsTaurus[11], c) >= 72:
    print(baseAnswersTaurus[3])
else:
    print("Söylediğinizi anlayamıyorum.")

