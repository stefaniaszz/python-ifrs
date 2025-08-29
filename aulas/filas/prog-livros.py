from livros import *

p = criar_pilha()
f = criar_fila()
receber(p)
arquivar(f)

while True:
    op = int(input())
    if op == 1:
        titulo = input()
        receber (p, titulo)
    elif op == 2:
        livro = ler(p)
        arquivar(f, livro)
    elif op == 3:
        mostrar_espera(p)
    elif op == 4:
        mostrar_espera(f)



