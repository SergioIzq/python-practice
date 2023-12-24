cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

if cadena1.find(cadena2) > -1:
    print("Cadena2 es subcadena de cadena1.")
else:
    print("Cadena1 es subcadena de cadena2.")
print (cadena1 if cadena1 < cadena2 else cadena2)