"""
Tenemos 3 funciones, la primera suma a la variable contador 1, la segunda le resta ese mismo valor y la tercera lo saca por pantalla.
Llamamos a la función de acuerdo al orden que pide el ejercicio.

El resultado siempre será 1 porque:
contador +=1 (contador=1)
contador +=1 (contador=2)
contador -=1 (contador=1)
print(contador) (muestra por pantalla)
"""
contador = 0

def incrementar():
    global contador
    contador += 1

def decrementar():
    global contador
    contador -= 1

def mostrar_contador():
    global contador
    print(contador)

incrementar()
incrementar()
decrementar()

mostrar_contador()
