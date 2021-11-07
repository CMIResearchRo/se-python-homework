"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""

my_str = input()

print("".join([x.upper() if i % 2 == 0 else x for i, x in enumerate(my_str)]))