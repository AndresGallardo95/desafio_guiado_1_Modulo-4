# desafio_guiado_1_Modulo-4

# Desafío Guiado 1 - Creación de Clases y Objetos

## Descripción General

Este proyecto consiste en la creación y manejo de una clase `Te` que representa diferentes tipos de té. A través de esta clase, se pueden obtener detalles como el tiempo de preparación, recomendaciones de consumo y precios según el sabor y formato del té. El proyecto incluye tres archivos principales:

1. `Te_clase.py`: Contiene la definición de la clase `Te` y sus métodos.
2. `instacias.py`: Crea instancias de la clase `Te` y compara sus tipos.
3. `pedido.py`: Interactúa con el usuario para crear un pedido de té y muestra la información relacionada con ese pedido.

## Archivos y Funcionalidades

### 1. `Te_clase.py`
Este archivo contiene la definición de la clase `Te`, la cual modela un tipo de té con atributos como sabor y formato. Los métodos estáticos en esta clase permiten obtener información específica relacionada con el té, como el tiempo de preparación, la recomendación de consumo y el precio.

- **Atributos de la Clase:**
  - `duracion`: Duración estándar de todos los tipos de té en días (365 días).

- **Métodos:**
  - `__init__(self, sabor, formato)`: Inicializa una instancia de la clase `Te` con el sabor y formato proporcionados.
  - `obtener_tiempo_y_recomendacion(sabor)`: Método estático que devuelve el tiempo de preparación y la recomendación de consumo según el sabor del té.
  - `obtener_precio(formato)`: Método estático que devuelve el precio del té según el formato seleccionado.

### 2. `instacias.py`
Este archivo crea dos instancias de la clase `Te`, una con sabor `1` (Té negro) y formato `300g`, y la otra con sabor `2` (Té verde) y formato `500g`. Luego, compara los tipos de estas instancias y muestra en pantalla si son del mismo tipo.

- **Flujo de Trabajo:**
  1. Importa la clase `Te` desde `Te_clase.py`.
  2. Crea dos instancias de `Te` con diferentes sabores y formatos.
  3. Almacena y muestra el tipo de dato de cada instancia.
  4. Compara los tipos de dato y muestra si son iguales o diferentes.

### 3. `pedido.py`
Este archivo interactúa con el usuario para crear un pedido de té. Solicita al usuario que ingrese el sabor y formato deseados, y luego utiliza los métodos de la clase `Te` para obtener y mostrar la información relevante del pedido.

- **Flujo de Trabajo:**
  1. Solicita al usuario que ingrese el sabor y formato del té.
  2. Utiliza los métodos estáticos de `Te` para obtener el tiempo de preparación, la recomendación de consumo y el precio.
  3. Muestra en pantalla todos los detalles del pedido: sabor, formato, precio, tiempo de preparación y recomendación.

## Cómo Ejecutar

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/AndresGallardo95/desafio_guiado_1_Modulo-4.git
   
