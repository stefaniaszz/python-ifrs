'''
Criar uma lista com diversas notas diferentes pelo usuário.
Mostrar a média das notas acima de 9.0.
'''

notas = list(map(float, input().split()))
cont = 0  #contagem de elementos
tam = len(notas)
for i in range(tam):
    if notas[i] >= 9:
        cont += 1
print('%d notas acima de 9' % (cont))
