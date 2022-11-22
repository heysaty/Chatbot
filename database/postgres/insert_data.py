def insert_data(tablename, speaker, text):

    query = f"""insert into {tablename}(speaker, text)
        values('{speaker}','{text}');"""
    return query
