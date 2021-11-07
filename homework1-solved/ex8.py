"""
    Ex. 8: Modificati urmatoarea bucata de cod astfel incat
    la rulare, daca valoarea care vine de la tastatura nu este 'cmi'
    sa afisam 'NOT OK'
"""

# In x vom salvea valoarea care vine de la tastatura
x = input()

# Daca valorea care vine de la tastatura este 'cmi', vom afisa 'OK'
# Rezolvarea:
if x != 'cmi':
    print('NOT OK')
