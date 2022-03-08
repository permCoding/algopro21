import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        nameCur = 'Дорси'
        sql = "DELETE FROM curators WHERE nameCur = %s"
        count = cur.execute(sql, (nameCur))
        conn.commit()
        print(f'deleted = {count} rows')
finally:
    conn.close()
