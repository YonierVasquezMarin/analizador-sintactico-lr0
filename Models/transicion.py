class Transicion:
    idSimbolo: int
    idEstadoDestino: int

    def __init__(self, idSimbolo, idEstadoDestino):
        self.idSimbolo = idSimbolo
        self.idEstadoDestino = idEstadoDestino