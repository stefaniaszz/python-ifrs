'''
estado = input()
if estado == 'roraima' or estado == 'acre' or estado == 'amapa' or estado == 'amazonas' or estado == 'para' or estado == 'rondonia' or estado == 'tocantins':
    print('Região Norte')
else:
    print('Outra região')
'''

estado = ['roraima', 'acre', 'amapa', 'amazonas', 'para', 'rondonia', 'tocantins']
nome = input()
if nome in estado:
    print('Região Norte')
else:
    print('Outra região')