""" super() = functie folosita intr-o clasa copil pentru a chema metode dintr-o clasa parinte. Permite extinderea functionalitatii a metodelor mostenite."""


class FormeGeometrice:
    pi = 3.14

    def __init__(self, forma: str, culoare: str, is_filled: bool):
        self.forma = forma
        self.culoare = culoare
        self.is_filled = is_filled

    def descriere_forma(self):
        print(f"{self.forma} este {self.culoare} si este {'plin' if self.is_filled else 'nu este plin'}")


class Cerc(FormeGeometrice):

    def __init__(self, forma: str, culoare: str, is_filled: bool, raza: float):
        super().__init__(forma, culoare, is_filled)
        self.raza = raza

    def descriere_forma(self):
        super().descriere_forma()
        """vreau totusi sa imi printeze si metoda de afisare din parinte, dar si propria metoda din copil"""
        """" adica s-a facut override la metoda parintelui, dar copilul va avea propriul comportament, adica isi va printa si propriul mesaj"""
        print(f"{self.forma} este o formă geometrică definită ca ansamblul tuturor punctelor dintr-un plan care sunt la aceeași distanță de un punct fix numit centru.")

    def aria(self):
        aria_cercului = FormeGeometrice.pi * self.raza * self.raza
        print(f'Aria cercului este {aria_cercului} cm^2')


class Patrat(FormeGeometrice):
    def __init__(self, forma: str, culoare: str, is_filled: bool, latura: float):
        super().__init__(forma, culoare, is_filled)
        self.latura = latura

    def __str__(self):
        return (f"{self.forma} este o formă geometrică bidimensională, specific un poligon cu patru laturi egale și patru unghiuri drepte.")

    def aria(self):
        aria_patratului = self.latura * self.latura
        print(f'Aria patratului este {aria_patratului}')


class Dreptunghi(FormeGeometrice):
    def __init__(self, forma: str, culoare: str, is_filled: bool, lungime: float, latime: float):
        super().__init__(forma, culoare, is_filled)
        self.lungime = lungime
        self.latime = latime

    def perimetrul(self):
        perimetrul_dreptunghiului = 2 * (self.lungime + self.latime)
        print(f'Perimetrul dreptunghiului este egal cu {perimetrul_dreptunghiului} cm')


cercul = Cerc('cercul', 'verde', True, 2.5)
cercul.aria()
cercul.descriere_forma()

patratul = Patrat('patratul', 'rosu', False, 2.5)
patratul.aria()
print(str(patratul))

dreptunghiul = Dreptunghi('dreptunghiul', 'mov', True, 12.5, 24.3)
dreptunghiul.descriere_forma()
