""""   2) Duck typing -> object must have necessary attributes/methods
Another way to achive polimorphism besides inheritance
Objects must have the minimum necessary atributes/methods
"If it looks like a duck and quacks like a duck, it must be a duck."
"""
from itertools import count
from tkinter.tix import Control


class Countries:
    has_guvern=True

class Romania(Countries):

    def speak(self):
        print("Romanians speak Romanian.")


class Slovenia(Countries):

    def speak(self):
        print("People in Slovenia speak Slovenian.")

class Cat:
    has_guvern=False

    def speak(self):
        print("The language of cats consists of meowing.")

countries =[Romania(), Slovenia(), Cat()]

for country in countries:
    country.speak()
    print(country.has_guvern)





