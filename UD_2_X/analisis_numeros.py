import random
lista = []
cuadrado = []
par = []
idk = []

for n in range(0, 20):
    lista = random.randint(0,20)
    print(lista)
    cuadrado.append(lista)
    par.append(lista)
    idk.append(lista % 2 == 0)

print("\nMostrando los cuadrados de los números de la lista....")

cuadrado = [n ** 2 for n in cuadrado]
print(cuadrado)

print("\nMostrando solo los pares de la lista....")
par = [n % 2 == 0 for n in par]
print(par)

print("\nMostrando solo los mayores de 10 de la lista....")
print(idk)