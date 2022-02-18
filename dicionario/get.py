print('='*80)
print('metdod get')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}

#Pegando um elemento do dicionario
recuperar1 = agenda.get('neymar' , 'contato não encontrado')
recuperar2 = agenda.get('messi' , 'contato não encontrado')
recuperar3 = agenda.get('ronaldo' , 'contato não encontrado')

#Saida
print(f'o celular do neymar : {recuperar1}')
print(f'o celular do messi : {recuperar2}')
print(f'o numero do ronaldo: {recuperar3}')

#tentar usar no trabalho do brasileirão