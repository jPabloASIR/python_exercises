"""
Tenemos un menú al que vamos a llamar 2 veces, cada opción en el menú sacará una frase diferente por pantalla. He agregado un while para darle una sensación de 'menú funcional', aunque como el ejercicio no dice nada más
lo único que hace el programa es sacar frases por pantalla.
"""

def mostrar_menu():
    while True:
        print("Seleccione una opción:")
        print("1. Jugar")
        print("2. Configuración")
        print("3. Créditos")
    
        opcion = input("Ingrese el número de la opción: ")
    
        if opcion == "1":
            print("¡Iniciando el juego...")
            break
        elif opcion == "2":
            print("Accediendo a la configuración...")
            break
        elif opcion == "3":
            print("No hay créditos...")
            break
        else:
            print("Opción no válida...")


mostrar_menu()
mostrar_menu()
