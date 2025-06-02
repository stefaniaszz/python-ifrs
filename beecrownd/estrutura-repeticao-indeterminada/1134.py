alcool = gasolina = diesel = 0 # contador para adicionar uma quantidade a cada looping do sistema
while True:
    try:
        codigo = int(input()) # o código que o usuario digitar, o sistema adiciona calcula na quantidade
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
        elif codigo == 4: # se ele colocar (4.FIM), o sistema finaliza o procedimento
            break
    except: #mas se ele colocar algo fora do que solicitei, ficará em branco aguardando um novo número válido
        break 
print('MUITO OBRIGADO') # agradecimento para cada ususario que utilizar o sistema
print('Alcool: %d' % (alcool)) #nos demais comandos, apenas o resultado de cada contagem
print('Gasolina: %d' % (gasolina))
print('Diesel: %d' % (diesel))

    
