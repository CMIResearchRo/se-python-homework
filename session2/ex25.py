"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa introduceti toate elemente intr-o lista si s-o afisati, dupa
    care va trebui sa creati un set (vezi ce e un set) din lista respectiva
    si sa il printati si pe acela.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa prima data: [1, 3, 4, 5, 5]
        Veti prina a doua oara: {1, 3, 4, 5}
"""

x = ()
l = []
s = {}
l2 = []
while x != 'exit':
    x = (input())
    if x == 'exit':
        break
    l.append(int(x))
    l2.append(str(x))

print(l)

s = set(l)

print(s)

###