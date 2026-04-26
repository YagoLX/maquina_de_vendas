from Menu import Menu
from Maquina import Maquina
from Estoque import Estoque

class MenuDosada(Menu):
    def rodar(self, maquina):
        

        preco = 0
        print (" ")
        print (" ")
        print (" ")
        print("MONTE SUA BEBIDA")
        print("No momento temos disponível para sua bebida")
        intervalo_permitido_bebida("LEITE", maquina)
        intervalo_permitido_bebida("CAFE", maquina)
        intervalo_permitido_bebida("CHA", maquina)
        intervalo_permitido_bebida("ACHOCOLATADO", maquina)
        intervalo_permitido_bebida("LACTOBACILOS", maquina)
        print("-----------------")
        print("Selecione sua bebida e a sua dosagem")
        
        
        #Vão contabilizar quanto o cliente colocou
        contador_leite = 0
        contador_cafe =0 
        contador_cha = 0
        contador_achocolatado = 0
        contador_lactobacilos = 0

        #Início pedido
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
                        bebida = "leite"

                elif escolha == 2:
                        contador_cafe += 10
                        bebida = "cafe"

                elif escolha == 3:
                        contador_cha +=10
                        bebida = "cha"

                elif escolha == 4:
                        contador_achocolatado += 10
                        bebida = "achocolatado"
                        
                elif escolha == 5:
                        contador_lactobacilos +=10
                        bebida = "lactobacilos"
                else:
                        print("Escolha inválida, gostaria de outra bebida?")
                        return "inicial"
                
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
                        


        #CONFERÊNCIA GERAL ESTOQUE
        contador = [(contador_leite, "LEITE"), (contador_cafe, "CAFE"), (contador_cha, "CHA"), (contador_achocolatado, "ACHOCOLATADO"), (contador_lactobacilos, "LACTOBACILOS")]

        print("Confirmação pedido")
        for (pedido, bebida) in contador:
                if pedido != 0:
                        max =  maquina.get_quantidade(bebida)
                        if pedido > max:
                               print("Você pediu algo fora de estoque, gostaria de outra bebida?") 
                               return "inicial"
                        else:
                                print (pedido*10,"%", bebida)
        
        preco = maquina.get_preco_dosada()   
        print("Ao todo ficou",preco, "reais")

        #CONFIRMAÇÃO PAGAMENTO
        print("Gostaria de proseguir para o pagamento?")
        print("[1] sim")
        print("[0] não")
        pagamento = int(input(":").replace(" ", ""))

        if pagamento == 1:
                for (pedido, bebida) in contador:
                        maquina.add_quantidade (bebida, -pedido) 
    
                maquina.set_valor_pago (preco)  
                maquina.salvar_tudo()
                return "pagamento"  
        else:
                print("Que pena, gostaria de mais algo?")
                return "inicial"

        
#verificar se a bebida ta disponivel de 0, 30%, 50%, 70% ou 100%
def intervalo_permitido_bebida(nome_bebida, maquina):
        qtdd = maquina.get_quantidade(nome_bebida)
        if qtdd < 3:
                print("Não temos", nome_bebida, "em estoque :(")
        elif qtdd < 5:
                print("Temos", nome_bebida + " a 30%")
        elif qtdd < 7:
                print("Temos", nome_bebida + " a 50%")
        elif qtdd< 10:
                print("Temos", nome_bebida + " a 70%") 

        else: print("Temos", nome_bebida, "a vontade :)")
