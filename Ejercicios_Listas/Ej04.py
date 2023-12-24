lista = [1,2,3,4,8,9]
lista2 = lista[::]

lista.sort()

if lista == lista2:
    print("La lista está ordenada")
else:
    print("La lista está desordenada")
