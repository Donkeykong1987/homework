'''Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
Wewnątrz konstruktora dodaj walidację:
Sprawdź, czy  email  zawiera znak  @ . Jeśli nie, podnieś wyjątek  ValueError  z
odpowiednim komunikatem.
Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
danymi.
'''

class UserRegistration:

    def __init__(self, email, password):

        if "@" not in email:
            raise ValueError("Email jest niepoprawny")
        
        if len(password) < 8:
            raise ValueError("Hasło ma za mało znaków")
        
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"Użytkownik: {self.email}, hasło: {'*' * len(self.password)}"

try:
    User = UserRegistration("pawelsadowski@gmail.com", "Donkeykong_87")
    print(User)
except ValueError as e:
    print("Błąd:", e)

try:
    User1 = UserRegistration("pawelsadowski87gmail.com", "donkey")
    print(User1)
except ValueError as e:
    print("Błąd:", e)

try:
    User2 = UserRegistration("pawelsadowski87@gmail.com", "donkey")
    print(User2)
except ValueError as e:
    print("Błąd:", e)