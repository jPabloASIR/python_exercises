# Función para validar el email
def validar_email(email):
    # Validación de la estructura del email
    if len(email) < 3 or "@" not in email:
        print("Email inválido. Debe tener al menos 3 caracteres, incluir '@', y tener una extensión válida como .com, .es, .net.")
        return
    if not (email.endswith(".com") or email.endswith(".es") or email.endswith(".net")):
        print("Email inválido. Debe tener una extensión válida como .com, .es, .net.")
        return
    if any(c in "!#$%&*?" for c in email):  # Verificamos si contiene símbolos no permitidos
        print("Email inválido. No debe contener símbolos especiales como (!@#$%&*?, etc.).")
        return
    return email

# Función para validar la contraseña
def validar_contraseña(password):
    if len(password) < 8:
        print("Contraseña insegura ❌. Debe tener al menos 8 caracteres.")
        return
    if not any(c.isupper() for c in password):
        print("Contraseña insegura ❌. Debe tener al menos una mayúscula.")
        return
    if not any(c.isdigit() for c in password):
        print("Contraseña insegura ❌. Debe tener al menos un número.")
        return
    if not any(c in "!@#$%&*?," for c in password):
        print("Contraseña insegura ❌. Debe tener al menos un símbolo especial (!@#$%&*?, etc.).")
        return
    return password

# Función para registrar un nuevo usuario
def registrar_usuario():
    email = input("Introduce un nombre de usuario (email): ")
    
    # Validación del email
    while not validar_email(email):
        email = input("Introduce un nombre de usuario (email): ")
    
    password = input("Introduce una contraseña: ")
    
    # Validación de la contraseña
    while not validar_contraseña(password):
        password = input("Introduce una contraseña: ")
    
    # Guardamos el usuario en el diccionario de usuarios
    usuarios[email] = password
    print("Usuario registrado con éxito ✅")

# Función para iniciar sesión
def iniciar_sesion():
    email = input("Introduce tu usuario (email): ")
    
    # Verificación de si el usuario existe
    if email not in usuarios:
        print("Acceso denegado ⛔. El usuario no existe.")
        return
    
    # Intentos de login
    intentos = 0
    while intentos < 3:
        password = input("Introduce tu contraseña: ")
        
        if usuarios[email] == password:
            print(f"Acceso concedido ✅. Bienvenida, {email}.")
            return
        else:
            intentos += 1
            print(f"Acceso denegado ⛔. Intento {intentos}/3")
    
    print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")

# Función principal que ejecuta el menú
def menu():
    while True:
        opcion = input("\n¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Diccionario para almacenar los usuarios registrados
usuarios = {}

# Llamada al menú principal
menu()
