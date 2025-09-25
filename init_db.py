import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:

    connection.executescript(f.read())

connection.commit()

connection.close()


print("Banco de dados 'database.db' foi inicializado com sucesso.")
