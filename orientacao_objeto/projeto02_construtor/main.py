# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

import os

# Importando a classe pessoa
from pessoa import Pessoa

os.system('cls')


# Criando as instâncias e passando os argumentos
john = Pessoa('John Doe', 50, 1970)
jane = Pessoa('Jane Smith', 40, 1980)

# Saída
print('-'*70)
print(john)
print('-'*70)
print(jane)
print('-'*70)
print()