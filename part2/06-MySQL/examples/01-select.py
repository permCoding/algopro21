
import pymysql.cursors
 
conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "SELECT * FROM students"
cur.execute(sql) 
rows = cur.fetchall()

for row in rows:
    print(f'name = {row["nameStud"]}')

conn.close()