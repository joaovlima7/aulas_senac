import os

os.system('cls')

print('-'*80)
print('Declarando sets')
print('='*80)

# Declaração
nomes = {'John', 'Jane', 'Carol'}
mumeros = {1, 2, 3, 4, 5, 6, 7} 

# Print(nomes[0]) # Erro, set não tem indice

# Mas posso varrer com for
for nome in nomes:
    print(nome, end= ' ')

print()
print()
print()
print('-'*80)
print('Adicionando elemento nos sets')
print('='*80)

# numeros.append() # Erro, não tem função append para sets

# Método add() Inserindo itens
print()
linguagens = {'Python', 'Java', 'PHP', 'C'}

# Inserindo um elemento no set.
print(f'Antes {linguagens}')
linguagens.add('C#')
print(f'Depois {linguagens}')

print()
print()
# Método update()
linguagens2 = {'Python', 'Java', 'PHP', 'C'}

# Inserindo mais de um elemento no set.
print(f'Antes {linguagens2}')
linguagens2.update(['Smalltalk', 'Javascript'])
print(f'Depois {linguagens2}')
print()