from Menu import Menu

class MenuDosada(Menu):
    def rodar(self, maquina):
        

        print("MONTE SUA BEBIDA")
        print("Selecione sua bebida e a sua dosagem")



        print("Temos disponíveis as seguintes opções")
        print("[1] leite")
        print("[2] cafe")
        print("[3] cha")
        print("[4] achocolatado")
        print("[5] lactobacilos")
        print("[6] voltar para menu inicial")
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
        elif escolha == 6:
                print (" ")
                print (" ")
                print (" ")
                print (" ")
                return "inicial"
        else:
                print("Escolha inválida, gostaria de outra bebida?")
                return ("dosada")

        maquina.set_quantidade(bebida, 10)
        quantidade = maquina.get_quantidade(bebida)











        return None
            
        #return entrada