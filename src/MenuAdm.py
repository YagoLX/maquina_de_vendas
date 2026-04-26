from Menu import Menu

class MenuAdm(Menu):
    def rodar(self, maquina):
        print("ENTROU NO MENU ADM")
        print("Saldo total da maquina: ",maquina.saldo)
        print(" ")
        print("Temos disponíveis as seguintes opções")
        print("[1] Definir o preco das latas")
        print("[2] Definir o preco das bebidas dosadas")
        print("[3] Adicionar latas a maquina")
        print("[4] Adicionar bebidas dosadas a maquina")
        print("[5] Sacar saldo")
        print("[6] voltar para menu inicial")
        escolha = int(input(":").replace(" ", ""))

        if escolha == 1:
            print("Defina o preco das latas: ")
            preco_lata = int(input(":").replace(" ", ""))
            maquina.set_preco_lata(preco_lata)
            return "inicial"
        elif escolha == 2:
            print("Defina o preco das bebidas dosadas: ")
            preco_dosada = int(input(":").replace(" ", ""))
            maquina.set_preco_lata(preco_dosada)
            return "incial"
        elif escolha == 3:
            print("Qual lata quer adicionar na maquina: ")
            print("[1] buzzcola")
            print("[2] guarana")
            print("[3] mineirinho")
            print("[4] brawndo")
            print("[5] suco")
            while True:
                escolha = int(input(":").replace(" ", ""))

                if escolha == 1:
                    bebida = "buzzcola"
                    break
                if escolha == 2:
                    bebida = "guarana"
                    break
                if escolha == 3:
                    bebida = "mineirinho"
                    break
                if escolha == 4:
                    bebida = "brawndo"
                    break
                if escolha == 5:
                    bebida = "suco"
                    break
                else:
                    print("Valor inválido, tente novamente")
            print("Quanto quer adicionar na maquina?")
            quantidade_extra = int(input(":").replace(" ", ""))
            maquina.add_quantidade(bebida, quantidade_extra)
        elif escolha == 4:
            print("Qual bebida quer adicionar na maquina: ")
            print("[1] leite")
            print("[2] cafe")
            print("[3] cha")
            print("[4] achocolatado")
            print("[5] lactobacilos")
            while True:
                escolha = int(input(":").replace(" ", ""))

                if escolha == 1:
                    bebida = "leite"
                    break
                elif escolha == 2:
                    bebida = "cafe"
                    break
                elif escolha == 3:
                    bebida = "cha"
                    break
                elif escolha == 4:
                    bebida = "achocolatado"
                    break
                elif escolha == 5:
                    bebida = "lactobacilos"
                    break
                else:
                    print("Valor inválido, tente novamente")
            print("Quanto em gramas quer adicionar na maquina?")
            quantidade_extra = int(input(":").replace(" ", ""))
            maquina.add_quantidade(bebida, quantidade_extra)
        elif escolha == 5:
            maquina.sacar_saldo()
            print("Obrigado por utilizar o programa :)")
        elif escolha == 6:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            return "inicial"
        else:
            print("Escolha inválida")
            return "MenuAdm"

        maquina.salvar_tudo()
        return None
        #return entrada