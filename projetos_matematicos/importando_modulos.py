import os

# Importando os símbolos
from math import pi, e

# Importando e utilizando um apelido para o módulo
from math import sqrt as rq

# Importando todos os símbolos da biblioteca
from math import *

# Limpando o terminal
os.system('cls')

# Saída
print(f'{e:.2f} | {pi:.2f} | {rq(9)}')

# Importando um símbolo dentro de uma função
def fatorial():
    from math import factorial
    print(f'Ftaorial de 4: {factorial(4)}')


# Saída Fatorial
print()
fatorial()
print()