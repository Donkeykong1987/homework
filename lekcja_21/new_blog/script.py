from datetime import date, timedelta
from new_blog import Blog, Author, Entry

# Tworzenie blogów
tech_blog = Blog.objects.create(name="Blog Techniczny", tagline="Najnowsze technologie")
food_blog = Blog.objects.create(name="Blog Kulinarny", tagline="Pyszne przepisy i recenzje")
# Tworzenie autorów
jan = Author.objects.create(name="Jan Kowalski", email="jan@example.com")
anna = Author.objects.create(name="Anna Nowak", email="anna@example.com")
piotr = Author.objects.create(name="Piotr Wiśniewski", 
email="piotr@example.com")

# Tworzenie wpisów
wpis1 = Entry.objects.create(
    blog=tech_blog,
    headline="Najlepsze Praktyki Python",
    body_text="Poznaj standardy kodowania i najlepsze praktyki w Python...",
    pub_date=date.today() - timedelta(days=5),
    number_of_comments=15,
    number_of_pingbacks=3,
    rating=9
)

wpis1.authors.add(jan, anna)

wpis2 = Entry.objects.create(
    blog=tech_blog,
headline="Tutorial Django ORM",
    body_text="Kompletny przewodnik po Django ORM z przykładami...",
    pub_date=date.today() - timedelta(days=2),
    number_of_comments=8,
    number_of_pingbacks=1,
    rating=8
)

wpis2.authors.add(jan)

wpis3 = Entry.objects.create(
    blog=food_blog,
    headline="Najlepszy Przepis na Pizzę",
    body_text="Jak zrobić autentyczną włoską pizzę w domu...",
    pub_date=date.today() - timedelta(days=1),
    number_of_comments=25,
    number_of_pingbacks=5,
    rating=10
)

wpis3.authors.add(anna, piotr)
print("Przykładowe dane zostały utworzone pomyślnie!")