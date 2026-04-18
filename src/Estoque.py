class  Estoque:
    #valor inteiro de gramas
    armazenamento_dosada = {"leite": 0, 
                             "cafe": 0,
                             "cha": 0,
                             "achocolatado": 0,
                             "lactobacilos": 0,
                            }
    
    #valor inteiro de latas
    armazenamento_lata = { "buzzcola": 0, #dos simpsons
                           "guarana" : 0,
                            "mineirinho": 0,
                            "brawndo": 0,  #do idiocracy
                            "suco": 0,
                            }
    
    #funcao auxiliar para padronizar strings de entrada
    def __ajustar_nome(self,nome):
        return (str(nome).replace(" ", "")).lower()
    
    #Verificar se a bebida é lata ou dosada
    def eh_lata(self, bebida):
        nome_bebida = self.__ajustar_nome(bebida)
        if nome_bebida in self.armazenamento_dosada:
            return True
        elif nome_bebida in self.armazenamento_dosada:
            return False
        else:
            print("ERRO: PRODUTO INVÁLIDO")
            return False
    
    #definir quantidade de determinada bebida
    def set_quantidade(self,bebida,quantidade):
        nome = self.__ajustar_nome(bebida)
        
        if nome in self.armazenamento_lata:
            self.armazenamento_lata[nome] = int(quantidade)

        elif nome in self.armazenamento_dosada:
            self.armazenamento_dosada[nome] = int(quantidade)

        else:
            print("Erro: bebida inválida na chamada da funcao set_quantidade")
    
    #soma quantidade a quantidade pré-existente do produto
    def add_quantidade(self,bebida,quantidade):
        nome = self.__ajustar_nome(bebida)
        
        if nome in self.armazenamento_lata:
            if self.armazenamento_lata[nome] + quantidade >= 0:
                self.armazenamento_lata[nome] += int(quantidade)
            else: print("Operacao inválida: a quantidade final deve ser não negativa")

        elif nome in self.armazenamento_dosada:
            if self.armazenamento_lata[nome] + quantidade >= 0:
                self.armazenamento_dosada[nome] += int(quantidade)
            else: print("Operacao inválida: a quantidade final deve ser não negativa")

        else:
            print("Erro: bebida inválida na chamada da funcao add_quantidade")
    
    #retorna quantidade do produto
    def get_quantidade(self, bebida):
        nome = self.__ajustar_nome(bebida)
        
        if nome in self.armazenamento_lata:
            return self.armazenamento_lata[nome]
        
        elif nome in self.armazenamento_dosada:
            return self.armazenamento_dosada[nome]
        else:
            print("Operação Inválida: Produto consultado não existe")

x = Estoque()
x.set_quantidade("leite", 10)
x.add_quantidade("buzzcola", 5)
print(str(x.armazenamento_dosada["leite"]) + ", " +str(x.armazenamento_lata["buzzcola"]))
y = x.get_quantidade('leite')
print(str(y))



