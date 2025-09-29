lista = ["Ana", "Pedro", "Alba", "Lucía", "albA", "alejAndrA"]
''' Este for recorre toda la variable lista desde la posición 0 (Ana) hasta la posición 5 (alejAndrA) y observa si la primera letra  del contenido de cada posición empieza por A, si no es así, aparecerá por pantalla guardada en la variable i.'''
for i in lista:
    if i[0] in 'A':

        continue
    print(f"Contraseña válida: {i}")



