clientes = []
for i in range(3):
    dados = input('Informe nome, data de nascimento e cidade: ').split() #recebe a informação 
    clientes.append(dados) # joga dentro da lista (clientes) o conteúdo adicionado em (dados)
print(clientes)
print(clientes[1][1]) # mostra o nome que eu quero pedindo a posição, dentro da lista que eu selecionei com a posição
