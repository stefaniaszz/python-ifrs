senha = '1234'
acerto = False
while acerto == False: #mesma regra do outro exercício, porém usando regras booleanas
    tent = input('Digite a senha: ')
    if tent == senha:
        acerto = True
    else:
        print('ERROR')
print('OK!')