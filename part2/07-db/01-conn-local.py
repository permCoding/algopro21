# pip3 install PyMySQL

import pymysql.cursors
 
conn = pymysql.connect(
    host='localhost', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_faculty',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor)

with conn.cursor() as cur:
    sql = "SELECT * FROM curators"
    cur.execute(sql) 
    rows = cur.fetchall()
    # print(rows)
    for row in rows:
        print(row["nameCur"])
