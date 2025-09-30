compras = []

i = 0
while i < 6:
    producto = input(f"Añada un producto en la posición {i}: ")
    i += 1
    compras.append(producto[0])


print("Mostrando la lista completa...")
i = 0
while i < 6:
    print(f"{compras[i]}")
    i += 1

print("Final del ejercicio.")