"""El ejercicio recoge 3 números por teclado y procede a guardar su suma y más tarde división en la variable promedio.


El problema residía en la antigua línea 19:

promedio = nota1 + nota2 + nota3 / 3

Daba como resultado promedio = 7.0 cuando nota1 = nota2 = nota3 = 3 lo cual es obviamente incorrecto.
Esto se debe a que primero realiza la operación nota3 / 3 y luego las sumas.

Se ha solucionado agregándole paréntesis para que tenga mayor prioridad la suma, como se ve en el código actual.
"""


nota1 = float(input("Introduzca la primera nota: "))
nota2 = float(input("Introduzca la segunda nota: "))
nota3 = float(input("Introduzca la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3


print(f"El promedio de las notas {nota1}, {nota2} y {nota3} es igual a: {promedio}")
