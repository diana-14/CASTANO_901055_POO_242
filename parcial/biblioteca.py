class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True
    
    def get_titulo(self):
        return self._titulo
    
    def get_autor(self):
        return self._autor
    
    def get_isbn(self):
        return self._isbn
    
    def esta_disponible(self):
        return self._disponible
    
    def cambiar_disponibilidad(self):
        self._disponible = not self._disponible

    def __str__(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"'{self._titulo}' por {self._autor} (ISBN: {self._isbn}) - {estado}"
    
    def __repr__(self):
        return self.__str__()

class Miembro:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion
        self._libros_prestados = []
    
    def agregar_libro(self, libro):
        if libro.esta_disponible():
            libro.cambiar_disponibilidad()
            self._libros_prestados.append(libro)
        else:
            print(f"El libro '{libro.get_titulo()}' no está disponible para préstamo.")
    
    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.cambiar_disponibilidad()
            self._libros_prestados.remove(libro)
        else:
            print(f"El libro '{libro.get_titulo()}' no está en la lista de préstamos de {self._nombre}.")

    def __str__(self):
        return f"Miembro: {self._nombre} (ID: {self._identificacion})"
    
    def __repr__(self):
        return self.__str__() + f" - Libros prestados: {[libro.get_titulo() for libro in self._libros_prestados]}"

class MiembroVIP(Miembro):
    def __init__(self, nombre, identificacion, limite_prestamos=10):
        super().__init__(nombre, identificacion)
        self._limite_prestamos = limite_prestamos
    
    def agregar_libro(self, libro):
        if len(self._libros_prestados) < self._limite_prestamos:
            super().agregar_libro(libro)
        else:
            print(f"{self._nombre} ha alcanzado el límite de préstamos de {self._limite_prestamos} libros.")
    
    def __str__(self):
        return f"Miembro VIP: {self._nombre} (ID: {self._identificacion}) - Límite de préstamos: {self._limite_prestamos}"
    
    def __repr__(self):
        return self.__str__() + f" - Libros prestados: {[libro.get_titulo() for libro in self._libros_prestados]}"

def prueba():

    libro1 = Libro("Romper el Círculo", "Colleen Hoover", "978-9877391971")
    
   
    miembro1 = Miembro("Carlos", "M001")
    miembro_vip1 = MiembroVIP("Lucía", "VIP001", limite_prestamos=5)
    
    
    print("Estado inicial")
    print(libro1)
    print(miembro1)
    print(miembro_vip1)
    
    print("\nPréstamo de libro")
    miembro1.agregar_libro(libro1)
    print(libro1)
    print(miembro1)
    
    print("\nDevolución de libro")
    miembro1.devolver_libro(libro1)
    print(libro1)
    print(miembro1)
    
    print("\nPréstamo de libro por Miembro VIP")
    miembro_vip1.agregar_libro(libro1)
    print(libro1)
    print(miembro_vip1)
    
    print("\nIntento de préstamo adicional por Miembro VIP (exceso de límite)")
    for i in range(6):
        miembro_vip1.agregar_libro(Libro(f"Libro {i+1}", "Autor", f"ISBN-{i+1}"))
    print(miembro_vip1)

prueba()
