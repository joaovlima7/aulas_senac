#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 08/02/2022
#Término: 08/02/2022 
#Exceçoes - Tratamento múltiplo

from lib2to3.pytree import type_repr
import os


os.system('cls')

def erro(a):
    try:
        eval(a)
    except TypeError:
        print('TypeError: impossivel realizar a operação')
    except NameError:
        print('NameError: variável não foi definida!')
    except ValueError:
        print('ValueError: tentando converter um literal em um inteiro!')


# Saída
print('-'*70)
print(erro('int + int'))
print(erro('var'))
print(erro('int("a")'))
print('-'*70)
print()