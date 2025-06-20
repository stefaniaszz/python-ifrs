X = [] #lista vazia aguardadno conteudo
for i in range(10): #determina a quantidade de testes
    valor = int(input())
    if valor <= 0: #verifica se o numero eh valido dentro do solicitado
        valor = 1 #se nao for, mostra 1
    X.append(valor) #se for, adiciona ele na lista
for i in range(10):
    print(f"X[{i}] = {X[i]}") #imprime os valores conforme solicitado no enunciado