from greetings import Alfred_Response
# from said import says, emotion
from said import User
import time

from regex import calculate

Alfred = Alfred_Response('greetings')
print("Alfred : ", Alfred.greet('greetings'))

while True:
    say = input("You : ").lower()
    Alfred = Alfred_Response(say)
    user = User(say)

    time.sleep(0.5)
    try:
        if say == "exit" or say == "bye":
            print("Alfred : ", Alfred.greet('bye'))
            break

        elif say in user.says()['greet'] :
            print("Alfred : ", Alfred.greet('greetings'))

        elif say in user.says()['how']:
            print("Alfred : ", Alfred.greet('how'))

        elif say in user.says()['good']:
            print("Alfred : ", Alfred.greet('good'))

        elif say in user.says()['feature']:
            print("Alfred : ", Alfred.greet('feature'))

        elif say in user.says()['name']:
            print("Alfred : ", Alfred.greet('name'))

        elif user.emotion(say) is not None:
            print("Alfred : ", user.emotion(say))

        else:
            sol, exp = calculate(say)
            print("Alfred : The answer of {} {} {} = {}".format(exp[0],exp[1],exp[2],sol))






    except:
        print("Alfred : ", user.emotion(say))
        print("Alfred : Sorry I didn't Understand. Please ask something else !!!")
        pass
