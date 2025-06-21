t = int(input()) #lê quantos testes vão ser feitos
fibonacci = [0, 1] #cria a lista com os dois primeiros números de Fibonacci
while len(fibonacci) <= 60: #gera os próximos números até o 60º
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)
for i in range(t): #para cada teste
    n = int(input())
    print(f"Fib({n}) = {fibonacci[n]}")