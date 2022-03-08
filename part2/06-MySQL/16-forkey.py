import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "ALTER TABLE `groups` \
            ADD FOREIGN KEY (`idCur`) \
            REFERENCES `curators`(`id`) \
            ON DELETE RESTRICT \
            ON UPDATE RESTRICT;"
        cur.execute(sql)
        conn.commit()
except:
    print('error foreign key')
finally:
    conn.close()
