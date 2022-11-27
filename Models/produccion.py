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
        self.__cargarLongitudDerivacion()

    def __cargarSimbolosDerivacion(self, derivacion: str):
        '''
        Por cada caracter de la derivacion, se trae una instancia de
        ese simbolo correspondiente de la clase Main.
        '''
        try:
            for simbolo in derivacion:
                self.derivacion.append(self.control.obtenerSimbolo(simbolo))
        except Exception as e:
            print(e)

    def __cargarLongitudDerivacion(self):
        self.__longitudDerivacion = len(self.derivacion)

    def simboloDelanteDelPunto(self) -> Simbolo | None:
        '''
        Devuelve el simbolo que se encuentra delante del punto.
        Si no hay simbolo delante del punto, devuelve None.
        '''
        if self.__posicionPunto < self.__longitudDerivacion:
            return self.derivacion[self.__posicionPunto]
        return None

    def __str__(self):
        contenidoDerivacion = ''
        for simbolo in self.derivacion:
            contenidoDerivacion += simbolo.contenido

        return f'{self.noTerminal} -> {contenidoDerivacion}'
