# Curso Técnico de Informática
# Autor: João Victor
# Data início: 04/02/2022
# Funções

# Importando bibliotecas
import os


print('-'*70)
print('Funções com retorno múltiplo')
print('='*70)

# função normal
def limpa_tela():
    os.system('cls')

def linha_simples(tamanho):
    print('-'*tamanho)

def linha_dupla(tamanho):
    print('-'*tamanho)

# Função com retorno múltiplo
def valores():
    x = 10
    y = 20

    return x,y


# Precisamos desempacotar esses valores
a, b = valores()

# Saída
limpa_tela

linha_dupla(70)
print(f'O primeiro valor é: {a}')
print(f'O segundo valor é: {b}')
linha_simples(70)