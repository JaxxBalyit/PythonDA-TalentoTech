# Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2
password = "jijaje"
password_input = input("Ingrese su contraseña: ").strip(" ")
if password_input.upper() == password.upper():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# Ejercicio 3
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num2 == 0.0:
    print("No se puede dividir por 0")
else:
    print(f"El resultado de la división es: {num1 / num2}")

# Ejercicio 4
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 5
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")

nombre = nombre.lower()

if (sexo == 'F' and nombre[0] < 'm') or (sexo == 'M' and nombre[0] > 'n'):
    grupo = 'A'
else:
    grupo = 'B'

print(f"Tu grupo es: {grupo}")

# Ejercicio 6
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = num1
if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print(f"El número mayor es: {mayor}")