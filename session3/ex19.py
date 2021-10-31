"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""

import json
import random

def f(x):
    x = 'test'
    return x
def writeToJSONFile(fileName, data):
    filePathNameWExt = fileName + ".json"
    jsonString = json.dumps(data)
    jsonFile = open(filePathNameWExt, "a")
    jsonFile.write(jsonString)
    jsonFile.write("\n")
    jsonFile.close()

def myValue():    
    letters = "qwertyuiopasdfghjklzxcvbnm0123456789"
    nr = [3, 4, 5, 6]
    nr = random.choice(nr)
    value = ''.join(random.choice(letters) for i in range(nr))
    return value
def myKey():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = random.choice(numbers)
    return key



fileName = f("")

data = {
    myKey() : myValue(),
    myKey() : myValue(),
    myKey() : myValue(),
    myKey() : myValue(),
    }
    

    
    
writeToJSONFile(fileName, data)









"""
import json
import random
def f(x):
    x = 'test'
    return x

def writeToJSONFile(fileName, data):
    filePathNameWExt = fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        json.dump(data, fp)
        
    
def myValue():    
    letters = "qwertyuiopasdfghjklzxcvbnm0123456789"
    nr = [3, 4, 5, 6]
    nr = random.choice(nr)
    value = ''.join(random.choice(letters) for i in range(nr))
    return value

def myKey():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = random.choice(numbers)
    return key

fileName = f("")
data = {
myKey() : myValue(),
myKey() : myValue(),
myKey() : myValue(),
myKey() : myValue()
}
writeToJSONFile(fileName, data)
"""