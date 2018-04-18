#!/usr/bin/env python


import sqlite3
connection  = sqlite3.connect('example3.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS test (id integer, name text, autor text)''')

cursor.execute('''INSERT INTO test VALUES(1, 'Pan Tadeusz', 'Adam Mickiewicz')''')
cursor.execute('''INSERT INTO test VALUES(2, 'Potop', 'Henryk Sienkiewicz')''')
connection.commit()

for row in cursor.execute('''SELECT * FROM test ORDER BY id'''):
    print(row)

connection.close()
