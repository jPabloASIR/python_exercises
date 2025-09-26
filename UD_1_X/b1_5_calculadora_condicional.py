num1 = input("Elige un número ")
num2 = input("Elige un segundo número ")

print( "1.Suma"
        "2.Resta"
        "3.Multiplicación"
        "4.División")

x = input("Su respuesta: ")

if int(x) == 1:
    x = float(num1) + float(num2)
    print(f"La suma de {num1} y {num2} es: {x}")
elif int(x) == 2:
    x = float(num1) - float(num2)
    print(f"La suma de {num1} y {num2} es: {x}")
elif int(x) == 3:
    x = float(num1) * float(num2)
    print(f"La suma de {num1} y {num2} es: {x}")
elif int(x) == 4:
    x = float(num1) / float(num2)
    print(f"La suma de {num1} y {num2} es: {x}")
else:
    print("Operación no reconocida")