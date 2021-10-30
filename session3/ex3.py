"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""


def func(x):
    list = []
    n = 0
    while n < x:
        list.append(n)
        n = n + 1
    print(list)

func(3)
    
###