def szyfruj(txt, klucz):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - klucz:
            zaszyfrowny += chr(ord(txt[i]) + klucz - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + klucz)
    return zaszyfrowny

klucz = input("Podaj klucz: ")
wiadomosc = raw_input("Podaj tajny ciag znakow: ")
zaszyfrowana_wiadomosc = szyfruj(wiadomosc, klucz)

print wiadomosc
print zaszyfrowana_wiadomosc
