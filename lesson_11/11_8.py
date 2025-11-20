'''Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
super().graj().
Instrument.graj()  ->  "Wydaje dźwięk."
Strunowy.graj()  ->  "Wydaje dźwięk. [Szarpnięcie struny]"
Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]"
'''

class Instrument:
    def play(self):
        return "Wydaje dźwięki"
    
class String(Instrument):
    def play(self):
        base_play_s = super().play()
        return f"{base_play_s} Szarpnięcie struny"

class Brass(Instrument):
    def play(self):
        base_play_b = super().play()
        return f"{base_play_b} Dmuchnięcie w ustnik"
    
class Guitar(String):
    def play(self):
        base_play_g = super().play()
        return f"{base_play_g} Akord G-dur"

class Trumpet(Brass):
    def play(self):
        base_play_t = super().play()
        return f"{base_play_t} Akord C-dur"

gitara = Guitar()
print(gitara.play())

trabka = Trumpet()
print (trabka.play())