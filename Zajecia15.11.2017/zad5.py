import sys
import json

class Ksiazka(dict):
    def __init__(self, tytul, isbn, autor):
        self.tytul = tytul
        self.isbn = isbn
        self.autor = autor


if len(sys.argv) == 1:
    exit(1)



obiekty = []


def dodawanie():
    a = Ksiazka(raw_input('Podaj tytul: '), raw_input('Podaj ISBN: '), raw_input('Podaj autora: '))
    obiekty.append(a)


def wyswietlanie():
    for ksiazka in obiekty:
        print ksiazka.autor, ksiazka.tytul, ksiazka.isbn


def usuwanie(ksiazki):
    isbn = raw_input('Podaj ISBN ksiazki do usuniecia')
    obiekty = [ksiazka for ksiazka in ksiazki if ksiazka.isbn != isbn]


def zapis():
    with open(sys.argv, 'w') as outfile:
        json.dumps(obiekty, outfile)


def odczyt():
    with open(plik, 'r') as infile:
        obiekty = json.loads(infile)


def loop():
    print '------------------------------'
    print '1. Dodawanie'
    print '2. Wyswietlanie'
    print '3. Usuwanie'
    print '4. Zapis'
    print '5. Odczyt'
    print '6. Wyjscie'
    wybor = input('Wybierz opcje: ')
    if wybor == 1:
        dodawanie()
    elif wybor == 2:
        wyswietlanie()
    elif wybor == 3:
        usuwanie(obiekty)
    elif wybor == 4:
        zapis()
    elif wybor == 5:
        odczyt()
    else:
        exit(0)

    loop()


loop()



