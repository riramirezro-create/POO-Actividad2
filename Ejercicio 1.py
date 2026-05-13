class Persona:
    
    def __init__(self, nombre, apellidos, numero_documento, anio_nacimiento, pais_nacimiento, genero):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento  
        self.genero = genero                    

    def imprimir(self):
        print("\n=== DATOS DE LA PERSONA ===")
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de Identidad: {self.numero_documento}")
        print(f"Año de Nacimiento: {self.anio_nacimiento}")
        print(f"País de Nacimiento: {self.pais_nacimiento}")
        print(f"Género: {self.genero}")
        print("===========================\n")

print("--- REGISTRO DE NUEVA PERSONA ---")

ingreso_nombre = input("Ingrese el nombre de la persona: ")
ingreso_apellidos = input("Ingrese los apellidos: ")
ingreso_documento = input("Ingrese el número de documento de identidad: ")
ingreso_anio = int(input("Ingrese el año de nacimiento (Ej. 1998): "))
ingreso_pais = input("Ingrese el país de nacimiento: ")
ingreso_genero = input("Ingrese el género ('H' para hombre, 'M' para mujer): ")

persona1 = Persona(ingreso_nombre, ingreso_apellidos, ingreso_documento, ingreso_anio, ingreso_pais, ingreso_genero)

persona1.imprimir()
