#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 08/12/2021
#Término: 10/12/2021 - Tuplas
#Atividade009 - letra b

# Importando biblíoteca
import os


# Limpando terminal
os.system('cls')

# Título
print('-'*130)
print('Adicione mais 2 elementos no dicionario anterior')
print('='*130)

# Dicionário 
inscricao = {'Nome': 'João', 'Idade': 18, 'peso': 52, 'Altura': 1.70}

# Adicionando novos elementos

# Elemento 1
inscricao['cidade'] = 'Juiz de Fora'

# Emeneto 2
inscricao['Estado'] = 'MG'

# Saída 
print(f'Dicionario com novos elementos: {inscricao}')
print('-'*130)
print('Fim do programa!')
print('='*130)