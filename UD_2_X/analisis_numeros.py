"""
Este programa genera una lista de 20 números enteros usando range().
Luego, se realizan las siguientes operaciones:
1. Se obtiene una lista con los cuadrados de todos los números.
2. Se obtiene una lista con solo los números pares.
3. Se obtiene una lista con los números mayores que 10.
4. Se crea un diccionario que relaciona cada número con su doble.
Finalmente, se muestran los resultados de todas estas operaciones.
"""

lista = list(range(1, 21))  


cuadrados = [n ** 2 for n in lista]


pares = [n for n in lista if n % 2 == 0]


mayores_que_10 = [n for n in lista if n > 10]


dobles = {n: n * 2 for n in lista}


print("Lista original de números:")
print(lista)

print("\nCuadrados de los números:")
print(cuadrados)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros mayores que 10:")
print(mayores_que_10)

print("\nDiccionario de números y sus dobles:")
print(dobles)

