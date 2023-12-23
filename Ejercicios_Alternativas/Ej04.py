email = "sergioIzq@gmail.com"
contrasenia = "sergio"

emailCliente = input("Introduzca un email: ")
contraseniaCliente = input("Introduzca una contraseña: ")

if emailCliente == email and contraseniaCliente == contrasenia:
    print("El email y contraseña son correctos.")
else:
    print("Usuario y/o contraseña incorrectos, inténtelo otra vez.")