import os

os.system('cls')

print('-'*80)
print('Adicionando e removendo itens de uma tupla')
print('='*80)

# Declaração 
nomes = ()

# Convertendo a tupla em lista
listaNomes = list(nomes)

# Entrada de dados 
for c in range(0, 4, 1):
    listaNomes.append(str(input('Digite o nome: ')))

# Convertendo a lista em tupla
nomes = tuple(listaNomes)

# Saída 
print('Nomes: \t', end= ' ')
for indice, nome in enumerate(nomes):
    print(f'{indice} : {nome}', end='   ')
    print()

print('-'*80)
print()

nome = str(input('Digite um nome para remover da tupla: '))
if (nome not in nomes):
    print('Nome não está na tupla!')
else:
    # Convertendo a tupla e lista
    listaNomes = list(nomes)
    listaNomes.remove(nome)

# Convertendo a lista em tupla
nomes = tuple(listaNomes)

# Saída
print('Nomes: \t', end= ' ')
for indice, nome in enumerate(nomes):
    print(f'{indice} : {nome}', end='   ')
print()
print('-'*80)
print()