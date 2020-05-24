import sqlite3

con=sqlite3.connect("sales.db")
#con.execute("create table book(id,price,name)")
books=[('021',25,'大学计算机'),('022',65,'疯狂讲义'),('077',23,'心理学')]
cur=con.cursor()
cur.execute("insert into book(id,price,name) values(?,?,?)",('001','55','大学英语'))
cur.executemany("insert into book(id,price,name) values(?,?,?)",books)

cur.execute("select * from book")
for row in cur:
    print(row)