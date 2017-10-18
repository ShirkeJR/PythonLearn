import math

def obl_odl(punkt, punkt_k):
    return math.sqrt(math.pow((punkt_k[0] - punkt[0]),2) + math.pow((punkt_k[1] - punkt[1]),2))

def funkcja(lista_p, punkt_k):
    return [(obl_odl(punkt, punkt_k), punkt) for punkt in lista_p]

lista_p = [(1,1), (2,2), (3,3)]
punkt_k = (5,5)

print funkcja(lista_p, punkt_k)

#sort