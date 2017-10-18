def flog(lista):
    lista2 = []
    for i in lista:
        lista2.append(i%2)
    return lista2

def fun(f, l):
    return f(l)

lista = [i for i in range(100)]

print fun(flog, lista)