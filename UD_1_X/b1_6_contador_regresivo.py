num = input("Escriba un número: ")

int(num)

while int(num) >= 0:
    print(f"{num}")
    num = int(num)- 1

print("¡Despegue!")