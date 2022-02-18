import os

# Limpando o terminal
os.system('cls')


def conversao(temperatura):
    conversao = ((temperatura - 32) * 5) / 9
    return conversao

print('-'*70)
print('Programa para converter temperatura')
print('Fahrenheit para Célsius')
print('='*70)

# Entrada
temperatura = float(input('Informe a temperatura em Fahrenheit: '))

# Invocando a função e guardando em uma variável
resultado = conversao(temperatura)

print('-'*70)
print(f'Temperatura em Fahrenheit: {temperatura}')
print(f'{temperatura} °F = {resultado:.1f} °C')
print('='*70)
print()