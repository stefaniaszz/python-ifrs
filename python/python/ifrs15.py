N = int(input())
cont_in = 0
cont_out = 0
for _ in range(N):
    X = int(input())
    if 10 <= X <= 20:
        cont_in += 1
    else:
        cont_out += 1
print('%d in' % cont_in)
print('%d out' % cont_out)