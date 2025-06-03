N = int(input())
cobaias = C = R = S = 0
for _ in range(N): #verifica cada caso de teste
    testes = input().split()
    qtd = int(testes[0]) # quantidade de cobaias
    tipo = testes[1] #verifica se é R, S ou C
    cobaias += qtd #atualiza o contador de cobaias
    
    if tipo == 'C': #atualiza o contador de cada cobaia
        C += qtd
    elif tipo == 'R':
        R += qtd
    elif tipo == 'S':
        S += qtd

percentC = (C / cobaias) * 100 if cobaias > 0 else 0 # calcula a porcentagem de cada um
percentR = (R / cobaias) * 100 if cobaias > 0 else 0
percentS = (S / cobaias) * 100 if cobaias > 0 else 0

print('Total: %d cobaias' % cobaias)
print('Total de coelhos: %d' % C)
print('Total de ratos: %d' % R)
print('Total de sapos: %d' % S)
print('Percentual de coelhos: %.2f %%' % (percentC))
print('Percentual de ratos: %.2f %%' % (percentR))
print('Percentual de sapos: %.2f %%' % (percentS))
