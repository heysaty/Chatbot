from response import Alfred_Response
from said import User
import time

from database.mongodb import insert_data
from regex import Regex






class Actions:

    def __init__(self):
        Alfred = Alfred_Response('greetings')
        print("Alfred : ", Alfred.greet('greetings'))
        self.name = input("You : ").lower()
        self.bot = 'Alfred'

    def decisions(self):
        print("Alfred : Welcome to the Chatroom !!! {} ;)".format(self.name))

        insert_data.store_session(self.name, self.bot, "Welcome to the Chatroom !!! {} ;)".format(self.name))

        while True:
            say = input("{} : ".format(self.name)).lower()

            insert_data.store_session(self.name,self.name, say)

            Alfred = Alfred_Response(say)
            user = User(say)
            regex = Regex(say)

            time.sleep(0.5)
            try:
                if say == "exit" or say == "bye" or say == "bye alfred":
                    print("Alfred : ", Alfred.greet('bye'))

                    insert_data.store_session(self.name, self.bot, Alfred.greet('bye'))

                    break

                elif user.thanks(say) is True:
                    print("Alfred : {} {} !!! How can I help you ?".format(Alfred.thank(), self.name))

                    insert_data.store_session(self.name, self.bot, "{} {} !!! How can I help you ?".format(Alfred.thank(), self.name))

                elif say in user.says()['greet']:
                    print("Alfred : ", Alfred.greet('greetings'))

                    insert_data.store_session(self.name, self.bot, Alfred.greet('greetings'))

                elif say in user.says()['how']:
                    print("Alfred : ", Alfred.greet('how'))

                    insert_data.store_session(self.name, self.bot, Alfred.greet('how'))

                elif say in user.says()['good']:
                    print("Alfred : ", Alfred.greet('good'))

                    insert_data.store_session(self.name, self.bot, Alfred.greet('good'))

                elif say in user.says()['feature']:
                    print("Alfred : ", Alfred.greet('feature'))

                    insert_data.store_session(self.name, self.bot,  Alfred.greet('feature'))

                elif user.song_suggestions(say) is True:
                    print("Alfred : Which kind of song do you want me to recommend !!! English or Hindi",)

                    insert_data.store_session(self.name, self.bot, "Which kind of song do you want me to recommend !!! English or Hindi")

                    say_song = input("{} : ".format(self.name)).lower()

                    insert_data.store_session(self.name, self.name, say_song)

                    text = Alfred.song_suggestion(say_song)
                    print(text)

                    insert_data.store_session(self.name, self.bot, text)


                elif user.whattime(say) is True:
                    print('Alfred : Current time is', Alfred.whattime())

                    insert_data.store_session(self.name, self.bot, 'Current time is' + Alfred.whattime())

                elif user.whatdate(say) is True:
                    print("Alfred : Today's Date is", Alfred.whatdate())

                    insert_data.store_session(self.name, self.bot, "Today's Date is"+Alfred.whatdate())

                elif user.whatday(say) is True:
                    print("Alfred : Today's Day is", Alfred.whatday())

                    insert_data.store_session(self.name, self.bot, "Today's Day is"+Alfred.whatday())

                elif say in user.says()['name']:
                    print("Alfred : ", Alfred.greet('name'))

                    insert_data.store_session(self.name, self.bot, Alfred.greet('name'))

                elif say[-1].isdigit() is True:
                    sol, exp = regex.calculate(say)
                    print("Alfred : The answer of {} {} {} = {}".format(exp[0], exp[1], exp[2], sol))

                    insert_data.store_session(self.name, self.bot, " The answer of {} {} {} = {}".format(exp[0], exp[1], exp[2], sol))

                elif user.remember(say) is True:
                    Alfred.note()
                    print('Alfred : Bravo !!! Your notes have been saved ;)')

                    insert_data.store_session(self.name, self.bot, " Bravo !!! Your notes have been saved ;)")

                elif user.show(say) is True:
                    print('Alfred : Here are your reminder notes : \n')
                    file = Alfred.view()
                    print(file)

                    text = "Here are your reminder notes : \n" + file

                    insert_data.store_session(self.name, self.bot, text)



                elif user.emotion(say) is not None:
                    print("Alfred : ", Alfred.greet(user.emotion(say)))

                    insert_data.store_session(self.name, self.bot, Alfred.greet(user.emotion(say)))

            except:
                print("Alfred : Sorry I didn't Understand. Please ask something else !!!")

                insert_data.store_session(self.name, self.bot, "Sorry I didn't Understand. Please ask something else !!!")
                pass
