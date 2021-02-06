import mysql.connector
my_db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db1'
    )

cur = my_db.cursor()
s="DELETE FROM book WHERE title='HTML'"
cur.execute(s)
my_db.commit()
