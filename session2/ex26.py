"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa printati True (boolean) de fiecare data cand elementul
    primit este par, si False (boolean) de fiecare data cand elemtnul primit
    este impar.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa:
        False
        False
        True
        False
        False
"""
x = ()
l = []
while x != 'exit':
    x = input()
    if x != 'exit':
        if int(x) % 2 == 0:
            l.append("True")
        else:
            l.append("False")
    elif x == 'exit':
        break
print('\n'.join(l))

###