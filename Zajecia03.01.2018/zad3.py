import sqlite3

connection = sqlite3.connect('baza2.db')

connection.execute('''CREATE TABLE IF NOT EXISTS KSIAZKA
              (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
              TITLE TEXT NOT NULL,
              PRICE REAL NOT NULL)''')

connection.execute('''CREATE TABLE IF NOT EXISTS AUTOR
              (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
              NAME TEXT NOT NULL)''')

connection.execute('''CREATE TABLE IF NOT EXISTS KSIAZKA_AUTOR
              (KSIAZKA_ID INTEGER,
              AUTOR_ID INTEGER,
              FOREIGN KEY (KSIAZKA_ID) REFERENCES KSIAZKA(ID),
              FOREIGN KEY (AUTOR_ID) REFERENCES AUTOR(ID))''')

print "Tabela stworzona"
#connection.execute('''DROP TABLE KSIAZKA''')
#connection.execute('''DROP TABLE AUTOR''')
#connection.execute('''DROP TABLE KSIAZKA_AUTOR''')
cursor = connection.cursor()

cursor.execute('''INSERT INTO KSIAZKA(TITLE, PRICE) VALUES ("Piraci z Karaibow", 50)''')
ksiazka_id = cursor.lastrowid
cursor.execute('''INSERT INTO AUTOR(NAME) VALUES ("Stefan Batory")''')
autor_id = cursor.lastrowid
cursor.execute('''INSERT INTO KSIAZKA_AUTOR VALUES (?, ?)''', (ksiazka_id, autor_id))
connection.commit()

cur = connection.execute('''SELECT * FROM KSIAZKA''')
for row in cur:
    print row

print ""

cur = connection.execute('''SELECT * FROM AUTOR''')
for row in cur:
    print row

print ""

cur = connection.execute('''SELECT * FROM KSIAZKA_AUTOR''')
for row in cur:
    print row

connection.commit()
connection.close()