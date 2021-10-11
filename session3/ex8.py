"""
    Ex. 8: Mai jos aveti un exemplu de cum functioneaza un decorator.
    Functia dec este definitia decoratorului.

    Functia f este decorata cu dec.

    Modificati decoratorul in asa fel incat pe langa 'x',
    f sa printeze si 'cmi' inainte.
"""


def dec(func):
    def wrapper():
        func()

    return wrapper


@dec
def f():
    print('x')


f()
