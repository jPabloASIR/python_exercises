"""
El programa comienza con un bucle while en True para que se repita siempre y cuando no se añade por teclado el número 3.

Si el usuario escribe por teclado el número 1 el programa le pedirá: nombre_usuario, email (con las condiciones del enunciado) y password (con las condiciones del enunciado), si el usuario pasa estas restricciones su usuario se guardará en la lista usuarios que,
al principio, aparece vacía. Agregamos el nuevo usuario con .append y le pasamos una lista en el mismo orden que de entrada.

Para el inicio de sesión primero comparo que la posición 0 de la lista usuarios (que debe de contener nombre_usuario) es igual al nombre que el usuario pasa por teclado, si no lo es, sale un mensaje de que no existe y regresa al menú.
El usuario tendrá 3 oportunidades para adivinar la contraseña del usuario introducida en el punto 1, si no lo consigue en esos intentos se devuelve al menú.

Este codigo usa LISTAS, cosa que NO pertenece al tema 1, si quieres ver este código con SOLO los apuntes del tema 1 ve abajo del todo.
"""

usuarios = []

# Bucle while con condición True para que de una se muestre por pantalla el menú.
while True:
    
    opcion = input("\n¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")
    
    if opcion == "1":

        nombre_usuario = input("Introduce un nombre de usuario: ")
        
        email = input("Introduce su email: ")

        # Este while comprueba todos los requisitos que debe de tener el email.
        while len(email) < 3 or "@" not in email or not (email.endswith(".com") or email.endswith(".es") or email.endswith(".net")) or any(c in "!#$%&*?" for c in email):
            print("Email inválido. Debe tener al menos 3 caracteres, incluir '@', y tener una extensión válida como .com, .es, .net.")
            email = input("Introduce un email válido: ")

        password = input("Introduce una contraseña: ")

        # Este while comprueba todos los requisitos que debe de tener la contraseña.
        # not any(c.isupper()) comprueba si NO hay ninguna mayúscula, el enunciado nos dice que debe contener mínimo 1, pero .isupper comprueba que TODAS las letras de un str sean mayúsculas, de esta forma, hace lo que pide en el ejercicio.
        # .isdigit() simplemente busca en la string si hay algún número, ya que el enunciado pide que la contraseña debe incluirlos.
        while len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in "!@#$%&*?," for c in password):
            print("Contraseña insegura ❌. Debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo especial (!@#$%&*?, etc.).")
            password = input("Introduce una contraseña válida: ")

        # Guardo el usuario como una lista en la lista principal de usuarios (.append es un comando de Python, por ende, puedo usarlo aunque no se haya visto en el Tema 1)
        usuarios.append([nombre_usuario, email, password])
        print("Usuario registrado con éxito ✅")

    elif opcion == "2":
        
        nombre_usuario = input("Introduce tu nombre de usuario: ")

        # Busco el usuario en la lista, para ello lo inicializo en False.
        encontrado = False
        for usuario in usuarios:
            if usuario[0] == nombre_usuario:  
                encontrado = True
                
                intentos = 0
                while intentos < 3:
                    password = input("Introduce tu contraseña: ")

                    # Compruebo si la contraseña coincide con la almacenada del usuario elegido
                    if usuario[2] == password:
                        print(f"Acceso concedido ✅. Bienvenida/o, {nombre_usuario}.")
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



"""
Según lo que hemos dado, el código debería de ser así:

El programa comienza con un bucle while en True para que se repita siempre y cuando no se añade por teclado el número 3.

Si el usuario escribe por teclado el número 1 el programa le pedirá: usuario, email (con las condiciones del enunciado) y password (con las condiciones del enunciado), si el usuario pasa estas restricciones su información se guardará en las 3 variables correspondientes.
(usuario_registrado , email_registrado , password_registrada)

El inicio de sesión es mucho más sencillo, simplemente primero veo si hay algo escrito en usuario_registrado, si es así, le pido el usuario (solo puede haber 1 a la vez).

usuario_registrado = ""
email_registrado = ""
password_registrada = ""


while True:
    opcion = input("\n¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")

    if opcion == "1":
        # Registro de usuario
        usuario = input("Introduce un nombre de usuario: ")
        email = input("Introduce tu email: ")

        
        while (
            len(email) < 3
            or "@" not in email
            or not (email.endswith(".com") or email.endswith(".es") or email.endswith(".net"))
            or any(c in "!#$%&*?" for c in email)
        ):
            print("Email inválido ❌. Debe tener al menos 3 caracteres, incluir '@' y una extensión válida (.com, .es, .net).")
            email = input("Introduce un email válido: ")

        password = input("Introduce una contraseña: ")

        
        while (
            len(password) < 8
            or not any(c.isupper() for c in password)
            or not any(c.isdigit() for c in password)
            or not any(c in "!@#$%&*?," for c in password)
        ):
            print("Contraseña insegura ❌. Debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo especial (!@#$%&*?, etc.).")
            password = input("Introduce una contraseña válida: ")

        
        usuario_registrado = usuario
        email_registrado = email
        password_registrada = password

        print("Usuario registrado con éxito ✅")

    elif opcion == "2":
        # Inicio de sesión
        if usuario_registrado == "":
            print("No hay ningún usuario registrado aún. Regístrate primero.")
            continue

        usuario = input("Introduce tu nombre de usuario: ")

        if usuario != usuario_registrado:
            print("Acceso denegado ⛔. El usuario no existe.")
            continue

        
        intentos = 0
        while intentos < 3:
            password = input("Introduce tu contraseña: ")

            if password == password_registrada:
                print(f"Acceso concedido ✅. Bienvenida/o, {usuario}.")
                break
            else:
                intentos += 1
                print(f"Acceso denegado ⛔. Intento {intentos}/3")

        if intentos == 3:
            print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
"""
