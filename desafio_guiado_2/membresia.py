# Grupo 3: Lolett Llanquinao - Jocelyn Cantero - Juan Torres - Leonardo Llaupe - Claudio Méndez

from abc import ABC, abstractmethod
# Clase abstracta
class Membresia(ABC):
# Posee herencia jerárquica: es clase padre de las clases Gratis y Básica
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta
    # Método abstracto
    @abstractmethod
    def cambiar_suscripcion(self, tipo: int):
        pass
    # Método con acceso tipo 'Protected'. Sólo acceden a él esta clase y toda las clases que heredan de ella.
    def _crear_nueva_membresia(self, tipo: int):
        if tipo == 1: 
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        if tipo == 2: 
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        if tipo == 3: 
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        if tipo == 4: 
            return Pro(self.correo_suscriptor, self.numero_tarjeta)
        
    # GETTERS
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta
    
class Gratis(Membresia):
    costo = 0 
    dispositivos = 1
    # Implementación del método abstracto, presentando POLIMORFISMO
    def cambiar_suscripcion(self, tipo: int):
        if tipo >= 1 and tipo <= 4:
            return self._crear_nueva_membresia(tipo)
        else:
            return self

class Basica(Membresia):
# Posee herencia jerárquica: es clase padre de las clases Familiar y SinConexion
# Posee herencia multinivel: es clase hija de la clase Membresia y, a la vez, clase padre de las clases Familiar y SinConexion
    costo = 3000
    dispositivos = 2

    def __init__(self, correo_sustriptor: str, numero_tarjeta: str):
        # Ejecuta el constructor de la clase abstracta padre
        super().__init__(correo_sustriptor, numero_tarjeta)
        # Al crear la membresía, asigna los días de regalo al atributo de instancia '__regalo', según el tipo de membresía
        if isinstance(self, Pro):
            self.__regalo = 15
        elif isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__regalo = 7
    # Getter        
    @property
    def regalo(self):
        return self.__regalo
    # Método que genera una membresía de tipo Gratis con el mismo correo y número de tarjeta de la membresía original
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    # Implementación del método abstracto, presentando POLIMORFISMO
    def cambiar_suscripcion(self, tipo: int):
        if tipo >= 2 and tipo <= 4:
            return self._crear_nueva_membresia(tipo)
        else:
            return self

class Familiar(Basica):
# Posee herencia multinivel: es clase hija de la clase Basica y, a la vez, clase padre de la clase Pro
    costo = 5000
    dispositivos = 5
    # Implementación del método abstracto, presentando POLIMORFISMO
    def cambiar_suscripcion(self, tipo: int):
        if tipo in [1, 2, 4]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self
        
    def control_parental(self):
        pass

class SinConexion(Basica):
# Posee herencia multinivel: es clase hija de la clase Basica y, a la vez, clase padre de la clase Pro
    dispositivos = 2
    # Implementación del método abstracto, presentando POLIMORFISMO
    def cambiar_suscripcion(self, tipo: int):
        if tipo in [1, 2, 3]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self
        
    def cantidad_offline(self):
        pass

class Pro(Familiar, SinConexion):
# Posee herencia múltiple: es clase hija de las clases Membresia y SinConexion
    costo = 7000
    dispositivos = 6
    # Implementación del método abstracto, presentando POLIMORFISMO
    def cambiar_suscripcion(self, tipo: int):
        if tipo in [1, 2, 3]:
            return self._crear_nueva_membresia(tipo)
        else:
            return self
        
    def control_parental(self):
        pass
    
    def cantidad_offline(self):
        pass

# Testing    
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))