import pymysql.cursors
import modules.module as m
import modules.csv as csv


def insert_many(rows): # пока только ONE
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `students` \
            (nameSt,sex,age,idGr) VALUES (%s,%s,%s,%s)"
            count = cur.executemany(sql, rows) # список кортежей
            conn.commit()
            print(f'inserted {count} rows')
    finally:
        conn.close()


def get_rows(lines):
    rows = []
    for line in lines[1:]:
        row = line.split(',')
        row[2] = int(row[2])
        row[3] = int(row[3])
        row[4] = int(row[4])
        row = tuple(row)        
        rows.append(row)
    return rows


lines = csv.get_lines('./csv/students.csv')
rows = get_rows(lines)
rows = list(map(lambda row: row[1:], rows))
# print(rows)
insert_many(rows)

# id,nameSt,sex,age,idGr
