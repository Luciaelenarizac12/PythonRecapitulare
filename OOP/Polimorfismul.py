""""Polimorfismul - in greek means to have many forms or faces (Poly= many & Morphe =form)

Sunt 2 modalitati de a implementa polimorfismul:
1) prin mostenire -> an object could be treated of the same type as a parent class

2) Duck typing -> object must have necessary attributes/methods
"""

from abc import ABC, abstractmethod

class Mobilier(ABC):

    @abstractmethod
    def functionalitate_si_utilizare(self):
        pass

    @abstractmethod
    def decor(self):
        pass

class Dulap(Mobilier):
    def __init__(self, denumire:str, usi:int, material:str):
        self.usi=usi
        self.material=material
        self.denumire=denumire

    def functionalitate_si_utilizare(self):
        print(f"{self.denumire} are un numar de {self.usi} usi si este din {self.material}.")

    def decor(self):
        print(f"{self.denumire} are si rol de decor")

class Masa(Mobilier):
    def __init__(self,denumire:str, forma:str, material:str):
        self.denumire = denumire
        self.forma=forma
        self.material=material


    def functionalitate_si_utilizare(self):
        print(f"{self.denumire} are forma {self.forma} si este din {self.material}.")

    def decor(self):
        print(f"{self.denumire} are si rol de decor")


class Biblioteca (Mobilier):
    def __init__(self, denumire:str, rafturi:int, inaltime:float):
        self.rafturi=rafturi
        self.inaltime=inaltime
        self.denumire = denumire

    def functionalitate_si_utilizare(self):
        print(f"{self.denumire} are inaltimea de {self.inaltime} m si are {self.rafturi} rafturi.")

    def decor(self):
        print(f"{self.denumire} are si rol de decor")

class Covor(Masa):
    def __init__(self,denumire:str, forma:str, material:str, tine_cald:bool):
        super().__init__(denumire,forma,material)
        self.tine_cald=tine_cald

    def functionalitate_si_utilizare(self):
        super().functionalitate_si_utilizare()
        print(f" Este {self.tine_cald} ca {self.denumire} pastreaza caldura in casa.")

    def decor(self):
        print(f"{self.denumire} are si rol de decor")

mobilier = [Masa('Masa','rotunda','lemn si rasina'), Dulap('Dulapul',2,'lemn masiv'), Biblioteca('Biblioteca', 40, 3.8), Covor ('Covorul', 'dreptunghiulara', 'lana, iuta si bumbac', True )]

for piesa in mobilier:
    piesa.functionalitate_si_utilizare()
    piesa.decor()