"""1) multiple inheritance = mosteneste de la mai mult de o clasa : C(A,B) """
"""2) multilevel inheritance = mosteneste de la un parent care mosteneste de la un bunic : A-> B(A)-> C(B)  """

class Animal:
    def __init__(self, nume):
        self.nume = nume
    def mananca(self):
        print(f" {self.nume} trebuie sa manance pentru a supravietui.")
    def doarme(self):
        print(f" {self.nume} doarme.")
    def se_spala(self):
        print(f" {self.nume} are un ritual de cleaning.")


class Pradator(Animal):
    def vaneaza(self):
        print(f"{self.nume} este un vanator.")

class Prada(Animal):
    def se_ascunde(self):
        print(f" {self.nume} este o prada.")

class Crocodil(Pradator):
    pass

class Vulpe(Pradator, Prada):
    pass

class Ariciul(Pradator, Prada):
    pass

crocodil = Crocodil("Crocodilul")
vulpe  = Vulpe("Vulpea")
arici =Ariciul("Ariciul")

crocodil.mananca()
crocodil.vaneaza()
vulpe.se_ascunde()
vulpe.vaneaza()
arici.se_spala()
arici.vaneaza()
arici.se_ascunde()
