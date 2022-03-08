import pymysql.cursors
import modules.module as m


def insert_many(rows): # пока только ONE
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `curators` (nameCur) VALUES (%s)"
            count = cur.executemany(sql, rows) # список кортежей
            conn.commit()
            print(f'inserted {count} rows')
    finally:
        conn.close()


def get_rows(lines):
    return [line.split(',')[1] for line in lines[1:]]


def get_lines(file_name):
    with open(file_name,mode='r',encoding='utf8') as f:
        return f.read().split('\n')


lines = get_lines('./csv/curators.csv')
rows = get_rows(lines)
# print(rows)
insert_many(rows)
