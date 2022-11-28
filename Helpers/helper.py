class Helper:
    listaNoTerminales: list[str]
    listaTerminales: list[str]
    listaProducciones: list[str]

    def __init__(self, cadenaNoTerminales: str, cadenaTerminales: str, cadenaProducciones: str) -> None:
        self.prepararListas(cadenaProducciones,
                            cadenaNoTerminales, cadenaNoTerminales)

    def __prepararListaNoTerminales(self, cadenaNoTerminales: str) -> list[str]:
        listaNoTerminales = []
        listaNoTerminal = cadenaNoTerminales.split(",")
        for noTerminal in listaNoTerminal:
            listaNoTerminales.append(noTerminal.strip())
        return listaNoTerminales

    def __prepararListaTerminales(self, cadenaTerminales: str) -> list[str]:
        listaTerminales = []
        listaTerminal = cadenaTerminales.split(",")
        for terminal in listaTerminal:
            listaTerminales.append(terminal.strip())
        return listaTerminales

    def __prepararListaProducciones(self, cadenaProducciones: str) -> list[str]:
        # Definir listas para las producciones
        listaProducciones = []
        separador = '\n'
        listaProducciones1 = cadenaProducciones.split(separador)
        produccionExtender = self.__retornarProducciones(listaProducciones1)
        if len(produccionExtender[0][1]) > 1:
            noTerminal = produccionExtender[0][0]
            if noTerminal in self.listaNoTerminales:
                produccionExtender.insert(0, ['Z', noTerminal])
        return produccionExtender

    def __retornarProducciones(self, listaProducciones1: list[str]) -> list():
        produccion = []
        for producciones in listaProducciones1:
            inicio = producciones.split("->")
            if "|" in producciones:
                derivacion = inicio[1].split("|")
                for i in derivacion:
                    produccion.append([inicio[0].strip(), i.strip()])
            else:
                # strip para cada item interno
                inicio = [inicio[0].strip(), inicio[1].strip()]
                produccion.append(inicio)
        return produccion

    def prepararListas(self, cadenaProducciones: str, cadenaTerminales: str, cadenaNoTerminales: str) -> None:
        self.listaNoTerminales = self.__prepararListaNoTerminales(
            cadenaNoTerminales)
        self.listaTerminales = self.__prepararListaTerminales(cadenaTerminales)
        self.listaProducciones = self.__prepararListaProducciones(
            cadenaProducciones)
