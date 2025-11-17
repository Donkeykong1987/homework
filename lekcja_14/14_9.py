'''Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która 
przyjmuje jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) 
dla wszystkich produktów w tej kategorii
'''

import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    query = '''
    SELECT nazwa_produktu, cena
    FROM Produkty p 
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = ?
    '''

    c.execute(query, (nazwa_kategorii,))
    wynik = c.fetchall()

    conn.close()
    return(wynik)

print(znajdz_produkty_w_kategorii("Książki"))