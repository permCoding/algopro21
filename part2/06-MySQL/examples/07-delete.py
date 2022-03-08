import pymysql.cursors

conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

name = 'Жданов'
city = 'Барда'
sql = "DELETE FROM students \
    WHERE nameStud = %s AND city = %s"
count = cur.execute(sql, (name,city))
conn.commit()
print(f'deleted = {count} rows')

conn.close()
