# 1. importam doar anumite functii din fisierul functiiSimple
#  from functiiSimple import say_goodbye
#  say_goodbye()


# 2.importam toate functiile create in fisierul functiiSimple folosind *
#  from functiiSimple import *
#  say_goodbye()


# 3. importam tot pachetul, din care apelam functia de care avem nevoie
#    import functiiSimple
#    functiiSimple.say_goodbye()


# 4. importam un pachet care este incorportat in Python ---> random

import random as r

random_numer=r.randrange(12)+1

print('Random number generated:', random_numer)


#   Module: Un modul în Python este un fișier .py care conține funcții, variabile și clase. Orice fișier .py este, de fapt, un modul, iar importarea lui într-un alt fișier este simplă, folosind import.
#   Pachete: Un pachet este un director care conține mai multe module, dar și un fișier special numit __init__.py.
#   Pachetele permit organizarea codului în sub-module, făcându-l mai ușor de gestionat și reutilizat.


# 5. import requests as rq
#  requests este una dintre cele mai populare biblioteci Python pentru a trimite cereri HTTP și a obține date de pe web.
#  Este folosită frecvent pentru a interacționa cu API-uri și pentru a descărca conținut de la diverse site-uri web.
#  poate fi folosit cu POSTMAN !! 