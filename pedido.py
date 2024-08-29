from Te_clase import Te

# Solicitar datos al usuario
sabor = int(input("Ingrese el sabor del té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato del té (300 o 500): "))

# Obtener los datos necesarios
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Mostrar la información del pedido
sabores = {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}
print(f"Sabor: {sabores[sabor]}")
print(f"Formato: {formato}gr")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
