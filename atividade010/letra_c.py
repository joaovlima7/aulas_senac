#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 08/12/2021
#Término: 10/12/2021 - Tuplas
#Atividade010 - letra a

# Importando biblíoteca
import os


# Limpando terminal
os.system('cls')

# Título
print('-'*125)
print('Apague 1 elemento no dicionario anterior')
print('='*125)

# Dicionário 
inscricao = {'Nome': 'João', 'Idade': 18, 'peso': 52, 'Altura': 1.70}

# Adicionando novos elementos

# Elemento 1
inscricao['cidade'] = 'Juiz de Fora'

# Emeneto 2
inscricao['Estado'] = 'MG'

# Apagando 1 elemento do dicionário

del(inscricao['peso'])

# Saída 
print(f'Dicionario com 1 elemento removido: {inscricao}')
print('-'*125)
print('Fim do programa!')
print('='*125)