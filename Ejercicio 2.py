from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    
 
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, 
                 distancia_sol, tipo, es_observable, periodo_orbital, periodo_rotacion):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
      
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    
    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")
        # Impresión de nuevos atributos
        print(f"Periodo orbital (años) = {self.periodo_orbital}")
        print(f"Periodo de rotación (días) = {self.periodo_rotacion}")

    
    def calcular_densidad(self):
       
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    
    def es_planeta_exterior(self):
        limite = 149597870 * 3.4
        if self.distancia_sol > limite:
            return True
        else:
            return False


def capturar_datos_planeta(numero_planeta):
    print(f"\n--- INGRESO DE DATOS DEL PLANETA {numero_planeta} ---")
    nombre = input("Ingrese el nombre del planeta: ")
    satelites = int(input("Ingrese la cantidad de satélites: "))
    masa = float(input("Ingrese la masa (ej. 5.97e24): "))
    volumen = float(input("Ingrese el volumen (ej. 1.08e12): "))
    diametro = int(input("Ingrese el diámetro en km: "))
    distancia = int(input("Ingrese la distancia media al Sol en km: "))
    
   
    print("Tipos de planeta: 1. GASEOSO | 2. TERRESTRE | 3. ENANO")
    opcion_tipo = int(input("Seleccione el tipo (1/2/3): "))
    if opcion_tipo == 1:
        tipo = TipoPlaneta.GASEOSO
    elif opcion_tipo == 2:
        tipo = TipoPlaneta.TERRESTRE
    else:
        tipo = TipoPlaneta.ENANO
        
   
    obs_input = input("¿Es observable a simple vista? (s/n): ").lower()
    observable = True if obs_input == 's' else False
    
    
    p_orbital = float(input("Ingrese el periodo orbital (en años): "))
    p_rotacion = float(input("Ingrese el periodo de rotación (en días): "))
    
    
    return Planeta(nombre, satelites, masa, volumen, diametro, distancia, tipo, observable, p_orbital, p_rotacion)



if __name__ == "__main__":
    
    planeta1 = capturar_datos_planeta(1)
    planeta2 = capturar_datos_planeta(2)

    
    print("\n=== RESULTADOS PLANETA 1 ===")
    planeta1.imprimir()
    print(f"Densidad del planeta = {planeta1.calcular_densidad()}")
    print(f"Es planeta exterior = {planeta1.es_planeta_exterior()}")

    
    print("\n=== RESULTADOS PLANETA 2 ===")
    planeta2.imprimir()
    print(f"Densidad del planeta = {planeta2.calcular_densidad()}")
    print(f"Es planeta exterior = {planeta2.es_planeta_exterior()}")
