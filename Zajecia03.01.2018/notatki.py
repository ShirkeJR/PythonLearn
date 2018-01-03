import sqlite3

con = sqlite3.connect("example.db")

cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS 
test(id integer, name text, value real)''')

cursor.execute('''INSERT INTO test VALUES (1, "Adam", 234235)''')

con.commit()

for row in cursor.execute('''SELECT * FROM test'''):
    print row

con.close()