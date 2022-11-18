from greetings import greet
from said import says
import time
from regex import calculate


print("Alfred : ", greet('greetings'))

while True:
    say = input("You : ")
    time.sleep(0.5)
    try:
        if say == "exit" or say == "bye":
            print("Alfred : ", greet('bye'))
            break
        elif say in says()['greet'] :
            print("Alfred : ", greet('greetings'))

        elif say in says()['how']:
            print("Alfred : ", greet('how'))

        elif say in says()['good']:
            print("Alfred : ", greet('good'))

        elif say in says()['feature']:
            print("Alfred : ", greet('feature'))

        elif say in says()['name']:
            print("Alfred : ", greet('name'))

        else:
            sol, exp = calculate(say)
            print("Alfred : The answer of {} {} {} = {}".format(exp[0],exp[1],exp[2],sol))






    except:
        print("Please ask something else !!!")
        pass
