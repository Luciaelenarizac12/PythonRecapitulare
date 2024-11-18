"""
A static method belong to a class rather than any object from that class ( instance).
Statis method is usually used for general utility functions,

Instance methods -> best for operations on instances of the class (objects)
Static methods -> best for utility functions that do not need access to class data
"""
class Angajat:
    def __init__(self, nume, prenume, varsta, functie):
        self.nume=nume
        self.prenume=prenume
        self.varsta=varsta
        self.functie=functie

    def afiseaza_angajat(self):
        return f"Angajatul {self.nume} {self.prenume} are varsta de {self.varsta} ani si lucreaza ca {self.functie}"

    @staticmethod
    def pozitii_in_companie(functie):
        pozitii_valide=['analist financiar', 'QA tester', 'Developer', 'design arhitect', 'business analyst', 'project manager']
        return functie in pozitii_valide


angajat1=Angajat('Daniel', 'Iacob', 26, 'analist financiar')
angajat2=Angajat('Ion', 'Mac', 28, 'Developer')
angajat3=Angajat('Alexandra', 'Nica', 26, 'project manager')
angajat4=Angajat('Alexandru', 'Solea', 30, 'design arhitect')


print(Angajat.pozitii_in_companie('QA tester'))
print(Angajat.pozitii_in_companie('project specialist'))
print(angajat1.afiseaza_angajat())