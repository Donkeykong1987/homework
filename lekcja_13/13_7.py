'''Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
najmniej 4 studentów i 3 audytoria
'''

import sqlite3

conn = sqlite3.connect("uczelnia.db")

c = conn.cursor()

studenci_do_dodania = [
    ("Jan", "Kowalski"),
    ("Karol", "Nowak"),
    ("Piotr", "Polak"),
    ("Anna", "Kołek")    
]

audytoria_do_dodania = [
    ("A", 9),
    ("J", 13),
    ("O", 21),
    ("C", 3)
]

c.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)",
              studenci_do_dodania)
c.executemany("INSERT INTO audytorium (nazwa_budynku, numer_sali) VALUES (?, ?)",
              audytoria_do_dodania)

conn.commit()

conn.close()