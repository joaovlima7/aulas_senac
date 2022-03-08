#_*_ coding: utf-8 _*_

import os


os.system('cls')

# Na abertura, se o arquivo não existir, ele será criado
# utilizamos o with para não ter que nos preocupar em fechar
# esse arquivo
with open('C:/projetosPython/aulas_senac/aula019_leitura_escrita_arquivos/arquivo.csv', 'w+') as arquivo:

    # Inserindo um cabecalho para os campos da tabela csv
    arquivo.write('Nome' + ';' + 'Endereço' + ';' + 'Telefone')

    # Saltar linha
    arquivo.write('\n')

    while(True):
        # Inserindo informações no arquivo
        nome = input('Insira seu nome: ')
        endereco = input('Insira seu endereço: ')
        celular = input('Insira seu telefone: ')

        # Armazenamento das informações no arquivo
        # Com o método write
        arquivo.write(nome)
        arquivo.write(';')
        arquivo.write(endereco)
        arquivo.write(';')
        arquivo.write(celular)

        resposta = input('Deseja continuar (s/n): ').lower()

        if resposta == 's':

             # Seek()
            # 0: define o ponto de referência no início do arquivo.
            # 1: define o ponto de referência na posição atual do arquivo.
            # 2: define o ponto de referência no final do arquivo.
            arquivo.seek(0,0)

            # Saltar linha
            arquivo.write('\n')
            continue

        else:
            lista = arquivo.readlines()
            break
    # Fazer uma pesquisa dentro do arquivo csv
    for linha in lista:
        if 'John' in linha:

            print(linha)