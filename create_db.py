import sqlite3
def create_db():
    con=sqlite3.connect(database=r'customerinfo.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customer(cid INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,email TEXT,pass TEXT)")
    con.commit()

create_db()