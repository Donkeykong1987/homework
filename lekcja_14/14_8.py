'''Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów 
należących do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT nazwa_kategorii, COUNT(id_produktu)
FROM Kategorie k
JOIN Produkty p ON k.id_kategorii = p.id_kategorii
GROUP BY nazwa_kategorii
'''

c.execute(query)
wynik = c.fetchall()

print(wynik)