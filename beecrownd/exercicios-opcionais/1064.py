listPositivos = [] #lista sem conteudo ainda
for _ in range(6): #quantidade de informação que será passado
    valor = input()
    try:
        num = float(valor)
        if num > 0: # se o numero for maior que zero, ou seja, positivo
            listPositivos.append(num) # adicionamos a lista (listPositivos[])
    except: #se não, só seguimos a verificação
        continue
media = sum(listPositivos) / len(listPositivos) # (sum) os numeros da (listPositivos) e divide pela quantidade (len) da mesma lista
print('%d valores positivos' % len(listPositivos))
print('%.1f' % media)

