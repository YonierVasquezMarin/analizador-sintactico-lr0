from Models.simbolo import Simbolo


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

    def __insertarPunto(self, derivacion, posicionPunto):
        '''
        Inserta el punto en la derivacion en la posicion indicada.
        '''
        derivacionConPunto = ''

        # Ir iterando la derivacion, y cuando coincide la posicion del punto
        # y el indice del caracter ahí se introduce primero el punto y luego el
        # caracter. Si al final de la iteracion no se ha introducido el punto,
        # se introduce al final de la derivacion.
        puntoAgregado = False
        for i in range(len(derivacion)):
            if i == posicionPunto:                  # Primero introducir el punto
                derivacionConPunto += '.'
                puntoAgregado = True
            derivacionConPunto += derivacion[i]     # Después agregar el caracter

        if not puntoAgregado:                       # Si no se ha agregado el punto, es porque va al final
            derivacionConPunto += '.'

        return derivacionConPunto

    def __str__(self):
        # Obtener solo la derivacion (sin el punto)
        contenidoDerivacion = ''
        for simboloDerivacion in self.derivacion:
            contenidoDerivacion += simboloDerivacion.contenido

        # Introducir el punto en el texto de la derivacion
        contenidoDerivacion = self.__insertarPunto(contenidoDerivacion, self.posicionPunto)

        # Si la produccion es RN se agrega su RN correspondiente a la derivacion
        if self.produccionRN is not None:
            contenidoDerivacion += f' [{self.produccionRN}]'
        
        return self.noTerminal + ' -> ' + contenidoDerivacion
