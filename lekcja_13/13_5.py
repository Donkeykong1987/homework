'''Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
powiodła
'''

import sqlite3

conn = sqlite3.connect("biblioteka.db")
c = conn.cursor()

nowy_rok_wydania = 1995
tytul_do_aktualizacji = "Zaginięcie"

c.execute("UPDATE biblioteka SET rok_wydania = ? WHERE tytul = ?",
(nowy_rok_wydania, tytul_do_aktualizacji))

conn.commit()

print(f"Zaktualizowano rok wydania dla tytułu: {tytul_do_aktualizacji}.Zmieniono {c.rowcount} rekordów")

c.execute("SELECT * FROM biblioteka WHERE tytul = ?", (tytul_do_aktualizacji,))
zaktualizowany_tytul = c.fetchone()
print(f"Nowy rok wydania: {zaktualizowany_tytul}")

conn.close()