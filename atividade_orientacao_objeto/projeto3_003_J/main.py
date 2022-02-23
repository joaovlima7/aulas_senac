# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - J

import os

# Importando a classe metros
from metros import Metros

os.system('cls')


metros = Metros

print('-'*60)
print('Metros quadrado de uma parede')
print('-'*60)

resultado = metros.calculo(10, 15)

print(f' A parede tem: {resultado} m²')
print('-'*60)