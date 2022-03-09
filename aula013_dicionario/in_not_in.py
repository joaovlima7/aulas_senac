print('='*80)
print('metodo in e not in')
print('='*80)

#declarações
agenda = { 'neymar': '9916 - 4566', 'mbappe': '5556 - 9988' , 'messi': '1344 - 9900'}
print()

#Imprimindo a agend
print(agenda)
print()

#Verificando se neymar esta no dicionario
if 'neymar' in agenda:
    print('VERDADEIRO!! neymar esta no dicionario')
else:
    print('FALSO!!! neymar não esta no dicionario')

#VERIFICAÇÃO se ronaldo esta no dicionario
if 'ronaldo' not in agenda:
    print('VERDADEIRO! ronaldo não esta na agenda')
else:
    print('FALSO!! ronaldo esta no dicionario')

#usar no trabalho do brasileirão