n = input("Ilosc liczb: ")
lista = []
for i in range(n):
    x = input("Liczba: ")
    lista.append(x)

kierunek = raw_input("asc/desc: ")
zakres_d = input("dol: ")
zakres_g = input("gora: ")
lista.sort()
if(kierunek != 'asc'):
    lista.reverse()
#zakres miejsc liczb
for i in range(zakres_d, zakres_g):
    print lista[i],
#zakres wartosci liczb
for i in range(len(lista)):
    if(zakres_d <= lista[i] <= zakres_g):
        print lista[i]