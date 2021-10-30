"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""
def deco(f):
    def inner(*args):
        output = f(*args)
        doc = open("output12.data", "w")
        doc.write(str(output))
        doc.close()
        doc = open("output12.data", "r")
        print(doc.read())
    return inner

    
@deco
def f(x):
    print(x)

f(4)

###