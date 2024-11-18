""""
Class methods -> allow operations related to the class itself
            -> Take (cls) as the first parameter, which represents the class itself
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

    @classmethod
    def get_nr_pisici(cls):
        return f"nr de pisici este: {cls.nr_pisici}"

    @classmethod
    def get_varsta_totala(cls):
        return f"varsta totala a pisicilor este: {cls.varsta_totala}"

pisica1=Pisica('Bonnie', 'british short hair', 'shaded', 3)
pisica2=Pisica('Clyde', 'scottis fold', 'silver tabby', 2)
pisica3=Pisica('Masha', 'main coon', 'white', 5)

print(Pisica.get_nr_pisici())
print(Pisica.get_varsta_totala())