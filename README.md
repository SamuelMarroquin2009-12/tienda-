Enunciado del Ejercicio: Sistema de Compras en una Tienda Virtual
Descripción General
Desarrollar un sistema de compras en una tienda virtual utilizando Programación Orientada a Objetos (POO). El sistema debe permitir la gestión de productos, la administración de un cliente y la simulación de una compra a través de un carrito de compras.

Requisitos del Sistema
El sistema debe contar con las siguientes tres clases:

Clase Producto

Atributos:
nombre (str): Nombre del producto.
precio (float): Precio del producto.
Métodos:
mostrar_info(): Devuelve una cadena con el nombre y el precio del producto.
Clase Cliente

Atributos:
nombre (str): Nombre del cliente.
carrito (list): Lista de productos agregados al carrito de compras.
Métodos:
agregar_producto(producto: Producto): Agrega un producto al carrito.
mostrar_carrito(): Muestra la lista de productos en el carrito.
calcular_total(): Devuelve la suma total de los precios de los productos en el carrito.
Clase Tienda

Atributos:
nombre (str): Nombre de la tienda.
productos (list): Lista de productos disponibles en la tienda.
Métodos:
agregar_producto(producto: Producto): Agrega un producto a la tienda.
mostrar_productos(): Muestra la lista de productos disponibles en la tienda.
Interacción con el Usuario (Menú de Opciones)
El sistema debe permitir al usuario interactuar a través de un menú en la consola con las siguientes opciones:

Agregar producto a la tienda: Permite registrar un nuevo producto en la tienda con su nombre y precio.
Mostrar productos de la tienda: Muestra todos los productos disponibles en la tienda.
Agregar producto al carrito: Permite que el cliente agregue un producto disponible en la tienda a su carrito de compras.
Mostrar carrito de compras: Muestra los productos que el cliente ha agregado al carrito.
Calcular total de compra: Calcula y muestra el precio total de los productos en el carrito.
Salir: Finaliza la ejecución del programa.
