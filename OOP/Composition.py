"""Composition --> the composed object directly own its components, which cannot exist independently 'owns-a' relationship """


class Motor:
    def __init__(self, putere_motor: float):
        self.putere_motor = putere_motor


class Far:
    def __init__(self, model_far: str):
        self.model_far = model_far


class Masina:
    def __init__(self, marca: str, model: str, culoare: str, putere_motor: float, faruri: str):
        self.marca = marca
        self.model = model
        self.culoare = culoare
        self.cai_putere = Motor(putere_motor)
        self.faruri = [Far(faruri) for far in range(4)] # 2 de ceata + 2 de zi

    def afiseaza_masina(self):
        return f"Masina cu marca {self.marca}, modelul {self.model} are culoarea {self.culoare}, un motor cu {self.cai_putere.putere_motor} cai putere si faruri cu {self.faruri[0].model_far}"


masina = Masina('Audi', 'A5', 'rosie', 7, 'xenon')

print(masina.afiseaza_masina())
