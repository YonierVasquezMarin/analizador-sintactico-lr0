class Simbolo:
    '''
    * tipo: terminal o no terminal
    '''

    id: int
    tipo: str
    contenido: str

    def __init__(self, id: int, tipo: str, contenido: str):
        self.id = id
        self.tipo = tipo
        self.contenido = contenido