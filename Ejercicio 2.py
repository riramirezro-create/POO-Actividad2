from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    
   
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, observable, periodo_orbital, periodo_rotacion):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol 
        self.tipo = tipo                   
        self.observable = observable       
        self.periodo_orbital = periodo_orbital 
        self.periodo_rotacion = periodo_rotacion 

    
    def imprimir(self):
        print(f"\n=== DATOS DEL PLANETA: {self.nombre.upper()} ===")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia media al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo de planeta: {self.tipo.value}")
        print(f"Observable a simple vista: {'Sí' if self.observable else 'No'}")
        print(f"Periodo orbital: {self.periodo_orbital} años")
        print(f"Periodo de rotación: {self.periodo_rotacion} días")
        print("===================================\n")

    
    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    
    def es_planeta_exterior(self):
        
        distancia_km_reales = self.distancia_sol * 1_000_000
        
        limite_exterior_km = 3.4 * 149597870
        
       
        return distancia_km_reales > limite_exterior_km



print("--- SISTEMA SOLAR - REGISTRO DE PLANETAS ---")


lista_planetas = []


for i in range(1, 3):
    print(f"\n--- Captura de datos para el Planeta {i} ---")
    
    nombre_p = input("Nombre del planeta: ")
    satelites_p = int(input("Cantidad de satélites: "))
    masa_p = float(input("Masa en kilogramos: "))
    volumen_p = float(input("Volumen en kilómetros cúbicos: "))
    diametro_p = int(input("Diámetro en kilómetros: "))
    distancia_p = int(input("Distancia media al Sol (en MILLONES de km): "))
    
  
    print("Tipos: 1. Gaseoso | 2. Terrestre | 3. Enano")
    opcion = input("Seleccione el tipo (1/2/3): ")
    if opcion == '1': tipo_p = TipoPlaneta.GASEOSO
    elif opcion == '2': tipo_p = TipoPlaneta.TERRESTRE
    else: tipo_p = TipoPlaneta.ENANO
    
   
    obs_p = input("¿Es observable a simple vista? (S/N): ").upper()
    observable_p = True if obs_p == 'S' else False
    
   
    orbital_p = float(input("Periodo orbital (en años): "))
    rotacion_p = float(input("Periodo de rotación (en días): "))
    
   
    nuevo_planeta = Planeta(nombre_p, satelites_p, masa_p, volumen_p, diametro_p, distancia_p, tipo_p, observable_p, orbital_p, rotacion_p)
    lista_planetas.append(nuevo_planeta)


print("\n\n--- RESULTADOS FINALES ---")
for planeta in lista_planetas:
    planeta.imprimir()
    print(f">> Densidad del planeta: {planeta.calcular_densidad()} kg/km³")
    
    if planeta.es_planeta_exterior():
        print(">> Ubicación: Es un planeta EXTERIOR del sistema solar.")
    else:
        print(">> Ubicación: NO es un planeta exterior (es interior).")
    print("-" * 40)
