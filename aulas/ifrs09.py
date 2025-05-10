senha = '1234'
tent = input('Digite a senha: ')
while tent != senha:
    print('ERROR') #digitando errado a senha, segue eternamente o teste, só para quando acertar o solicitado
    tent = input('Digite a senha: ')
print('OK!')