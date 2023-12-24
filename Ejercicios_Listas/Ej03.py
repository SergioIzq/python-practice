lista = ["buenos","días","por","la","mañana"]

cadena = input("Introduce una cadena: ")

if cadena in lista:
    print("La cadena",cadena,"está en la lista.")
    print("La cadena aparece",lista.count(cadena),"vez.")
    nuevaCadena = input("Introduce una nueva cadena para sustuirla por la primera introducida: ")
    apariciones =   lista.count(cadena)
    pos = 0
    for i in range(0,apariciones):
        pos = lista.index(cadena,pos)
        lista[pos] = nuevaCadena
    print(lista)
else:
    print("La cadena no está en la lista.")