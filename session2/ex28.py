"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""

x = int(input())
s = 0
y = x + 1
for i in range(0,y):
    s = s + i
print(s)

###