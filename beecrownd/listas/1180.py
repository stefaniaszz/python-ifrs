n = int(input()) #numero de testes
x = list(map(int, input().split())) #testes
menor = min(x) #encontrando o menor valor da lista
posicao = x.index(menor) #posicao do menor valor
print('Menor valor:', menor)
print('Posicao:', posicao)