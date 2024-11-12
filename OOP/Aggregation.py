""""Aggregation = represents a relationship where one object (the whole) contains references to one or more Independent objects (the parts). """


class Reprezentanta:
    def __init__(self, nume: str, locatie: str):
        self.nume = nume
        self.locatie = locatie
        self.masini = []

    def adauga_masina(self, masina):
        self.masini.append(masina)

    def lista_masini(self):
        return [f" marca masinii este {masina.marca} iar modelul {masina.model}" for masina in self.masini]


class Masina:
    def __init__(self, marca: str, model: str, an: int, culoare: str, is_4x4: bool):
        self.marca = marca
        self.model = model
        self.an = an
        self.culoare = culoare
        self.is_4x4 = is_4x4


reprezentanta = Reprezentanta('Casa Auto', 'Iasi')

masina1 = Masina('Dacia', 'Sandero Stepway', 2023, 'visiniu', True)
masina2 = Masina('Volkswagen', 'Taigo', 2024, 'kaki', True)
masina3 = Masina('Volkswagen', 'ID.4', 2020, 'alb', False)
masina4 = Masina('Audi', 'A6', 2020, 'gri', False)
masina5 = Masina('BMW', 'i5 M60 xDrive Touring', 2023, 'mustar', True)

reprezentanta.adauga_masina(masina1)
reprezentanta.adauga_masina(masina2)
reprezentanta.adauga_masina(masina3)
reprezentanta.adauga_masina(masina4)
reprezentanta.adauga_masina(masina5)

print(reprezentanta.nume)
# print(reprezentanta.lista_masini())

for masina in reprezentanta.lista_masini():
    print(masina)
