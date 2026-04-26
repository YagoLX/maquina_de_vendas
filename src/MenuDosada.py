from Menu import Menu

class MenuDosada(Menu):
    def rodar(self, maquina):
        
        #Guardar estoque inicial, para caso cancele voltar para a origem
        leite0 = maquina.get_quantidade("leite")
        cafe0 = maquina.get_quantidade("cafe")
        cha0 = maquina.get_quantidade("cha")
        achocolatado0 = maquina.get_quantidade("achocolatado")
        lactobacilos0 = maquina.get_quantidade("lactobacilos")


        preco = 0
        print("MONTE SUA BEBIDA")
        print("Selecione sua bebida e a sua dosagem")

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
                                                bebida = "leite"
                                        elif escolha == 2:
                                                bebida = "cafe"
                                        elif escolha == 3:
                                                bebida = "cha"
                                        elif escolha == 4:
                                                bebida = "achocolatado"
                                        elif escolha == 5:
                                                bebida = "lactobacilos"
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                                
                                        #Checar estoque
                                        quantidade = maquina.get_quantidade(bebida)

                                        if quantidade == 0:
                                                print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        
                                        maquina.set_bebida(bebida)
                                        #Aumentar preço
                                        preco += maquina.get_preco_dosada()

                                        #Alterar estoque
                                        quantidade_bebida = 10
                                        maquina.add_quantidade(bebida, quantidade_bebida)

                                        #Confirmar pedido
                                        print("CONFIRMAÇÃO PEDIDO")
                                        print("Você pediu uma bebida 100%", bebida)
                                        print("Gostaria de proseguir para o pagamento?")
                                        print("[1] sim")
                                        print("[2] não")
                                        pagamento = int(input(":").replace(" ", ""))
                                        
                                        if (pagamento == 1):
                                                return "pagamento"
                                                break
                                        #if (pagamento == 0) voltar helppp

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
                                        elif escolha1 == 2:
                                                bebida1 = "cafe"
                                        elif escolha1 == 3:
                                                bebida1 = "cha"
                                        elif escolha1 == 4:
                                                bebida1 = "achocolatado"
                                        elif escolha1 == 5:
                                                bebida1 = "lactobacilos"
                                        else:
                                                print("Escolha inválida, gostaria de outra bebida?")
                                                
                                        #Checar estoque
  
                                        quantidade = maquina.get_quantidade(bebida1)

                                        if quantidade == 0:
                                                print ("Não temos essa opção, gostaria de escolher outro sabor?")
                                        

                                        #Aumentar preço
                                        preco += maquina.get_preco_dosada()

                                        #Alterar estoque
                                        quantidade_bebida = 5
                                        maquina.add_quantidade(bebida, -quantidade_bebida)


                                        print("Escolha sua outra opção 50%")
                                        print("[1] leite")
                                        print("[2] cafe")
                                        print("[3] cha")
                                        print("[4] achocolatado")
                                        print("[5] lactobacilos")
                                        escolha2 = int(input(":").replace(" ", ""))

                                        if escolha2 == 1:
                                                bebida2 = "leite"
                                        elif escolha2 == 2:
                                                bebida2 = "cafe"
                                        elif escolha2 == 3:
                                                bebida2 = "cha"
                                        elif escolha2 == 4:
                                                bebida2 = "achocolatado"
                                        elif escolha2 == 5:
                                                bebida2 = "lactobacilos"
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
                                        elif escolha1 == 2:
                                                bebida1 = "cafe"
                                        elif escolha1 == 3:
                                                bebida1 = "cha"
                                        elif escolha1 == 4:
                                                bebida1 = "achocolatado"
                                        elif escolha1 == 5:
                                                bebida1 = "lactobacilos"
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
                                        elif escolha2 == 2:
                                                bebida2 = "cafe"
                                        elif escolha2 == 3:
                                                bebida2 = "cha"
                                        elif escolha2 == 4:
                                                bebida2 = "achocolatado"
                                        elif escolha2 == 5:
                                                bebida2 = "lactobacilos"
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









        #return entrada