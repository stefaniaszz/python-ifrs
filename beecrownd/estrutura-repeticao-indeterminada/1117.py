notas = []
while len(notas) < 2: # "obriga" que coloque mais de 1 nota para dar continuidade ao calculo da nota
        nota = float(input())
        if 0 <= nota <= 10:  # verifica se a nota é válida
            notas.append(nota) # se for válida, vai pra dentro da lista (notas=[])
        else: 
            print('nota invalida') # se não, apresenta divergência
media = sum(notas) / len(notas) # (sum) soma todas as notas armazenadas na lista de uma vez só // (len) retorna para a soma a quantidade de notas válidas adicionadas na lista
print('media = %.2f' % media)

