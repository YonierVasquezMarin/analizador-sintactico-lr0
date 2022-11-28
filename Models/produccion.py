from Models.simbolo import Simbolo
import copy

class Produccion:
    id: int
    noTerminal: str
    derivacion: list[Simbolo]
    produccionTransicionada: bool
    produccionRN: str | None
    __longitudDerivacion: int
    posicionPunto: int
    control = None

    def __init__(self, id: int, noTerminal: str, derivacion: str, control):
        self.id = id
        self.noTerminal = noTerminal
        self.derivacion = []
        self.produccionTransicionada = False
        self.produccionRN = None
        self.__longitudDerivacion = 0
        self.posicionPunto = 0
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
        if self.posicionPunto < self.__longitudDerivacion:
            return self.derivacion[self.posicionPunto]
        return None

    def marcarRN(self):
        '''
        Marca la produccion como una produccion de reduccion. Se escribe
        R0 ó R1 ó R2, etc... 
        '''
        self.produccionRN = 'R' + str(self.id)

    def moverPunto(self):
        '''
        Mueve el punto a la siguiente posicion de la derivacion.
        '''
        if self.posicionPunto != len(self.derivacion):
            # Sólo mueve el punto si éste no se encuentra al final de la derivación
            self.posicionPunto += 1

    def __str__(self):
        contenidoDerivacion = ''
        for simbolo in self.derivacion:
            contenidoDerivacion += simbolo.contenido

        return f'{self.noTerminal} -> {contenidoDerivacion}'
