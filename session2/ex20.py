"""
    Veti primi un string de la tastatura.
    Veti primi un numar intreg de la tastatura, x.
    Va trebui sa creati un dictionar care sa contina ca si chei, toate numerele
    pana la x, iar ca si valori caracterele de pe indexurile corespunzatoare.

    Observatii:
        - lungimea stringului va fi mereu egala cu numarul primit
        - indexarea in python incepe de la 0 (prima cheie va fi 0)

    exemplu:
        Veti primi: 'cmi', 3
        Veti printa: {
            0: 'c',
            1: 'm',
            2: 'i'
        }
"""

a = input()

b = int(input())

l1 = list()
l2 = list()

d1 = {

}
for n in a:
    l1.append(n)
print(l1)
for i in range(b):
    l2.append(i)
print(l2)
d1 = zip(l2, l1)
d2 = dict(d1)

print(d2)
###