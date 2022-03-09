# Importando biblioteca
import os 


os.system('cls')

print('-'*80)
print('Dicionários: Varrendo com for')
print('='*80)

# Declaração
agenda = {
    'Jojo': '99196-3030',
    'Dio': '99196-5050',
    'Jolyne': '99196-6060',
    'Lisa Lisa': '99196-7070',
    'Speedwagon': '99196-8080',
}

# Saída com for
print('Nome \t\t\tcelular')
print('-'*80)
for chave, valor in agenda.items():
    print(f'{chave}     \t\t{valor}')
    print('-'*80)
    print()