"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

vocale = ['a', 'e', 'i', 'o', 'u']

x = input()
vocale = sum(x.count(i) for i in vocale)
print(vocale)

###