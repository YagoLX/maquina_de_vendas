from Estoque import Estoque 
from Maquina  import Maquina, ler_arquivo
from MenuAdm import MenuAdm
from MenuDosada import MenuDosada
from MenuInicial import MenuInicial
from MenuLatas import MenuLatas
from MenuPagamento import MenuPagamento 

maquina = Maquina()
ler_arquivo(maquina)

menus = {
    "inicial": MenuInicial,
    "latas": MenuLatas,
    "adm": MenuAdm,
    "dosada": MenuDosada,
    "pagamento":MenuPagamento,
}

menu_atual = menus["inicial"]()

while menu_atual != None:
    prox = menu_atual.rodar(maquina)
    if prox == None:
        break
    menu_atual = menus[prox]()

    



