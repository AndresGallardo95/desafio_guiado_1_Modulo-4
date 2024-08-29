from Te_clase import Te

# Crear dos instancias de la clase Te
te1 = Te(1, 300)  
te2 = Te(2, 500)  

# Almacenar el tipo de dato de cada instancia
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrar el tipo de dato de cada instancia
print(tipo_te1)  # Muestra el tipo de dato de la primera instancia (te1)
print(tipo_te2)  # Muestra el tipo de dato de la segunda instancia (te2)

# Comparar los tipos de dato
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")  # Mensaje si ambos tipos son iguales
else:
    print("Los objetos no son del mismo tipo")  # Mensaje si los tipos son diferentes
