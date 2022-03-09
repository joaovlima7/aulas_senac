# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

# Criando a classe
from re import A


class Retangulo:
    base = 0
    altura = 0

    # Método construtor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Membros de uma classe
    def area(base, altura): # A = b * h
        a = base * altura
        return A

    def perimetro(base, altura): # P = 2 (b + h)
        p = 2 * (base + altura)
        return p