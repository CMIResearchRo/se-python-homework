"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
x = int(input())

save = x
new_nr = 0
while x:
    aux = x % 10
    x = x // 10
    new_nr = new_nr * 10 + aux

if new_nr == save:
    print(True)
else:
    print(False)
