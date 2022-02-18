import os

os.system('cls')

print('-'*80)
print('Varrendo tuplas com for enumerate')
print('='*80)

# Declaração
numeros = (1, 2, 3, 4, 5, 6)
atores = ('Norman Reedus', 'Melissa Mcbride', 'Lauren Cohan')
personagens = ('Daryl Dixon', 'Carol Peletier', 'Maggie Rhee')
decimais = (1.2, 3.4, 5.6, 7.8)
mix = ( 'John', 40, 1.77, True)

# Saída
print('Números: \t', end= ' ')
for indice, ator in enumerate(numeros):
    print(f'{indice} : {numeros}', end='   ')
    print()

print('Atores: \t', end= ' ')
for indice, ator in enumerate(atores):
    print(f'{indice} : {ator}', end='   ')
    print()

print('Personagens: \t', end= ' ')
for indice, personagens in enumerate(personagens):
    print(f'{indice} : {personagens}', end='    ')
    print()

print('Decimais: \t', end= ' ')
for indice, decimais in enumerate(decimais):
    print(f'{indice} : {decimais}', end='   ')
    print()

print('Mix: \t', end= ' ')
for indice, item in enumerate(mix):
    print(f'{indice} : {item}', end='   ')
    print()