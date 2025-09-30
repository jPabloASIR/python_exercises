estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]


def media(numeros):
    return float(sum(numeros)) / max(len(numeros), 1)


avg = [media(i) for i in zip(notas_matematicas,notas_fisica, notas_quimica)]


state = []
for promedio in avg:
    if promedio >= 6.5:
        state.append("Aprobado")
    elif promedio >= 5:
        state.append("En recuperación")
    else:
        state.append("Reprobado")


for indice, (a, b, c, d, e, f) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica, avg, state), start=1):
    print(indice, a, "- Matemáticas: ", b, " Física: ", c, " Química: ", d, " Promedio: ", e, " Estado: ", f)

