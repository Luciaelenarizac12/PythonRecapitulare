class Animal:
    def __init__(self, specie):
        self.specie=specie

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
        Animal.__init__(self, 'vulpe')

    def scoate_sunete(self):
        print(f'{self.specie} face ikikikik')

pisica=Pisica()
pisica.merge()
pisica.scoate_sunete()


vulpe=Vulpe()
vulpe.doarme()
vulpe.scoate_sunete()

a=Animal('iepurele')
a.merge()
a.doarme()


