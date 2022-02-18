# Importando biblioteca
import os 


os.system('cls')

print('-'*80)
print('Dicionários: Métodos copy()')
print('='*80)

# Declaração
elementos = {} # Dicionário
periodica = [] # Lista

for c in range(0, 2):

    # Entrada de dados com for
    elementos['Simbolo'] = str(input('Simbolo do elemento: '))
    elementos['Nome'] = str(input('Nome do elemento: '))

    # Usa o append() com o copy() para fazer uma cópia do dicionário
    periodica.append(elementos.copy())

# Saída na tabela periódica
print()
print('-'*80)
print(periodica)

# For aninhado
print('-'*80)
for elemento in periodica: # Para cada elemento na minha lista
    for chave, valor in elemento.items(): # Para cada chave e valor nos meus elementos
        print(f'{chave} : {valor}') # Imprime a chave e o valor
print()