# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - F

import os

# Importando a classe calculo
from calculo import Calculo

os.system('cls')

calculo1 = Calculo
calculo2 = Calculo

print('-'*60)
print('Mostrando o dobro e o triplo do número 10')
print('-'*60)

resultado1 = calculo1.dobro1(10, 2)
resultado2 = calculo2.triplo1(10, 3)

print(f'O dobro do número 10 é: {resultado1}')
print(f'O triplo do número 10 é: {resultado2}')
print('-'*60)
print('FIM DO PROGRAMA !')