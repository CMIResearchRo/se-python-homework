"""
    Veti primi un input de la tastatura (input()). By default, orice input
    de la tastatura este ca si tip de date str (string).
    Inputul vostru va fi intotdeauna un numar intreg, deci trebuie sa il
    convertiti la int, iar dupa ce aveti inputul, trebuie sa afisati toate
    numerele impare pana la numarul respectiv.

    exemplu:
        Daca veti primi 6, veti afisa:
        1
        3
        5
        cate un singur numar pe linie.
"""

x = int(input())

for i in range(x):
    if i % 2 == 1:
        print(i)