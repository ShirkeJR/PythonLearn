def fun(napis):
    slownik = {}
    for line in napis.split('\n'):
        elementy = line.split(': ')
        slownik[elementy[0]] = elementy[1]
    return slownik

napis1 = """k1: w1
k2: w2
k3: w3"""

slownik = fun(napis1)

print slownik.items()