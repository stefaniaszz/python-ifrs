pares = []
for _ in range(5): #quantidade de informação que será passado
    num = int(input())
    try:
        if num % 2 == 0: # verifica se é par
            pares.append(num) # se for adiciona a lista (pares[])
    except: #se não, continua a verificação
        continue
print('%d valores pares' % len(pares)) #apresenta os pares armazenados na lista (pares[])

    