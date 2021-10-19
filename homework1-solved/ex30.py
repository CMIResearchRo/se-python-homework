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
my_str = input("String for solution 1\n")

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

# Solution 2
my_str = input("String for solution 2\n")
opened = tuple('([{')
closed = tuple(')]}')
mapper = dict(zip(opened, closed))

queue = []
flag = 0
for character in my_str:
    if character in opened:
        queue.append(mapper[character])
    elif character in closed:
        if not queue or character not in queue:
            flag = 1
            break
        else:
            queue.remove(character)

if not queue and flag == 0:
    print(True)
else:
    print(False)
