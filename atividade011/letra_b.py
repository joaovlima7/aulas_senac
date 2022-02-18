import os

# Limpando o terminal
os.system('cls')

# Criando uma função
def cadastrar():
    alunos = {}
    lista = []
    for c in range(2):
        alunos['Nome'] = str(input('Nome do aluno: '))
        alunos['Matricula'] = str(input('Matrícula do aluno: '))
        alunos['Nascimento'] = str(input('Data de nascimento do aluno: '))

        lista.append(alunos.copy())

    os.system('cls')
    print('-'*70)
    print('Alunos cadastrados')
    print('='*70)

    for aluno in lista: # Para cada elemento na minha lista
        for chave, valor in aluno.items(): # Para cada chave e valor do aluno
            print(f'{chave} : {valor}', end=' ' + '\n')
        print('-'*80)


# Programa principal
print('-'*70)
print('Cadastro de alunos')
print('='*70)
cadastrar()