import pymysql.cursors
import modules.module as m
import modules.csv as csv


def insert_one(rows): # пока только ONE
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `groups` (`nameGr`,`idCur`) VALUES (%s,%s)"
            row = rows[0]
            count = cur.execute(sql, (row[1], row[2])) # только nameGr, idCur
            conn.commit()
            print(f'inserted = {count} rows')
    finally:
        conn.close()


lines = csv.get_lines('./csv/groups.csv')
rows = csv.get_rows(lines)
insert_one(rows)
