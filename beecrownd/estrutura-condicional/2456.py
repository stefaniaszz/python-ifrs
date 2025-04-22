n1, n2, n3, n4, n5 = map(int, input().split())
if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:
    print('C')
elif n1 >= n2 and n2 >= n3 and n3 >= n4 and n4 >= n5:
    print('D')
else:
    print('N')