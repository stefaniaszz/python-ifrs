codPeca1, numPeca1, valorPeca1 = input().split()
codPeca1 = int(codPeca1)
numPeca1 = int(numPeca1)
valorPeca1 = float(valorPeca1)

codPeca2, numPeca2, valorPeca2 = input().split()
codPeca2 = int(codPeca2)
numPeca2 = int(numPeca2)
valorPeca2 = float(valorPeca2)

valorTotal = ((numPeca1 * valorPeca1) + (numPeca2 * valorPeca2))
print('VALOR A PAGAR: R$ %.2F' % valorTotal)
