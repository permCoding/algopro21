import pymysql.cursors
import modules.module as m
import modules.csv as csv


def create(): # чистит id записей
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = " \
CREATE TABLE `soft0016_faculty`.`students` \
(`id` INT NOT NULL AUTO_INCREMENT, \
`nameSt` VARCHAR(20) NOT NULL, \
`sex` INT NOT NULL, \
`age` INT NOT NULL, \
`idGr` INT NOT NULL, \
PRIMARY KEY (`id`)) \
ENGINE = InnoDB;"
            cur.execute(sql)
            conn.commit()
    finally:
        conn.close()


create()
