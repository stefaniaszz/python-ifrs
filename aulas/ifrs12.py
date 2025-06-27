'''
Considere um tipo de investimento financeiro, em que você investe um valor inicial (c), seja corrigido mensalmente por uma taxa fixa (i) e, após um número de meses, atinja um valor final (m). 
Construa um programa que verifique a quantidade de meses (t) para se atingir o valor final. 
Você deve informar c, i, m.
'''

c = float(input('Qual valor você deseja investir?'))
i = float(input('Qual a taxa de juros do seu banco?'))
m = float(input('Qual valor final desejado?'))
t = 0
while c < m:
    c = c * i
    t += 1
    print('%.2f' % c)
print('%d meses' % t)