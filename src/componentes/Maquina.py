from .Estoque import Estoque
from interface.Menu import Menu
from interface.MenuInicial import MenuIncial
import interface


class Maquina:
    qualquerr_coisa = 0
    def __init__(self):
        self.compras =  [] 
        self.estoque = Estoque()
        self.gerenciador = MenuIncial()


