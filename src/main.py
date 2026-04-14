import interface.Menu
from componentes.Maquina import Maquina
from enum import Enum
from interface.ProdEnum import ProdEnum

maquina = Maquina()
print(maquina.qualquerr_coisa)
print(ProdEnum.LEITE.value)
print(ProdEnum.LEITE.name)
