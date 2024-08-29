class Te:
    duracion = 365  # Todos los té tienen una duración de 365 días

    def __init__(self, sabor, formato):
        self.sabor = sabor
        self.formato = formato

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno"
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día"
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer"
        else:
            return None, None

    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return None
