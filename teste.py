n = int(input("Digite o número de casos de teste: "))  # Lê o número de casos de teste

for _ in range(n):
    k = int(input("Digite o número de filtros: "))  # Lê o número de filtros
    total_tomadas = 1  # Começa com 1 tomada da parede

    # Lê as tomadas de cada filtro em uma única linha
    tomadas = list(map(int, input("Digite o número de tomadas de cada filtro, separados por espaço: ").split()))

    # Verifica se o número de filtros corresponde ao número de entradas
    if len(tomadas) != k:
        print("Erro: O número de filtros não corresponde ao número de tomadas fornecidas.")
        continue

    # Calcula o total de tomadas
    for t in tomadas:
        total_tomadas += t - 1  # Adiciona as tomadas do filtro, subtraindo 1

    # Calcula o total de aparelhos que podem ser alimentados
    total_aparelhos = total_tomadas - 1  # Subtrai 1 para a tomada da parede
    print('%d' % total_aparelhos)