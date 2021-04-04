import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "DELETE FROM curators WHERE nameCur = %s"
        nameCur = 'Дорси'
        count = cur.execute(sql, (nameCur))
        conn.commit()
        print(f'deleted = {count} rows')
finally:
    conn.close()
