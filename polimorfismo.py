"""
class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bici')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()

if __name__ == '__main__':

    main()
"""

class Voltaje:

    def __init__(self, corriente, resistencia):
        self.corriente = corriente
        self.resistencia = resistencia

    def calcular_voltaje(self):
        return self.corriente * self.resistencia
        

class MiliVoltaje(Voltaje):

    def __init__(self, corriente, resistencia):
        super().__init__(corriente, resistencia)

    def calcular_voltaje(self):
        return (self.corriente * self.resistencia)*1000
        

if __name__ == "__main__":
    voltios = Voltaje(corriente=100, resistencia=120)
    print(f'V: {voltios.calcular_voltaje()}')

    milivoltios = MiliVoltaje(100, 120)
    print(f'mV: {milivoltios.calcular_voltaje()}')