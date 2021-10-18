"""
    Ex. 10: Modificati urmatoarea bucata de cod astfel incat
    la rulare, sa printati dictionarul d1 care va avea ca si chei elementele
    din l1 iar ca valori, elementele din l2

    Raspunsul corect la printare arata asa:
    {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd'
    }
"""

# In variabila l1 si l2 avem urmtoarele liste:
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c', 'd']

# In varaibila d1 avem un dictionar gol
# d1 = {}

# Rezolvare:
d1 = {
    l1[i]: l2[i] for i in range(len(l1))
}

# Afisam listele l1 si l2
print(l1, l2)
