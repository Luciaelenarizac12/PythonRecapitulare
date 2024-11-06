class Student:
    anul_facultatii = 2024
    nr_studenti = 0
    student_list = []

    def __init__(self, nume: str, prenume: str, varsta: int, universitate: str, cod_student: str, profil: str):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.universitate = universitate
        self.cod_student = cod_student
        self.profil = profil
        Student.nr_studenti += 1
        Student.student_list.append(self)

    def __str__(self):
        return f'Numele studentului este {self.nume} {self.prenume} si are codul de student {self.cod_student}. Acesta are varsta de {self.varsta} ani si invata la universitatea {self.universitate}. De asemenea, acesta este repartizat pe profilul {self.profil}. '

    def invata(self):
        print(f"Studentul {self.nume} {self.prenume} invata cu drag si spor.")

    def mananca(self):
        print(f"Studentul {self.nume} {self.prenume} manaca atunci cand are timp.")

    def doarme(self):
        print(
            f"La varsta sa de {self.varsta} ani, studentul {self.nume} {self.prenume} doarme cat ii permite timpul, deoarece un mare procent il dedica invatatului pentru {self.profil}.")

    def youngest_student(self, student_list):
        cel_mai_tanar_student = student_list[0]
        for student in student_list:
            if student.varsta < cel_mai_tanar_student.varsta:
                cel_mai_tanar_student = student
        print(
            f'Studentul cu numele de {cel_mai_tanar_student.nume} {cel_mai_tanar_student.prenume} este cel mai tanar din lista de studenti, anume are varsta de {cel_mai_tanar_student.varsta} ani. ')
