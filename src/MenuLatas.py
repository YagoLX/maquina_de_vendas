from Menu import Menu
from Maquina import Maquina


class MenuLatas(Menu):

    def rodar(self, maquina):
        print("Temos disponíveis as seguintes opções")
        print("[1] buzzcola")
        print("[2] guarana")
        print("[3] mineirinho")
        print("[4] brawndo")
        print("[5] suco")
        print("[6] voltar para menu inicial")   
        escolha = int(input(":").replace(" ", ""))

        print ("Você escolheu", escolha)

        if escolha == 1:
                bebida = "buzzcola"
        if escolha == 2:
                bebida = "guarana"
        if escolha == 3:
                bebida = "mineirinho"
        if escolha == 4:
                bebida = "brawndo"
        if escolha == 5:
                bebida = "suco"
        if escolha == 6:
                print (" ")
                print (" ")
                print (" ")
                print (" ")
                return "inicial"

        #Settar a quantidade de cada estoque deve ser feita no menu de ADM previamente!!!!
        maquina.set_quantidade(bebida, 10)
        quantidade = maquina.get_quantidade(bebida)

        #checar estoque
        if quantidade == 0:
            print ("Não temos essa opção, gostaria de outra bebida?")
            return "latas"
       
        print("Gostaria de quantas latas?")
        quantidade_cliente = int(input(":").replace(" ", ""))

        #checar estoque
        if quantidade_cliente > quantidade:
            print ("Não temos isso tudo :(, gostaria de outra bebida?")
            return "latas"

        print ("O preço total fica:", quantidade_cliente*maquina.preco_lata, "R$")

        print ("Qual forma de pagamento?")

        print ("Aproveite sua bebida :)")

        #Ajustar estoque e saldo

        maquina.saldo = maquina.saldo + quantidade_cliente*maquina.preco_lata
        maquina.add_quantidade(bebida, -quantidade_cliente)

        
        #Testes de saldo e quantidade estoque

        print (" ")
        print("---------Teste Máquina-------------")
        print ("Saldo final da máquina", maquina.saldo, "R$")
        print ("Estoque final de ",bebida, "foi de ",maquina.get_quantidade(bebida))


        return None
        


        #return entrada
