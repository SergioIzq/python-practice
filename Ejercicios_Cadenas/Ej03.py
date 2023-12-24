cadena = input("Introduce una cadena: ")

lista = cadena.split(" ")
for palabra in lista:
    print(palabra[0], end = "")
print()

for palabra in lista:
    print(palabra.capitalize(), end = " ")
print()

for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print(palabra, end="")