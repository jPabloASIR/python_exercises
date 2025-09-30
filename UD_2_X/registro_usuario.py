def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}.")


'''Llamada a la función (posicional)'''
registrar_usuario("Laura", 25, "Madrid")

'''Llamada a la función (nombrado)'''
registrar_usuario(edad=25, ciudad="Madrid", nombre="Laura")

'''Llamada a la función (ciudad omitida)'''
registrar_usuario("Laura", 25)


