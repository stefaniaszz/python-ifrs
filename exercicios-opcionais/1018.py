valor = int(input().strip())
notas = [100, 50, 20, 10, 5, 2, 1]
quantidadeNotas = {}
valorOriginal = valor
for nota in notas:
    quantidade = valor // nota
    quantidadeNotas[nota] = quantidade
    valor %= nota
print(valorOriginal)
for nota in notas:
    print(f'{quantidadeNotas[nota]} nota(s) de R$ {nota},00')
