"""
    Ex. 10: Decoratorul de mai jos printeaza 'cmi' inainte de apelul oricarei
    functii pe care o decoreaza.

    Folosindu-va de kwargs, printati si valoarea lui y dupa ce printati cmi,
    in decorator.

"""


def dec(func):
    def wrapper(*args, **kwargs):
        print('cmi')
        # your code goes here
        func(*args, **kwargs)

    return wrapper


@dec
def f(x, y):
    print(x)


f(x=1, y=2)
