"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""
###

a = input()

l1 = []
l2 = ""

for x in a:
    l2 = x + l2
    l1.append(x)
l2 = list(l2)
if l2 == l1:
    print(True)
else:
    print(False)

###