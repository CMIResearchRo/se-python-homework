"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import random

x = int(input())

options = ['a', 'c', 'x', 'm', 'j', 'x', 'q', 's', 'r']

print("".join(random.choice(options) for _ in range(x)))
