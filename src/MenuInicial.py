from Menu import Menu

class MenuInicial(Menu):
    def rodar(self, maquina):
        #while(True){
        print("ola, entrou no rodar do inicial")
        print("Bem vindo a cafeteira 3000 ultraevolution"  )
        print(" ")
        print("Selecione uma opção!")
        print("[1] Monte sua própria bebida!")
        print("[2] Bebida em lata")
        print(" ")
        print("[0] Opção secreta - acesso administrativo")
        entrada = int(input(":").replace(" ", ""))

        if entrada == 1:
            return "dosada"
        
        if entrada == 2:
            return "lata"
        
        if entrada == 0:
            return "adm"
            
        #return entrada