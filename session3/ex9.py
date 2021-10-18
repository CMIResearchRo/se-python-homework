"""
    Ex. 9: Mai jos aveti o functie care accepta mai multi parametri,
    folosindu-se de *args. Momentan functia printeaza ce primeste.

    Modificati functia incat sa printeze doar al doilea parametru primit.

"""


def f(*args):
    print(*args)


# Nu modificati linia de mai jos
f(1, 2, 3)
