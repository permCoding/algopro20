import pymysql.cursors
import module as m


conn = m.get_connection()

try:
    with conn.cursor() as cur:
        sql = "SELECT * FROM curators WHERE id = %s"
        id = 5
        cur.execute(sql, id)
        row = list(cur)[0]
        print(row['nameCur'])
        # for row in cur:
        #     print(row)
finally:
    conn.close()
