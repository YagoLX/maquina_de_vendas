from Estoque import Estoque
import csv

#equivalente ao conceito de blackboard
class Maquina:
    def __init__(self):
        self.estoque = Estoque()
        self.preco_lata = 10
        self.preco_dosada = 5
        self.saldo = 0
        self.nvendas = 0

#Atualiza os dados da maquina com os dados do csv.
    def ler_arquivo(self):
        with open('Estoque.csv') as arq:
            reader = csv.reader(arq)
            lista = list(reader)
            self.saldo = lista[0][0]
            self.nvendas = lista[0][1]
            self.estoque = Estoque()
            self.preco_lata = 10
            self.preco_dosada = 5
            dosada = list(self.estoque.armazenamento_dosada)
            lata = list(self.estoque.armazenamento_lata)
            for i in range(5):
                self.estoque.armazenamento_dosada[dosada[i]] += int(lista[6][i])
                self.estoque.armazenamento_lata[lata[i]] += int(lista[i+1][0])  #tem que ter o shift por conta do csv

#Saldo - nao coloquei set_saldo porque nao faz sentido colocar um saldo na maquina, ela nao da troco.
    #adiciona o saldo - menu pagamento
    def add_saldo(self, value):
        self.saldo += value
    #retorna o saldo - menu adm
    def get_saldo(self):
        return self.saldo
    #zera o saldo - menu adm
    def sacar_saldo(self):
        aux = self.saldo
        self.saldo = 0
        print(f"voce sacou: {aux} reais")
    
#Numero de vendas
    #retorna o numero de vendas - menu adm
    def get_nvendas(self):
        return self.nvendas
    #adiciona o numero de vendas - menu pagamento
    def add_nvendas(self):
        self.nvendas += 1

#Funcao salvar - atualizar o csv com saldo, numero de vendas e estoque
    def salvar_tudo(self):
        with open('Estoque.csv') as arq:
            writer = csv.writer(arq)
            writer.writerow(0) = [self.saldo, self.nvendas]
            dosada = list(self.estoque.armazenamento_dosada)
            lata = list(self.estoque.armazenamento_lata)
            linha_dosada = []
            for i in range(5):
                linha_dosada.append(self.estoque.armazenamento_dosada[dosada[i]])
                writer.writerow(i+1) = self.estoque.armazenamento_lata[lata[i]]
            writer.writerow(5) = linha_dosada

        ##escrever no csv

#Quantidades
    def set_quantidade(self, bebida, quantidade):
        self.estoque.set_quantidade(bebida, quantidade)

    def get_quantidade(self, bebida):
        return self.estoque.get_quantidade(bebida)

    def add_quantidade(self,bebida,quantidade):
        self.estoque.add_quantidade(bebida,quantidade)
    
