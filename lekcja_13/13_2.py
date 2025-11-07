'''Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
Użyj metody executemany do dodania wszystkich książek za jednym razem
'''

import sqlite3
conn = sqlite3.connect("biblioteka.db")

c = conn.cursor()

ksiazki_do_dodania = [
    ("Pan Tadeusz", "Adam Mickiewicz", 1834),
    ("W pustyni i w puszczy", "Henryk Sienkiewicz", 1973),
    ("Zaginięcie", "Remigiusz Mróz", 2015)
]

c.executemany("INSERT INTO biblioteka (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
              ksiazki_do_dodania)

conn.commit()

conn.close()