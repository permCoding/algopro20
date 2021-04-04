import pymysql.cursors
import modules.module as m
import modules.csv as csv


def insert_many(rows): # пока только ONE
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "INSERT INTO `groups` (nameGr,idCur) VALUES (%s,%s)"
            count = cur.executemany(sql, rows) # список кортежей
            conn.commit()
            print(f'inserted {count} rows')
    finally:
        conn.close()


lines = csv.get_lines('./csv/groups.csv')
rows = csv.get_rows(lines)
rows = list(map(lambda row: (row[1],row[2]), rows))
# print(rows)
insert_many(rows)
