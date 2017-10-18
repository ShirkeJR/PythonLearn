def funkcja(napis):
    return [(slowo, len(slowo)) for slowo in napis.split()]
napis = raw_input("Podaj napis: ")
print funkcja(napis)