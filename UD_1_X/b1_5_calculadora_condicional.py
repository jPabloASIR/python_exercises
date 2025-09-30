num1 = float(input("Elige un número "))
num2 = float(input("Elige un segundo número "))

x = int(input( "1.Suma"
               "2.Resta"
               "3.Multiplicación"
               "4.División"
               ":"))


if x == 1:
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")
    
elif x == 2:
    print(f"La resta de {num1} y {num2} es: {num1 - num2}")

elif x == 3:
    print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
    
elif x == 4:
    print(f"La división de {num1} y {num2} es: {num1 / num2}")
    
else:
    print("Operación no reconocida")
