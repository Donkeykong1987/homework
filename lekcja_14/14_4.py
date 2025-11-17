'''Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT AVG(cena)
FROM Produkty
WHERE id_kategorii = 2
'''

c.execute(query)
wynik = c.fetchone()

print(f"Srednia wartość produktów z kategorii Książki to: {wynik[0]}")