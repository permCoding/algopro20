# pip3 install PyMySQL

import pymysql.cursors
 
conn = pymysql.connect(
    host='localhost', 
    user='soft0015', 
    password='9LlvnQos', 
    db='soft0015_faculty',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
 
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM curators ORDER BY nameCur DESC") 
    rows = cur.fetchall()
    rows.sort(key=lambda item: (item['nameCur'], -item['id']))
    for row in rows:
        # print(row)
        print("{0} {1}".format(row['id'], row['nameCur']))
