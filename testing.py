import random
import time
import questions_sample

prjName = 'Project X:'

helloThereInputs = ("hello", "hi", "greetings", "hey", "hola", "merhaba", "bonjour", "sua s’dei", "hallo", "ciao", "selam")
helloThereResponses = ["hi", "hey", "selam", "hi there", "hello", "Mutluyum! Benimle konuşuyorsun"]
horoscopes = ["boğa", "ikizler", "yengeç", "aslan"]
otherHoroscopes = ("koç","başak","terazi","akrep","yay","oğlak","kova","balık")

def greetings(hti, htr):
    """Bu fonksiyon giriş ekranını temsil etmekte ve kullanıcının girişini hti içerisinde kontrol edip htr içerisinden rastgele cevap vermekte"""
    userInput = input('Kullanıcı: ')
    for word in userInput.split():
        if word.lower() in hti:
            time.sleep(2)
            print("{} ".format(prjName) + random.choice(htr))
            continue
        else:
            print("{} Neyden bahsediyorsun, görgü kurallarına geri dönmem gerekirse önce selam söyle!".format(prjName))
            return greetings(hti, htr)
    print("{0} Umarım kızmazsın fakat şu anda yalnızca boğa, ikizler, yengeç ve aslan burçları hakkında yorum yapabiliyorum.".format(prjName))



def loopGreetings():
    """Bu fonksiyon çok güzel duran bir fonksiyon olmasına karşın henüz kullanmıyoruz"""
    readyForTalk = False
    while readyForTalk == False:
        userInput = input("Kullanıcı: ")
        for word in userInput.split():
            if word in helloThereInputs:
                print("{0} Tekrar {1}".format(prjName, random.choice(helloThereResponses)))
                print("{} KOnuşmaya hazır mısın?".format(prjName, prjName))
            else:
                readyForTalk = True


def trueHoroscopes(choosen):
    """Bu fonksiyon kullanıcnın girdisini kontrol ederek gerekli fonskiyona yönlendirmekte"""
    if choosen == "boğa":
        smp = "taurus"
        loopHoroscope(smp)
    elif choosen == "aslan":
        smp = "leo"
        loopHoroscope(smp)
    elif choosen == "yengeç":
        smp = "cancer"
        loopHoroscope(smp)
    elif choosen == "ikizler":
        smp = "gemini"
        loopHoroscope(smp)

def navigating():
    """Bu fonksiyon kullanıcı fonksiyon içerisinde "4"ü seçtiğinde tekrar burç seçimine yönlendirmekte"""
    print("{} Hangi Burcu Seçmek İstersin?:".format(prjName))
    userInput = input("Kullanıcı: ")
    lowerInput = userInput.lower()
    if userInput.lower() in helloThereInputs:
        print("{0} Tekrar {1}".format(prjName, random.choice(helloThereResponses)))
        return navigating()
    elif userInput.lower() not in helloThereInputs:
        trueHoroscopes(userInput.lower())
    else:
        return navigating()


def loopHoroscope(smp):
    """Bu fonksiyon seçilen burca yönelik opsiyonelleri ve farklı burç girişi için yönlendirmeyi yapmakta"""
    print("Şu anda {} burcundasın".format(smp))
    print("{} Seçtiğin burç hakkında sunmak istediğim üç opsiyonel var, bunlar: \n "
          "Ekrana -- 1 -- yazarak burcun hakkında genen bilgileri öğrenebilirsin."
          "\n Ekrana -- 2 -- yazarak burcun hakkında soru seçimi yapabilirsin."
          "\n Ekrana -- 3 -- yazarak burcun hakkında soru girişi yapabilirsin."
          "\n Ekrana -- 4 -- yazarak farklı bir burç girebilirsin. ".format(prjName))
    loopHoroscopes = ["taurus", "leo"]
    userInput = int(input("Kullanıcı: "))
    if userInput in helloThereInputs:
        print("{0} Tekrar {1}".format(prjName, random.choice(helloThereResponses)))
        return loopHoroscope(smp)
    elif userInput not in range(1, 5):
        print("{0} Tekrar {1}".format(prjName, random.choice(helloThereResponses)))
        return loopHoroscope(smp)
    elif smp == "taurus":
        match userInput:
            case 1:
                questions_sample.taurus()
                time.sleep(1.5)
                return loopHoroscope("taurus")
            case 2:
                print("2")
            case 3:
                print("3")
            case 4:
                navigating()
    elif smp == "leo":
        match userInput:
            case 1:
                questions_sample.leo()
                time.sleep(1.5)
                return loopHoroscope("leo")
            case 2:
                print("2")
            case 3:
                print("3")
            case 4:
                navigating()


greetings(helloThereInputs, helloThereResponses)
print("{} Burcun nedir? ".format(prjName))
readyForMove = False
while readyForMove == False:
    userInput = input("Kullanıcı: ")
    if userInput.lower() in horoscopes:
        readyForMove = True
        trueHoroscopes(userInput.lower())
    elif userInput.lower() in helloThereInputs:
        print("{0} Tekrar {1}".format(prjName, random.choice(helloThereResponses)))
        readyForMove = False
    elif userInput.lower() == "hayır":
        print("{} Üzücü :'( görüşmek üzere...".format(prjName))
        quit()
    elif userInput.lower() in otherHoroscopes:
        print("{} Üzgünüm fakat bu burç hakkında yorum yapamıyorum. Söylemiş olduğum dört burç arasından birisini yazar mısın?".format(prjName))
    else:
        print("{} Lütfen bana burcunu söyler misin?".format(prjName))
