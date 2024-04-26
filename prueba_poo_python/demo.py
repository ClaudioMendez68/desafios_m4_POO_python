# Se le solicita crear un pequeño script 'demo.py' que permita modificar los valores de los atributos de una campaña ya creada
from campania import Campania
from anuncio import Video, Display, Social
from datetime import datetime

# Cree una instancia de Campania (debe tener solo 1 anuncio de tipo Video)
video_1 = Video('http://..', 'http://..', 'instream', 3)
anuncios = [video_1]
campania_1 = Campania('Pachulí', (2024,4,14), (2024,4,30), anuncios)

# Solicite mediante input un nuevo nombre de la campaña y un nuevo sub_tipo para el anuncio
now = datetime.now()
# Envuelva ambas asignaciones en un bloque try/except

try:
    nuevo_nombre = input('Ingrese el nuevo nombre para la campaña: ')
    campania_1.nombre = nuevo_nombre
    nuevo_sub_tipo = input('Ingrese el nuevo sub tipo del anuncio: ')
    campania_1.anuncios[0].sub_tipo = nuevo_sub_tipo
# En caso de que se produzca una excepción, añada su mensaje en un archivo error.log
except Exception as e:
    with open("error.log", "a+") as log_error:
        log_error.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log_error.close()
print(campania_1)