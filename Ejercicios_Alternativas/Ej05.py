anio = int(input("Introduzca un año para comprobar si es bisiesto: "))

if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
    print("Año bisiesto.")
else:
    print("Año no bisiesto.")