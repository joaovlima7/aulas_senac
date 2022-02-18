import os

os.system('cls')

print('-'*80)
print('Verificação in e not in')
print('='*80)

# Declaração
numeros = (1, 2, 3, 4, 5, 6)
atores = ('Norman Reedus', 'Melissa Mcbride', 'Lauren Cohan')
personagens = ('Daryl Dixon', 'Carol Peletier', 'Maggie Rhee')
decimais = (1.2, 3.4, 5.6, 7.8)
mix = ( 'John', 40, 1.77, True)

# Condicional
# pode testar com o not in
if (3 in numeros and 'Meggie Rhee' in personagens):
    resposta = 'Estão contidos em números e personagens.'
else:
    resposta = 'Não estão contidos em números e personagens.'

if ('Maria' not in atores and 1.10 not in decimais):
    resposta2 = 'Não estão contidos em atores e decimais'
else:
    resposta2 = 'Estão contidos em atores e decimais'

# Saída
print(f'Verificação 1: {resposta}\n')
print(f'Verificação 2: {resposta2}\n')
print('-'*80)
print()