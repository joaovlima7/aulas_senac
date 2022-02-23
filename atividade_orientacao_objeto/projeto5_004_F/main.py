# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 004 - F

import os

# Importando a classe bissexto
from bissexto import Bissexto


os.system('cls')

bissexto = Bissexto

# Entrada de dados
ano = int(input('Digite o ano: '))

#Condicionais
if (ano <= 0):
    print('Ano inválido!!')
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

print()
print('-'*40)
