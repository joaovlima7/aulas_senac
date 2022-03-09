import os 

# Importando o módulo cálculos
from modulos.calculos import soma


# Código principal
a = int(input('Digite o valor de "a": '))
b = int(input('Digite o valor de "b": '))

# Chamando a função
resultado = soma(a, b)

# Saída
os.system('cls')
print(f'A soma de {a} + {b} = {resultado}')
print()