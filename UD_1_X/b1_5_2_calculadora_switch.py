num1 = float(input("Elige un número "))
num2 = float(input("Elige un segundo número "))

x = int(input( "1.Suma"
               "\n2.Resta"
               "\n3.Multiplicación"
               "\n4.División"
               ":"))


match x:
    case 1:
        print(f"La suma de {num1} y {num2} es: {num1 + num2}")
    case 2:
        print(f"La resta de {num1} y {num2} es: {num1 - num2}")
    case 3:
        print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
    case 4:
        print(f"La división de {num1} y {num2} es: {num1 / num2}")
    case _:
        print("Operación no reconocida")