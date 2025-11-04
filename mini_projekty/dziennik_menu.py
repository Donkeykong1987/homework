from dziennik_kod import(
    choice, 
    add_student, 
    add_subject, 
    add_grade, 
    subject_avg, 
    student_avg
)


students_list_grades = {
    "Paweł": {
        "matematyka": [3, 6, 1] ,
        "historia": [1, 3, 4.5],
        "biologia": [1, 2, 2.5],
    },
    "Jan": {
        "matematyka": [3.5, 2, 1.5],
        "historia": [4, 5, 4.5],
        "biologia": [3, 6, 3.5],
    },
    "Kasia": {
        "matematyka": [2.5, 5, 4.5],
        "historia": [1, 4, 5.5],
        "biologia": [1, 2, 3.5],
    }
}

print("Wyświetl listę uczniów - wciśnij 1")
print("Dodaj ucznia - wciśnij 2")
print("Dodaj przedmiot - wciśnij 3")
print("Dodaj ocenę - wciśnij 4")
print("Policz średnią z jednego przedmiotu dla danego ucznia - wciśnij 5")
print("Policz średnia ogólną dla danego ucznia - wciśnij 6")
print("Zakończ - wciśnij 7")

while True:
    user_choice = int(input("Co chcesz zrobić: wcisnij (1-7):"))
    if user_choice == 1:
        print(choice(students_list_grades))
    if user_choice == 2:
        print(add_student(students_list_grades))
    if user_choice == 3:
        print(add_subject(students_list_grades))
    if user_choice == 4:
        print(add_grade(students_list_grades))
    if user_choice == 5:
        print(subject_avg(students_list_grades))
    if user_choice == 6:
        print(student_avg(students_list_grades))
    if user_choice == 7:
        print("Koniec")
        break