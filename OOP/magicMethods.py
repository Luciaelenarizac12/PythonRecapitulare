"""
Magic methods -> dunder methods (double underscore) __init__ (constuctor) , __str__ ( metoda de printare), __eq__ ( equals) , __gt__ (mai mare ca), __ld__ (less than)

"""

class Pisica:
    nr_pisici=0
    varsta_totala=0

    def __init__(self, nume, rasa, colorit, varsta):
        self.nume=nume
        self.rasa=rasa
        self.colorit=colorit
        self.varsta=varsta
        Pisica.nr_pisici+=1
        Pisica.varsta_totala += varsta

    def prezinta_pisica(self):
        return f"{self.nume} {self.rasa} {self.colorit} {self.varsta}"

    def __str__(self):
        return f" pisica se numeste {self.nume} si este {self.rasa} "

    def __eq__(self, other):  # compara vasta pisicilor cu equals, returneaza un boolean
        return self.varsta == other.varsta

    def __gt__(self, other):
        return self.varsta > other.varsta\

    def __add__(self, other):
        return self.varsta + other.varsta

    def __contains__(self, keyword):
        return keyword in self.rasa or keyword in self.colorit

    def __getitem__(self, key):
        if key == 'nume':
            return self.nume




pisica1=Pisica('Grasunel', 'siameza', 'gri', 4)
pisica2=Pisica('Rex', 'burmeza', 'maro', 6)
pisica3=Pisica('Biru', 'birmaneza', 'alba', 1)
pisica4=Pisica('Mitu', 'persana', 'alba', 1)

print(str(pisica1.prezinta_pisica()))
print(pisica2.prezinta_pisica())
print(pisica3==pisica4)
print(pisica2 > pisica4)
print(pisica2 + pisica4)
print('Rex' in pisica4 )
print('siameza' in pisica1 )
print(pisica3['nume'])