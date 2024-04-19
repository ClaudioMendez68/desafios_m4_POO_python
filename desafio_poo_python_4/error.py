# Grupo 3: Lolett LLanquinao - Juan Torres - Leonardo Llaupe - Claudio Méndez

class Error(Exception):
    pass

class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        
    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            return self.mensaje

