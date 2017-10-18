def fiboGen():
    fib0, fib1 = 0, 1
    yield fib0
    yield fib1
    while True:
        fib0, fib1 = fib1, fib1+ fib0
        yield fib1

liczba = input("Podaj liczbe fibonachi: ")
j = 0
listafib = []
for i in fiboGen():
    listafib.append(i)
    if(liczba == j):
        break
    j = j + 1

print listafib
