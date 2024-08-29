class Te:
    """
    La clase Te representa un tipo de té con diferentes sabores y formatos.
    Proporciona métodos para obtener el tiempo de preparación, la recomendación 
    de consumo y el precio del té según el sabor y el formato seleccionados.

    Atributos de clase:
    -------------------
    duracion : int
        Duración estándar en días de todos los tipos de té (365 días).

    Métodos:
    --------
    __init__(self, sabor, formato):
        Inicializa una nueva instancia de la clase Te con el sabor y formato especificados.

    obtener_tiempo_y_recomendacion(sabor):
        Método estático que retorna el tiempo de preparación y la recomendación
        de consumo según el sabor del té.

    obtener_precio(formato):
        Método estático que retorna el precio del té según el formato seleccionado.
    """

    duracion = 365  # Todos los té tienen una duración de 365 días

    def __init__(self, sabor, formato):
        """
        Inicializa una nueva instancia de la clase Te.

        Parámetros:
        -----------
        sabor : int
            Un número entero que representa el sabor del té.
            Valores permitidos:
                1: Té negro
                2: Té verde
                3: Agua de hierbas

        formato : int
            Un número entero que representa el formato del té en gramos.
            Valores permitidos:
                300: 300 gramos
                500: 500 gramos
        """
        self.sabor = sabor
        self.formato = formato

    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        """
        Retorna el tiempo de preparación y la recomendación de consumo 
        según el sabor del té.

        Parámetros:
        -----------
        sabor : int
            Un número entero que representa el sabor del té.
            Valores permitidos:
                1: Té negro
                2: Té verde
                3: Agua de hierbas

        Retorna:
        --------
        tuple:
            Una tupla que contiene:
            - tiempo : int
                Tiempo de preparación en minutos.
            - recomendacion : str
                Recomendación de consumo como texto.
        """
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
        """
        Retorna el precio del té según el formato seleccionado.

        Parámetros:
        -----------
        formato : int
            Un número entero que representa el formato del té en gramos.
            Valores permitidos:
                300: 300 gramos
                500: 500 gramos

        Retorna:
        --------
        int:
            El precio del té en pesos chilenos.
        """
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000
        else:
            return None
