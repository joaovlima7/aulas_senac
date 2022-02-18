#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 04/02/2022
#Término: 11/02/2022 
#Atividade 011 - letra f

# Crie uma função que receba 2 lista: -lista 1: nome, peso, idade 
#-lista 2:John, 40, 1.8 -Sua função deve criar um dicionário contendo 
# chave e valor utilizando como base essas duas listas. 
# Depois, seu programa deverá imprimir esse dicionário 
#utilizando o laço for... items... 


# Importando as bibliotecas
import os


# Limpando a tela
os.system('cls')

print('-'*60)
print('LISTA DENDRO DO DICIONÁRIO')
print('='*60)

lista1 = ['Nome', 'Peso', 'Idade']
lista2 = ['John', 40, 18]
lista3 = [lista1,lista2]

def juntalista(lista1,lista2):
    lista3 = juntalista(lista1,lista2)
    lista3 = list(zip(juntalista))
    return lista3

print(lista3)


print()
print('-'*60)
print('FIM DO PROGRAMA!')