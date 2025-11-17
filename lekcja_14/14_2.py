'''Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
MAX().'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT nazwa_produktu, MAX(cena) 
FROM Produkty
'''

c.execute(query)
wynik = c.fetchone()

print(wynik)