baseQuestions = {"1- Soru örneği 1": "Cevap örneği 1", "2- Soru örneği 2": "Cevap örneği 2", "3- Soru örneği 3":"Cevap örneği 3", "4- Soru örneği 4": "Cevap örneği 4"}

# def test(y): hatalı, henüz alınan değeri bölüp liste içerisindeki keylerde aratamıyoruz.
#     if y.split() in baseQuestions:
#         print("başarılı")

for word in baseQuestions.keys():
    print(word)
print("Hangi soruyu seçmek istersin? ")
x = input("User: ")

#test(x) hatalı, henüz alınan değeri bölüp liste içerisindeki keylerde aratamıyoruz.

if x == "1":
    print(baseQuestions.get("1- Soru örneği 1"))
elif x == "2":
    print(baseQuestions.get("1- Soru örneği 2"))
elif x == "3":
    print(baseQuestions.get("1- Soru örneği 3"))
elif x == "4":
    print(baseQuestions.get("1- Soru örneği 4"))
