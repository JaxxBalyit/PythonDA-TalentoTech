# Ejercicio 1
lista = ["mango", "mandarina", "naranja", "pera", "Palta", "Arazá"]

for fruta in lista:
    if fruta.lower() == "naranja":
        continue
    print(fruta)


# Ejercicio 2
while True:
    numero = int(input("Ingrese un número impar: "))
    if numero % 2 != 0:
        break 
    else:
        print("El número ingresado no es impar. Por favor, inténtelo de nuevo.")

print("Gracias, has ingresado un número impar:", numero)