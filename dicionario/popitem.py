print('='*80)
print('metdod popitem')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}

#antes
print('Antes')
print(agenda)

#copia a chave e o valor e exclui do dicionario origem
novaAgenda = agenda.popitem()
print()

#depois
print('depois')
print(agenda)
print()

#Imprimindo a tupla 
print(f'Tupla retornada: {novaAgenda}')
print()
print()