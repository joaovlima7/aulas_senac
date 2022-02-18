import os
from math import pow

os.system('cls')


def calculo_imc(peso=0.0, altura=0.0):

    # Calculando o imc
    imc = peso / pow(altura, 2)
    # retorno o valor do imc
    return imc

print('-'*70)
print('Calcular o IMC')
print('='*70)

try:
    peso = float(input('Informe o seu peso: '))
    altura = float(input('Informe sua altura: '))

    resultado = calculo_imc(peso, altura)

    print('-'*70)
    print(f'O cálculo do imc é igual a {resultado:.2f}')
    print('='*70)

except ValueError:
    print('Valor inválido')
    print('-'*70)
    print()
    