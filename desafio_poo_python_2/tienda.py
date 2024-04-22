from abc import ABC, abstractmethod
from producto import Producto
# Definir la o las clases necesarias para instanciar los distintos tipos de tienda (utilice ABSTRACCIÓN y ENCAPSULAMIENTO)
class Tienda(ABC):
    # Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y realizar ventas
    @abstractmethod
    # Los productos tienen un nombre, un precio y un stock
    def ingresar_producto(self, producto, precio, stock):
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod
    # Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida
    def realizar_venta(self, producto, cantidad):
        pass
    
# Cada tienda creada, independiente de su tipo, posee un nombre, un listado de productos y un costo de delivery
# Al momento de crear una nueva tienda, se debe solicitar el nombre y el costo de delivery
# (todas las tiendas se crean inicialmente sin productos)
class Restaurante(Tienda):
    # a. Método constructor
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
            self.__nombre_tienda = nombre_tienda
            self.__costo_delivery = costo_delivery
            self.__listado_productos = []

    # Getters
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    # b. Método para ingresar un producto
    def ingresar_producto(self, producto: str, precio: int, stock: int = 0):
        # Los productos de las tiendas de tipo “supermercado” siempre tienen stock igual a 0
        nuevo_producto = Producto(producto, precio, 0)
        self.listado_productos.append(nuevo_producto)

    # c. Método para listar productos
    def listar_productos(self):
        if len(self.listado_productos) > 0:
            print(f'Restaurante: "{self.nombre_tienda}"')
            print('Listado de Productos:')
            print('=====================')
            for p in self.listado_productos:
                # Se debe ocultar el stock de los productos en el caso de las tiendas de tipo Restaurante y Farmacia
                print(f'{p.producto}: ${p.precio: ,}'.replace(',', '.'))
        else:
            print(f'No hay productos en el Restaurante "{self.nombre_tienda}"')
    
    # d. Método para realizar ventas
    def realizar_venta(self, producto: str, cantidad: int):
        print('Venta realizada con éxito')
    
class Supermercado(Tienda):
    # a. Método constructor
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.__listado_productos = []        
    # Getters
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    # b. Método para ingresar un producto
    def ingresar_producto(self, producto: str, precio: int, stock: int = 0):
        # Si el producto ya existe en la tienda (dado por su nombre), se debe modificar su stock
        nuevo_producto = Producto(producto, precio, stock)
        if nuevo_producto in self.listado_productos:
            i = self.listado_productos.index(nuevo_producto)
            self.__listado_productos[i].stock = self.listado_productos[i] + nuevo_producto
        else:
            self.__listado_productos.append(nuevo_producto)

    # c. Método para listar productos
    def listar_productos(self):
        if len(self.listado_productos) > 0:
            print(f'Supermercado: "{self.nombre_tienda}"')
            print('Listado de Productos:')
            print('====================')
            for p in self.listado_productos:
                print(f'{p.producto}: ${p.precio: ,}\nStock: {p.stock}'.replace(',', '.'))
            # Las tiendas de tipo Supermercado deben añadir el mensaje “Pocos productos disponibles” junto a la cantidad de stock
            # en caso de que el stock del producto sea inferior a 10
                if p.stock < 10:
                    print('Pocos productos disponibles')
        else:
            print(f'No hay productos en el supermercado "{self.nombre_tienda}"')
    
    # d. Método para realizar ventas
    def realizar_venta(self, producto: str, cantidad: int):
        # El Supermercado debe tener stock existente del producto indicado
        # (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción)
        for p in self.listado_productos:
            i = self.listado_productos.index(p)
            if p.producto == producto:
                if p.stock >= cantidad:
                    print(f'Se han vendido {cantidad} unidades de {producto}')
                    self.__listado_productos[i].stock = p.stock - cantidad
                # si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible
                elif p.stock < cantidad:
                    print(f'Venta realizada de {p.stock} unidades disponibles')
                    self.__listado_productos[i].stock = 0                    
        
class Farmacia(Tienda):
    # a. Método constructor
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.__listado_productos = []        
    # Getters
    @property
    def nombre_tienda(self):
        return self.__nombre_tienda
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    @property
    def listado_productos(self):
        return self.__listado_productos
    
    # b. Método para ingresar un producto
    def ingresar_producto(self, producto: str, precio: int, stock: int = 0):
        # Si el producto ya existe en la tienda (dado por su nombre), se debe modificar su stock
        nuevo_producto = Producto(producto, precio, stock)
        if nuevo_producto in self.listado_productos:
            i = self.listado_productos.index(nuevo_producto)
            self.listado_productos[i].stock = self.listado_productos[i] + nuevo_producto
        else:
            self.listado_productos.append(nuevo_producto)

    # c. Método para listar productos
    def listar_productos(self):

        if len(self.listado_productos) > 0:
            print(f'Farmacia: "{self.nombre_tienda}"')
            print('Listado de Productos:')
            print('====================')
            for p in self.listado_productos:
                # Se debe ocultar el stock de los productos en el caso de las tiendas de tipo Restaurante y Farmacia
                print(f'{p.producto}: ${p.precio: ,}'.replace(',', '.'))
                # Las Farmacias deben añadir el mensaje “Envío gratis al solicitar este producto”
                # junto al precio de los productos con un valor superior a $15.000
                if p.precio > 15000:
                    print('Envío gratis al solicitar este producto')
        else:
            print(f'No hay productos en la farmacia "{self.nombre_tienda}"')
    
    # d. Método para realizar ventas
    def realizar_venta(self, producto: str, cantidad: int):
        # La Farmacia debe tener stock existente del producto indicado
        # (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción)
        # Farmacia, no se puede solicitar una cantidad superior a 3 por producto en cada venta 
        # (si se solicita una cantidad mayor a 3, no se realiza ninguna acción)
        if cantidad <= 3:
            for p in self.listado_productos:
                i = self.listado_productos.index(p)
                if p.producto == producto:
                    if p.stock >= cantidad:
                        print(f'Se han vendido {cantidad} unidades de {producto}')
                        self.__listado_productos[i].stock = p.stock - cantidad
                    # si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible
                    elif p.stock < cantidad:
                        print(f'Venta realizada de {p.stock} unidades disponibles')
                        self.__listado_productos[i].stock = 0      
        else:
            print('No podemos vender más de 3 unidades de este producto')
# TESTING
if __name__ == '__main__':
    farmacia_1 =  Farmacia('Doctor Mortiz', 2900)
    farmacia_1.ingresar_producto('Tapsin', 1900, 10)
    farmacia_1.ingresar_producto('Flatulín', 17800, 8)
    farmacia_1.listar_productos()
    print(farmacia_1.listado_productos[0].stock)
    farmacia_1.realizar_venta('Tapsin', 4)
    print(farmacia_1.listado_productos[0].stock)