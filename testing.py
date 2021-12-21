import random
import time
import questions_sample

prjName = 'Project X:'
helloThereInputs = ("hello", "hi", "greetings", "hey", "hola", "merhaba", "bonjour", "sua s’dei", "hallo", "ciao")
helloThereResponses = ["hi", "hey", "nods", "hi there", "hello", "I am glad! You are talking to me"]
horoscopes = ["boğa", "ikizler", "yengeç", "aslan"]

def greetings(hti, htr):
    """Bu fonksiyon kullanıcının girdisini hti içerisinde aratıp, htr içerisinden rastgele değer seçerek karşılık vermekte"""
    userInput = input('Greetings: ')
    for word in userInput.split():
        if word.lower() in hti:
            print("{}".format(prjName) + random.choice(htr))
        else:
            print("{} Neyden bahsediyorsun, görgü kurallarına geri dönmem gerekirse önce selam söyle!".format(prjName))
            return greetings(hti, htr)
    print("{0}Let's talk about horoscopes :)\n{0}Do you have any questions you want to ask?".format(prjName))
    loopGreetings()

def loopGreetings():
    """Bu fonksiyon kullanıcının girdisini sürekli hti içerisinden kontrol etmekte"""
    readyForTalk = False
    while readyForTalk == False:
        userInput = input("User: ")
        for word in userInput.split():
            if word in helloThereInputs:
                print("{0}{1} again".format(prjName,random.choice(helloThereResponses)))
                print("{}Ready for talk?".format(prjName, prjName))
            else:
                readyForTalk = True

def trueHoroscopes(userInput):
    """Bu fonksiyon kullanının girdisini kontrol ederek gerekli fonskiyona yönlendirmekte"""
    if userInput == "boğa":
        horoscopeBull()
    elif userInput == "aslan":
        horoscopeLion()

def navigating():
    """Bu fonksiyon kullanıcı fonksiyon içerisinde "4"ü seçtiğinde tekrar burç seçimine yönlendirmekte"""
    print("{} Hangi Burcu Seçmek İstersin?:".format(prjName))
    userInput = input("User: ")
    trueHoroscopes(userInput)

def horoscopeBull():
    print("{} Seçtiğin burcu hakkında sunmak istediğim üç opsiyonel var, bunlar: \n "
          "Ekrana -- 1 -- yazarak burcun hakkında genen bilgileri öğrenebilirsin."
          "\n Ekrana -- 2 -- yazarak burcun hakkında soru seçimi yapabilirsin."
          "\n Ekrana -- 3 -- yazarak burcun hakkında soru girişi yapabilirsin."
          "\n Ekrana -- 4 -- yazarak farklı bir burç girebilirsin. ".format(prjName))
    userInput = input("User: ")
    if userInput == "1":
        questions_sample.taurus()
        time.sleep(1.5)
        return horoscopeBull()
    elif userInput == "2":
        print("2")
    elif userInput == "3":
        print("3")
    elif userInput == "4":
        navigating()
    elif userInput in helloThereInputs:
        print("Bu kadar merhaba yeter")
        return horoscopeBull()

def horoscopeLion():
    print("{} Seçtiğin burcu hakkında sunmak istediğim üç opsiyonel var, bunlar: \n "
          "Ekrana -- 1 -- yazarak burcun hakkında genen bilgileri öğrenebilirsin."
          "\n Ekrana -- 2 -- yazarak burcun hakkında soru seçimi yapabilirsin."
          "\n Ekrana -- 3 -- yazarak burcun hakkında soru girişi yapabilirsin."
          "\n Ekrana -- 4 -- yazarak farklı bir burç girebilirsin. ".format(prjName))
    userInput = input("User: ")
    if userInput == "1":
        questions_sample.leo()
        time.sleep(1.5)
        return horoscopeLion()
    elif userInput == "2":
        print("2")
    elif userInput == "3":
        print("3")
    elif userInput in helloThereInputs:
        print("Bu kadar merhaba yeter")
        return horoscopeLion()
    elif userInput == "4":
        navigating()

greetings(helloThereInputs, helloThereResponses)  # Program Burda Başlıyor
print("{} Burcun nedir? ".format(prjName))
userInput = input("User: ")
if userInput.lower() in horoscopes:
    trueHoroscopes(userInput.lower())
