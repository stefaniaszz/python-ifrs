def pesquisa_linear (lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i+1
    return 0

arq = open("palavrasDesord.txt", "r") #abre o arquivo importado e readlines
palavras = arq.readlines()  
for i in range(len(palavras)):
    palavras[i] = palavras[i].rstrip() #tira o \n do enter no final das palavras ou espaços desnecessários
arq.close()
while True:
    palavra = input("palavra a pesquisar: ")
    pos = pesquisa_linear(palavras, palavra)
    print(pos)

