class Transicion:
    idSimbolo: int
    idEstadoDestino: int
    control = None

    def __init__(self, idSimbolo, idEstadoDestino, control):
        self.idSimbolo = idSimbolo
        self.idEstadoDestino = idEstadoDestino
        self.control = control
    
    def __str__(self) -> str:
        simbolo = self.control.obtenerSimboloAPartirDeSuId(self.idSimbolo)
        estadoDestino = self.control.obtenerEstado(self.idEstadoDestino)
        esEquivalenteAlEstado = estadoDestino.equivalenteAlEstado
        nombreEstado = ''
        
        # Si el estado destino es equivalente a otro, se debe mostrar el nombre del estado equivalente
        if esEquivalenteAlEstado != None:
            estadoEquivalente = self.control.obtenerEstado(estadoDestino.equivalenteAlEstado)
            nombreEstado = estadoEquivalente.nombre
        else:
            nombreEstado = estadoDestino.nombre

        return f'Transición de {simbolo.contenido} a {nombreEstado}'