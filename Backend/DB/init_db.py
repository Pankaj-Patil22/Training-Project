import sqlite3

connection = sqlite3.connect('CAFEDB.db')

with open('reservations_table.sql') as f:
    connection.executescript(f.read())


cursor = connection.cursor()

connection.commit()
connection.close()