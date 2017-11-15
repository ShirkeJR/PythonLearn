def textwrap(napis, width):
    while napis:
        tmp = napis[:width]
        print tmp.center(width)
        napis = napis[width:]

tekst = open("1.txt", "r").read().replace("\n", " ")
width = input("Zmienna width: ")

textwrap(tekst, width)