import os

from agenda import Agenda

os.system('cls')

# Instanciando o objeto
cadastro = Agenda

# Entrada de dados
for c in range(3):
    cadastro.dicionario['nome'] = str(input('Nome: '))
    cadastro.dicionario['telefone'] = str(input('Telefone: '))

    cadastro.lista.append(cadastro.dicionario.copy())

# Saída
os.system('cls')
print('AGENDA TELEFÔNICA---------------------------------')
print('\nNome\tTelefone')
for registro in cadastro.lista:
    print('', end=' ' + '\n')
    for chave, valor in registro.items():
        print(f'{valor}', end='\t')

print()
print()