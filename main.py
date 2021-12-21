import random
import time
import questions_sample

prj_name = 'Project X:'
hello_there_inputs = ("hello", "hi", "greetings", "hey" , "hola", "merhaba", "bonjour", "sua s’dei", "hallo", "ciao")
hello_there_responses = ["hi", "hey", "nods", "hi there", "hello", "I am glad! You are talking to me"]
horoscopes = ["boğa", "ikizler", "yengeç", "aslan"]

def greetings(hti, htr):
    userInput = input('Greetings: ')
    for word in userInput.split():
        if word.lower() in hti:
            print("{}".format(prj_name) + random.choice(htr))
            continue
        else:
            print("{} Neyden bahsediyorsun, görgü kurallarına geri dönmem gerekirse önce selam söyle!".format(prj_name))
            return greetings(hti, htr)
    print("{}Let's talk about horoscopes :)\n{}Do you have any questions you want to ask?".format(prj_name, prj_name))
    loopGreetings()
def loopGreetings(): #Şimdilik bu fonksiyonu devre dışı bırakıyorum, ilerleyen zamanlarda geri döneceğim. Şimdilik readyForTalk yeterli olacaktır.
    readyForTalk = False
    while readyForTalk == False:
        userInput = input("User: ")
        for word in userInput.split():
            if word in hello_there_inputs:
                print("{0}{1} again".format(prj_name,random.choice(hello_there_responses)))
                print("{}Ready for talk?".format(prj_name, prj_name))
            else:
                readyForTalk = True

def trueHoroscopes():
    if userInput == "boğa":
        horoscopeBull()

def horoscopeBull():
    print("{} Seçtiğin burcu hakkında sunmak istediğim üç opsiyonel var, bunlar: \n "
    "Ekrana -- 1 -- yazarak burcun hakkında genen bilgileri öğrenebilirsin."
    "\n Ekrana -- 2 -- yazarak burcun hakkında soru seçimi yapabilirsin."
    "\n Ekrana -- 3 -- yazarak burcun hakkında soru girişi yapabilirsin."
    "\n Ekrana -- 4 -- yazarak farklı bir burç girebilirsin. ".format(prj_name))
    userInput = input("User: ")
    if userInput == "1":
        questions_sample.taurus()
        time.sleep(1.5)
        return horoscopeBull()
    elif userInput == "2":
        print("2")
    elif userInput == "3":
        print("3")
    elif userInput in hello_there_inputs:
        print("Bu kadar merhaba yeter")
        return horoscopeBull()

greetings(hello_there_inputs, hello_there_responses)
print("{} Burcun nedir? ".format(prj_name))
userInput = input("User: ")
if userInput.lower() in horoscopes:
    trueHoroscopes()
