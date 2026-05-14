class Persona:
    

    def __init__(self, nombre, apellidos, numero_documento_identidad, anio_nacimiento, pais_nacimiento, genero):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anio_nacimiento = anio_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def imprimir(self):
        
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numero_documento_identidad}")
        print(f"Año de nacimiento = {self.anio_nacimiento}")
        print(f"País de nacimiento = {self.pais_nacimiento}")
        print(f"Género = {self.genero}")
        print() 



if __name__ == "__main__":
    
    print("--- INGRESO DE DATOS PERSONA 1 ---")
    nombre1 = input("Ingrese el nombre: ")
    apellidos1 = input("Ingrese los apellidos: ")
    doc1 = input("Ingrese el documento de identidad: ")
    anio1 = int(input("Ingrese el año de nacimiento: ")) 
    pais1 = input("Ingrese el país de nacimiento: ")
    genero1 = input("Ingrese el género (H/M): ")

    
    p1 = Persona(nombre1, apellidos1, doc1, anio1, pais1, genero1)

    print("\n--- INGRESO DE DATOS PERSONA 2 ---")
    nombre2 = input("Ingrese el nombre: ")
    apellidos2 = input("Ingrese los apellidos: ")
    doc2 = input("Ingrese el documento de identidad: ")
    anio2 = int(input("Ingrese el año de nacimiento: "))
    pais2 = input("Ingrese el país de nacimiento: ")
    genero2 = input("Ingrese el género (H/M): ")

    
    p2 = Persona(nombre2, apellidos2, doc2, anio2, pais2, genero2)

    print("\n=== DATOS REGISTRADOS ===")
    p1.imprimir()
    p2.imprimir()
