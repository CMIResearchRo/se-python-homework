"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
x = input()
l = []
for i in range(len(x)):
    if i % 2 ==0:
        l.append(x[i].upper())
    elif i % 2 == 1:
        l.append(x[i].lower())
print("".join(l))

###