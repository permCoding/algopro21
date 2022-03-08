import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        name_table = 'curators'
        nameCur = 'Джек Дорси'
        
        sql = "INSERT INTO " + \
            name_table +\
            " (nameCur) VALUES(%s)"
        
        count = cur.execute(sql, nameCur)
        conn.commit()
        print(f'inserted = {count}')
        #
        #
finally:
    conn.close()
