def area_circulo(raio):
    area = 3.14159 * (raio * raio)
    return area
raio = float(input())
area = area_circulo(raio)
print('A=%.4f' % area)