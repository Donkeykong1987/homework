'''Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
SUM() oraz klauzuli WHERE z JOIN
'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT SUM(p.cena)
FROM Produkty p
JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
WHERE k.id_kategorii = 1;

'''

c.execute(query)
wynik = c.fetchone()

print(wynik[0])