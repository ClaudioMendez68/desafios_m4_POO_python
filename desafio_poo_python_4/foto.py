# Grupo 3: Lolett LLanquinao - Juan Torres - Leonardo Llaupe - Claudio Méndez

from error import Error, DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        try:
            if ancho >= 1 and ancho <= Foto.MAX:
                self.__ancho = ancho
            else:
                raise DimensionError(f'El ancho no puede ser mayor a {Foto.MAX}', ancho, Foto.MAX)
        except DimensionError as error:
            print(f'ERROR: {error.mensaje}')
    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        try:
            if alto >= 1 and alto <= Foto.MAX:
                self.__alto = alto
            else:
                raise DimensionError(f'El alto no puede ser mayor a {Foto.MAX}', alto, Foto.MAX)
        except DimensionError as error:
            print(f'ERROR: {error.mensaje}')

# TESTING
foto_1 = Foto(2000, 2000, 'https:// ...')
print(foto_1.ancho)
foto_1.ancho = 2300 
foto_1.alto = 2550

print(f'Ancho de la foto: {foto_1.ancho}')
print(f'Alto de la foto: {foto_1.alto}')