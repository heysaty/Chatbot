
class User:

    def __init__(self, say):
        self.say = say

    said = {
        'greet': ['hi', 'hello', 'hey', 'hola', 'hi alfred', 'hello alfred', 'hey alfred',
                  'whats up alfred', 'hola alfred'],
        'how': ['how are you', 'whats up'],
        'good': ['good', 'very good', 'perfect', 'nice', 'i am good', 'i am very good', 'i am happy'],
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
        ]

    }

    note = ['remember', 'note', 'write']

    view = ['show', 'view']

    ignore_words = ['i', 'like', 'love', 'to', 'is', 'a', 'want', 'has', 'have', 'as', 'would', 'should',
                    'very', 'much', 'what', 'add', 'multiply', 'subtract', 'and', 'sum', 'minus', 'addition',
                    'mul', 'of', 'alfred','drinking']

    def emotion(self, say):

        says_lst = self.say.split(" ")

        for word in says_lst:
            if word not in self.ignore_words and word[-1].isdigit() is False and word.isdigit() is False:
                return word

    def says(self):
        return self.said

    def remember(self, say):
        says_lst = self.say.split(" ")

        for word in says_lst:
            if word in self.note:
                return True

    def show(self, say):
        says_lst = self.say.split(' ')

        for word in says_lst:
            if word in self.view:
                return True

    def whattime(self,say):
        says_lst = self.say.split(' ')

        for word in says_lst:
            if word == 'time':
                return True

    def whatdate(self,say):
        says_lst = self.say.split(' ')

        for word in says_lst:
            if word == 'date':
                return True

    def whatday(self, say):
        says_lst = self.say.split(' ')

        for word in says_lst:
            if word == 'day':
                return True



