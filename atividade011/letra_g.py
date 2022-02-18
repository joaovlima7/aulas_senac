#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 04/02/2022
#Término: 11/02/2022 
#Atividade 011 - letra g

#Crie um programa que apresente ao usuário as seguintes operações:
#-1. Soma -2. Subtração -3. Produto -4. Divisão -5. Divisão inteira 
#-6. Resto da divisão –7. Sair Escolhida a operação, peça também 2 números.
# Em seguida você criará funções que retorna o resultado das operações,
# imprimindo o resultado. 

# Importando as bibliotecas
import os


# Limpando a tela
os.system('cls')

# Título
print('='*70)
print('CÁLCULOS')
print('-'*70)
print('1- soma')
print('2- subtração')
print('3- produto')
print('4- divisão')
print('5- divisão inteira')
print('6- resto da divisão')
print('7- sair')

#Entrada de dados
escolha = input('Digite o numero: ')
print()

# Validação
if (not(escolha.isnumeric())) or (int(escolha) < 1) or (int(escolha) > 7):
        print('Digite apenas numeros inteiros de 1 a 7.')
else:
    escolha = int(escolha)
    print('-'*70)
    print(f'Você escolheu a função numero: {escolha}')
    print('-'*70)

if(escolha == 1):
    flag = True
    while(True):
        print('-'*70)
        print('Função somar: ')
        print('-'*70)

while(True):
     valor_a = float(input('Insira o primeiro valor: '))    
     break
while(True):
          valor_b = float(input('Insira o segundo valor: '))
          retorno = (valor_a, valor_b)
          
          print(retorno)
          if(escolha == 1):
           flag = True
           while(True):
            print('-'*70)
            print('Função somar: ')
            print('-'*70)