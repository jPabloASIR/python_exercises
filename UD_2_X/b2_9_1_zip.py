"""
Este programa combina tres listas paralelas: nombre de estudiantes, notas de matemáticas y notas de física. Para recorrerlas al mismo tiempo vamos a utilizar la función zip(), que empareja los elementos de las listas
por posición.

- zip(...) crea tuplas como ("Ana", 8, 9), ("Luis", 7, 6), ...
- en cada iteración, esas tuplas se "desempaquetan" en las variables

Así, en cada vuelta del bucle for se obtiene un estudiante junto con sus dos notas correspondientes.
"""

nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]

for nombre, mat, fis in zip(nombres, notas_matematicas, notas_fisica):
    print(f"{nombre} - Matemáticas: {mat}, Física: {fis}")
