precos = {
    1: 4.00, #cachorro quente
    2: 4.50, #x-salada
    3: 5.00, #x-bacon
    4: 2.00, #torrada
    5: 1.50 #refrigerante
}

cod, qtd = map(int, input().split())
if cod in precos:
    total = precos[cod] * qtd
    print(f'Total: R$ {total:.2f}')
else:
    print('Código do item inválido.')