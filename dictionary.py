""""dictionary -> a changeable, unordered collection of unique key: value pairs
                -> fast because they use hashing, allow us to access a value quickly
"""

capitals= { 'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# print(capitals['Russia']) # imi afiseaza valoarea
# print(capitals.get('Germany')) # functia get ma ajuta sa caut in dictionarul meu aceasta valoare cu ajutorul unei chei
# print(capitals.keys()) # imi face o lista cu cheile dictionarului
# print(capitals.values()) # imi face o lista cu valorile dictionarului
# print(capitals.items()) # imi printeaza itemii (cheie-valoare) dictionarului

# capitals.update({'Germany':'Berlin'}) # a adaugat o pereche noua in dictionar
# capitals.update({'USA':'Las Vegas'}) # a actualizat valoarea unei perechi
# capitals.pop('China') #imi sterge o pereche cu totul cu ajutorul unei key
# capitals.clear() #imi goleste dictionarul

for key, value in capitals.items():
    print(key, value)


