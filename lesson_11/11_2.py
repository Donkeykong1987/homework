'''Zadanie 2 – Atrybuty Produkt
Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.
'''

class Product:
    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category

item = Product("mleko", 4.50, "nabiał")

print(item.product_name)
print(item.product_category)
print(item.product_price)