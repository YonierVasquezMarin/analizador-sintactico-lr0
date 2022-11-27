from Models.estado import Estado
from Models.produccion import Produccion
from Models.simbolo import Simbolo


class Control:
    noTerminales: list[ str ]
    terminales: list[ str ]
    simbolos: list[ Simbolo ]
    producciones: list[ Produccion ]
    estados: list[ Estado ]
    control = None

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
        for i in range(len(self.noTerminales)):
            self.simbolos.append(Simbolo(i, 'noTerminal', self.noTerminales[i]))

        for i in range(len(self.terminales)):
            self.simbolos.append(Simbolo(i, 'terminal', self.terminales[i]))

    def __cargarProducciones(self, producciones: list[list[str]]):
        '''Crea una instancia de Produccion para cada produccion.'''
        for i in range(len(producciones)):
            self.producciones.append(Produccion(i, producciones[i][0], producciones[i][1], self))

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

    def obtenerSimbolo(self, contenido) -> Simbolo : 
        '''
        Devuelve una instancia de Simbolo correspondiente al contenido
        pasado por parametro.
        '''
        for simbolo in self.simbolos:
            if simbolo.contenido == contenido:
                return simbolo
        raise Exception('Error: no se encontró el simbolo con contenido "', contenido, '"')

    def __cargarEstados(self):
        '''Carga un estado inicial I0, y desde éste se crean los demás estados.'''

        # Creo el estado inicial I0
        self.estados.append(Estado(0, self))

        # Pasar al estado I0 la primera produccion, y desde éste se crean los demás estados.
        self.estados[0].producciones.append(self.producciones[0])
        self.estados[0].cargarProduccionesFaltantes()