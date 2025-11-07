'''Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
napisane przez Twojego ulubionego autora
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")

c = conn.cursor()

c.execute("SELECT tytul, autor FROM biblioteka WHERE autor = ?",
          ("Remigiusz Mróz", ))

ulubiony_tytul = c.fetchall()
for tytul in ulubiony_tytul:
    print(tytul)

conn.close()

