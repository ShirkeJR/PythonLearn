from math import *

def krotkiZLiczby(liczba):
    i = 2
    e = floor(sqrt(liczba))
    r = dict()
    s = []
    while i <= e:
        if liczba % i == 0:
            if i in r:
                r[i] += 1
            else:
                r[i] = 1
            liczba /= i
            e = floor(sqrt(liczba))
        else:
            i += 1
    if liczba > 1:
        if liczba in r:
            r[liczba] += 1
        else:
            r[liczba] = 1

    return [(item1, item2) for item1, item2 in r.iteritems()]


liczba = input("Podaj liczbe: ")
print krotkiZLiczby(liczba)
