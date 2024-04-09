class Te():
    formato = [300, 500]
    tiempo = 0
    recomendacion = ""
    
    @staticmethod
    def preparacion(sabor):
        if sabor == 1:
            Te.tiempo = 3
            Te.recomendacion = "Se recomienda consumir en el desayuno"
        elif sabor == 2:
            Te.tiempo = 5
            Te.recomendacion = "Se recomienda consumir al medio día"
        elif sabor == 3:
            Te.tiempo = 6
            Te.recomendacion = "Se recomienda consumir al atardecer"
        return Te.tiempo, Te.recomendacion
    
    @staticmethod
    def precio(formato):
        if formato == 1:
            precio = 3000
        elif formato == 2:
            precio = 5000
        return precio
        
    
if __name__ == "__main__":
    print(Te.preparacion(1))
    print(Te.precio(2))
