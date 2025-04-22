import math # Importa a biblioteca math para usar funções matemáticas, como sqrt
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = math.sqrt((x2 - x1) **2 + (y2 - y1) **2)
print('%.4f' % distancia) 