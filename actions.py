from response import Alfred_Response
from said import User
import time

from regex import Regex


class Actions:

    def __init__(self):
        Alfred = Alfred_Response('greetings')
        print("Alfred : ", Alfred.greet('greetings'))
        self.name = input("You : ")

    def decisions(self):
        print("Alfred : Welcome to the Chatroom !!! {} ;)".format(self.name))
        while True:
            say = input("{} : ".format(self.name)).lower()
            Alfred = Alfred_Response(say)
            user = User(say)
            regex = Regex(say)

            time.sleep(0.5)
            try:
                if say == "exit" or say == "bye" or say == "bye alfred":
                    print("Alfred : ", Alfred.greet('bye'))
                    break

                elif user.thanks(say) is True:
                    print("Alfred : {} {} !!! How can I help you ?".format(Alfred.thank(), self.name))

                elif say in user.says()['greet']:
                    print("Alfred : ", Alfred.greet('greetings'))

                elif say in user.says()['how']:
                    print("Alfred : ", Alfred.greet('how'))

                elif say in user.says()['good']:
                    print("Alfred : ", Alfred.greet('good'))

                elif say in user.says()['feature']:
                    print("Alfred : ", Alfred.greet('feature'))

                elif user.song_suggestions(say) is True:
                    print("Alfred : Which kind of song do you want me to recommend !!! English or Hindi",)
                    say_song = input("{} : ".format(self.name)).lower()
                    Alfred.song_suggestion(say_song)


                elif user.whattime(say) is True:
                    print('Alfred : Current time is', Alfred.whattime())

                elif user.whatdate(say) is True:
                    print("Alfred : Today's Date is", Alfred.whatdate())

                elif user.whatday(say) is True:
                    print("Alfred : Today's Day is", Alfred.whatday())

                elif say in user.says()['name']:
                    print("Alfred : ", Alfred.greet('name'))

                elif say[-1].isdigit() is True:
                    sol, exp = regex.calculate(say)
                    print("Alfred : The answer of {} {} {} = {}".format(exp[0], exp[1], exp[2], sol))

                elif user.remember(say) is True:
                    Alfred.note()
                    print('Alfred : Bravo !!! Your notes have been saved ;)')

                elif user.show(say) is True:
                    print('Alfred : Here are your reminder notes : \n')
                    Alfred.view()



                elif user.emotion(say) is not None:
                    print("Alfred : ", Alfred.greet(user.emotion(say)))

            except:
                print("Alfred : ", user.emotion(say))
                print("Alfred : Sorry I didn't Understand. Please ask something else !!!")
                pass
