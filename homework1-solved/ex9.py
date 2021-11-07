"""
    Ex. 9: Modificati urmatoarea bucata de cod astfel incat
    la rulare, sa afisati doar elementele pare de la 0 la x
"""

# In x vom salvea valoarea care vine de la tastatura
x = input()

# Convertim valoarea care vine de la tastatura intr-un intreg
x = int(x)

# Vom printa toate numerele intregi de la 0 pana la x (primit de la tastatura)
# functia range(x) ne va intoarce lista de elemente intregi [0, 1, 2, .., x]
# Iteram prin toate elementele listei oferite de functia range()
for i in range(x):
    # Rezolvare:
    if i % 2 == 0:
        print(i)
