from Models.control import Control
from View.grafica import Grafica
from Helpers.helper import Helper


class Main:
    '''Ejecuta el programa'''
    control: Control
    grafica: Grafica = None

    def __init__(self) -> None:
        self.grafica = Grafica(self.comenzarPrograma)

    def comenzarPrograma(self, listaNoTerminales, listaTerminales, listaProducciones):
        '''Se ejecuta el programa, obteniendo los valores desde 
        la interfaz gráfica'''
        helper = Helper(listaNoTerminales, listaTerminales, listaProducciones)

        control = Control(helper.listaNoTerminales,
                          helper.listaTerminales, helper.listaProducciones)
        return control.estados


main = Main()
