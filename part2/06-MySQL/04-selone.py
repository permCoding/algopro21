import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "SELECT * FROM curators WHERE id = %s"
        id = 5
        cur.execute(sql, id)
        row = cur.fetchone()
        print(row['nameCur'])
finally:
    conn.close()
