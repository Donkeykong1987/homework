'''Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena 
jest wyższa niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT nazwa_produktu, cena
FROM Produkty
WHERE cena > (SELECT AVG(cena) FROM Produkty)
'''

c.execute(query)

wynik = c.fetchall()

print("Lista produktów ktorych cena jest wyższa niż średnia cena:")
for row in wynik:
    print(f"{row[0]}: {row[1]}")