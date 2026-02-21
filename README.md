class Entidad:  # Ejemplo: Libro, Producto, Jugador
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Sistema:  # Ejemplo: Biblioteca, Tienda, Juego
    def __init__(self):
        self.lista = []

    def agregar(self, objeto):
        self.lista.append(objeto)


# El Menú (Cópialo casi igual para el examen)
def ejecutar():
    sis = Sistema()
    while True:
        print("1. Agregar / 2. Mostrar / 3. Salir")
        op = input("Seleccione: ")
        if op == "1":
            # Lógica de creación
            pass
        elif op == "3":
            break