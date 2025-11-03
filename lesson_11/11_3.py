'''Zadanie 3 – Dziedziczenie Pracownik -> Programista
Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.
'''

class Employee:
    def __init__(self, name, hourly_rate=0):
        self.name = name
        self.__salary = hourly_rate

    def calculate_salary(self, number_of_hours):
        if number_of_hours > 0:
            self.__salary *= number_of_hours
            return f"{self.name} otrzymał pensję {self.__salary}zł za {number_of_hours} godzin pracy"
        else:
            return "Nie przepracowano ani jednej godziny, brak pensji"

    def check_salary(self):
        return self.__salary

class Programmer(Employee):

    def __init__(self, name, hourly_rate, programming_languages):
        super().__init__(name, hourly_rate)
        self.programming_languages = programming_languages
        


person = Programmer("Paweł", 5, "Python")

print(person.calculate_salary(140))
print(f"{person.name} zna następujące języki programowania: {person.programming_languages}")