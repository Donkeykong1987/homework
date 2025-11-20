'''adanie 10 – Eksploracja MRO
Stwórz następującą, złożoną hierarchię dziedziczenia:
class A
class B(A)
class C(A)
class D(B)
class E(C)
class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
odpowiedź, używając print(F.mro()). (challenge)
'''

class A:
    def kim_jestes(self):
        print("Jestem z klasy A")
    
class B(A):
    def kim_jestes(self):
        print("Jestem z klasy B")

class C(A):
    def kim_jestes(self):
        print("Jestem z klasy C")

class D(B):
    def kim_jestes(self):
        print("Jestem z klasy D")

class E(C):
    def kim_jestes(self):
        print("Jestem z klasy E")

class F(D, E):
    pass

print(F.mro())

f = F()
f.kim_jestes()