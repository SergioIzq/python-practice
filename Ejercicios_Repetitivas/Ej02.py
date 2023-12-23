num = int(input("Introduce un número para realizar el factorial"))
fact = 1
for i in range(2,num+1):
    fact *= i
print("El factorial de",num,"es",fact)