agenda = {}
'''Pasar esto a bucle'''
name = input("Introduce nombre: ")
tlf = input("Introduce teléfono: ")

name2 = input("Introduce nombre: ")
tlf2 = input("Introduce teléfono: ")

name3 = input("Introduce nombre: ")
tlf3 = input("Introduce teléfono: ")

'''Las variables anteriores se van pasando una a una a la agenda'''
agenda.update({name : tlf, name2 : tlf2, name3 : tlf3})

'''Se recorre el diccionario entero sacando por pantalla sus valores'''
print("Mostrando la agenda completa...")
for clave, valor in agenda.items():
    print(clave, ":", valor)


ans = input("Buscar contacto: ")
'''Si el nombre coincide con el que tenemos en la agenda, saldrá también su número. Sino, else'''
if ans == name:
    print(f"Teléfono: {tlf}")
elif ans == name2:
    print(f"Teléfono: {tlf2}")
elif ans == name3:
    print(f"Teléfono: {tlf3}")
else:
    print("Contacto no encontrado...")

print("Saliendo del programa.")