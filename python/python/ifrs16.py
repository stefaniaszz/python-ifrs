N = int(input())
for i in range(N):
    n1, n2, n3 = map(float, input().split())
    media_pond = (n1 * 2 + n2 * 3 + n3 * 5) / 10
    print('%.1f' % media_pond)