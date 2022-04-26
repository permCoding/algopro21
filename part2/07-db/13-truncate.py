import pymysql.cursors
import modules.module as m
import modules.csv as csv


def truncate(): # чистит id записей
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "TRUNCATE `groups`"
            count = cur.execute(sql)
            conn.commit()
            print(f'deleted = {count} rows')
    finally:
        conn.close()


truncate()
