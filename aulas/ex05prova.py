n = int(input())
cont_pares = cont_impares = 0
for _ in range (n):
    valor = int(input())
    if valor % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
print('%d são pares' % (cont_pares))
print('%d são impares' % (cont_impares))
