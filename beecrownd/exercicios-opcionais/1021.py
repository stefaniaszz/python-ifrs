valor = float(input())
valor_cent = int(round(valor * 100)) #converte o valor para centavos
notas = [10000, 5000, 2000, 1000, 500, 200] #define notas e moedas disponíveis 
moedas = [100, 50, 25, 10, 5, 1]
result = [] #inicializador da cotagem de notas e moedas
for nota in notas: #calcula a quantidade de notas
    qtd = valor_cent // nota
    valor_cent %= nota
    result.append(qtd)
for moeda in moedas: #calcula a quantidade de moedas
    qtd = valor_cent // moeda
    valor_cent %= moeda
    result.append(qtd)
print('NOTAS:')
print(result[0], 'nota(s) de R$ 100.00')
print(result[1], 'nota(s) de R$ 50.00')
print(result[2], 'nota(s) de R$ 20.00')
print(result[3], 'nota(s) de R$ 10.00')
print(result[4], 'nota(s) de R$ 5.00')
print(result[5], 'nota(s) de R$ 2.00') 
print('MOEDAS')
print(result[6], 'moeda(s) de R$ 1.00')
print(result[7], 'moeda(s) de R$ 0.50')
print(result[8], 'moeda(s) de R$ 0.25')
print(result[9], 'moeda(s) de R$ 0.10')
print(result[10], 'moeda(s) de R$ 0.05')
print(result[11], 'moeda(s) de R$ 0.01')