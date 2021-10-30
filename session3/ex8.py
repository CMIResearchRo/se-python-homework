"""
    Ex. 8: Mai jos aveti un exemplu de cum functioneaza un decorator.
    Functia dec este definitia decoratorului.

    Functia f este decorata cu dec.

    Modificati decoratorul in asa fel incat pe langa 'x',
    f sa printeze si 'cmi' inainte.
"""


def dec(func):
    print("cmi")
    return func


@dec
def f():
    print('x')


f()

###
