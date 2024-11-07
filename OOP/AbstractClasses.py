"""Clasele abstracte:
O clasă abstractă nu poate fi instanțiată pe cont propriu. Este destinată a fi extinsă (mostenita) prin alte clase.
Poate conține metode abstracte, care sunt declarate, dar nu au o implementare (corp).
Avantajele unei clase abstracte:
1) Previne instanțierea clasei în sine.
2) Impune claselor copil (subclase) să folosească metodele abstracte moștenite.

abc -> abstract base classes
ABC -> abstract base class (ABC este o clasă de bază din modulul abc, pe care o folosim ca superclasă pentru a crea o clasă abstractă. Atunci când o clasă moștenește ABC, aceasta devine o clasă abstractă și nu poate fi instanțiată direct.)
"""
from abc import ABC, abstractmethod
class AgentieTurism (ABC):

    @abstractmethod
    def vinde_bilete_avion(self):
        pass

    @abstractmethod
    def cauta_cele_mai_bune_oferte_pt_cumparatori(self):
        pass

class ChristianTour(AgentieTurism):

    def vinde_bilete_avion(self):
        print("Christian Tour este o agentie de turism care vinde bilete pentru vacante cu destinatii din intreaga lume.")

    def cauta_cele_mai_bune_oferte_pt_cumparatori(self):
        print("Christian Tour are cele mai bune preturi de pe piata la momentul actual.")

class Paralela45(AgentieTurism):
    def vinde_bilete_avion(self):
        print("Paralela45 este si ea o agentie de turism care vinde bilete pentru vacante cu destinatii din intreaga lume.")

    def cauta_cele_mai_bune_oferte_pt_cumparatori(self):
        print("Paralela45 are preturi destul de mari la momentul actual.")



cristian_tour=ChristianTour()
cristian_tour.vinde_bilete_avion()
cristian_tour.cauta_cele_mai_bune_oferte_pt_cumparatori()

paralela_45=Paralela45()
paralela_45.vinde_bilete_avion()
paralela_45.cauta_cele_mai_bune_oferte_pt_cumparatori()



