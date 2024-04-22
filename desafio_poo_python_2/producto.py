class Producto():
    # Si no se indica stock, se asume que es 0. Utilice ENCAPSULAMIENTO
    def __init__(self, producto: str, precio: int, stock: int = 0) -> None:
        self.__producto = producto
        self.__precio = precio
        self.__stock = stock
    
    # De cada producto se puede obtener su nombre, su precio o su stock.    
    # GETTERS
    @property
    def producto(self):
        return self.__producto
    @property
    def precio(self):    
        return self.__precio
    @property
    def stock(self):
        return self.__stock
    
    # No se puede modificar el nombre ni el precio de un producto, solo su stock
    # SETTER
    @stock.setter
    def stock(self, stock):
        # Si se intenta modificar el stock por un valor menor a 0, se debe asignar 0
        if stock > 0:
            self.__stock = stock
        else:
            self.__stock = 0

    # Si el producto ya existe en la tienda (dado por su nombre), 
    # se debe modificar su stock, sumando al valor existente el stock del nuevo ingreso
    # Pruebe sobrecargar los operadores __add__, __sub__ y __eq__
    def __eq__(self, other):
        return self.producto == other.producto
    def __add__(self, other):
        return self.stock + other.stock
    def __sub__(self, other):
        return self.stock - other.stock



# TESTING
if __name__ == '__main__':
    producto_1 = Producto('Tapsin', 5900, 4)
    print(producto_1.producto)
    print(producto_1.precio)
    print(producto_1.stock)
    
    producto_1.stock = 7+5
    print(producto_1.stock)