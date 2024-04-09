import te

tipo =""
opcion_sabor = int(input("""
Elija un sabor de té:
1. Té Negro
2. Té verde
3. Infusión de hierbas
> """))

if opcion_sabor == 1:
    tipo = "Té Negro"
elif opcion_sabor == 2:
    tipo = "Té Verde"
elif opcion_sabor == 3:
    tipo = "Infusión de Hierbas"
    
opcion_formato = int(input(
"""
Elija el formato del producto:
1. 300 gramos
2. 500 gramos
> """
))

if opcion_formato == 1:
    formato = te.Te.formato[0]
elif opcion_formato == 2:
    formato = te.Te.formato[1]
    
tiempo, recomendacion = te.Te.preparacion(opcion_sabor)
precio = te.Te.precio(opcion_formato)

print(tipo +":")
print("--------------------")
print(f"Formato: {formato} gramos")
print(f"Precio: ${precio}.-")
print(f"Tiempo de Preparación: {tiempo} minutos")
print(f"{recomendacion}")