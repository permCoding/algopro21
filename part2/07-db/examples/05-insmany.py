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

st1 = ('Жданов', 197, 1, '2002-09-10', 'Пермь')
st2 = ('Микова', 222, 0, '2001-10-07', 'Пермь')
st3 = ('Мамин', 199, 1, '2001-11-10', 'Пермь')
st4 = ('Комов', 195, 1, '2002-01-17', 'Пермь')
studs = (st1, st2, st3, st4)

count = cur.executemany(sql, studs)
conn.commit()

print(f'inserted {count} rows')

conn.close()
