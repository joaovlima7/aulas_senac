print('='*80)
print('Declaração metodod keys , values , items')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}

#pegando chaves , valores e itens
#Acessando propiedades dp dicionario
chaves = agenda.keys()
valores = agenda.values()
itens = agenda.items

#Verificando o tamanho da agenda
tamanho = len(agenda)

print(agenda)
print(f'Tamanho da agenda: {tamanho}')

print('-'*80)
print(f'Todas as chaves da agenda \n{chaves}')
print()
print(f'Todas as valores da agenda \n{valores}')
print()
print(f'Todos os itens  da agenda \n{itens}')
print()