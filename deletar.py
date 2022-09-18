def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):

  coluna = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as fp:                   
    
  # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
   linha = fp.readline()
   linha_separada = linha.split(sep=',') 
   linha = linha_separada[indice_coluna]
   
   coluna.append(linha)
  # use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'
   while linha:
        
        if tipo_dado == 'str':
            coluna.append(linha)
        elif tipo_dado == 'int':
            coluna.append(linha)
        else: 
            print('Error')
        
        linha = fp.readline()

  return coluna

# extrair a coluna valor_venda
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
print(valor_venda) # deve retornar ['vhigh', 'med', 'low', ...]