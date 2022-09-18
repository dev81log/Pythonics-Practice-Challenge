# função para ler, extrair valores do TXT
def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []

    # le o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
    with open(file=nome_arquivo, mode='r', encoding='utf8') as fp:

    # extrair linha do arquivo utilizando o parametro 'numero_linha'
    linha = fp.readline()
    count = 1

    # quebra a linha em palavras com o comando split ' '
    while count < numero_linha:
        linha = linha.rstrip('\n')
        linha_formatada = linha.split(sep=' ')
        palavras_linha.append(linha_formatada)
        count += 1

    return palavras_linha

# chamada de função com parâmetros da linha selecionada
linha10 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=11)
print(linha10)  # deve retornar ['Mas', 'eis', 'que', 'chega', 'a', 'roda', 'viva']
