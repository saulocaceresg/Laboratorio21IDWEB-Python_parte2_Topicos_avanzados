# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0304, C0305, C0301, C0116
"""
4.	Crea un programa que permita gestionar libros en una biblioteca usando clases y objetos.
De los libros me interesa título, autor, año y ver si está disponible. Cada libro se debe poder prestar (si está disponible) y devolver (si no está disponible). Crear la clase biblioteca que administre los libros, debe manejar un conjunto de libros y se debe poder agregar libro nuevo, listar libros para mostrar todos los libros con su disponibilidad, buscar por autor y prestar libro (busca el libro por título y lo presta si está disponible).
Crear una clase Libro Digital que herede de Libro y tenga propiedades adicionales de formato (ej: "PDF", "EPUB") y tamañoMB. Sobrescribir el método prestar para que siempre esté disponible (los libros digitales no se prestan físicamente).
Crear al menos 3 libros físicos y 2 libros digitales, agregarlos a la biblioteca y probar los métodos:
•	Listar todos los libros
•	Prestar un libro físico
•	Prestar un libro digital 5 veces
•	Intentar prestar un libro ya prestado
•	Buscar libros por autor

"""
print("====================== EJERCICIO 2(4.) ======================")

class Biblioteca:
    """
    Clase padre que administra los libros
    """
    def __init__(self, libros):
        # Se inicializa con la lista de libros
        self.libros = libros
    
    # Método para agregar libro
    def agregar(self, libro_nuevo):
        print(f"-> AGREGANDO \"{libro_nuevo.titulo}\"...")
        self.libros.append(libro_nuevo)
        print("-> LIBRO AGREGADO")
    
    # Método para buscar un libro por su autor (funciona por que solo hay un libro por autor)
    def buscar(self, autor):
        print(f"\n-> BUSCANDO LIBRO DE \"{autor}\"...")
        for a in self.libros:
            if a.autor == autor:
                print("-> LIBRO ENCONTRADO:")
                print(a.mostrar_datos())
                break
    
    # Método para prestar libro
    def prestar_libro(self, titulo):
        print(f"\n-> LIBRO A PRESTAR: {titulo}")
        libro_disponible = True
        for t in self.libros:
            # Si el libro es digital siempre estará disponible
            if t.titulo == titulo and isinstance(t, LibroDigital):
                # Sobreescrito para que los libros digitales siempre estén disponibles
                libro_disponible = True
                print(f"-> SE HA PRESTADO EL LIBRO DIGITAL \"{t.titulo}\"")
                break
            if t.titulo == titulo and t.disponible:
                print(f"-> SE HA PRESTADO EL LIBRO \"{t.titulo}\"")
                t.disponible = False # Luego de que lo preste se pone como NO DISPONIBLE (false)
                libro_disponible = True
                break # Se cierra para no buscar más
            
            libro_disponible = False
        
        if libro_disponible is False:
            print("-> LIBRO NO DISPONIBLE")

    # Método para listar libros, usando el método mostrar_datos de Libro
    def listar_libros(self):
        print("\n------ LIBROS ------")
        for i in self.libros:
            print(i.mostrar_datos())

class Libro:
    """
    Clase para objetos Libro
    """
    def __init__(self, titulo, autor, anio, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    # Método para imprimir el estado de disponibilidad del libro
    def disponibilidad(self):
        if self.disponible:
            return "DISPONIBLE"
        return "NO DISPONIBLE"

    def mostrar_datos(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}\nEstado: {self.disponibilidad()}\n"

# Crear una clase Libro Digital que herede de Libro y tenga propiedades adicionales de formato (ej: "PDF", "EPUB") y tamañoMB. Sobrescribir el método prestar para que siempre esté disponible (los libros digitales no se prestan físicamente).
class LibroDigital(Libro):
    """
    Clase hija LibroDigital de Libro
    """
    def __init__(self, titulo, autor, anio, disponible, formato, tamanioMB):
        super().__init__(titulo, autor, anio, disponible)
        self.formato = formato
        self.tamanioMB = tamanioMB
    
    def mostrar_datos(self):
        return super().mostrar_datos() + f"Formato: {self.formato}\nTamaño: {self.tamanioMB}\n"

# Crear al menos 3 libros físicos y 2 libros digitales, agregarlos a la biblioteca y probar los métodos:
# •	Listar todos los libros
# •	Prestar un libro físico
# •	Prestar un libro digital 5 veces
# •	Intentar prestar un libro ya prestado
# •	Buscar libros por autor

lista_libros = [
    Libro("1984", "George Orwell", "1949", True),
    Libro("Nosotros", "Yevgueni Zamiatín", "1921", True),
    Libro("Un Mundo Feliz", "Aldous Huxley", "1932", True),
    LibroDigital("All Tomorrows", "C.M Kösemen", "2006", True, "PDF", "4.8 MB"),
    LibroDigital("No tengo boca y debo gritar", "Harlan Ellison", "1967", True, "EPUB", "0.05 MB")
    ]

biblioteca = Biblioteca(lista_libros)

# Enlistando libros
biblioteca.listar_libros()

# Prestando libro físico
biblioteca.prestar_libro("1984")
biblioteca.listar_libros()

# Prestando libro digital cinco veces
biblioteca.prestar_libro("All Tomorrows")
biblioteca.prestar_libro("All Tomorrows")
biblioteca.prestar_libro("All Tomorrows")
biblioteca.prestar_libro("All Tomorrows")
biblioteca.prestar_libro("All Tomorrows")

# Prestando un libro ya prestado (físico y NO DISPONIBLE)
biblioteca.prestar_libro("1984")

# Buscando por autor
biblioteca.buscar("Yevgueni Zamiatín")

# Agregando libros
biblioteca.agregar(Libro("La amenaza de Andrómeda", "Michael Crichton", "1969", True))
biblioteca.listar_libros()

print("=============================================================")
