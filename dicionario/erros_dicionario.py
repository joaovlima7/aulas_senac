print('='*80)
print('Declarando erros no dicionario')
print('='*80)

#Indicies iguais
dicionario1 = {'nome': 'jhon' , 'nome': 'maria'}

#posso ter uma tupla como indicie a uma lista como valor
dicionario2 = {(1, 2), [1, 2]}

#Mas não posso ter uma lista como indicie e um tupla como valor
dicionario3 = {[1,3], (1,2)}

print(dicionario1)
print(dicionario2)
print(dicionario3)