import os 

# Limpando o terminal
os.system('cls')


def titulo():
    print('-'*70)
    print('aluno(a)\t\tMatrícula\tNascimento')
    print('='*70)

def busca_aluno(cadastro_alunos):
    aluno = str(input('Entre com o nome do aluno: '))

    # Usando um laço 
    # para encontrar o valor no cadastro_alunos
    for item in cadastro_alunos:
        if item['nome'] == aluno:
            print('Encontrado!')
            return item
        else:
            break


cadastro_alunos = [
    {'nome': 'Diana Prince', 'matricula': '123456789', 'nascimento': 1960},
    {'nome': 'Carol Danvers', 'matricula': '987654321', 'nascimento': 1970},
    {'nome': 'Natalia Alianovna', 'matricula': '951753258', 'nascimento': 1980}
]

# Imprimindo o cadastro_alunos original
titulo()
for item in cadastro_alunos:
    for c, v in item.items():
        print(f'{v}', end='    \t')
        print()
print('-'*70)
print()

# Invocando a função
resultado = busca_aluno(cadastro_alunos)

# Se a busca for verdadeira
if resultado:
    for chave, valor in resultado.items():
        print(f'{valor}', end='     \t')
        print()
        print('-'*70)
        print()