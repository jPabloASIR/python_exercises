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