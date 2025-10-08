# Diccionario de estudiantes con notas en tres materias
estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

# Creamos un iterador sobre las claves del diccionario
it_estudiantes = iter(estudiantes)

# Recorremos manualmente el iterador
while True:
    try:
        nombre = next(it_estudiantes)
        notas = estudiantes[nombre]

        # Calculamos el promedio redondeado a 2 decimales
        promedio = round(sum(notas) / len(notas), 2)

        # Determinamos el estado
        if promedio >= 6.5:
            estado = "Aprobado"
        elif promedio >= 5:
            estado = "En recuperación"
        else:
            estado = "Reprobado"

        # Mostramos el reporte
        print(f"{nombre} - Notas: {notas}, Promedio: {promedio}, Estado: {estado}")

    except StopIteration:
        # Finalizamos cuando el iterador se agota
        break