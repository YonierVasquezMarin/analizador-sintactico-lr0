from Models.estado import Estado
from Models.produccion import Produccion
from Models.simbolo import Simbolo


class Control:
    noTerminales: list[str]
    terminales: list[str]
    simbolos: list[Simbolo]
    producciones: list[Produccion]
    estados: list[Estado]

    def __init__(self, noTerminales: list[str], terminales: list[str], producciones: list[str]):
        self.noTerminales = noTerminales
        self.terminales = terminales
        self.simbolos = []
        self.producciones = []
        self.estados = []
        self.__cargarSimbolos()
        self.__cargarProducciones(producciones)
        self.__cargarEstados()

    def __cargarSimbolos(self):
        '''
        Crea una instancia de Simbolo para cada no terminal y terminal.
        El atributo 'tipo' de Simbolo puede ser 'noTerminal' o 'terminal'.
        '''
        indice = 0

        for noTerminal in self.noTerminales:
            self.simbolos.append(Simbolo(indice, 'noTerminal', noTerminal))
            indice += 1
        
        for terminal in self.terminales:
            self.simbolos.append(Simbolo(indice, 'terminal', terminal))
            indice += 1

    def __cargarProducciones(self, producciones: list[list[str]]):
        '''Crea una instancia de Produccion para cada produccion.'''
        for i in range(len(producciones)):
            self.producciones.append(Produccion(
                i, producciones[i][0], producciones[i][1], self))

    def obtenerProducciones(self, noTerminal: str):
        '''
        Devuelve una lista de Produccion correspondiente al no terminal
        pasado por parametro.
        '''
        producciones = []
        for produccion in self.producciones:
            if produccion.noTerminal == noTerminal:
                producciones.append(produccion)
        return producciones

    def obtenerSimbolo(self, contenido) -> Simbolo:
        '''
        Devuelve una instancia de Simbolo correspondiente al contenido
        pasado por parametro.
        '''
        for simbolo in self.simbolos:
            if simbolo.contenido == contenido:
                return simbolo
        raise Exception('Error: no se encontró el simbolo con contenido "', contenido, '"')

    def obtenerSimboloAPartirDeSuId(self, idSimbolo) -> Simbolo:
        '''
        Devuelve una instancia de Simbolo correspondiente al id
        pasado por parámetro
        '''
        for simbolo in self.simbolos:
            if simbolo.id == idSimbolo:
                return simbolo
        raise Exception(
            'Error: no se encontró el símbolo con id "', idSimbolo, '"')

    def __cargarEstados(self):
        '''Carga un estado inicial I0, y desde éste se crean los demás estados.'''

        # Crear el estado inicial I0
        self.estados.append(Estado(0, self))

        primerEstado = self.estados[0]

        # Pasar al estado I0 la primera produccion y cargar sus producciones internas
        primerEstado.producciones.append(self.producciones[0])
        primerEstado.cargarProduccionesFaltantes()

        # Cargar los demás estados
        primerEstado.crearEstadosYTransiciones()

        # Definir nombre para el primer estado
        primerEstado.nombre = 'I0'

    def crearEstado(self) -> Estado:
        '''Crea un nuevo estado y lo agrega a la lista de estados.'''
        idEstado = len(self.estados)
        estado = Estado(idEstado, self)
        self.estados.append(estado)
        return estado

    def obtenerEstado(self, idEstado) -> Estado:
        '''Retornar el estado solicitado'''
        estadoRetornar = None

        for estado in self.estados:
            if estado.id == idEstado:
                estadoRetornar = estado
                break

        return estadoRetornar

    def cantidadEstadosNoIgual(self) -> int:
        '''Retorna la cantidad de estados que no son iguales.'''
        cantidadEstadosNoIguales = 0
        for estado in self.estados:
            if estado.equivalenteAlEstado == None:
                cantidadEstadosNoIguales += 1 
        return cantidadEstadosNoIguales
