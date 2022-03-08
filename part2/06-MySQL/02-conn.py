# pip3 install PyMySQL

import pymysql.cursors

def get_connection():
    return pymysql.connect(
        host='localhost', 
        user='soft0016', 
        password='x9c1RYsc', 
        db='soft0016_faculty',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor)


conn = get_connection()
try:
    with conn.cursor() as cur:
        sql = "SELECT * \
            FROM curators \
            ORDER BY nameCur ASC, id DESC"
        cur.execute(sql) 
        rows = cur.fetchall()
        # rows.sort(key=lambda item: (item['nameCur'], -item['id']))
        for row in rows:
            print(f'{row["id"]}\t{row["nameCur"]}')
except:
    print('ошибка чтения')
finally:
    print('соединение закрыто')
    conn.close()
