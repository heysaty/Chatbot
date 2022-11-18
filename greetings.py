import random

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
        "Happy !!! How are you ?",
    ],

    'good': [
        'Perfect !!!'
    ],
    'feature': [
        ''' I can do many things....like tell you about the weather, record a note for you and 
            do some calculations :)
            '''
    ],
    'name': [
           "They call me Alfred",
           "I usually go by Alfred",
           "My name is the Alfred"
        ]

}


def greet(says):
    return random.choice(responses[says])
