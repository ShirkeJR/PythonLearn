import sys

def fun(plik):
    slownik = {}
    for line in file:
        elementy = line.splitlines()
        elementy = elementy[0].split(': ')
        slownik[elementy[0]] = elementy[1]
    return slownik

filename = sys.argv[0]

file = open(filename, "r")
slownik = fun(file)
file.close()

print slownik.items()
