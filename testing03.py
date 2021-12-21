from strsimpy.longest_common_subsequence import LongestCommonSubsequence

lcs = LongestCommonSubsequence()
baseQuestionsTaurus = ["boğa burcunun yönetici gezegeni nedir?", #0
                       "boğa burcu gezegeni nedir?", #1
                       "boğa burcu rengi nedir?", #2
                       "boğa burcunun rengi nelerdir?", #3
                       "boğa burcunun sevdiği renkler nelerdir?", #4
                       "boğa burcu renkleri nelerdir?", #5
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
print("value")
print(lcs.distance(baseQuestionsTaurus[0], c.lower()))
print(lcs.distance(baseQuestionsTaurus[2], c.lower()))
print(lcs.distance(baseQuestionsTaurus[3], c.lower()))
print(lcs.distance(baseQuestionsTaurus[4], c.lower()))
print(lcs.distance(baseQuestionsTaurus[5], c.lower()))
print(lcs.distance(baseQuestionsTaurus[6], c.lower()))
print(lcs.distance(baseQuestionsTaurus[7], c.lower()))
print(lcs.distance(baseQuestionsTaurus[8], c.lower()))
print(lcs.distance(baseQuestionsTaurus[9], c.lower()))
print(lcs.distance(baseQuestionsTaurus[10], c.lower()))
print(lcs.distance(baseQuestionsTaurus[11], c.lower()))


if lcs.distance(baseQuestionsTaurus[0], c) <= 9 or lcs.distance(baseQuestionsTaurus[1], c) <= 9:
    print(baseAnswersTaurus[0])
elif lcs.distance(baseQuestionsTaurus[2], c) <= 7 or lcs.distance(baseQuestionsTaurus[3], c) <= 7\
        or lcs.distance(baseQuestionsTaurus[4], c) <= 9 or lcs.distance(baseQuestionsTaurus[5], c) <= 9:
    print(baseAnswersTaurus[1])
elif lcs.distance(baseQuestionsTaurus[6], c) <= 7 or lcs.distance(baseQuestionsTaurus[7], c) <= 7\
        or lcs.distance(baseQuestionsTaurus[8], c) <= 7:
    print(baseAnswersTaurus[2])
elif lcs.distance(baseQuestionsTaurus[9], c) <= 7 or lcs.distance(baseQuestionsTaurus[10], c) <= 7\
        or lcs.distance(baseQuestionsTaurus[11], c) <= 7:
    print(baseAnswersTaurus[3])
else:
    print("Söylediğinizi anlayamıyorum.")
