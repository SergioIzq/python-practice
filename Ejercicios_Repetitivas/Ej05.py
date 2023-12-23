import math

num = int(input("Introduzca el número a comprobar: "))
contador = 0
for i in range(1,int(math.sqrt(num))):
    if num % i == 0:
        contador += 1
if contador == 1:
    print("El número introducido es primo")
else:
    print("El número introducido no es primo")
    
# Versión alternativa

# num = int(input("Introduzca el número a comprobar: "))
# esPrimo = True
# for i in range(2,num):
#     if num % i == 0:
#         esPrimo = False
#         break
# if esPrimo: 
#     print("El número introducido es primo")
# else:
#     print("El número introducido no es primo")
