'''Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
tabeli ksiazki.
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")

c = conn.cursor()

c.execute("SELECT * FROM biblioteka")
wszystkie_tytuly = c.fetchall()
print(wszystkie_tytuly)

conn.close()