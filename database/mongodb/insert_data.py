from . import mongodb
from datetime import datetime


mydatabase = mongodb.client['conversations']


def store_session(user_name, speaker, text):
    # Access collection of the database


    mycollection = mydatabase[user_name]

    conversation = {
        'speaker': speaker,
        'text': text,
        'datetime': datetime.now()
    }

    mycollection.insert_one(conversation)
