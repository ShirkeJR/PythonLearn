import pdb

def fibo(liczba):
    fibonacci_numbers = [0, 1]
    pdb.set_trace()
    [fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]) for i in range(2, liczba)]
    pdb.set_trace()
    return fibonacci_numbers


liczba = input('Podaj liczbe elementow ciagu: ')
pdb.set_trace()
print fibo(liczba + 1)

