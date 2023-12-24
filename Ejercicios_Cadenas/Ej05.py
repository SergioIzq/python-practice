cadena1 = input("Cadena: ")
if cadena1.lower() == cadena1[::-1].lower():
    print("Palíndromo")
else:
    print("No es palíndromo")