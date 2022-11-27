import copy
from Models.produccion import Produccion
from Models.transicion import Transicion


class Estado:
    id: int
    nombre: str
    equivalenteAlEstado: int | None
    producciones: list[ Produccion ]
    transiciones: list[ Transicion ]
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
                produccionesNoTerminal = self.control.obtenerProducciones(simboloSiguiente.contenido)

                # Solo tomar en cuenta las producciones que no estan
                # en el estado. Se comparan sus IDs.
                for produccionExterna in produccionesNoTerminal:
                    noTerminalExiste = False
                    for produccionEstado in self.producciones:
                        if produccionExterna.id == produccionEstado.id:
                            noTerminalExiste = True
                            break
                    if not noTerminalExiste:
                        self.producciones.append(copy.deepcopy(produccionExterna))

            # Si el simbolo siguiente es un terminal, se pasa a la siguiente produccion
            else:
                if posicionProduccionAnalizar == len(self.producciones) - 1:
                    posicionProduccionAnalizar = 0
                    break # Se terminaron de analizar todas las producciones

            posicionProduccionAnalizar += 1