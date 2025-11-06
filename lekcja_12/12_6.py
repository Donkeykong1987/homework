'''Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
(raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
testuje tę funkcję w bloku try...except
'''

class InvalidPasswordError(Exception):
    pass

def set_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Hasło jest za krótkie")
    
    print("Hasło jest dobre")
        

try:
    my_password = input("Wprowadź hasło (minimum 8 znaków): ")
    set_password(my_password)
except InvalidPasswordError as e:
    print(f"Błąd walidacji:", {e})