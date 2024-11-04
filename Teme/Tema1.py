""""Creaza o clasa cu numele Student. Printeaza numarul de obiecte din clasa ta. """


class Student:
    anul_facultatii=2024
    nr_studenti=0
    def __init__(self, nume: str, prenume: str, varsta: int, universitate: str, cod_student: str, profil: str):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.universitate = universitate
        self.cod_student = cod_student
        self.profil = profil
        Student.nr_studenti +=1


    def __str__(self):
        return f'Numele studentului este {self.nume} {self.prenume} si are codul de student {self.cod_student}. Acesta are varsta de {self.varsta} ani si invata la universitatea {self.universitate}. De asemenea, acesta este repartizat pe profilul {self.profil}. '

    def invata(self):
        print("Studentul invata cu drag si spor.")

    def mananca(self):
        print("Studentul manaca atunci cand are timp.")

    def doarme(self):
        print("Studentul doarme cat ii permite timpul.")

student1: Student=Student ('Andrei', 'Popescu', 19, 'UAIC', 3939399405056, 'Informatica si Statistica')
student2: Student=Student ('Marian', 'Popovici', 20, 'UMF', 3939399408888, 'Farmacie')
student3: Student=Student ('Alexandra', 'Rusu', 19, 'UPA', 3939399403939, 'Cibernetica')
student4: Student=Student ('Florin', 'Puiu', 21, 'UMF', 3939399401000, 'Medicina')
student5: Student=Student ('Dorin', 'Grosu', 20, 'UAIC', 3939399409999, 'Cibernetica')


print(str(student2))
print(f"Numarul total de studenti in anul {Student.anul_facultatii} este de {Student.nr_studenti}. ")