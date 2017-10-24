def fibo(liczba):
    fibonacci_numbers = [0, 1]
    [fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2]) for i in range(2, liczba)]
    return fibonacci_numbers
    
liczba = input('Podaj liczbe elementow ciagu: ')
print fibo(liczba+1)

