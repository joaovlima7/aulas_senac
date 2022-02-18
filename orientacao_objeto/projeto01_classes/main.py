# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

import os

# Importando as classes
from conta import Conta
from carro import Carro
from pessoa import Pessoa


os.system('cls')

# --------------------------------------------------
print('PROGRAMA PRINCIPAL -----------------------')
print()

print('Objetos tipo pessoa ----------------------')

# Criando objetos pessoa
gerente = Pessoa('John Doe', 50)
officeboy = Pessoa('Smith', 20)

print(f'\tNome: {gerente.nome}')
print(f'\tIdade: {gerente.idade}')

# --------------------------------------------------
print('Objetos do tipo Carro --------------------')

# Criando objetos Carro
gol = Carro('Wolkswagen', 'Branca', 'BRA3049', 1985)
ferrari = Carro('F250', 'Vermelha', 'BRA6060', 2020)
prios = Carro('Toyota', 'Marrom', 'BRA9090', 2022)
print(f'\tFabricante: {gol.fabricante}')
print(f'\tAgência: {gol.cor}')
print(f'\Placa: {gol.placa}')
print(f'\Ano: {gol.ano}')

print()

# --------------------------------------------------
print('Objetos do tipo conta --------------------')

# Criando objetos conta
john = Conta('John Doe', 123456, 1550, 13)
jane = Conta('Jane Doe', 654321, 2525, 15)

print(f'\tNome do Cliente: {john.cliente}')
print(f'\tAgência: {john.agencia}')
print(f'\tNúmero da conta: {john.conta}')
print(f'\tDigito: {john.digito}')

# --------------------------------------------------
print('-'*70)