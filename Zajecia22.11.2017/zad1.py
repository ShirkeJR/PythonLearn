import math

def pobierzLiczbe(liczba):
    try:
        pierw = math.sqrt(liczba)
    except (TypeError, ValueError) as ex:
        print "Zle dane: " + str(ex)
    else:
         return pierw
    finally:
        print "Koniec"


print pobierzLiczbe(2)
print pobierzLiczbe(-2)
print pobierzLiczbe("Tak")

try:
    liczba = input("Podaj liczbe do pierw: ")
except (NameError, SyntaxError):
    print "Zly format danych"
else:
    print pobierzLiczbe(liczba)