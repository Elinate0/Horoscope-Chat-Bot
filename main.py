import random

prj_name = 'Project X:'

hello_there_inputs = ("hello", "hi", "greetings", "hey" , "hola", "merhaba", "Bonjour", "Sua s’dei", "Hallo", "Ciao")
hello_there_responses = ["hi", "hey", "nods", "hi there", "hello", "I am glad! You are talking to me"]

def Greetings(hti, htr):

    user_input = input('Greetings: ')

    for word in user_input.split():
        if word.lower() in hti:
            print("{}".format(prj_name) + random.choice(htr))
            continue
        else:
            print("{} What are you talking about, If I have to go back to etiquette, first say hi!".format(prj_name))
            return Greetings()

    print("{}Let's talk about horoscopes :)\n{}Do you have any questions you want to ask?".format(prj_name,prj_name))

def Loop_Greetings(hti, htr):
    user_input = input("LGreetings: ")

    if user_input in hti:
        print("{0}{1} again".format(prj_name,random.choice(hello_there_responses)))
        print("{}Ready for talk?".format(prj_name, prj_name))
        pass
    else:
        pass
    user_input = input("User: ")
    if user_input in hello_there_inputs:
        return Loop_Greetings()
    else:
        pass

Greetings(hello_there_inputs, hello_there_responses)

user_input = input("User: ")
if user_input in hello_there_inputs:
    for word in user_input.split():
        if word in hello_there_inputs:
            Loop_Greetings(hello_there_inputs, hello_there_responses)
            pass
        else:
            continue
else:
    pass
