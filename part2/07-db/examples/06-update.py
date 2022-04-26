import pymysql.cursors

conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_labrab',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

try:
    with conn.cursor() as cur:
        
        nameStud = 'Жданов'
        city = 'Барда'        
        
        sql = "UPDATE students \
            SET city = %s \
            WHERE nameStud = %s"
        
        count = cur.execute(sql, (city,nameStud))
        conn.commit()
        print(f'updates {count} rows')
except:
    print('error UPDATE')
finally:
    conn.close()
