from Models.control import Control
from View.grafica import Grafica


class Main:
    '''Ejecuta el programa'''
    control: Control
    grafica: Grafica = None
    listaNoTerminales: str
    listaTerminales: str
    listaProducciones: str

    def __init__(self) -> None:
        self.grafica = Grafica(self.comenzarPrograma)

    def comenzarPrograma(self):
        '''Se ejecuta el programa, obteniendo los valores desde 
        la interfaz gráfica'''
        self.listaNoTerminales = ''
        self.listaTerminales = ''
        self.listaProducciones = ''

        control = Control(self.listaNoTerminales,
                          self.listaTerminales, self.listaProducciones)

        return control.estados
