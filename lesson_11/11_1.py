'''Zadanie 1 – Klasa Film
Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
obiekty tej klasy i wydrukuj informacje o nich.
'''

class Movie:
    def __init__(self, title, director, production_year):
        self.title = title
        self.director = director
        self.production_year = production_year

    def information(self):
        return f"{self.title}, {self.production_year}, reżyseria: {self.director}"
    

movie_1 = Movie("Skazani na Shawshank", "Frank Darabont", 1994)
movie_2 = Movie("Furioza", "Cyprian Olencki", 2021)

print(movie_1.information())
print(movie_2.information())