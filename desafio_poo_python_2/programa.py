from tienda import Restaurante, Supermercado, Farmacia

# Crear tienda
validador = True
while validador:
    opcion_tienda = int(input('''
Ingresa el tipo de tienda:
1. RESTAURANTE
2. SUPERMERCADO
3. FARMACIA
0. Salir
>>> '''))
    if opcion_tienda == 1:
        nombre_tienda = input('Ingrese el nombre del restaurant: ')
        costo_delivery = int(input('Ingrese el precio del delivery: '))
        tienda = Restaurante(nombre_tienda, costo_delivery)
        validador = False
    elif opcion_tienda == 2:
        nombre_tienda = input('Ingrese el nombre del supermercado: ')
        costo_delivery = int(input('Ingrese el precio del delivery: '))
        tienda = Supermercado(nombre_tienda, costo_delivery)
        validador = False
    elif opcion_tienda == 3:
        nombre_tienda = input('Ingrese el nombre de la farmacia: ')
        costo_delivery = int(input('Ingrese el precio del delivery: '))
        tienda = Farmacia(nombre_tienda, costo_delivery)
        validador = False
    elif opcion_tienda == 0:
        exit()
    else:
        print(f'Opción {opcion_tienda} NO es válida')
    
# Ingresar productos
validador = True
while validador:
    opcion_producto = int(input(f'''
¿Desea ingresar un producto a "{tienda.nombre_tienda}?":
1. SI
2. NO
>>> '''))
    if opcion_producto == 1:
            producto = input('Ingrese nombre del producto: ')
            precio = int(input('Ingrese el precio del producto: '))
            stock = int(input('Ingrese el stock del producto: '))
            tienda.ingresar_producto(producto, precio, stock)
    elif opcion_producto == 2:
        validador = False
    else:
        print (f'Opción {opcion_producto} NO es válida')
        
# Se le debe dar al usuario las opciones de listar los productos existentes, realizar una venta, o salir del programa
validador = True
while validador:
    opcion_operacion = int(input(f'''
Ingrese una operación a realizar en "{tienda.nombre_tienda}":
1. LISTAR PRODUCTOS
2. REALIZAR UNA VENTA
0. Salir
>>> '''))
    if opcion_operacion == 1:
        tienda.listar_productos()
    elif opcion_operacion == 2:
        producto = input('Ingrese nombre del producto: ')
        cantidad = int(input('Ingrese cantidad: '))
        tienda.realizar_venta(producto, cantidad)
    elif opcion_operacion == 0:
        validador = False
    else:
        print (f'Opción {opcion_operacion} NO es válida')