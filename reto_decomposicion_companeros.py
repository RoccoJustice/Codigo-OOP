class Automovil:
    
    def __init__(self, modelo, marca, color, dueño):
        
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.dueño = 'pepito'
        self.estado = 'En reposo'
        self.motor = Motor(cilindros = 4)
        
    def acelerar(self, tipo = 'despacio'):

        if(tipo == 'rapida'):
        
            self.motor.inyeccionGasolina(10)
        
        else:
            
            self.motor.inyeccionGasolina(3)
            
    def enfriar(self, temperatura = 50):
        
        if((temperatura <= 50) and (temperatura > 80)):
            
            self.motor.inyeccionRefrigerante(10)
            
        elif(temperatura >= 80):
            
            self.motor.inyeccionRefrigerante(20)
            
        else:
            
            self.motor.inyeccionRefrigerante(5)
    
        
class Motor: 

    def __init__(self, cilindros, fabricate, tipo = 'gasolina'):

        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0
        self.fabricante = fabricate
            
    def inyeccionGasolina(self):
        
        pass
        
    def inyeccionRefrigerante(self):
        
        pass```
    