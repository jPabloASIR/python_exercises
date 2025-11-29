"""
Recorremos un diccionario de estudiantes con sus notas en tres asignaturas, calculando el promedio de cada uno y decidiendo su nota:

- "Aprobado" si el promedio es mayor o igual a 6.5
- "En recuperación" si el promedio es mayor o igual a 5 pero menor que 6.5
- "Reprobado" si el promedio es menor que 5

Se utiliza un iterador manual sobre las claves del diccionario usando las funciones
de Python iter() y next():

- iter(): crea un iterador a partir de un objeto iterable (diccionario en este caso). Permite recorrer los elementos de forma secuencial.
- next(): devuelve el siguiente elemento del iterador. Si el iterador se ha acabado, lanza una excepción StopIteration, que permite terminar el bucle.
"""
estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

it_estudiantes = iter(estudiantes)

while True:
    try:
        nombre = next(it_estudiantes)
    except StopIteration:
        break
        
    notas = estudiantes[nombre]

    promedio = round(sum(notas) / len(notas), 2)

    if promedio >= 6.5:
        estado = "Aprobado"
    elif promedio >= 5:
        estado = "En recuperación"
    else:
        estado = "Reprobado"

    print(f"{nombre} - Notas: {notas}, Promedio: {promedio}, Estado: {estado}")

