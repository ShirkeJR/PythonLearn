import sqlite3

connection = sqlite3.connect('baza.db')

connection.execute('''CREATE TABLE IF NOT EXISTS KSIAZKA
              (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
              TITLE TEXT NOT NULL,
              AUTHOR TEXT NOT NULL,
              PRICE REAL NOT NULL)''')
print "Tabela stworzona"

connection.execute('''INSERT INTO KSIAZKA(TITLE, AUTHOR, PRICE) VALUES ("Piraci z Karaibow", "Stefan Batory", 50)''')
connection.execute('''INSERT INTO KSIAZKA(TITLE, AUTHOR, PRICE) VALUES ("Muminki", "Alicja Moczek", 25)''')
connection.execute('''INSERT INTO KSIAZKA(TITLE, AUTHOR, PRICE) VALUES ("Pogramowanie dla opornych", "Adam Malysz", 20)''')
connection.commit()

cursor = connection.execute('''SELECT * FROM KSIAZKA''')
for row in cursor:
    print row

print ""

#rollback - Anulowanie transackcji
connection.execute('''INSERT INTO KSIAZKA(TITLE, AUTHOR, PRICE) VALUES ("Muminki2", "Alicja Moczek2", 25)''')
connection.rollback()

cursor = connection.execute('''SELECT * FROM KSIAZKA''')
for row in cursor:
    print row

connection.execute('''DROP TABLE KSIAZKA''')
connection.commit()
connection.close()