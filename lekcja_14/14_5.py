'''Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT imie, email
FROM Klienci
'''

c.execute(query)
wynik = c.fetchall()

print(f"Dane klientów to: {wynik}")
