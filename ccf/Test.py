import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create  table   user (id int(10)    primary key ,name varchar(20))')
cursor.close()
conn.close()