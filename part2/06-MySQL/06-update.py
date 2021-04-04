import pymysql.cursors
import modules.module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "UPDATE curators SET nameCur = %s WHERE nameCur = %s"
        nameCurOld = 'Джек Дорси'
        nameCurNew = 'Дорси'
        count = cur.execute(sql, (nameCurNew,nameCurOld))
        conn.commit()
        print(f'updates {count} rows')
finally:
    conn.close()
