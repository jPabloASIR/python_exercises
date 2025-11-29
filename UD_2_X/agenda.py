"""
Tenemos un diccionario vacío al cual le iremos agregando contactos a placer del usuario con su respectivo número de teléfono.
Una vez terminada, se mostrará por pantalla usando las variables que pide el ejercicio: print(clave, ":", valor).
Por último, se le pedirá al usuario un nombre y, si está en el diccionario, saldrá por pantalla su número de teléfono.
"""
agenda = {}

num_contactos = int(input("¿Cuántos contactos quieres agregar? "))

for i in range(num_contactos):
    nombre = input(f"Introduce el nombre del contacto {i}: ")
    tlf = input(f"Introduce el teléfono de {nombre}: ")
    agenda[nombre] = tlf

print("\nMostrando la agenda completa...")
for clave, valor in agenda.items():
    print(clave, ":", valor)

ans = input("Introduce un nombre: ")

if ans in agenda:
    print(f"Teléfono de {ans}: {agenda[ans]}")
else:
    print("Contacto no encontrado...")

print("Saliendo del programa.")

