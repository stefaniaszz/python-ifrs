import math

n = int(input())
phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2
fibonacciN = (phi**n - psi**n) / math.sqrt(5)
print('%.1f' % fibonacciN)
              