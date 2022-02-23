# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - E

import os

# Importando a classe Inteiro
from inteiro import Inteiro

os.system('cls')


inteiro1 = Inteiro
inteiro2 = Inteiro

print('-'*60)
print('Mostrando o antecessor e o sucessor do número inteiro')
print('-'*60)

resultado1 = inteiro1.antes(5, 1)
resultado2 = inteiro2.depois(5, 1)

print(f'O antecessor do número 5 é: {resultado1}')
print(f'O sucessor do número 5 é: {resultado2}')
print('-'*60)
print('FIM DO PROGRAMA !')