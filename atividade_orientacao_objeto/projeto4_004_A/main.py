# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 004 - A

import os

# Importando a classe pareimpar
from pareimpar import Pareimpar


os.system('cls')

Parouimpar = Pareimpar()

# Entrada de dados
numero = int(input('Digite um número: '))

if (numero %2) == 0:
    print('O número é par !')
else:
    print('O número é impar !')
    