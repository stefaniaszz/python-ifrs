#Mostrar os números pares de 1 até n
n = int(input())
for i in range (1, n+1):
   if i % 2 == 0: #verificar o resultado do resto, se for 1 é impar e se for 0 é par
      print(i)