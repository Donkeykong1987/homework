'''Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta 
o imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: 
Klienci, Zamowienia, Zamowienia_Produkty i Produkty'''

import sqlite3

conn = sqlite3.connect("sklep.db")
c = conn.cursor()

query = '''
SELECT nazwa_produktu
FROM Produkty p
JOIN Zamowienia_Produkty z ON p.id_produktu = z.id_produktu
JOIN Zamowienia k ON z.id_zamowienia = k.id_zamowienia
JOIN Klienci l ON k.id_klienta = l.id_klienta
WHERE l.id_klienta = 1
'''

c.execute(query)
wynik = c.fetchall()

print(wynik)