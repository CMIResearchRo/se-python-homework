"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""

def SumRecurs(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + SumRecurs(list[1:])

print(SumRecurs([1, 2, 3]))

###