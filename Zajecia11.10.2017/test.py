print('Hello world')

#d1 = raw_input('Wprowadz da...') #string
#d2 = input('Wprowadz dane 1') #typ

# tutaj prezentacja z podstawowymi komendami/funkcjami itp.


def suma(a, b):
    return a + b

a = 3
b = 5

if (a > b):
    print('Suma tego to: ' + str(suma(a,b)))
else:
    print('Nie, bo suma to: ' + str(suma(b,a)))

lista = [1, 2, 3, 4, 5]
for i in range(len(lista)):
    print lista[i]


