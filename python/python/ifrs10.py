#COnstruir um programa que receba a nota final de n alunos(as), sendo n informado pelo uduário. Você deve mostrar a média das notas dos(as) estudantes aprovados(as). Nota miníma para aprovação: 7.0

num = int(input())
soma = cont = 0
for i in range(num):
    nota = float(input())
    if nota >= 7.0:
        soma += nota 
        cont += 1
media = soma / cont    
print('Média das notas dos aprovados(as): %.f' % (media))