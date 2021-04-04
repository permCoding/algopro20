import pymysql.cursors


def get_connection():
    return pymysql.connect(
        host='localhost', 
        user='soft0016', 
        password='x9c1RYsc', 
        db='soft0016_faculty',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor)
