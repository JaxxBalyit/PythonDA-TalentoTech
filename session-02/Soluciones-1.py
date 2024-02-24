# Ejercicio 1
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 <= num2)


# Ejercicio 2
cadena = input("Ingrese una cadena de texto: ")
if(len(cadena) > 3 and len(cadena) < 10):
    print("La cadena tiene entre 3 y 10 caracteres")
else:
    print("La cadena no cumple con los requisitos")


# Ejercicio 3
numero_magico = 12345679
numero_usuario = int(input("Introduce un número entre 1 y 9: "))
if numero_usuario < 1 or numero_usuario > 9:
    print("El número no cumple con los requisitos")
else:
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print("El valor final del número mágico es: ", numero_magico)


# Ejercicio 4
a = 5
b = 2
c = 3

suma_resultado = a + b
resta_resultado = a - c
multiplicacion_resultado = b * c

print("La suma de a y b es:", suma_resultado)
print("La resta de a y c es:", resta_resultado)
print("El resultado de multiplicar b por c es:", multiplicacion_resultado)


# Ejercicio 5

# Correcciones de nombres de variables
my_var = "John"
myvar = 23
my_var = "str"
my2var = 3.25
_my_var = (1, 3, 2)
myVar = 48
MYVAR = "cadena"
# my-var = [1,5]  # Este nombre de variable sigue siendo inválido y no puede ser corregido en Python
myvar2 = []


# Ejercicio 6
my_first_name = "John"
