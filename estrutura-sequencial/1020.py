diasTotais = int(input())
anos = diasTotais // 365
resto = diasTotais % 365
meses = resto // 30
dias = resto % 30
print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)
