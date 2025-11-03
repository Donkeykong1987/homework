'''Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
pętli wydrukuj pole każdej figury
'''

class Figure:

    def __init__(self, x):
        self.x = x
    
    def count_area(self):
        pass

class Square(Figure):
    def count_area(self):
        area = self.x ** 2
        return area

class Circle(Figure):
    def count_area(self):
        pi = 3.14159
        area = pi * self.x ** 2
        return area

my_square = Square(4)
my_circle = Circle(5)

figure_list = [my_square.count_area(), my_circle.count_area()]
print(figure_list)

for object in figure_list:
    print(object)
