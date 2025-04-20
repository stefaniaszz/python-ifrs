n = int(input())
for _ in range(n):
    k = int(input())
    total_tomadas = 1
    for _ in range(k):
        tomadas = int(input())
        total_tomadas += tomadas
total_aparelhos = total_tomadas - k + 1
print('%d' % total_aparelhos)
