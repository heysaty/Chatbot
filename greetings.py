import random


class Alfred_Response:
    def __init__(self, say):
        self.say = say

    responses = {
        "greetings": [
            "Welcome !!! I am Alfred, How can I help you ;)",
            "Hello there, I am Alfred What's up !!! "
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
        
    -> tell you about the weather
    -> record a note for you
    -> do some calculations 
                '''
        ],
        'name': [
            "They call me Alfred",
            "I usually go by Alfred",
            "My name is the Alfred"
        ]

    }

    def greet(self, say):
        return random.choice(self.responses[say])

    def note(self):

        text = self.say.replace('note', '')
        text = '-> ' + text.replace('remember', '') + '\n'

        file = open('notes.txt', 'a')

        file.write(text)
        file.close()

    def view(self):
        file = open('notes.txt','r')
        print(file.read())

