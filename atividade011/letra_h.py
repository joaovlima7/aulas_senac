#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 04/02/2022
#Término: 11/02/2022 
#Atividade 011 - letra h

# Importando as bibliotecas
import os


# Limpando a tela
os.system('cls')

# Título
print('='*70)
print('DADOS DA ACADEMIA')
print('-'*70)
print()

# Declaração
lista = ['Código', 'Nome', 'Altura', 'Peso']
lista_valores = []
lista_alunos = []
resultado = []

# Entrada de dados
codigo = int(input('Digite seu codigo: '))
lista_valores.append(codigo)
print()
nome = str(input('Digite seu nome: '))
lista_valores.append(nome)
print()
altura = float(input('Digite sua altura: '))
lista_valores.append(altura)
print()
peso = float(input('Digite seu peso: '))
lista_valores.append(peso)
print()

# Outro usuário
print('Outro usuário')
print()
codigo = int(input('Digite seu codigo: '))
lista_valores.append(codigo)
print()
nome = str(input('Digite seu nome: '))
lista_valores.append(nome)
print()
altura = float(input('Digite sua altura: '))
lista_valores.append(altura)
print()
peso = float(input('Digite seu peso: '))
lista_valores.append(peso)
print()

# Saída de dados
print('-'*70)
print('Código          Nome            Altura          Peso')
print('-'*70)

# Validação
for i, c in enumerate(lista_alunos):
    print()
    for valor in c():
        print(f'{valor}', end='\t\t')

media_alt, media_kg = resultado(lista_alunos)                                     
print(f'Média:                         {media_alt:5.2f}\t\t{media_kg:5.2f}')