import psycopg2
from config import config

# establishing the connection
conn = psycopg2.connect(
    database=config.databaseName, user=config.username, password=config.password, host=config.host, port=config.port
)

cur = conn.cursor()

cur.execute('SELECT * from hole_by_hole_score')
hole_by_hole_score = cur.fetchall()
print(hole_by_hole_score)





cur.close()
conn.close()
# Connection established to: (
#    'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# )