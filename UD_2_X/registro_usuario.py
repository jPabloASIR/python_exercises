"""
Tenemos una función con 3 parámetros (con 'ciudad' teniendo un valor predefinido), se sacará por pantalla:
-El valor de los 3 parámetros en orden (primera llamada)
-El valor de los 3 parámetros en orden, pero usando el valor predefinido de ciudad (segunda llamada)
-El valor de los 3 parámetros en orden, pero en la llamada aparecen con otro orden (tercera llamada)

Siempre que los parámetros sean los mismos que los de la función se podrán sacar por pantalla, con ciudad nisiquiera necesitando que le pasemos un valor.
El orden en el cual ponemos los parámetros en la tercera llamada no importa ya que el print tiene un orden fijo (precisamente porque estamos usando los propios parámetros y no las posiciones de dichos parámetros).

No es lo mismo registrar_usuario(edad=25, ciudad="Madrid", nombre="Laura") que registrar_usuario(25, "Madrid", "Laura")
"""
def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}.")


# Todos los argumentos posicionales
registrar_usuario("Laura", 25, "Madrid")

# Omitimos Madrid en la llamada
registrar_usuario("Laura", 25)

# Todos los argumentos en distinto orden
registrar_usuario(edad=25, ciudad="Madrid", nombre="Laura")





