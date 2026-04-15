from Estoque import Estoque

#equivalente ao conceito de blackboard
class Maquina:
    def __init__(self):
        self.estoque = Estoque()
        self.preco_lata = 10
        self.saldo = 0


