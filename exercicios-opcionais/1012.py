a, b, c = map(float, input().split())
area = (a * c) /2
circulo = 3.14159 * (c ** 2)
trapezio = (a + b) * c /2
quadrado = b**2
retangulo = a * b
print('TRIANGULO: %.3f' % area)
print('CIRCULO: %.3f' % circulo)
print('TRAPEZIO: %.3f' % trapezio)
print('QUADRADO: %.3f' % quadrado)
print('RETANGULO: %.3f' % retangulo)