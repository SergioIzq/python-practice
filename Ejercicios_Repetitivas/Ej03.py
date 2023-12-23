import os

numSecreto = int(input("Introduzca un número secreto: "))
os.system("cls")
i = 1
num = int(input("Introduzca un número para adivinar: "))
while num != numSecreto:
    if(num > numSecreto):
        print("El número introducido es mayor que el número secreto.")
    else:
        print("El número introducido es menor que el número secreto.")
    i += 1
    num = int(input("Introduzca un número para adivinar: "))

print("Felicidades has adivinado el número secreto en",i,"intentos")