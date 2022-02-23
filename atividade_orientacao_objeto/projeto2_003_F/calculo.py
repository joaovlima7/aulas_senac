# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - F

class Calculo:
    numero = 10
    dobro = 0
    triplo = 0

    # Metodo construtor
    def __init__(self, numero, dobro, triplo):
        self.numero = numero
        self.dobro = dobro
        self.triplo = triplo

    # Membros de uma classe
    def dobro1(numero, dobro):
        a = numero * dobro
        return a

    def triplo1(numero, triplo):
        b = numero * triplo
        return b
        