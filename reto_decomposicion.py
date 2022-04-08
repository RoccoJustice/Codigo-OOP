class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._corriente = False
        self._motor = Motor(cilindros = 4) 
        self._faros = Faros(tipo = 'halogeno')
        
    def acelerar(self, tipo = 'despacio'): 
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento'
    
    def alumbrar(self, alumbramiento = 'poco'):
        if alumbramiento == 'poco':
            self._faros.prender('On')
        else:
            self._faros('Off')
        
        self._corriente = True
    
class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'): 
        self.cilindros = cilindros
        self.tipo = tipo 
        self._temperatura = 0 

    def inyecta_gasolina(self, cantidad): 
        pass 

class Faros:
    def __init__(self, tipo, distancia_alum, lumenes):
        self.metodo = tipo
        self.distancia_alum = distancia_alum
        self.lumenes = lumenes

    def prender(self, prendido):
        pass