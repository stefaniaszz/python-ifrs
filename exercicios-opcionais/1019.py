def converterSegundos(segundos):
    horas = segundos //3600
    minutos = (segundos % 3600) // 60
    segundosRestantes = segundos % 60
    return horas, minutos, segundosRestantes
n = int(input())
horas, minutos, segundos = converterSegundos(n)
print(f'{horas}:{minutos}:{segundos}')