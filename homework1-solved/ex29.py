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
x = input()
vowels = 'aeiou'
counter_v = 0
counter_c = 0
for character in x:
    if character in vowels:
        counter_v += 1
    else:
        counter_c += 1
print(counter_v)
print(counter_c)

