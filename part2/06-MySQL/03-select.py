import pymysql.cursors
import modules.module as m


conn = m.get_connection()
cur = conn.cursor()

sql = "SELECT * FROM curators WHERE id = %s"
id = 5
cur.execute(sql, id)
row = list(cur)[0]
print(row['nameCur'])

conn.close()

# try:
#     with conn.cursor() as cur:
#         sql = "SELECT * FROM curators WHERE id = %s"
#         id = 5
#         cur.execute(sql, id)
#         row = list(cur)[0]
#         print(row['nameCur'])
#         # for row in cur:
#         #     print(row)
# finally:
#     conn.close()
