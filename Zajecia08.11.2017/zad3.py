import sys

fileName = "plik2.txt" #sys.argv[1]

file = open(fileName, "r")
tekst = file.read()
slownik = {}
for slowo in tekst.split():
    slownik[slowo] = tekst.count(slowo)
file.close()

print slownik.items()