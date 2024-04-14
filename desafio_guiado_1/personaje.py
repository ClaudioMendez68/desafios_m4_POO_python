class Personaje():
    # Método Constructor
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__nivel = 1
        self.__experiencia = 0
        
    # Métodos Getter
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def nivel(self):
        return self.__nivel
    
    @property
    def experiencia(self):
        return self.__experiencia
    
    # Métodos Setter
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @nivel.setter
    def nivel(self, nuevo_nivel: int):
        self.__nivel = nuevo_nivel
        
    @experiencia.setter
    def experiencia(self, nueva_experiencia: int):
        self.__experiencia = nueva_experiencia  
    
    # Getter de estado
    @property
    def estado(self):
        return f'NOMBRE: {self.nombre}     NIVEL: {self.nivel}     EXP: {self.experiencia}' 
    # Setter de estado
    @estado.setter
    def estado(self, nueva_experiencia: int):
        self.experiencia += nueva_experiencia
        # Se incorpora la lógica de cálculo del estado de los personajes por refactorización del código
        if self.experiencia < 0 and self.nivel <= 1:
            self.experiencia = 0
        elif self.experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            self.experiencia += 100
        elif self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
            
    # Sobrecarga método operador 'menor que'
    def __lt__(self, other):
        return self.nivel < other.nivel
    # Sobrecarga método operador 'mayor que'
    def __gt__(self, other):
        return self.nivel > other.nivel
    # Sobrecarga método operador 'igual que'
    def __eq__(self, other):
        return self.nivel == other.nivel
    
    # Método no estático que retorna la probabilidad de ganar
    def probabilidad(self, enemigo):
        if Personaje.__gt__(self, enemigo):
            return 0.66
        elif Personaje.__eq__(self, enemigo):
            return 0.50
        elif Personaje.__lt__(self, enemigo):
            return 0.33
        
    # Método que muestra diálogo de enfrentamiento al orco. Retorna opción de juego
    @staticmethod
    def dialogo(probabilidad):
        print(f'Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco.')
        print('')
        print('Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.')
        print('Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.')
        opcion = int(input(
'''
¿Qué deseas hacer?
1. Atacar
2. Huir
'''))
        return opcion