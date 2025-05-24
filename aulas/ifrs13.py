'''
Duas cidades A e B estão em franco crescimento populacional. A possui uma população inferior a B, mas tem uma taxa atual de crescimento maior. Com certeza, em algum tempo a população de A será maior que a de B.
Indique em quantos anos isso acontecerá.
Você deverá informar as populações de A e B (lembre que popA < popB), bem como as taxas de crescimento de ambas (lembre que taxaA > taxaB).
'''

popA, popB = map(int, input('População de A e B: ').split())
taxaA, taxaB = map(float, input('Taxa de crescimento de A e B: ').split())
anos = 0
while popA < popB:
    popA = popA * taxaA
    popB = popB * taxaB
    anos += 1
    print('%d %d' % (popA, popB))
print('%d anos' % (anos))

