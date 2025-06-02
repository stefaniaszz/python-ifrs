idades = [] #lista aguardando ser preenchida
while True: 
    try:
        num = float(input())
        if num < 0: #verifica se a idade é maior que 0, se for negativo, para o programa de primeira
            break
        idades.append(num) #se não for negativo, adiciona a lista (idades[]) até aparecer um numero negativo
    except:
        break
if len(idades) > 0: #verifica os números maior que 0 adicionados dentro da lista
    media = sum(idades)/len(idades) #soma todos em busca da média de idade
    print('%.2f' % (media))