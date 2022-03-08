
import pymysql.cursors

conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

id = 2
sql = "SELECT * FROM students WHERE id = %s"
cur.execute(sql, id)
row = cur.fetchone()
print(row)

conn.close()
