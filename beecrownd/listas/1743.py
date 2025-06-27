x, y = list(map(int, input().split()))
compativel = True
for i in range(5):
    if x[i] + y[i] != 1: # se um dos testes da tomada der resultado diferente de 1, é falso, ou seja, nao compativel
        compativel = False
        break
if compativel:
    print('Y')
else:
    print('N')
