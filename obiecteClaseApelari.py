""""Press Shift+F10 to execute it or replace it with your code.
Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings."""
""""o clasa este un blueprint pentru cum un obiect si reprezenta cum ar trebui sa arate si sa functioneze respectivul obiect"""
class Laptop:
    #constructor
    def __init__(self, marca:str, placa_de_baza:str, memorie_ram:str, procesor:str, placa_video:str, monitor:str):
        self.marca = marca  #atribut sau instante
        self.placa_de_baza = placa_de_baza
        self.memorie_ram = memorie_ram
        self.procesor = procesor
        self.placa_video = placa_video
        self.monitor = monitor

    # acestea sunt metode (sau functii)
    def __str__(self):
        return f"Laptopul {self.marca} are o placa de baza '{self.placa_de_baza}', memorie de {self.memorie_ram}, procesor {self.procesor}, placa video {self.placa_video} si monitor {self.monitor})"

    def procesare_date(self):
        print(
            f'Laptopul cu marca {self.marca} poate efectua calcule complexe și rapide, de la aritmetică simplă la calcule științifice avansate, esențiale în știință, finanțe, inginerie și multe alte domenii.')

    def inteligenta_artificiala(self):
        print(
            f'Laptopul cu marca {self.marca} poate recunoaște fețe, obiecte, voci și multe altele, utilizând algoritmi de învățare automată.')


asus: Laptop = Laptop ('ASUS', 'MSI MPG B550 Gaming Plus',
              'Kingston Fury Beast 32GB (2x16GB) DDR5-5200', 'AMD Ryzen 7 5800X3D',
              'AMD Radeon RX 7900 XTX', 'ASUS TUF Gaming VG27AQ')

"""object -> a bundle of related atributes and methods"""

print(str(asus))
    # apelam metodele noastre:
asus.procesare_date()
asus.inteligenta_artificiala()

print(asus.monitor)


