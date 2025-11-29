"""
Tenemos 4 funciones:
-sumar(a,b): Devuelve el valor de la suma de 2 variables
-restar(a,b): Devuelve el valor de la resta de 2 variables
-multiplicar(a,b): Devuelve el valor de la multiplicación de 2 variables
-dividir(a,b): Devuelve el valor de la división de 2 variables

Después de pedirle los 2 valores al usuario, hago un print para tener una frase y luego llamo a cada función para obtener el valor de su operación.
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

x = float(input("Primer número: "))
y = float(input("Segundo número: "))

print(f"La suma es {sumar(x,y)}")

print(f"La resta es {restar(x,y)}")

print(f"La multiplicación es {multiplicar(x,y)}")

print(f"La división es {dividir(x,y)}")




