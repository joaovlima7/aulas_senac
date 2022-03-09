# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

class Pessoa:

    # O método construtor do python é o __init__
    # O paramêtro self é obrigatório
    def __init__(self, nome, idade, nascimento):

        # Criando os atributos dentro do construtor
        self.nome = nome
        self.idade = idade
        self.nascimento = nascimento

    def __str__(self): # Método interno para dar saída String
        return f'''
        Nome: {self.nome}
        Data Nascimento: {self.nascimento}
        Idade: {self.idade} anos'''