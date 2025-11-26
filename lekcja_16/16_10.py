'''Walidator nagłówków: Napisz funkcję  validate_request(request_dict: dict) ,
która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
nagłówki:  Host  i  User-Agent .
Jeśli któregoś z nagłówków brakuje w kluczu  headers , funkcja powinna podnieść
wyjątek  ValueError  z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
Host").
'''

my_dict_1 = {
    "headers": {
        "Host": "example-store.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Accept": "application/json"
    }
}

my_dict_2 = {
    "headers": {
        "NonHost": "example-store.com",
        "Agent": "MyCoolBrowser/1.0",
        "Accept": "application/json"
    }
}

def validate_request(request_dict: dict):
    headers = request_dict.get("headers", {})
    keys_to_check = ["Host", "User-Agent"]

    for key in keys_to_check:        
        try:
            print(f"Klucz {key} istnieje. Wartość: {headers[key]}")
        except KeyError:
            print(f"Nagłówek '{keys_to_check}' nie istnieje.")

validate_request(my_dict_1)
validate_request(my_dict_2)