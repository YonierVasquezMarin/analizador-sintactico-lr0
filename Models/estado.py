import copy
from Models.produccion import Produccion
from Models.transicion import Transicion


class Estado:
    id: int
    nombre: str
    equivalenteAlEstado: int | None
    producciones: list[Produccion]
    transiciones: list[Transicion]
    control: None

    def __init__(self, id, control):
        self.id = id
        self.nombre = ""
        self.equivalenteAlEstado = None
        self.producciones = []
        self.transiciones = []
        self.control = control

    def cargarProduccionesFaltantes(self):
        '''
        Revisa el simbolo despues del punto de cada produccion, y si es un no terminal
        se cargan las producciones de ese no terminal.
        '''
        posicionProduccionAnalizar = 0

        while True:
            # Ir probando cada produccion del estado
            produccionAnalizar = self.producciones[posicionProduccionAnalizar]
            simboloSiguiente = produccionAnalizar.simboloDelanteDelPunto()

            # Si el simbolo siguiente es un no terminal, se cargan sus producciones
            if simboloSiguiente.tipo == 'noTerminal':
                produccionesNoTerminal = self.control.obtenerProducciones(
                    simboloSiguiente.contenido)

                # Solo tomar en cuenta las producciones que no estan
                # en el estado. Se comparan sus IDs.
                for produccionExterna in produccionesNoTerminal:
                    noTerminalExiste = False
                    for produccionEstado in self.producciones:
                        if produccionExterna.id == produccionEstado.id:
                            noTerminalExiste = True
                            break
                    if not noTerminalExiste:
                        self.producciones.append(
                            copy.deepcopy(produccionExterna))

            # Si el simbolo siguiente es un terminal, se pasa a la siguiente produccion
            else:
                if posicionProduccionAnalizar == len(self.producciones) - 1:
                    posicionProduccionAnalizar = 0
                    break  # Se terminaron de analizar todas las producciones

            posicionProduccionAnalizar += 1

    def crearEstadosYTransiciones(self):
        '''
        Usando las producciones actuales del estado, por cada simbolo
        después del punto se crea un estado y una transicion.
        '''

        # Por cada produccion del estado se verifica el simbolo siguiente
        # y se crea un estado y una transicion si no existe
        for produccion in self.producciones:
            simboloSiguienteAlPunto = produccion.simboloDelanteDelPunto()

            if simboloSiguienteAlPunto != None:

                # Si no existe transicion con ese simbolo se crea un estado y
                # su correspondiente transicion
                if not self.existeTransicion(simboloSiguienteAlPunto):

                    # Obtener las producciones que tienen el punto antes del simbolo
                    produccionesConPuntoSimbolo = self.produccionesConPuntoSimbolo(
                        simboloSiguienteAlPunto)

                    # Crear nuevo estado y nueva transicoin
                    nuevoEstado: Estado = self.control.crearEstado()
                    idNuevoEstado = nuevoEstado.id
                    idSimboloSiguienteAlPunto = simboloSiguienteAlPunto.id
                    nuevaTransicion = Transicion(
                        idSimboloSiguienteAlPunto, idNuevoEstado)
                    self.transiciones.append(nuevaTransicion)

                    # Darle al nuevo estado las producciones que tienen el punto
                    # antes del simbolo
                    nuevoEstado.recibirProduccionesTransicion(
                        produccionesConPuntoSimbolo)

                    # Para el nuevo estado cargar las producciones internas faltantes
                    nuevoEstado.cargarProduccionesFaltantes()

                    # Comparar este estado con los demás estados
                    estadoEquivalente = nuevoEstado.compararConDemasEstados()
                    if estadoEquivalente != None: # si hay estado equivalente
                        nuevoEstado.nombre = self.generarNombreEstado()
                        nuevoEstado.crearEstadosYTransiciones()
                    else: # no hay estado equivalente
                        nuevoEstado.equivalenteAlEstado = estadoEquivalente.id
                        nuevoEstado.nombre = self.generarNombreEstado(estadoEquivalente.id)

            else:
                produccion.marcarRN()
                

    def existeTransicion(self, simbolo):
        '''
        Verifica si existe una transicion con el simbolo dado.
        '''
        for transicion in self.transiciones:
            if self.control.obtenerSimbolo(transicion.idSimbolo) == simbolo:
                return True
        return False

    def produccionesConPuntoSimbolo(self, simbolo) -> list[Produccion]:
        '''
        Devuelve las producciones que tienen el punto antes del simbolo dado.
        '''
        producciones = []
        for produccion in self.producciones:
            if produccion.simboloDelanteDelPunto() == simbolo:
                producciones.append(produccion)
        return producciones

    def recibirProduccionesTransicion(self, producciones):
        '''
        Recibe las producciones de una transicion, les mueve el punto
        a la derecha y las agrega al estado.
        '''
        for produccion in producciones:
            produccionEstadoAnterior = copy.deepcopy(produccion)
            produccionEstadoAnterior.moverPunto()
            self.producciones.append(produccionEstadoAnterior)

    def compararConDemasEstados(self):
        '''
        Compara las producciones del estado con las producciones de
        los demás estados, usando sus IDs. Adicional, las posiciones
        de los puntos deben ser diferentes.
        '''
        posicionEstadoComparar = 0
        estadoComparar = None

        while posicionEstadoComparar < len(self.control.estados):
            estadoComparar = self.control.estados[posicionEstadoComparar]
            posicionEstadoComparar += 1

            # Primero comparar la cantidad de producciones de ambos estados
            if len(self.producciones) != len(estadoComparar.producciones):
                break

            # Primero: comparar los ids de las producciones
            for i in range(len(self.producciones)):
                if self.producciones[i].id != estadoComparar.producciones[i].id:
                    estadoComparar = None
                    break

            # Segundo: comparar la posicion de sus puntos
            if estadoComparar != None:
                for i in range(len(self.producciones)):
                    if self.producciones[i].posicionPunto != estadoComparar.producciones[i].posicionPunto:
                        estadoComparar = None
                        break
        return estadoComparar

    def generarNombreEstado(self, idEstadoEquivalente: int | None) -> str:
        '''
        Si el parámetro "idEstadoEquivalente" es dado el nombre es "IGUAL A I{idEstado}".
        Si el parámetro no es dado, desde control se trae el indice del último estado válido.
        '''
        if idEstadoEquivalente != None:
            estadoEquivalente = self.control.obtenerEstado(idEstadoEquivalente)
            idEstadoEquivalente = estadoEquivalente.id
            return "IGUAL A I" + str(idEstadoEquivalente)
        else:
            cantidadEstadosNoIguales = self.control.cantidadEstadosNoIgual()
            return "I" + str(cantidadEstadosNoIguales)

    def __formatoProducciones(self) -> str:
        cadena = ''
        for produccion in self.producciones:
            cadena = cadena + produccion + '\n'
        return cadena

    def __formatoTransiciones(self) -> str:
        cadena = ''
        for transicion in self.transiciones:
            simbolo = self.control.obtenerSimboloAPartirDeSuId(
                transicion.idSimbolo)
            cadena = cadena + 'Transición a ' + simbolo.contenido + \
                ' a I-{transicion.idEstadoDestino}\n'
        return cadena

    def __str__(self):
        if self.equivalenteAlEstado is not None:
            return f'IGUAL A {self.equivalenteAlEstado}'
        return f'I-{self.id}\n{self.__formatoProducciones}\n{self.__formatoTransiciones}'
