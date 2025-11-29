"""
Tenemos un menú al que vamos a llamar 2 veces, cada opción en el menú sacará una frase diferente por pantalla. Como el ejercicio no dice nada más, no le he puesto nada para que el menú se siga mostrando hasta que el
usuario pulse x botón.
"""

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Créditos")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        print("¡Iniciando el juego...")
    elif opcion == "2":
        print("Accediendo a la configuración...")
    elif opcion == "3":
        print("No hay créditos...")
    else:
        print("Opción no válida.")


mostrar_menu()
mostrar_menu()
