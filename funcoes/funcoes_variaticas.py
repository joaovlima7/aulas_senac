# Curso Técnico de Informática
# Autor: João Victor
# Data início: 04/02/2022
# Funções

# Importando bibliotecas
#import os
#from funcoes_uteis import limpa_telas as lt
#from funcoes_uteis import linha_simples as ls
#from funcoes_uteis import linha_dupla as ld

print('Funções Variádicas')

def lista(*lista):
    print(lista)


def dicionario(**dicionario):
    print(dicionario)

#limpar a tela
lt()

#Inserir uma linha dupla
ld(70)
print('Funções variádicas')
ls(70)

# Imprimindo uma lista qualquer
lista('um', 'dois', 'três', 'quatro')

# Imprimindo uma dicionário qualquer
dicionario(domingo = 1, segunda = 2, terca = 3)

# Inserir uma linha simples
ls(70)
print()