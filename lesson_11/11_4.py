'''Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y)
'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        point = (self.x, self.y)
        return f"{point}"

my_point = Point(1, 5)

print(my_point)  