import random
from datetime import datetime


class Alfred_Response:
    def __init__(self, say):
        self.say = say

    responses = {
        "greetings": [
            "Welcome !!! I am Alfred, How are you ;)",
            "I am Alfred !!! I am here to help ;)"


        ],
        "bye": [
            "Bye !!! Nice chatting with you :)",
            "Goodbye , have a Good Day !!!",
            "See U !!! Bye"
        ],
        'how': [
            "I am very Good! How are you ?",
            "I am great !!! How are you ?",
        ],

        'good': [
            'Perfect !!! Tell me something about yourself...'
        ],
        'feature': [
            ''' I can do many things....like 
        
    -> show you current time
    -> show you today's date 
    -> show you today's day
    -> record a note for you
    -> do some calculations for you
                '''
        ],
        'name': [
            "They call me Alfred",
            "I usually go by Alfred",
            "My name is the Alfred"
        ],
        'coffee': [
            "That's great! I also love a strong coffee..."
        ],

        'tea': [
            "That's great! I also love a warm cup of tea..."
        ]


    }

    def greet(self, say):
        return random.choice(self.responses[say])

    def note(self):
        text = self.say.replace('note', '')
        text = ' -> ' + text.replace('remember', '') + '\n'

        file = open('notes.txt', 'a')

        file.write(text)
        file.close()

    def view(self):
        file = open('notes.txt', 'r')
        print(file.read())

    def whattime(self):
        return datetime.now().strftime("%H:%M")

    def whatdate(self):
        return datetime.now().date()

    def whatday(self):
        return datetime.now().strftime("%A")
