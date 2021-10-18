"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
my_str = input()

opened = ['(', '[', '{']
closed = [')', ']', '}']

stack = []
flag = 0
for character in my_str:
    if character in opened:
        stack.append(character)
    else:
        idx = closed.index(character)
        if opened[idx] in stack:
            stack.remove(opened[idx])
        else:
            flag = 1
            break

if stack or flag == 1:
    print(False)
else:
    print(True)

# (([)])