"""
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base # inicializamos las variables
        self.altura = altura
    
    def area(self): # definimos el método
        return self.base * self.altura

class Cuadrado(Rectangulo): # La forma en la que heredamos el comportamiento es definir la super clase al momento de definir la sub clase
    
    def __init__(self, lado): # aquí solo recibe un lado porque es lo único que necesitamos para calcular el área
        super().__init__(lado, lado) # super nos permite recibir una referencia de la super clase y nos permite llamar a su constructor. Siempre que inicializamos una sub clase, debemos inicializar la super clase

if __name__ == '__main__':
    rectangulo = Rectangulo(3, 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area()) # aquí vemos como podemos ejecutar el método área aunque no esté definido dentro de esta clase. Así es como sabemos que estamos heredando el método
"""


class Vehiculo:

    def __init__(self, combustible, velocidad, tipo, propulsion):
        self.combustible = combustible
        self.velocidad = velocidad
        self.tipo = tipo
        self.propulsion = propulsion

    def ficha(self):
        print(f'Este vehículo utiliza como combustible: {self.combustible}')
        print(f'Este vehículo tine una velocidad maxima de: {self.velocidad}')
        print(f'Este vehículo es de tipo: {self.tipo}')
        print(f'Este vehiculo se mueve gracias a un sistema de propulsión: {self.propulsion}\n')
        

class Automovil(Vehiculo):

    def __init__(self, combustible, velocidad, tipo, propulsion):
        super().__init__(combustible, velocidad, tipo, propulsion)

if __name__ == '__main__':
    vehiculo = Vehiculo('Gasolina', '250 km/h', 'Terrestre', 'Motor de combustión interna')
    vehiculo.ficha()

    automovil = Automovil('Diesel', '100 km/h', 'Anfibio', 'Propulsión a chorro')
    automovil.ficha()