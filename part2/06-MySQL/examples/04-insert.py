import pymysql.cursors

conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

sql = "INSERT INTO students \
    (nameStud, rating, gender, date, city) \
    VALUES (%s,%s,%s,%s,%s)"

stud = ('Жданов', 197, 1, '2002-09-10', 'Пермь')

count = cur.execute(sql, stud)
conn.commit()

print(f'inserted {count} rows')

conn.close()
