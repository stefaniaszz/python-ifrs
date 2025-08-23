from fila import *

f = criar_fila()
enfileirar(f, "C")
enfileirar(f, "D")
enfileirar(f, "E")
jog1 = "A"
jog2 = "B"

for i in range (8):
    ponto1, ponto2 = list(map(str, input("Pontuação: ").split()))
    if ponto1 > ponto2:
        enfileirar(f, jog2) #se o jogador 1 ganhou, sai o jogador 2 e vem o próximo da fila
        jog2 = desenfileirar(f)
        vencedor = jog1
    else:
        enfileirar(f, jog1)
        jog1 = desenfileirar(f)
        vencedor = jog2
    print("O vencedor foi o %s" % (vencedor))