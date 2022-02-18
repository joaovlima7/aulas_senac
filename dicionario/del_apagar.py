print('='*80)
print('Declaração metodod del ()')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}

del(agenda[str(input('quem voce quer apagar: '))]) #Argumento chave
tamanho = len(agenda)

print(agenda)
print(f'Tamanho da agenda: {tamanho}')


#tentar usar no trbalho do elenco