# Grupo 3: Juan Torres, Diego Larenas, Matías Valdivia, Claudio Méndez
from ingredientes import vegetales, proteicos, masa

class Pizza(): 
    precio = 10000
    tamano = 'Familiar'
    
    @staticmethod
    def validar(ingrediente: str, lista: list):
        """Valida si un ingrediente se encuentra dentro de una lista de ingredientes

        Args:
            ingrediente (str): Ingrediente a evaluar
            lista (list): Lista de ingredientes disponibles

        Returns:
            bool: Resultado de la validación
        """
        for elem in lista:
            if ingrediente == elem:
                return True
        return False

    def crear_pedido(self):
        """Genera un pedido y valida si los ingredientes están disponibles

        Returns:
            bool: Resultado si la Pizza es posible de elaborar
        """
        self.proteico = input("Ingrese el ingrediente proteico [Pollo , Vacuno , Carne Vegetal] : ").lower()
        self.vegetal_1 = input("Ingrese el primer ingrediente vegetal [Tomate, Aceitunas, Champiñones] : ").lower()
        self.vegetal_2 = input("Ingrese el segundo ingrediente vegetal [Tomate, Aceitunas, Champiñones] : ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa [Tradicional , Delgada] : ").lower()
                
        if self.validar(self.proteico, proteicos) and self.validar(self.vegetal_1, vegetales) and self.validar(self.vegetal_2, vegetales) and self.validar(self.tipo_masa, masa):
            self.validacion = True
        else:
            self.validacion = False
            
        return self.validacion


if __name__ == '__main__':
    #test = Pizza.validar('pollo', proteicos)
    #print(test)
    pedido_1 = Pizza()
    print(pedido_1.crear_pedido())