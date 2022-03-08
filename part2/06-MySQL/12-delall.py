import pymysql.cursors
import modules.module as m
import modules.csv as csv


def del_all():
    conn = m.get_connection()
    try:
        with conn.cursor() as cur:
            sql = "DELETE FROM `groups`"
            count = cur.execute(sql)
            conn.commit()
            print(f'deleted = {count} rows')
    finally:
        conn.close()


del_all()
