import sys

def szyfruj(txt, klucz):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - klucz:
            zaszyfrowny += chr(ord(txt[i]) + klucz - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + klucz)
    return zaszyfrowny

fileName1 = "plik4.txt" #sys.argv[1]
fileName2 = "plik5.txt" #sys.argv[2]

file = open(fileName1, "r")
tekst = file.read()
file.close()

zaszyfrowany_tekst = szyfruj(tekst, 3)

file = open(fileName2, "w")
file.writelines(zaszyfrowany_tekst)
file.close()