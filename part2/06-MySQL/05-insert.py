import pymysql.cursors
import module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "INSERT INTO curators (nameCur) VALUES(%s)"
        nameCur = 'Джек Дорси'
        cur.execute(sql, nameCur)
        conn.commit()
finally:
    conn.close()
