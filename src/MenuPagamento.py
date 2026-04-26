from Maquina import Maquina
from Menu import Menu

class MenuPagamento(Menu):
    def rodar(self, maquina):
        print("voce entrou no menu pagamento")
        print(" ")
        print("Valor a ser pago:", maquina.get_valor_pago())
        print("Qual a forma de pagamento?")
        print("[1] Credito")
        print("[2] Debito")
        print("[3] Pix")
        print("[4] Dinheiro")
        escolha = int(input(":").replace(" ", ""))

        if escolha == 1:
           maquina.add_saldo(maquina.get_valor_pago())
        elif escolha == 2:
            maquina.add_saldo(maquina.get_valor_pago())
        elif escolha == 3:
            maquina.add_saldo(maquina.get_valor_pago())
        elif escolha == 4:
            maquina.add_saldo(maquina.get_valor_pago())
        else:
            print("Escolha inválida")

        print("Obrigado por utilizar o programa :)")
        maquina.salvar_tudo()
        return None