class User:

    def __init__(self, say):
        self.say = say

    said = {
        'greet': ['hi', 'hello', 'hey', 'whats up', 'hola'],
        'how': ['how are you'],
        'good': ['good', 'very good', 'perfect', 'nice'],
        'feature': [
            'help',
            'what can you do',
            'help me',
            'what can you do for me'
            'what are your features'
        ],
        'name': [
            'name',
            'your name',
            'what is your name',
        ],
        'calculate': [
            'wfsf'
        ]
    }

    ignore_words = ['i', 'like', 'love', 'to', 'is', 'a', 'want', 'has', 'have', 'as', 'would', 'should',
                    'very', 'much', 'what', 'add', 'multiply', 'subtract', 'and', 'sum', 'minus', 'addition',
                    'mul', 'of', 'alfred']

    def emotion(self, say):

        says_lst = self.say.split(" ")

        for word in says_lst:
            if word not in self.ignore_words and word[-1].isdigit() is False and word.isdigit() is False:
                return word

    def says(self):
        return self.said
