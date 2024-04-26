# En un archivo campania.py, definir la clase que permita crear instancias de tipo Campania.
from datetime import date
from error import LargoExcedidoException
from anuncio import Video, Display, Social

class Campania():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino    
        # Puede usar en el constructor un parámetro estructura de datos para crear cada instancia de Anuncio
        self.__anuncios = [self.instancias_anuncios(anuncio) for anuncio in anuncios]

    # Usar en el constructor un parámetro estructura de datos. Puede refactorizar esta lógica en un método
    def instancias_anuncios(self, anuncio: dict):
        if isinstance(anuncio, Video):
            return anuncio
        elif isinstance(anuncio, Display):
            return anuncio
        elif isinstance(anuncio, Social):
            return anuncio

    # GETTERS
    @property
    def vidweo(self):
        return self.__video
    @property
    def nombre(self):
        return self.__nombre
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    # SETTERS
    # Se le solicita solamente crear el método getter para el atributo 'anuncios', sin crear su setter
    @nombre.setter
    def nombre(self, nombre):
    # Modificar el nombre de una campaña debe validarse que no supere los 250 caracteres. 
    # De ser así, se debe lanzar una excepción 'LargoExcedidoException'
        if len(nombre) <= 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoException(f'ERROR: El nombre no debe contener más de 250 caracteres')
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino

    # Método sobrecargado '__str__'  debe retornar cadena de texto que informe
    # nombre de la campaña y la cantidad de anuncios por cada tipo
    def __str__(self) -> str:
        n_video = 0
        n_display = 0
        n_social = 0
        for anuncio in self.anuncios:
            if isinstance(anuncio, Video):
                n_video += 1
            elif isinstance(anuncio, Display):
                n_display += 1
            elif isinstance(anuncio, Social):
                n_social += 1
        return f'Nombre de la campaña: {self.nombre}\nAnuncios: {n_video} Video, {n_display} Display, {n_social} Social'
    
# TESTING
if __name__ == '__main__':
    video_1 = Video('http://..', 'http://..', 'instream', 3)
    display_1 = Display(1440, 1280, 'http://..', 'http://..', 'tradicional')    
    social_1 = Social(480, 720,'http://..', 'http://..', 'facebook')
    anuncios = [video_1, display_1, social_1]
    campania_1 = Campania('Pachulí', (2024,4,14), (2024,4,30), anuncios)
    
    for anuncio in campania_1.anuncios:
        print(anuncio.sub_tipo)