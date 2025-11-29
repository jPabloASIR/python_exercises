"""
Este programa recorre una lista de nombres usando enumerate(), que devuelve el índice y el valor de cada elemento en cada vuelta del bucle.  
Luego convierte el resultado de enumerate() en una lista de tuplas para mostrar cada índice junto con su nombre de forma agrupada.
"""

nombres = ["Ana", "Luis", "Marta", "Carlos"]

for indice, nombre in enumerate(nombres):
    print(indice, nombre)

lista_tuplas = list(enumerate(nombres))
print(lista_tuplas)
