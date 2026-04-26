from Estoque import Estoque
import csv

#equivalente ao conceito de blackboard
class Maquina:
    def __init__(self):
        self.__estoque = Estoque()
        self.__preco_lata = 10
        self.__preco_dosada = 5
        self.__saldo = 0
        self.__nvendas = 0
        self.__quantidade_cliente = 0
        self.__bebida = "vazio"

#Atualiza os dados da maquina com os dados do csv.
    def ler_arquivo(self):
        with open('Estoque.csv') as arq:
            reader = csv.reader(arq)
            lista = list(reader)
            self.saldo = int(lista[0][0])
            self.__nvendas = int(lista[0][1])
            self.__estoque = Estoque()
            self.__preco_lata = 10
            self.__preco_dosada = 5
            dosada = list(self.__estoque.armazenamento_dosada)
            lata = list(self.__estoque.armazenamento_lata)
            for i in range(5):
                self.__estoque.armazenamento_dosada[dosada[i]] += int(lista[6][i])
                self.__estoque.armazenamento_lata[lata[i]] += int(lista[i+1][0])  #tem que ter o shift por conta do csv

#Saldo - nao coloquei set_saldo porque nao faz sentido colocar um saldo na maquina, ela nao da troco.
    #adiciona o saldo - menu pagamento
    def add_saldo(self, value):
        self.__saldo += value
    #retorna o saldo - menu adm
    def get_saldo(self):
        return self.__saldo
    #zera o saldo - menu adm
    def sacar_saldo(self):
        aux = self.__saldo
        self.__saldo = 0
        print(f"voce sacou: {aux} reais")
    
#Numero de vendas
    #retorna o numero de vendas - menu adm
    def get_nvendas(self):
        return self.__nvendas
    #adiciona o numero de vendas - menu pagamento
    def add_nvendas(self):
        self.__nvendas += 1

#Funcao salvar - atualizar o csv com saldo, numero de vendas e estoque
    def salvar_tudo(self):
        with open('Estoque.csv', 'w') as arq:
            writer = csv.writer(arq)
            writer.writerow([self.__saldo, self.__nvendas,'','',''])
            dosada = list(self.__estoque.armazenamento_dosada)
            lata = list(self.__estoque.armazenamento_lata)
            linha_dosada = []
            for i in range(5):
                linha_dosada.append(self.__estoque.armazenamento_dosada[dosada[i]])
                aux = [self.__estoque.armazenamento_lata[lata[i]],'','','','']
                writer.writerow(aux)
            writer.writerow(linha_dosada)

#Quantidades
    def set_quantidade(self, bebida, quantidade):
        self.__estoque.set_quantidade(bebida, quantidade)

    def get_quantidade(self, bebida):
        return self.__estoque.get_quantidade(bebida)

    def add_quantidade(self,bebida,quantidade):
        self.__estoque.add_quantidade(bebida,quantidade)
     
    def get_quantidade_cliente(self):
        return self.quantidade_cliente
    
    def set_quantidade_cliente(self, quantidade_cliente):
        self.quantidade_cliente = quantidade_cliente

    def get_bebida (self):
        return self.bebida

    def set_bebida (self, bebida):
        self.bebida = bebida

    def eh_lata (self, bebida):
        return self.estoque.eh_lata(bebida)

    def set_preco_lata(self, preco_lata):
        self.preco_lata = preco_lata

    def get_preco_lata(self):
        return self.preco_lata

    def set_preco_dosada(self, preco_dosada):
        self.preco_dosada = preco_dosada

    def get_preco_dosada(self):
        return self.preco_dosada