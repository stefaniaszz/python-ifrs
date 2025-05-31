'''
Criar uma lista com diversas notas diferentes pelo usuário.
Mostrar a média das notas.
'''

'''
notas = list(map(float, input().split()))
media = sum(notas) / len(notas) = simplificação de estrutura, sem (tam e soma=0)
print(media)
'''

notas = list(map(float, input().split()))
sum = 0 #somador
tam = len(notas) #contagem de elementos
for i in range(tam):
    sum = sum+notas[i] #(i) conteúdo dentro de ([]) que é a lista
media = sum/tam 
print('%.1f' % media)

