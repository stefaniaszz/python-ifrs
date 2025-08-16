
def criarFila():
    list = [] #chama e retorna lista vazia pra inserir a fila
    return list

def enfileirar(fila, entrada):
    fila.append(entrada) #adiciona a entrada de argumentos na lista
    
def desenfileirar(fila):
    return fila.pop(0) #remove o primeiro da fila 

def mostrarFila(fila):
    print(fila)


f = criarFila()
enfileirar(f, "XYZ")
enfileirar(f, "ABC")
enfileirar(f, "KKK")
mostrarFila(f)
v1 = desenfileirar(f)
enfileirar(f, "IF")
mostrarFila(f)