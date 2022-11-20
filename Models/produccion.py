from Models.simbolo import Simbolo
from Models.main import Main


class Produccion:
    id: int
    noTerminal: str
    derivacion: list[Simbolo]
    produccionTransicionada: bool
    produccionRN: str | None
    __longitudDerivacion: int
    __posicionPunto: int
    main: Main

    def __init__(self, id, noTerminal, derivacion, main):
        self.id = id
        self.noTerminal = noTerminal
        self.derivacion = derivacion
        self.produccionTransicionada = False
        self.produccionRN = None
        self.__longitudDerivacion = len(derivacion)
        self.__posicionPunto = 0
        self.main = main

    
