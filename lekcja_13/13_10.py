'''Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.
'''

import sqlite3

def znajdz_sale_studenta():
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    query = """
    SELECT s.nazwisko, a.numer_sali
    FROM studenci s
    JOIN przypisania p ON s.id_studenta = p.id_studenta
    JOIN audytorium a ON a.id_audytorium = p.id_audytorium
    """

    c.execute(query)
    results = c.fetchall()
    conn.close()

    for row in results:
        print(row)

    
znajdz_sale_studenta()