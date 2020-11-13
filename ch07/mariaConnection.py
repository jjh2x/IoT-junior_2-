import pymysql

db = pymysql.connect(host = 'localhost', user='root', password='5146',
db = 'IncheonNational', charset = 'utf8')

cur = db.cursor()

cur.execute("desc student")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
print(rows)

db.close()