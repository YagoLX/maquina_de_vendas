from Menu import Menu
from Maquina import Maquina
from Estoque import Estoque

class MenuDosada(Menu):
    def rodar(self, maquina):
        
        #Guardar estoque inicial, para caso cancele voltar para a origem
        leite0 = maquina.get_quantidade("leite")
        cafe0 = maquina.get_quantidade("cafe")
        cha0 = maquina.get_quantidade("cha")
        achocolatado0 = maquina.get_quantidade("achocolatado")
        lactobacilos0 = maquina.get_quantidade("lactobacilos")
        maquina = Maquina()

        preco = 0
        print("MONTE SUA BEBIDA")
        print("No momento temos disponível para sua bebida")
        intervalo_permitido_bebida("LEITE", maquina)
        intervalo_permitido_bebida("CAFE", maquina)
        intervalo_permitido_bebida("CHA", maquina)
        intervalo_permitido_bebida("ACHOCOLATADO", maquina)
        intervalo_permitido_bebida("LACTOBACILOS", maquina)
        print("Selecione sua bebida e a sua dosagem")
        contador_leite = 0
        contador_cafe =0 
        contador_cha = 0
        contador_achocolatado = 0
        contador_lactobacilos = 0

        #bebida comeca vazia
        bebida = []
        #gramatura de cada opcao escolhida
        #Lógica vários pedidos
        #Armazenar cada pedido em um vetor de pedidos e ir somando. Ao final printar tudo
        Terminou = False
        #Loop grandão para fazer todos os pedidos


        #Para cada escolha de dosagem, um if diferente (bronco eu sei)
        #Não fiz as validações para entradas inválidas help!!!
        while(not Terminou):
                print("Você tem 3 opções de dosagem")
                print("[1] 100%")
                print("[2] 50% 50%")
                print("[3] 30% 70%")
                dosagem = int(input(":").replace(" ", ""))

                if (dosagem == 1):
                                        print("Escolha sua opção 100%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha = int(input(":").replace(" ", ""))

                                        if escolha == 1:
                                                contador_leite +=10
                                                #bebida = "leite"

                                        elif escolha == 2:
                                                contador_cafe += 10
                                                #bebida = "cafe"

                                        elif escolha == 3:
                                                contador_cha +=10
                                               #bebida = "cha"

                                        elif escolha == 4:
                                                contador_achocolatado += 10
                                                #bebida = "achocolatado"
                                                
                                        elif escolha == 5:
                                                contador_lactobacilos +=10
                                                #bebida = "lactobacilos"
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                        # Conferir no fim usando a funcao qtdd_bebida_valida(nome_bebida, contador, maquina)
                                        
                                        #Checar estoque
                                        #quantidade = maquina.get_quantidade(bebida[0])

                                        
                                        # if quantidade <10:
                                        #         print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        # else:
                                        #         maquina.set_bebida(bebida)
                                        #         #Aumentar preço
                                        #         preco += maquina.get_preco_dosada()

                                        #          #Alterar estoque
                                        #          #quantidade_bebida = 10
                                        #         #maquina.add_quantidade(bebida, quantidade_bebida)

                                        #         #Confirmar pedido
                                        #         print("CONFIRMAÇÃO PEDIDO")
                                        #         print("Você pediu uma bebida 100%", bebida)
                                        #         print("Gostaria de proseguir para o pagamento?")
                                        #         print("[1] sim")
                                        #         print("[2] não")
                                        #         pagamento = int(input(":").replace(" ", ""))
                                        
                                        #         if (pagamento == 1):
                                        #                 return "pagamento"
                                        #                 break
                                        #         #if (pagamento == 0) voltar helppp

                elif (dosagem == 2):

                                        print("Escolha sua opção 50%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha1 = int(input(":").replace(" ", ""))

                                        if escolha1 == 1:
                                                bebida1 = "leite"
                                                contador_leite += 5
                                        elif escolha1 == 2:
                                                bebida1 = "cafe"
                                                contador_cafe +=5
                                        elif escolha1 == 3:
                                                bebida1 = "cha"
                                                contador_cha += 5
                                        elif escolha1 == 4:
                                                bebida1 = "achocolatado"
                                                contador_achocolatado += 5
                                        elif escolha1 == 5:
                                                bebida1 = "lactobacilos"
                                                contador_lactobacilos +=5
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")

                                        # Conferir no fim usando a funcao qtdd_bebida_valida(nome_bebida, contador, maquina)    
                                        # #Checar estoque
  
                                        # quantidade = maquina.get_quantidade(bebida1)

                                        # if quantidade == 0:
                                        #         print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        

                                        # #Aumentar preço
                                        # preco += maquina.get_preco_dosada()

                                        # #Alterar estoque
                                        # quantidade_bebida = 5
                                        # maquina.add_quantidade(bebida, -quantidade_bebida)


                                        print("Escolha sua outra opção 50%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha2 = int(input(":").replace(" ", ""))

                                        if escolha2 == 1:
                                                bebida2 = "leite"
                                                contador_leite += 5
                                        elif escolha2 == 2:
                                                bebida2 = "cafe"
                                                contador_cafe  += 5
                                        elif escolha2 == 3:
                                                bebida2 = "cha"
                                                contador_cha  += 5
                                        elif escolha2 == 4:
                                                bebida2 = "achocolatado"
                                                contador_achocolatado  += 5
                                        elif escolha2 == 5:
                                                bebida2 = "lactobacilos"
                                                contador_lactobacilos += 5
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                                
                                        #Checar estoque
  
                                        quantidade = maquina.get_quantidade(bebida2)

                                        if quantidade == 0:
                                                print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        

                                        #Aumentar preço
                                        preco += maquina.get_preco_dosada()

                                        #Alterar estoque
                                        quantidade_bebida = 5
                                        maquina.add_quantidade(bebida2, -quantidade_bebida)


                                        #Confirmação
                                        print("CONFIRMAÇÃO PEDIDO")
                                        print("Você pediu uma bebida 50%", bebida1, " e 50%", bebida2)
                                        print("Gostaria de proseguir para o pagamento?")
                                        print("[1] sim")
                                        print("[2] não")
                                        pagamento = int(input(":").replace(" ", ""))
                                        
                                        if (pagamento == 1):
                                                return "pagamento"
                                                break

                else: 
                                        print("Escolha sua opção 30%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha1 = int(input(":").replace(" ", ""))

                                        if escolha1 == 1:
                                                bebida1 = "leite"
                                                contador_leite += 3
                                        elif escolha1 == 2:
                                                bebida1 = "cafe"
                                                contador_cafe +=3
                                        elif escolha1 == 3:
                                                bebida1 = "cha"
                                                contador_cha += 3
                                        elif escolha1 == 4:
                                                bebida1 = "achocolatado"
                                                contador_achocolatado += 3
                                        elif escolha1 == 5:
                                                bebida1 = "lactobacilos"
                                                contador_lactobacilos += 3
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                                
                                        #Checar estoque
                                        quantidade = maquina.get_quantidade(bebida1)

                                        if quantidade == 0:
                                                print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        
                                        #Aumentar preço
                                        preco += maquina.get_preco_dosada()

                                        #Alterar estoque
                                        quantidade_bebida = 3
                                        maquina.add_quantidade(bebida, -quantidade_bebida)

                                        print("Escolha sua outra opção 70%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha2 = int(input(":").replace(" ", ""))

                                        if escolha2 == 1:
                                                bebida2 = "leite"
                                                contador_leite += 7
                                        elif escolha2 == 2:
                                                bebida2 = "cafe"
                                                contador_cafe += 7
                                        elif escolha2 == 3:
                                                bebida2 = "cha"
                                                contador_cha +=7
                                        elif escolha2 == 4:
                                                bebida2 = "achocolatado"
                                                contador_achocolatado += 7
                                        elif escolha2 == 5:
                                                bebida2 = "lactobacilos"
                                                contador_lactobacilos +=7
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                                
                                        #Checar estoque
  
                                        quantidade = maquina.get_quantidade(bebida2)

                                        if quantidade == 0:
                                                print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        
                                        maquina.set_bebida(bebida2)
                                        #Aumentar preço
                                        preco += maquina.get_preco_dosada()

                                        #Alterar estoque
                                        quantidade_bebida = 7
                                        maquina.add_quantidade(bebida2, -quantidade_bebida)


                                        #Confirmar pedido
                                        print("CONFIRMAÇÃO PEDIDO")
                                        print("Você pediu uma bebida 30%", bebida1, " e 70%", bebida2)
                                        print("Gostaria de proseguir para o pagamento?")
                                        print("[1] sim")
                                        print("[2] não")
                                        pagamento = int(input(":").replace(" ", ""))
                                        
                                        if (pagamento == 1):
                                                return "pagamento"
                                                break

       
                        
                return None
#verificar se a bebida ta disponivel de 0, 30%, 50%, 70% ou 100%
def intervalo_permitido_bebida(nome_bebida, maquina):
        qtdd = maquina.get_quantidade(nome)
        if qtdd < 3:
                print(nome_bebida + ": 0%")
        elif qtdd < 5:
                print(nome_bebida + ": 30%")
        elif qtdd < 7:
                print(nome_bebida + ": 50%")
        elif qtdd< 10:
                print(nome_bebida + ": 70%") 
        else: print(nome_bebida + ": 100%")

def qtdd_bebida_valida(nome_bebida, contador, maquina):
        if contador == 0:
                return True
        else:
                max =  maquina.get_quantidade(nome_bebida)
                if contador<=max:
                        return True
                else: return False