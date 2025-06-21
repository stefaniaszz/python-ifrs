n = int(input()) #quantidade capturado
mochila = [] 
for i in range(n):
    pomekon = input() #nomes
    if pomekon not in mochila: #verifica se o pomekon capturado ainda não tem na mochila
        mochila.append(pomekon) #se nao tiver, adicionar
totalPomekons = 151 #quantidade total
faltam = totalPomekons - len(mochila) #quantos faltam dentro da mochila
print('Falta(m) %d pomekon(s).' % (faltam))

             