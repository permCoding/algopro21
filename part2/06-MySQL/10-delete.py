import pymysql.cursors
import modules.module as m


def delete(nameGr):
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM `groups` WHERE nameGr = %s"
            count = cur.execute(sql, (nameGr))
            conn.commit()
            print(f'deleted = {count} rows')
    except:
        print('ошибка записи')
    finally:
        conn.close()


delete('ПИб-1')
