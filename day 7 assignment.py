import mysql.connector
database = mysql.connector.connect(host ='localhost', user ='root', passwd ='9793', database ='Collegerec')

cur = database.cursor()
#
cur.execute("update students set mark = 80  where name = 'vikas' ")

cur.execute("select * from students")

for r in cur:
    print(r)

cur.close()
database.commit()