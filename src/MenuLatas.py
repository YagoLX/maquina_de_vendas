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
       
        maquina.set_bebida(bebida)

        print("Gostaria de quantas latas?")
        quantidade_cliente = int(input(":").replace(" ", ""))

        #checar estoque
        if quantidade_cliente > quantidade:
            print ("Não temos isso tudo :(, gostaria de outra bebida?")
            return "latas"

        #Passar para alguma função quanto o cliente pediu
        #maquina.set_quantidade_cliente(quantidade_cliente)

        #Cálculo do Preço
        preco = quantidade_cliente * maquina.get_preco_lata()
        

        print("CONFIRMAÇÃO PEDIDO")
        print("Você pediu ",quantidade_cliente, bebida)
        print("Ao todo ficou ",preco, "reais")
        print("Gostaria de proseguir para o pagamento?")
        print("[1] sim")
        print("[2] não")
        pagamento = int(input(":").replace(" ", ""))

        Valida = False
        while(not Valida):
                if (pagamento == 1):
                        invalida = False

                        #Alterar estoque
                        maquina.add_quantidade(bebida, -quantidade_cliente)
                        #Passar funcao para menu Pagamento
                        maquina.set_valor_pago(preco)
                        return "pagamento"
                        break

                elif (pagamento == 0):
                        
                        invalida = False
                        return "inicial"
                        break
                else: 
                        print("Opção Inválida")

                print("Gostaria de proseguir para o pagamento?")
                print("[1] sim")
                print("[2] não")
                pagamento = int(input(":").replace(" ", ""))




        return None
