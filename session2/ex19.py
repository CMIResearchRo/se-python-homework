"""
    Veti primi un string de la tastatura.
    Va trebui sa printati un tuplu care sa contina toate literele acelui string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: ('c', 'm', 'i')
"""

x = input()

y = list()

for a in x:
    y.append(a)
    
print(tuple(y))

###