'''Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
__add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
sobie współrzędne).
__sub__(self, other) : do odejmowania wektorów.
eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
dwa wektory i wykonując na nich wszystkie zaimplementowane operacje.
'''

class Vector_2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector_2D):
            return(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        if isinstance(other, Vector_2D):
            return(self.x - other.x, self.y - other.y)
    
    def __eq__(self,other):
        if isinstance(other, Vector_2D):
            return(self.x == other.x, self.y == other.y)
    
v1 = Vector_2D(1, 5)
v2 = Vector_2D(-5, 7)

add = v1 + v2
sub = v1 - v2
eq = v1 == v2

print((f"Suma wektorów v1 i v2 wynosi: {add}"))
print((f"Różnica wektorów v1 i v2 wynosi: {sub}"))
print((f"Czy wektory v1 i v2 są równe?", eq))