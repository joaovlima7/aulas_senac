# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 21/02/2022
# Término: 22/02/2022
# Orientação a Objetos
# Atividade 003 - E

class Inteiro:
    numero = 5
    antecessor = 0
    sucessor = 0
    
    # Método construtor
    def __init__(self, numero, antecessor, sucessor):
        self.numero = numero
        self.antecessor = antecessor
        self.sucessor = sucessor
        
    # Membros de uma classe
    def antes(numero, antecessor):
        ante = numero -  antecessor
        return ante

    def depois(numero, sucessor):
        suce = numero + sucessor
        return suce