'''To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
samej bazie uczelnia.db. Tabela powinna mieć strukturę:
id_przypisania  (INTEGER, klucz główny)
id_studenta  (INTEGER) – będzie to tzw. klucz obcy wskazujący na  id_studenta  w
tabeli  studenci .
id_audytorium  (INTEGER) – klucz obcy wskazujący na  id_audytorium  w tabeli
audytoria 
'''


import sqlite3

conn = sqlite3.connect("uczelnia.db")

c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY,
        id_studenta INTEGER,
        id_audytorium INTEGER
    )
''')

c.execute("SELECT id_studenta FROM studenci")
studenci_ids = [row[0] for row in c.fetchall()]

c.execute("SELECT id_audytorium FROM audytorium")
audytoria_ids = [row[0] for row in c.fetchall()]

for i in range(min(len(studenci_ids), len(audytoria_ids))):
    c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
    (studenci_ids[i], audytoria_ids[i])
    )



conn.commit()



conn.close()
