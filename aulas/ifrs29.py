def cifragem(palavra, deslocamento):
    novaPalavra = ''
    for letra in palavra:
        posicao = ord(letra) - 65
        novaPosicao = (posicao + deslocamento) % 26 + 65
        novaLetra = chr(novaPosicao)
        novaPalavra += novaLetra
    return novaPalavra


palavra = input('Escolha uma palavra: ')
posicao = int(input('Escolha um deslocamento: '))
palavra_cifrada = cifragem(palavra, posicao)
print("legal", palavra_cifrada)

