# En otro archivo anuncio.py, definir la clase Anuncio y las clases que permitan crear instancias de tipo Video, Display y Social,
# cada una de ellas con sus atributos de clase y valores correspondientes respectivos
from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
        
    # No se le solicita implementar las reglas de los atributos url_archivo ni url_clic, pero sí debe definir sus getter y setter
    # GETTERS
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    @property
    def url_archivo(self):
        return self.__url_archivo
    @property
    def url_clic(self):
        return self.__url_clic
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    # SETTERS
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic
    # Al modificar sub_tipo de algún anuncio ya creado, validar que se esté ingresando un subtipo permitido.
    # Los subtipos permitidos para cada clase corresponden a los elementos de la tupla definida en el atributo SUB_TIPOS respectivo. 
    # De no cumplirse esta condición al cambiar el valor de sub_tipo, se debe lanzar una excepción SubTipoInvalidoException
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if sub_tipo in self.SUB_TIPOS:
            self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoException(f'ERROR: {sub_tipo} no es un tipo válido')

    @abstractmethod
    def comprimir_anuncio():
        pass
    @abstractmethod
    def redimensionar_anuncio():
        pass
        
    # mostrar_formatos es un método estático que muestra en pantalla los formatos y subtipos asociados
    @staticmethod
    def mostrar_formatos(formato: str, sub_tipo: tuple):
        print(f'FORMATO {formato}:')
        print('================')
        print(f'- {sub_tipo[0]}')
        print(f'- {sub_tipo[1]}')

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self,url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1 , 1, url_archivo, url_clic, sub_tipo)
        self.ancho = 1
        self.alto = 1
        self.__sub_tipo = sub_tipo
        # Se valida 'duracion' inicial 
        self.__duracion = duracion if duracion > 0 else 5
        
    # GETTERS
    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    @property
    def duracion(self):
        return self.__duracion
    
    # SETTERS
    @ancho.setter
    def ancho(self, ancho):
        pass
    @alto.setter
    def alto(self, alto):
        pass
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5
            
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
        
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__sub_tipo = sub_tipo

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")
        

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
        self.__sub_tipo = sub_tipo
    
    @property
    def sub_tipo(self):
        return self.__sub_tipo
        
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

    

# TESTING
if __name__ == '__main__':
    video_1 = Video(1920, 1080, 'http://..', 'http://..', 'instream', 3)
    video_1.mostrar_formatos('Display', ("instream", "outstream"))
    video_1.sub_tipo = 'display'