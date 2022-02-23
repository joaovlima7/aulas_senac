# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - J

class Metros:
    largura = 0
    altura = 0

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calculo(largura, altura):
        a = largura * altura
        return a