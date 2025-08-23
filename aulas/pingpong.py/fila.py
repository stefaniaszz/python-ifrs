
def criar_fila():
    list = [] #chama e retorna lista vazia pra inserir a fila
    return list

def enfileirar(fila, entrada):
    fila.append(entrada) #adiciona a entrada de argumentos na lista
    
def desenfileirar(fila):
    return fila.pop(0) #remove o primeiro da fila 

def mostrar_fila(fila):
    print(fila)