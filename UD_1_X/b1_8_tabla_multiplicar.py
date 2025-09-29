'''Script que recoge 1 número pasado por teclado guardada en la variable num con bucle for '''

num = int(input("Escriba su número: "))
'''Como el bucle for debe de ir desde el 0 y terminar en el 10, su rango es de 0 a 11'''
for i in range(0, 11):
    print(num, 'x', i, '=', num*i)

