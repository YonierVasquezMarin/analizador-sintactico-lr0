from Models.simbolo import Simbolo
import copy

class Produccion:
    id: int
    noTerminal: str
    derivacion: list[Simbolo]
    produccionTransicionada: bool
    produccionRN: str | None
    __longitudDerivacion: int
    __posicionPunto: int
    control = None

    def __init__(self, id: int, noTerminal: str, derivacion: str, control):
        self.id = id
        self.noTerminal = noTerminal
        self.derivacion = []
        self.produccionTransicionada = False
        self.produccionRN = None
        self.__longitudDerivacion = 0
        self.__posicionPunto = 0
        self.control = control
        self.__cargarSimbolosDerivacion(derivacion)

    def __cargarSimbolosDerivacion(self, derivacion: str):
        '''
        Por cada simbolo de la derivacion, se trae una instancia de
        ese simbolo correspondiente de la clase Main.
        '''
        noTerminales = self.control.noTerminales
        terminales = self.control.terminales

        try:
            for simbolo in derivacion:
                self.derivacion.append(self.control.obtenerSimbolo(simbolo))
        except Exception as e:
            print(e)


    def __str__(self):
        contenidoDerivacion = ''
        for simbolo in self.derivacion:
            contenidoDerivacion += simbolo.contenido

        return f'{self.noTerminal} -> {contenidoDerivacion}'
