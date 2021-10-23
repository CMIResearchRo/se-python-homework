"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
vocale = ['a', 'e', 'i', 'o', 'u']
consoane = "bcdfghjklmnpqrstvwxz"
x = input()
vocale = sum(x.count(i) for i in vocale)
consoane = sum(x.count(i) for i in consoane)
print(vocale)
print(consoane)
