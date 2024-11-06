class Animal:
    """Mostenirea permite unei alte clase se mosteneasca atribute si metode din alta clasa. Ajuta la reutilizarea codului intr-un mod mai eficient."""


    def __init__(self, specie):
        self.specie = specie
        self.is_wild = False

    def manaca(self):
        print(f'{self.specie} mananca')

    def doarme(self):
        print(f'{self.specie} doarme')

    def merge(self):
        print(f'{self.specie} merge')


class Pisica(Animal):
    def __init__(self):
        Animal.__init__(self, 'pisica')

    def scoate_sunete(self):
        print(f'{self.specie} face miau miau miau')


class Vulpe(Animal):
    def __init__(self):
        Animal.__init__(self, 'vulpea')
        self.is_wild = True

    def is_free(self):
        if self.is_wild:
            print(f"{self.specie} este un animal salbatic")
        else:
            print(f"{self.specie} este un animal domestic")



pisica = Pisica()
pisica.merge()
pisica.scoate_sunete()

vulpe = Vulpe()
vulpe.doarme()
vulpe.is_free()

a = Animal('iepurele')
a.merge()
a.doarme()
