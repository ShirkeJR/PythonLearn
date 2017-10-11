def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

def fib_iter2(n):
    a, b = 0, 1
    for i in range(1, n - 1):
        a, b = b, a + b
    return b

max_liczba = input("Podaj do ktorego wyrazu ciagu fib: ")

for i in range(max_liczba+1):
    print(str(fib_rek(i)))
    #print(str(fib_iter2(i)))
