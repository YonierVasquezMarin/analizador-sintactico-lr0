from Models.produccion import Produccion
from Models.transicion import Transicion


class Estado:
    id: int
    nombre: str
    equivalenteAlEstado: int | None
    conjuntoProducciones: list[ Produccion ]
    transiciones: list[ Transicion ]

    def __init__(self, id):
        self.id = id
        self.nombre = ""
        self.equivalenteAlEstado = None
        self.conjuntoProducciones = []
        self.transiciones = []