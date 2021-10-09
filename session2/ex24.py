"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""

a = input()

l1 = []
l2 = []

for x in a:
    l1.append(x)
    l2.append(x)
l2.reverse()
if l2 == l1:
    print(True)
else:
    print(False)

###