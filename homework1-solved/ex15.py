"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input()
vowels = 'aeiou'
counter = 0
for character in x:
    if character in vowels:
        counter += 1

print(counter)