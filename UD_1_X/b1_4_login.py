usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("¿Cuál es tu usuario? ")
contra = input("¿Cuál es su contraseña ")

if (usuario_correcto == usuario and contrasena_correcta == contra):
    print("Acceso concedido.")

else:
    print("No has aprobado, womp womp.")