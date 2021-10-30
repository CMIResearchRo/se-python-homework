"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""

def deco(f):
    def inner():
        doc = open("output11.data", "w")
        doc.write(f())
        doc.close()
        doc = open("output11.data", "r")
        print(doc.read())
    return inner
    
@deco
def f():
    return "CMI"

f()
###