salario = float(input())
reajuste = 0
if salario <= 400.00:
    reajuste = 15
elif salario <= 800.00:
    reajuste = 12
elif salario <= 1200.00:
    reajuste = 10
elif salario <= 2000.00:
    reajuste = 7
else:
    reajuste = 4

valorReajuste = (salario * reajuste) / 100
novoSalario = salario + valorReajuste

print(f'Novo salario: {novoSalario:.2f}')
print(f'Reajuste ganho: {valorReajuste:.2f}')
print(f'Em percentual: {reajuste} %')