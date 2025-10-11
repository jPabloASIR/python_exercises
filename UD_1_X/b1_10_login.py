usuarios = []

# Bucle while con condición True para que de una se muestre por pantalla el menú
while True:
    
    opcion = input("\n¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")
    
    if opcion == "1":

        nombre_usuario = input("Introduce un nombre de usuario: ")
        
        email = input("Introduce su email: ")

        # Este while comprueba todos los requisitos que debe de tener el email
        while len(email) < 3 or "@" not in email or not (email.endswith(".com") or email.endswith(".es") or email.endswith(".net")) or any(c in "!#$%&*?" for c in email):
            print("Email inválido. Debe tener al menos 3 caracteres, incluir '@', y tener una extensión válida como .com, .es, .net.")
            email = input("Introduce un email válido: ")

        password = input("Introduce una contraseña: ")

        # Este while comprueba todos los requisitos que debe de tener la contraseña
        while len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in "!@#$%&*?," for c in password):
            print("Contraseña insegura ❌. Debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo especial (!@#$%&*?, etc.).")
            password = input("Introduce una contraseña válida: ")

        # Guardo el usuario como una lista en la lista principal de usuarios (.append es un comando de Python, por ende, puedo usarlo aunque no se haya visto en el Tema 1)
        usuarios.append([nombre_usuario, email, password])
        print("Usuario registrado con éxito ✅")

    elif opcion == "2":
        
        nombre_usuario = input("Introduce tu nombre de usuario: ")

        # Busco el usuario en la lista, para ello lo inicializo en False
        encontrado = False
        for usuario in usuarios:
            if usuario[0] == nombre_usuario:  
                encontrado = True
                
                intentos = 0
                while intentos < 3:
                    password = input("Introduce tu contraseña: ")

                    # Compruebo si la contraseña coincide con la almacenada del usuario elegido
                    if usuario[2] == password:
                        print(f"Acceso concedido ✅. Bienvenida, {nombre_usuario}.")
                        break
                    else:
                        intentos += 1
                        print(f"Acceso denegado ⛔. Intento {intentos}/3")

                if intentos == 3:
                    print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")
                break
        
        if not encontrado:
            print("Acceso denegado ⛔. El usuario no existe.")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
