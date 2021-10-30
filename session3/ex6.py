"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""
def func(text):
    l = (ord(x) for x in text)
    l2 = [x + 1 for x in l]
    return(''.join(chr(x) for x in l2))
print(func('aabbcc'))

###
