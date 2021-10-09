"""
    Veti primi stringuri de la tastatura, pana cand primiti stringul 'exit'.
    Va trebui sa printati o lista cu stringurile primite fara ultimul caracter
    al fiecarui string.

    Observatii:
        - lungimea stringurilor va fi intotdeauan cel putin 1

    exemplu:
        Veti primi: 'cmi', 'center', 'for', 'machines'
        Veti printa: ['cm', 'cente', 'fo', 'machine']
"""
x = ()
l = []

while x != "exit":
    x = input()
    if x == "exit":
        break 
    y = x[0:-1]
    l.append(y)

print(l)

###