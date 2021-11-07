"""
    Ex. 3: Modificati urmatoarea bucata de cod astfel incat
    la rulare, in loc sa ne oprim din adaugat elementele primite de la
    tastatura in lista pana sa primim 'exit', ne vom opri cand vom primi 'stop'
"""

# Cream o variabila l1 care are ca si valoare o lista goala
l1 = []

# Preluam input de la tastatura si il salvam in variabila x
x = input()

# Cat timp de la tastatura nu primim exit ca si valoare
while x != 'stop':
    # Adaugam la lista elementul nou primit de la tastatura
    l1.append(x)
    x = input()

# Afisam lista l1.
print(l1)
