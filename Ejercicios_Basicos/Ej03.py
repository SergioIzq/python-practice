import math

radio = float(input("Introduce el radio del círculo a calcular: "))
perimetro = 2 * math.pi * radio
area = radio**2 * math.pi

print("El perímetro del círculo con radio",radio,"es",perimetro,"y el área es",area)
