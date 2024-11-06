from Tema1 import Student

student1: Student = Student('Andrei', 'Popescu', 18, 'UAIC', 3939399405056, 'Informatica si Statistica')
student2: Student = Student('Marian', 'Popovici', 22, 'UMF', 3939399408888, 'Farmacie')
student3: Student = Student('Alexandra', 'Rusu', 19, 'UPA', 3939399403939, 'Cibernetica')
student4: Student = Student('Florin', 'Puiu', 21, 'UMF', 3939399401000, 'Medicina')
student5: Student = Student('Dorin', 'Grosu', 20, 'UAIC', 3939399409999, 'Cibernetica')
student6: Student = Student('Mihai', 'Novic', 23, 'UBC', 39393994092323, 'Statistica')

"""1) Printam numarul total de obiecte din clasa Student"""
print(f"Numarul total de studenti in anul {Student.anul_facultatii} este de {Student.nr_studenti}.")

"""2) Printam numele primului student."""
print(student1.nume)

"""3) Apelam functia DOARME pentru studentul 6"""
student6.doarme()

"""4) Printam lista de obiecte de tipul Student"""
for student in Student.student_list:
    print(student)

"""5) Printam cel mai tanar student. Pentru varianta aceasta, putem folosi oricare alt student din listă pentru a apela metoda youngest_student."""
student2.youngest_student(Student.student_list)


