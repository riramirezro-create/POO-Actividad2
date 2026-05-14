from enum import Enum

class tipoCom(Enum):
    GASOLINA = "Gasolina"; BIOETANOL = "Bioetanol"; DIESEL = "Diésel"
    BIODISESEL = "Biodiésel"; GAS_NATURAL = "Gas natural"

class tipoA(Enum):
    CIUDAD = "Carro de ciudad"; SUBCOMPACTO = "Subcompacto"; COMPACTO = "Compacto"
    FAMILIAR = "Familiar"; EJECUTIVO = "Ejecutivo"; SUV = "SUV"

class tipoColor(Enum):
    BLANCO = "Blanco"; NEGRO = "Negro"; ROJO = "Rojo"; NARANJA = "Naranja"
    AMARILLO = "Amarillo"; VERDE = "Verde"; AZUL = "Azul"; VIOLETA = "Violeta"

class Automovil:
    
    def __init__(self, marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMaxima, color, esAutomatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMaxima = velocidadMaxima
        self.color = color
        self.velocidadActual = 0 
        
        self.esAutomatico = esAutomatico 
        self.valorMultas = 0.0
        self.cantidadMultas = 0

    def getMarca(self): return self.marca
    def setMarca(self, marca): self.marca = marca
    
    def getModelo(self): return self.modelo
    def setModelo(self, modelo): self.modelo = modelo
    
    def getMotor(self): return self.motor
    def setMotor(self, motor): self.motor = motor
    
    def getTipoCombustible(self): return self.tipoCombustible
    def setTipoCombustible(self, tipoCombustible): self.tipoCombustible = tipoCombustible
    
    def getTipoAutomovil(self): return self.tipoAutomovil
    def setTipoAutomovil(self, tipoAutomovil): self.tipoAutomovil = tipoAutomovil
    
    def getNumeroPuertas(self): return self.numeroPuertas
    def setNumeroPuertas(self, numeroPuertas): self.numeroPuertas = numeroPuertas
    
    def getCantidadAsientos(self): return self.cantidadAsientos
    def setCantidadAsientos(self, cantidadAsientos): self.cantidadAsientos = cantidadAsientos
    
    def getVelocidadMaxima(self): return self.velocidadMaxima
    def setVelocidadMaxima(self, velocidadMaxima): self.velocidadMaxima = velocidadMaxima
    
    def getColor(self): return self.color
    def setColor(self, color): self.color = color
    
    def getVelocidadActual(self): return self.velocidadActual
    def setVelocidadActual(self, velocidadActual): self.velocidadActual = velocidadActual

    def getEsAutomatico(self): return self.esAutomatico
    def setEsAutomatico(self, esAutomatico): self.esAutomatico = esAutomatico

    def acelerar(self, incrementoVelocidad):
        if self.velocidadActual + incrementoVelocidad <= self.velocidadMaxima:
            self.velocidadActual += incrementoVelocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")
            self.cantidadMultas += 1
            multaActual = 50000 * self.cantidadMultas 
            self.valorMultas += multaActual
            print(f">>> ALERTA: Multa generada por ${multaActual}. Intento de exceso de velocidad.")

    def desacelerar(self, decrementoVelocidad):
        if (self.velocidadActual - decrementoVelocidad) >= 0:
            self.velocidadActual -= decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidadActual = 0

    def calcularTiempoLlegada(self, distancia):
        if self.velocidadActual == 0: return 0.0
        return distancia / self.velocidadActual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipoCombustible.value}")
        print(f"Tipo de automóvil = {self.tipoAutomovil.value}")
        print(f"Número de puertas = {self.numeroPuertas}")
        print(f"Cantidad de asientos = {self.cantidadAsientos}")
        print(f"Velocidad máxima = {self.velocidadMaxima}")
        print(f"Color = {self.color.value}")
        print(f"Automático = {'Sí' if self.esAutomatico else 'No'}")

    def tieneMultas(self):
        return self.valorMultas > 0

    def calcularValorTotalMultas(self):
        return self.valorMultas

print("=== INGRESO DE DATOS DEL VEHÍCULO ===")
m_marca = input("Marca: ")
m_modelo = int(input("Modelo (Año): "))
m_motor = int(input("Motor (Ej: 3): "))
m_puertas = int(input("Número de puertas: "))
m_asientos = int(input("Cantidad de asientos: "))
m_vel_max = int(input("Velocidad máxima (km/h): "))

auto_input = input("¿Es automático? (S/N): ").upper()
m_automatico = True if auto_input == 'S' else False

print("\nTipos Combustible: 1.Gasolina 2.Bioetanol 3.Diésel 4.Biodiésel 5.Gas Natural")
opc_comb = input("Seleccione número: ")
if opc_comb == '1': m_combustible = tipoCom.GASOLINA
elif opc_comb == '2': m_combustible = tipoCom.BIOETANOL
elif opc_comb == '3': m_combustible = tipoCom.DIESEL
elif opc_comb == '4': m_combustible = tipoCom.BIODISESEL
else: m_combustible = tipoCom.GAS_NATURAL

print("\nTipos Auto: 1.Ciudad 2.Subcompacto 3.Compacto 4.Familiar 5.Ejecutivo 6.SUV")
opc_tipo = input("Seleccione número: ")
if opc_tipo == '1': m_tipo = tipoA.CIUDAD
elif opc_tipo == '2': m_tipo = tipoA.SUBCOMPACTO
elif opc_tipo == '3': m_tipo = tipoA.COMPACTO
elif opc_tipo == '4': m_tipo = tipoA.FAMILIAR
elif opc_tipo == '5': m_tipo = tipoA.EJECUTIVO
else: m_tipo = tipoA.SUV

print("\nColores: 1.Blanco 2.Negro 3.Rojo 4.Naranja 5.Amarillo 6.Verde 7.Azul 8.Violeta")
opc_color = input("Seleccione número: ")
if opc_color == '1': m_color = tipoColor.BLANCO
elif opc_color == '2': m_color = tipoColor.NEGRO
elif opc_color == '3': m_color = tipoColor.ROJO
elif opc_color == '4': m_color = tipoColor.NARANJA
elif opc_color == '5': m_color = tipoColor.AMARILLO
elif opc_color == '6': m_color = tipoColor.VERDE
elif opc_color == '7': m_color = tipoColor.AZUL
else: m_color = tipoColor.VIOLETA

auto1 = Automovil(m_marca, m_modelo, m_motor, m_combustible, m_tipo, m_puertas, m_asientos, m_vel_max, m_color, m_automatico)

print("\n=== DATOS IMPRESOS ===")
auto1.imprimir()

print("\n=== INICIO DE PRUEBAS DEL LIBRO ===")
auto1.setVelocidadActual(100)
print(f"Velocidad actual = {auto1.getVelocidadActual()}")

auto1.acelerar(20)
print(f"Velocidad actual = {auto1.getVelocidadActual()}")

auto1.desacelerar(50)
print(f"Velocidad actual = {auto1.getVelocidadActual()}")

auto1.frenar()
print(f"Velocidad actual = {auto1.getVelocidadActual()}")

auto1.desacelerar(20) 

print("\n=== REPORTE FINAL DE MULTAS ===")
if auto1.tieneMultas():
    print(f"El vehículo presenta un total de multas por pagar de: ${auto1.calcularValorTotalMultas()}")
else:
    print("El vehículo ha completado el recorrido sin infracciones.")
