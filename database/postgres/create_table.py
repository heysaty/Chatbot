
def create_table(tablename):

    query = """CREATE TABLE {}(
        id SERIAL PRIMARY KEY ,
        speaker VARCHAR(50),
        text VARCHAR(300) NOT NULL,
        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""".format(tablename)

    return query
