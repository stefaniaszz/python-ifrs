n = int(input())
soma_distancia = 0
for i in range(n):
    t, v = map(int, input().split())
    distancia = t * v 
    if 1 <= t <= 100 and 0 <= v <= 120:
        soma_distancia += distancia
print('%d' % soma_distancia)

