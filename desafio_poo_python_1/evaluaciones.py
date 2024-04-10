from pizza import Pizza

# Imprimir valores de los atributos de la clase
print(f'Precio: ${Pizza.precio}.-')
print(f'Tamaño: {Pizza.tamano}')

# Muestre en pantalla si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de tomate", "salsa bbq"]
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Crear una instancia de la clase importada, ejecutar el script que solicite ingredientes y tipo de masa al usuario
pizza_1 = Pizza()
pizza_1.crear_pedido()

# Usar la función print(), para que se muestre en pantalla los ingredientes vegetales,
# el ingrediente proteico y el tipo de masa de la instancia creada en el paso anterior,
# y si esa instancia es una pizza válida o no.
if pizza_1.validacion:
    print("Pizza válida")
    print("=========================")
    print("Ingredientes de su Pizza:")
    print("=========================")
    print(f"Proteína: {pizza_1.proteico}")
    print(f"Vegatales: {pizza_1.vegetal_1} - {pizza_1.vegetal_2}")
    print(f"Tipo de Masa: {pizza_1.tipo_masa}")
else:
    print("NO es una Pizza válida")
    
# Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza válida haciendo uso del atributo "validacion"
print(Pizza.validacion)