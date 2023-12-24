cadena = input("Introduce una cadena: ")
diccionario = {}

listaPalabras = cadena.split(" ")
for palabra in listaPalabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
for campo,valor in diccionario.items():
    print(campo,"=>",valor)
