# Curso Técnico de Informática
# Autor: João Victor
# Data de início: 16/02/2022
# Término: 16/02/2022
# Orientação a Objetos

class Conta:

    # Método __init__ obrigatório (construtor)
    def __init__(self, cliente, conta, agencia, digito):
        self.cliente = cliente
        self.conta = conta
        self.agencia = agencia
        self.digito = digito 