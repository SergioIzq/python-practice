cadena = input("Introduce una cadena: ")
caracter = input("Introduce un carácter: ")

for i in range(10):
    cadena = cadena.replace(str(i),caracter)
print(cadena)