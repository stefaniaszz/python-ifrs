while True:
    try:
        a = int(input())
        resultado = 12345 / a
        print(resultado)
    except:
        print('Aconteceu uma divisão por zero e por isso vou parar por aqui') #não escrever nada após o except, colocar direto o break no final, não precisa colocar um print
        break
#continua o prgrama 
print('mas vamos seguindo o baile')