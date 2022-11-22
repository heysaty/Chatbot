import psycopg2
import sys
sys.path.insert(1, '/Users/apple/code/Chatbot/database/postgres')
from create_table import create_table
from insert_data import insert_data
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/apple/code/Chatbot')
from config import config



# establishing the connection





def insert_text(tablename, speaker, text):
    conn = psycopg2.connect(
        database=config.databaseName, user=config.username, password=config.password, host=config.host, port=config.port
    )
    try:
        cur=conn.cursor()
        cur.execute(create_table(tablename))
    except:
        pass
    finally:
        conn.commit()
        cur.close()
        cur_ = conn.cursor()
        cur_.execute(insert_data(tablename, speaker, text))
        conn.commit()
        cur_.close()
        conn.close()


# insert_text('hello4', 'satya', 'hiii')

#
# cur.execute('SELECT * from hole_by_hole_score')
# hole_by_hole_score = cur.fetchall()
# print(hole_by_hole_score)
#
# cur.close()
# conn.close()
