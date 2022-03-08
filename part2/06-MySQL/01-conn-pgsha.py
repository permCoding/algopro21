# pip3 install PyMySQL

import pymysql.cursors

# http://pgsha.ru:35080/phpmyadmin/index.php 
conn = pymysql.connect(
    host='pgsha.ru', 
    user='soft0016', 
    password='x9c1RYsc', 
    db='soft0016_faculty',
    port=35006,
    cursorclass=pymysql.cursors.DictCursor)

with conn.cursor() as cur:
    sql = "SELECT nameCur FROM curators"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
