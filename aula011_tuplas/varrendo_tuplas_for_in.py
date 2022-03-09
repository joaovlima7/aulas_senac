import os

os.system('cls')

print('-'*80)
print('Varrendo tuplas com for in')
print('='*80)

# Declaração
numeros = (1, 2, 3, 4, 5, 6)
atores = ('Norman Reedus', 'Melissa Mcbride', 'Lauren Cohan')
personagens = ('Daryl Dixon', 'Carol Peletier', 'Maggie Rhee')
decimais = (1.2, 3.4, 5.6, 7.8)
mix = ( 'John', 40, 1.77, True)

# Saída 
print('Números: ', end= ' ')
for numero in numeros:
    print(numero, end= ' ')
    print()

print('Atores: ', end= ' ')
for atorAtriz in atores:
    print(atorAtriz, end= ' ')
    print()

print('Personagens: ', end= ' ')
for personagem in personagens:
    print(personagem, end= ' ')
    print()

print('Decimais: ', end= ' ')
for decimal in decimais:
    print(decimal, end= ' ')
    print()

print('Mix: ', end= ' ')
for decimal in decimais:
    print(decimal, end= ' ')
    print()

print('-'*80)
print() 