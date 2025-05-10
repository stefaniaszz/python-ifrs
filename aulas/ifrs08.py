opcao = 's' #definir a variável da condição do while
while opcao == 's': #enquanto o usuário colocar (s) o programa vai seguir rodando, independente de ser True or False
    valor = int(input())
    if valor % 2 == 0:
        print('É par')
    else:
        print('Não é par')
    opcao = input('Quer continuar? (s/n): ') #se eu tirar essa linha, segue eternamente pedindo um número de teste (loop infinito)
print('FIM') #aparece apenas se o usuário não quiser mais continuar o programa