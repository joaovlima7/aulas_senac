# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

import os

# Importando a classe Retângulo
from retangulo import Retangulo


os.system('cls')


# Instanciando os objetos 
retangulo1 = Retangulo
retangulo2 = Retangulo
retangulo3 = Retangulo
retangulo4 = Retangulo

# Cabeçalho
print('CÁLCULOS PARA ÁREA E PERÍMETRO DE UM RETÂNGULO')
print('-'*70)

# Argumentos para encontrar a área
resultado1 = retangulo1.area(10, 5)
resultado2 = retangulo2.area(100, 5)

print('ÁREA ----------------------------------------')
print(f'A área do retângulo é: {resultado1}')
print(f'A área do retângulo é: {resultado2}')
print('-'*70)

# Argumentos para encontrar o perímetro
resultado3 = retangulo3.perimetro(10, 5)
resultado4 = retangulo4.perimetro(100, 5)

print('PERÍMETRO -----------------------------------')
print(f'O perímetro do retângulo é: {resultado3}')
print(f'O perímetro do retângulo é: {resultado4}')
print('-'*70)

print()