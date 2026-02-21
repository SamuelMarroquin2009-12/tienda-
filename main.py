class Producto:
    def __init__(self, nombre: str, precio:float ):
        self.nombre = nombre
        self.precio = precio
    def mostar_info(self):
        return f"Producto {self.nombre} por ${self.precio}"
class Cliente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.carrito= []
    def agregar_producto(self, producto:Producto):
        self.carrito.append(producto)
        print(f"listo {producto.nombre} se añadio al carrito de {self.nombre}. ")
    def mostrar_carrito(self):
        if not self.carrito:
            print("carrito esta vacio")
        else :
            print(f"----- carrito de {self.nombre} -----")
            for p in self.carrito:
                print(p.mostar_info())
    def calcular_total(self):
        total = sum(p.precio for p in self.carrito)
        return total
class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos_disponibles = []
    def agregar_producto(self,producto: Producto):
        self.productos_disponibles.append(producto)
    def mostrar_productos(self):
        print(f"\n--- Catalogo de {self.nombre} ---")
        if not self.productos_disponibles:
            print("Catalogo esta vacio")
        else:
            for i, p in enumerate(self.productos_disponibles, 1):
                print(f"{i}. {p.mostar_info()}")


def menu():
    # 1. Inicializamos los objetos base
    mi_tienda = Tienda("Super Tienda Samuel")
    # Para el ejercicio, asumimos un único cliente para simular la compra
    nombre_cliente = input("Bienvenido, ¿cuál es tu nombre? ")
    cliente = Cliente(nombre_cliente)

    while True:
        print(f"\n--- MENÚ TIENDA VIRTUAL: {mi_tienda.nombre} ---")
        print("1. Agregar producto a la tienda")
        print("2. Mostrar productos de la tienda")
        print("3. Agregar producto al carrito")
        print("4. Mostrar carrito de compras")
        print("5. Calcular total de compra")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                nuevo_prod = Producto(nombre, precio)
                mi_tienda.agregar_producto(nuevo_prod)
                print("Producto registrado con éxito.")
            except ValueError:
                print("Error: El precio debe ser un número. Inténtalo de nuevo.")

        elif opcion == "2":
            mi_tienda.mostrar_productos()

        elif opcion == "3":
            mi_tienda.mostrar_productos()
            if mi_tienda.productos_disponibles:
                try:
                    indice = int(input("Ingrese el número del producto que desea: ")) - 1
                    if 0 <= indice < len(mi_tienda.productos_disponibles):
                        producto_elegido = mi_tienda.productos_disponibles[indice]
                        cliente.agregar_producto(producto_elegido)
                    else:
                        print("Ese número no está en la lista.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            cliente.mostrar_carrito()

        elif opcion == "5":
            total = cliente.calcular_total()
            print(f"Total a pagar: ${total:.2f}")

        elif opcion == "6":
            print(f"Gracias por comprar con nosotros, {cliente.nombre}. ¡Vuelve pronto!")
            break
        else:
            print("Opción no válida, Samuel. Intenta de nuevo.")


# Ejecutamos el programa
if __name__ == "__main__":
    menu()