# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 004 - H

import os

# Importando a classe equacao
from equacao import Equacao


os.system('cls')

equacao = Equacao

#Declaração
equacao = 'X² - 6x + 5 = 0'
a = 1
b = -6
c = 5

#Calculo do delta
delta = (b ** 2) - (4 * a * c)

#Calculando as raízes
resultado1 = (-b + (delta ** (1/2))) / (2 * a)
resultado2 = (-b - (delta ** (1/2))) / (2 * a)

print(f'As raízes da equação são {resultado1}, {resultado2}')
print()
print('-'*40)