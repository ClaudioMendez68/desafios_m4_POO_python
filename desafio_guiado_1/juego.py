# Importación de módulos necesarios para el desarrollo del juego
import os, sys, random
from personaje import Personaje

clear = 'cls' if sys.platform == 'win32' else 'clear'
os.system(clear)

print('¡Bienvenido a Gran Fantasía!')
# Creación de personajes
name = input('Por favor indique nombre de su personaje:\n')
person = Personaje(name)
orco = Personaje('Orco')
# Visualización en consola del estado de los personajes
print(person.estado)
print('¡Oh no!, ¡Ha aparecido un Orco!')
# Se llama al método diálogo para visualizar diálogos e ingresar opción de juego
opt = person.dialogo(person.probabilidad(orco))
# Mecánica del juego según opciones ingresadas por el jugador
while opt == 1:
    aleatorio = random.uniform(0, 1)
    if aleatorio <= person.probabilidad(orco):
        print('¡Le has ganado al orco, felicidades!')
        print('¡Recibirás 50 puntos de experiencia!')
        person.estado = 50
        orco.estado = -30
    else:
        print('¡Oh no! ¡El orco te ha ganado!')
        print('¡Has perdido 30 puntos de experiencia!')
        person.estado = -30
        orco.estado = 50
        
    print(person.estado)
    print(orco.estado)    
    opt = person.dialogo(person.probabilidad(orco))
    os.system(clear)
    
print('¡Has huido! El orco ha quedado atrás.')
