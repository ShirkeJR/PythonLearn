def textwrap(napis):
    while napis:
        tmp = napis[:width]
        print tmp
        napis = napis[width:]

tekst = open("1.txt", "r").read().replace("\n", " ")
width = input("Zmienna width: ")

textwrap(tekst)