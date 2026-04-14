class  Estoque:

    qualquer_coisa = 0
    _enum_size = 9
    _valor_inicial = 10
    armazenamento = []
    def __init__(self):
       
        for i in range (self._enum_size):
            self.armazenamento.append(self._valor_inicial)
        #print(self.armazenamento)

