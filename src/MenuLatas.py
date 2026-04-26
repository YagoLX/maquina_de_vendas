from Menu import Menu
from Maquina import Maquina


class MenuLatas(Menu):

    def rodar(self, maquina):

        print (" ")
        print (" ")
        print (" ")
        print (" ")
        print("ESCOLHA SUA LATINHA")
        print("No momento temos disponível para sua bebida")
        tem_estoque ("buzzcola", maquina)
        tem_estoque ("guarana", maquina)
        tem_estoque ("mineirinho", maquina)
        tem_estoque ("brawndo", maquina)
        tem_estoque ("suco", maquina)

        print (" ")
        print (" ")
        print("Escolha sua bebida")
        print("[1] buzzcola")
        print("[2] guarana")
        print("[3] mineirinho")
        print("[4] brawndo")
        print("[5] suco")
        print("[6] voltar para menu inicial")   
        escolha = int(input(":").replace(" ", ""))


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

        #Cálculo do Preço
        preco = quantidade_cliente * maquina.get_preco_lata()
        
        print("CONFIRMAÇÃO PEDIDO")
        print("Você pediu",quantidade_cliente, bebida)
        print("Ao todo ficou ",preco, "reais")
        print("Gostaria de proseguir para o pagamento?")
        print("[1] sim")
        print("[0] não")
        pagamento = int(input(":").replace(" ", ""))

        Valida = False
        while(not Valida):
                if (pagamento == 1):
                        #Alterar estoque
                        maquina.add_quantidade(bebida, -quantidade_cliente)
                        #Passar funcao para menu Pagamento
                        maquina.set_valor_pago(preco)
                        maquina.salvar_tudo()
                        return "pagamento"
                        break

                elif (pagamento == 0):
                        print("Que pena, gostaria de mais algo?")
                        return "inicial"
                        break
                else: 
                        print("Opção Inválida")

                print("Gostaria de proseguir para o pagamento?")
                print("[1] sim")
                print("[0] não")
                pagamento = int(input(":").replace(" ", ""))


        return None

def tem_estoque (nome_bebida, maquina):
        qtdd = maquina.get_quantidade(nome_bebida)
        if qtdd == 0:
                print("Não temos", nome_bebida, ":(")

        else: print("Temos", qtdd, nome_bebida)