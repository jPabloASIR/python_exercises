"""
Tenemos una lista vacía que iremos llenando mediante compras.append, que añadirá 5 valores (range(5)) en la última posición disponible de compras.
Una vez esté lista, se mostrará por pantalla, luego el usuario podrá eliminar 1 producto si es que está en la lista.
Finalmente usamos .sort() para ordenar la lista y así poder mostrarla en orden ascendente.
"""

compras = []
    
for i in range(5):
    producto = input(f"Añada un producto {i}: ")
    compras.append(producto)
    
print("\nLista completa:")
for p in compras:
    print(p)
    
eliminar = input("\nProducto a eliminar: ")
if eliminar in compras:
    compras.remove(eliminar)
    print(f"{eliminar} eliminado.")
else:
    print(f"{eliminar} no encontrado.")
    
compras.sort()
print("\nLista ordenada:")
for p in compras:
    print(p)  


