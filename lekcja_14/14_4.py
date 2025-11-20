'''Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT AVG(cena)
FROM Produkty p
JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
WHERE k.nazwa_kategorii = ?
'''

c.execute(query, ("Książki",)
wynik = c.fetchone()

conn.close()

print(f"Srednia wartość produktów z kategorii Książki to: {wynik[0]}")
