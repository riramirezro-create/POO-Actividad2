from enum import Enum


class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"


class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, 
                 num_puertas, cant_asientos, vel_max, color, es_automatico):
      
        self.__marca = marca
        self.__modelo = modelo
        self.__motor = motor
        self.__tipo_combustible = tipo_combustible
        self.__tipo_automovil = tipo_automovil
        self.__num_puertas = num_puertas
        self.__cant_asientos = cant_asientos
        self.__velocidad_maxima = vel_max
        self.__color = color
        self.__velocidad_actual = 0
      
        self.__es_automatico = es_automatico
        self.__multas_totales = 0  

    
    def get_marca(self): return self.__marca
    def set_marca(self, m): self.__marca = m

    def get_modelo(self): return self.__modelo
    def set_modelo(self, m): self.__modelo = m

    def get_velocidad_actual(self): return self.__velocidad_actual
    def set_velocidad_actual(self, v): self.__velocidad_actual = v

   
    def get_es_automatico(self): return self.__es_automatico
    def set_es_automatico(self, a): self.__es_automatico = a

    
    def acelerar(self, incremento):
        if self.__velocidad_actual + incremento <= self.__velocidad_maxima:
            self.__velocidad_actual += incremento
            print(f"Acelerando... Nueva velocidad: {self.__velocidad_actual} km/h")
        else:
            print("¡ALERTA! No se puede superar la velocidad máxima permitida.")
            
            self.__multas_totales += 100000 
            print(f"Se ha generado una multa. Valor total acumulado: ${self.__multas_totales}")

    def desacelerar(self, decremento):
        if self.__velocidad_actual - decremento >= 0:
            self.__velocidad_actual -= decremento
            print(f"Desacelerando... Nueva velocidad: {self.__velocidad_actual} km/h")
        else:
            print("No se puede desacelerar a una velocidad negativa.")

    def frenar(self):
        self.__velocidad_actual = 0
        print("Vehículo frenado. Velocidad: 0 km/h")

    def calcular_tiempo_llegada(self, distancia):
        if self.__velocidad_actual == 0:
            return float('inf') 
        return distancia / self.__velocidad_actual

    
    def tiene_multas(self):
        return self.__multas_totales > 0

    def obtener_total_multas(self):
        return self.__multas_totales

    def imprimir(self):
        print("\n--- DATOS DEL AUTOMÓVIL ---")
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Motor: {self.__motor} litros")
        print(f"Combustible: {self.__tipo_combustible.value}")
        print(f"Tipo: {self.__tipo_automovil.value}")
        print(f"Puertas: {self.__num_puertas}")
        print(f"Asientos: {self.__cant_asientos}")
        print(f"Velocidad Máxima: {self.__velocidad_maxima} km/h")
        print(f"Color: {self.__color.value}")
        print(f"Transmisión: {'Automática' if self.__es_automatico else 'Manual'}")
        print(f"Velocidad Actual: {self.__velocidad_actual} km/h")
        print(f"¿Tiene multas?: {'SÍ' if self.tiene_multas() else 'NO'}")
        print(f"Total multas: ${self.obtener_total_multas()}")


def capturar_automovil():
    print("\n--- INGRESO DE DATOS DEL VEHÍCULO ---")
    marca = input("Marca: ")
    modelo = int(input("Modelo (año): "))
    motor = float(input("Motor (litros): "))
    
    print("Combustible: 1.Gasolina, 2.Bioetanol, 3.Diesel, 4.Biodiesel, 5.Gas Natural")
    c = int(input("Opción: "))
    tipo_c = list(TipoCom)[c-1]

    print("Tipo: 1.Ciudad, 2.Subcompacto, 3.Compacto, 4.Familiar, 5.Ejecutivo, 6.SUV")
    t = int(input("Opción: "))
    tipo_a = list(TipoA)[t-1]

    puertas = int(input("Número de puertas: "))
    asientos = int(input("Cantidad de asientos: "))
    vel_max = int(input("Velocidad máxima (km/h): "))

    print("Color: 1.Blanco, 2.Negro, 3.Rojo, 4.Naranja, 5.Amarillo, 6.Verde, 7.Azul, 8.Violeta")
    col = int(input("Opción: "))
    color = list(TipoColor)[col-1]

    auto_input = input("¿Es automático? (s/n): ").lower()
    es_auto = True if auto_input == 's' else False

    return Automovil(marca, modelo, motor, tipo_c, tipo_a, puertas, asientos, vel_max, color, es_auto)


if __name__ == "__main__":
    mi_auto = capturar_automovil()
    
    
    print("\n--- INICIANDO SIMULACIÓN ---")
    mi_auto.set_velocidad_actual(100)
    print(f"Velocidad establecida en: {mi_auto.get_velocidad_actual()} km/h")
    
    mi_auto.acelerar(20)
    mi_auto.desacelerar(50)
    
    mi_auto.frenar()
    mi_auto.imprimir()
