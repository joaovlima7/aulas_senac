#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 09/12/2021
#Término: 19/12/2021 - Tuplas
#Funções

# Importando as bibliotecas
import os


os.system('cls')

print('-'*70)
print('Funções: parâmetros e argumentos')
print('='*70)

# Função
def soma(a, b):

    soma = a + b
    print(f'A soma de {a} + {b} = {soma}')

def subtracao(a, b):
    subtracao = a - b
    print(f'A subtração de {a} - {b} = {subtracao}')

# Duas linhas depois: invocando a função
# e passando 2 argumentos
x = 2
y = 3
soma(x, y)
subtracao(10, 5)
print('-'*70)
print()