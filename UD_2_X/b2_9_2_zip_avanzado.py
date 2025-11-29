"""
Este programa toma listas de estudiantes y sus notas en Matemáticas, Física
y Química, calcula el promedio de cada uno, determina su estado (Aprobado,
En recuperación o Reprobado) y guarda toda la información en un diccionario.

Luego imprime un reporte mostrando las notas, el promedio y el estado de cada estudiante.
"""

estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]

nota = {}

for nombre, mat, fis, qui in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    promedio = round((mat + fis + qui) / 3, 2)

    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    nota[nombre] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": qui,
        "Promedio": promedio,
        "Estado": estado
    }


for nombre in estudiantes:
    datos = nota[nombre]
    print(f"{nombre} - Matemáticas: {datos['Matemáticas']}, "
          f"Física: {datos['Física']}, "
          f"Química: {datos['Química']}, "
          f"Promedio: {datos['Promedio']}, "
          f"Estado: {datos['Estado']}")
