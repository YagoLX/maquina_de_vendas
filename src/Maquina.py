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

#Depois a inicializacao deve vir de um arquivo .txt ou .csv

    @classmethod
    def do_arquivo(self, caminho):
        with open(caminho) as arq:
            reader = csv.reader(arq)
            lista = list(reader)
            self.saldo = lista[0][0]
            self.nvendas = lista[0][1]

#Saldo - nao coloquei set_saldo porque nao faz sentido colocar um saldo na maquina, ela nao da troco.
    #retorna o saldo - menu adm
    def get_saldo(self):
        return self.saldo
    #adiciona o saldo - menu pagamento
    def add_saldo(self, value):
        self.saldo += value
    #zera o saldo - menu adm
    def sacar_saldo(self):
        aux = self.saldo
        self.saldo = 0
        return aux
    
#Numero de vendas
    #retorna o numero de vendas - menu adm
    def get_nvendas(self):
        return self.nvendas
    #adiciona o numero de vendas - menu pagamento
    def add_nvendas(self):
        self.nvendas += 1

    def salvar_tudo(self):
        ##escrever no csv
    
'''
to-do:
- Criar uma funcao que aumenta o saldo
- Criar uma funcao que manipula o estoque quando compra uma lata ou dosada a depender da posicao
- Criar uma funcao que faz o saque do saldo
- Criar tudo que yagao colocou na foto do gpo do matzao
- 
- Criar uma funcao que salva tudo no txt quando desligar a maquina   (final)

'''

