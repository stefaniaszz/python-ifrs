valor = list(map(int, input().split()))
resultado = valor[:]
valor.sort()
for v in valor:
    print(v)
print()
for v in resultado:
    print(v)