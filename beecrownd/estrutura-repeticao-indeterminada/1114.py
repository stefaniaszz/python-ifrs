senha = '2002'
acerto = False
while acerto == False:
    tent = input()
    if tent == senha:
        acerto = True
    else:
        print('Senha Invalida')
print('Acesso Permitido')