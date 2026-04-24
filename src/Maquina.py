from Estoque import Estoque

#equivalente ao conceito de blackboard
class Maquina:
    def __init__(self):
        self.estoque = Estoque()
        self.preco_lata = 10
        self.saldo = 0

    def set_quantidade (self, bebida, quantidade):
        self.estoque.set_quantidade(bebida, quantidade)

    def get_quantidade(self, bebida):
        return self.estoque.get_quantidade(bebida)

    def add_quantidade(self,bebida,quantidade):
        self.estoque.add_quantidade(bebida,quantidade)
    


