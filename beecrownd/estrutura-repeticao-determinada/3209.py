n = int(input())
for i in range(n):
    filtros = [int(x) for x in input().split()]
    if not filtros:
        print()
        continue
    dif = filtros[0] - 1
    qtd_filtro = sum(filtros[1:])
    print(qtd_filtro - dif)
