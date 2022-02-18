# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

class Animal:

    # Utilizando parâmetros nomeados
    def __init__(self, nome='Sem nome', raca='labrador', nascimento=1970):

        self.nome = nome
        self.raca = raca
        self.nascimento = nascimento

    # Método interno (__str__) para dar saída String
    def __str__(self):
        return f'''
        Nome: {self.nome}
        Raça: {self.raca}
        Idade: {self.nascimento} anos.'''