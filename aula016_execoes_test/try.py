#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 08/02/2022
#Término: 08/02/2022 
#Exceçoes - try

import os


os.system('cls')

def divisao(a,b):
    try:
        d = a / b
        return d
    except ZeroDivisionError:
        return 'Erro! Não podemos dividir um número por zero'

a = 10
b = 0

# Calculando a divisão
resultado = divisao(a, b)

# Saída
print('-'*70)
print(f'O número {a} / {b} = {resultado}')
print('-'*70)
print()