while True:  
    try:
        palavra = input()
        if len(palavra) > 20 or not palavra.islower(): #verifica se a palavra tem menos de 20 caracteres e contém, apenas letras minúsculas
            continue #se não, fica em branco aguardando a próxima palavra pára verificação
        if len(palavra) >= 10: # se passou da etapa anterior, será verificado se a palavra tem mais de 10 letras
            print('palavrao') # se tiver, terá essa saída
        else:
            print('palavrinha') #se não tiver, terá essa
    except:
        break

                      