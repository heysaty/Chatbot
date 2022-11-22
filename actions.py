from response import Alfred_Response
from said import User
import time
from database.postgres import postgresdb
from database.mongodb import insert_data
from regex import Regex






class Actions:

    def __init__(self):
        Alfred = Alfred_Response('greetings')
        print("Alfred : ", Alfred.greet('greetings'))
        self.name = input("You : ").lower()
        self.bot = 'Alfred'

    def decisions(self):

        global chat
        print("Alfred : Welcome to the Chatroom !!! {} ;)".format(self.name))
        insert_data.store_session(self.name, self.bot, "Welcome to the Chatroom !!! {} ;)".format(self.name))
        postgresdb.insert_text(self.name,self.bot,"Welcome to the Chatroom !!! {} ;)".format(self.name))

        while True:
            say = input("{} : ".format(self.name)).lower()

            insert_data.store_session(self.name,self.name, say)
            postgresdb.insert_text(self.name,self.name,say)

            Alfred = Alfred_Response(say)
            user = User(say)
            regex = Regex(say)

            time.sleep(0.5)
            try:
                if say == "exit" or say == "bye" or say == "bye alfred":

                    print("Alfred : ", Alfred.greet('bye'))
                    insert_data.store_session(self.name, self.bot, Alfred.greet('bye'))
                    postgresdb.insert_text(self.name, self.bot, Alfred.greet('bye'))

                    break

                elif user.thanks(say) is True:
                    chat= "Alfred : {} {} !!! How can I help you ?".format(Alfred.thank(), self.name)
                    # print("Alfred : {} {} !!! How can I help you ?".format(Alfred.thank(), self.name))


                elif say in user.says()['greet']:
                    chat = "Alfred : ", Alfred.greet('greetings')


                elif say in user.says()['how']:
                    chat = "Alfred : ", Alfred.greet('how')



                elif say in user.says()['good']:
                    chat = "Alfred : ", Alfred.greet('good')

                elif say in user.says()['feature']:
                    chat = "Alfred : ", Alfred.greet('feature')


                elif user.song_suggestions(say) is True:
                    print("Alfred : Which kind of song do you want me to recommend !!! English or Hindi",)

                    insert_data.store_session(self.name, self.bot, "Which kind of song do you want me to recommend !!! English or Hindi")
                    postgresdb.insert_text(self.name, self.bot,"Which kind of song do you want me to recommend !!! English or Hindi")
                    say_song = input("{} : ".format(self.name)).lower()

                    insert_data.store_session(self.name, self.name, say_song)
                    postgresdb.insert_text(self.name, self.name, say_song)

                    text = Alfred.song_suggestion(say_song)
                    print(text)

                    insert_data.store_session(self.name, self.bot, text)
                    postgresdb.insert_text(self.name, self.bot, text)

                    continue


                elif user.whattime(say) is True:
                    chat = 'Alfred : Current time is', Alfred.whattime()


                elif user.whatdate(say) is True:
                    chat = "Alfred : Today's Date is", Alfred.whatdate()


                elif user.whatday(say) is True:
                    chat = "Alfred : Today's Day is", Alfred.whatday()


                elif say in user.says()['name']:
                    chat = "Alfred : ", Alfred.greet('name')


                elif say[-1].isdigit() is True:
                    sol, exp = regex.calculate(say)

                    chat = "Alfred : The answer of {} {} {} = {}".format(exp[0], exp[1], exp[2], sol)

                elif user.remember(say) is True:
                    Alfred.note()
                    chat = 'Alfred : Bravo !!! Your notes have been saved ;)'

                elif user.show(say) is True:
                    print('Alfred : Here are your reminder notes : \n')
                    file = Alfred.view()
                    print(file)

                    text = "Here are your reminder notes : \n" + file

                    insert_data.store_session(self.name, self.bot, text)
                    postgresdb.insert_text(self.name, self.bot, text)
                    continue



                elif user.emotion(say) is not None:
                    chat = "Alfred : ", Alfred.greet(user.emotion(say))




                print(chat)
                insert_data.store_session(self.name, self.bot, chat)
                postgresdb.insert_text(self.name, self.bot, chat)
            except:
                print("Alfred : Sorry I didn't Understand. Please ask something else !!!")

                insert_data.store_session(self.name, self.bot, "Sorry I didn't Understand. Please ask something else !!!")
                postgresdb.insert_text(self.name, self.bot, "Sorry I didn't Understand. Please ask something else !!!")
                pass
