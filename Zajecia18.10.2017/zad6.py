import os

def genDir(roz, sciezka):
    for plik in os.listdir(sciezka):
        if(roz in plik):
            yield plik

sciezka = raw_input('Podaj sciezke: ')
rozszerzenie = raw_input('Podaj rozszerzenie: ')

for i in genDir(rozszerzenie, sciezka):
    print i


