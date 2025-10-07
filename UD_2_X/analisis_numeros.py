import random
lista = []
cuadrado = []
par = []
idk = []
dobles = {}

for n in range(0, 20):
    num = random.randint(0, 20) ''' num contiene el valor actual del número aleatorio'''
    lista.append(num) ''' Ese valor se guarda en la posición correspondiente de la lista llamada lista '''
    print(lista)
    cuadrado.append(lista)
    par.append(lista)
    idk.append(lista)
    dobles[num] = num * 2 ''' Doble del valor actual de num '''

print("\nMostrando los cuadrados de los números de la lista....")

cuadrado = [n ** 2 for n in cuadrado]
print(cuadrado)

print("\nMostrando solo los pares de la lista....")
par = [n % 2 == 0 for n in par]
print(par)

print("\nMostrando solo los mayores de 10 de la lista....")
idk = [n > 10 for n in idk]
print(idk)

print("\nDiccionario con los números y sus dobles:")
print(dobles)
