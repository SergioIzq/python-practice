num = int(input("Introduce un número: "))
lista = []
while num > 0:
    lista.append(num)
    num = int(input("Introduce un número: "))

print("El mayor número introducido ha sido",max(lista))
for i in lista:
    if(i % 2 == 0):
        print(i)
