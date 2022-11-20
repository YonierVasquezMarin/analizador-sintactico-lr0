from Models.estado import Estado
from Models.produccion import Produccion
from Models.simbolo import Simbolo


class Main:
    simbolos: list[ Simbolo ]
    producciones: list[ Produccion ]
    estados: list[ Estado ]

    def __init__(self, noTerminales, terminales, producciones):
        self.simbolos = []
        self.producciones = []
        self.estados = []