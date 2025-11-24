def choice(register):
    return list(register.keys())
           
def add_student(register):
    new_student = input("Podaj imię nowego ucznia: ")
    if new_student not in register:
        register.setdefault(new_student, {})
        return f"Dodano ucznia {new_student}"
    else:    
        return "Podany uczeń już istnieje w dzienniku"
            
        

def add_subject(register):        
    check_student = input("Dla jakiego ucznia przypisać przedmiot: ")
    if check_student in register:
        check_subject = input("Jaki przedmiot dopisać: ")
        if check_subject not in register[check_student]:
            register[check_student][check_subject] = []
            return f"Dodano przedmiot {check_subject} dla ucznia {check_student}"
        else:
            return "Podany przedmiot istnieje"
    else:
        return "Podany uczeń nie istnieje. Wybierz 2 aby go dodać"

def add_grade(register):
    check_student = input("Dla jakiego ucznia przypisać ocenę: ")
    if check_student in register:
        check_subject = input("Dla jakiego przemiotu przypisać ocenę: ")
        if check_subject in register[check_student]:
            new_grade = float(input("Podaj ocenę którą chcesz dodać: "))
            register[check_student][check_subject].append(new_grade)
            return f"Dodano ocenę {new_grade} dla przedmiotu {check_subject} u ucznia {check_student}"
        else:
            return "Podany przedmiot nie istnieje, wybierz 3, aby dodać przedmiot"
    else:
        return "Wybrany uczeń nie istnieje, wybierz 2 aby go dodać"

def subject_avg(register):
    check_student = input("Dla jakiego ucznia chcesz policzyć średnią: ")
    if check_student in register:
        check_subject = input("Dla jakiego przemiotu policzyć średnią: ")
        if check_subject in register[check_student]:
            avg_student_subject = sum(register[check_student][check_subject])/len(register[check_student][check_subject])
            return f"Średnia z przedmiotu {check_subject} dla ucznia {check_student} wynosi {avg_student_subject:.2f}"
        else:
            return "Podany przedmiot nie istnieje, wybierz 3, aby dodać przedmiot"
    else:
        return "Wybrany uczeń nie istnieje, wybierz 2 aby go dodać"

def student_avg(register):
    
    check_student = input("Dla jakiego ucznia chcesz policzyć średnią: ")

    if check_student in register:
        subject_avgs = []
        for subject, grades in register[check_student].items():
            if len(grades) == 0:
                print(f"Brak ocen z przedmiotu: {subject}")
            else:
                subject_avg = sum(grades) / len(grades)
                subject_avgs.append(subject_avg)

        if len(subject_avgs) == 0:
            return "Uczeń nie ma żadnych ocen."
        
        else:
            final_avg = sum(subject_avgs) / len(subject_avgs)
            return f"Średnia ucznia {check_student}: {final_avg:.2f}"
    else:
        return "Nie znaleziono ucznia w dzienniku."
