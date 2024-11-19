""" @property -> decorator used to define a method as a property (it can be accessed like an atribute)
                -> benefit : add additional logic when read, write or delete attributes
                -> gives you getter (to read), setter (to write) and deleter method (to delete) """


class Calculator:
    def __init__(self, monitor: str, procesor: int, placa_de_baza: str, memorie_ram: int):
        self._monitor = monitor  # ca sa facem atributele private trebuie sa folosim un _ -> adica self._monitor=monitor
        self._procesor = procesor
        self._placa_de_baza = placa_de_baza
        self._memorie_ram = memorie_ram


#daca facem atributele private (ele vor deveni interne), ele nu vor mai putea fi accesate in mod direct de alte clase din afara clasei Calculator
# aici folosim getter
    @property
    def procesor(self):
        return f" {self._procesor} cu codul BX8071513900K"
    @property
    def memorie_ram(self):
        return f" {self._memorie_ram} cu codul CMW32GX4M2E3200C16"

# aici folosim setter
    @procesor.setter
    def procesor(self, new_procesor):
        if new_procesor > 5:
          self._procesor= new_procesor
        else:
            print ("Procesorul nu poate avea un model mai vechi de 5.")

    @memorie_ram.setter
    def memorie_ram(self, new_memorie_ram):
        if new_memorie_ram > 8:
          self._memorie_ram= new_memorie_ram
        else:
            print ("Memoria RAM este foarte mica.")

#aici folosim deleter
    @procesor.deleter
    def procesor(self):
        del self._procesor
        print(" Procesorul a fost sters.")

    @memorie_ram.deleter
    def memorie_ram(self):
        del self._memorie_ram
        print(" Memoria RAM a fost stearsa.")

calculator = Calculator('Dell UltraSharp U2723QE', 5, 'ASUS ROG Strix Z790-E Gaming WiFi',
                        8)
calculator.procesor=4
calculator.memorie_ram=32

# del calculator.memorie_ram
# del calculator.procesor

# print(calculator._memorie_ram) #daca folosim atributele private din constructor , folosind _, imi printeaza direct elementele selectate din obiect
# print(calculator._procesor)

print(calculator.memorie_ram)  # daca le printam simplu, practic apelam metodele create cu ajutorul decoratorului @property -> aici folosim de fapt getter ul pentru ca ne ajuta sa citim
print(calculator.procesor)





