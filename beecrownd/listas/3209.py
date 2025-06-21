n = int(input())  #numero de casos de teste
for _ in range(n):
    dados = [] #lista vazia para armazenar oq for enviado
    while len(dados) < 1: #le a primeira linha e verifica
        dados += list(map(int, input().split())) #converte os números da linha em inteiros e adiciona na list
    k = dados[0] #o primeiro número indica quantos filtros de linha serão informados
    while len(dados) < k + 1: #continua lendo entradas até ter todos os K valores esperados (quantidade de tomadas de cada filtro)
        dados += list(map(int, input().split()))  #adiciona mais inteiros à lista, caso estejam em outra linha
    tomadas = dados[1:] #pega apenas os valores das tomadas (ignorando o primeiro, que é K)
    total = sum(tomadas) - (k - 1) #calcula o total de aparelhos que podem ser ligados: soma das tomadas menos (k - 1)
    print(total)


