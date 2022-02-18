print('='*80)
print('metodod updte ()')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}

print()
print('Antes da atualização')
print(agenda)

#Criando uma segunda agenda
agenda2  ={'pele': '7658 - 888' , 'gaucho': '2233 - 111'}

print()
print('Depois da atualização')
#Atualizando o dicionario
agenda.update(agenda2)

print(agenda)
