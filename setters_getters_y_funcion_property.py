"""
def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;) ")
    return wrapper

@funcion_decoradora
def zumbido():
    print("Bzzz")

#zumbido = funcion_decoradora(zumbido)

zumbido()
"""

"""
class Millas:
	def __init__(self, distancia = 0):
		self._distancia = distancia

	def convertir_a_kilometros(self):
		return (self._distancia * 1.609344)

	# Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor

if __name__ == '__main__':
    avion = Millas(2)
    print(avion.convertir_a_kilometros())
    print(avion.obtener_distancia())
    print(avion.definir_distancia(3))
    print(avion.convertir_a_kilometros())
    print(avion.obtener_distancia())
"""

"""
class Millas:
	def __init__(self):
		self._distancia = 10 # atributo privado
	
	def obtener_distancia(self): # Función para obtener el valor de _distancia
		print("Llamada al método getter")
		return self._distancia
	
	def definir_distancia(self, recorrido): # Función para definir el valor de _distancia
		print("Llamada al método setter")
		self._distancia = recorrido
	
	def eliminar_distancia(self): # Función para eliminar el atributo _distancia
		del self._distancia

	distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

if __name__ == '__main__':
   
    avion = Millas()  # Creamos un nuevo objeto 
    avion.distancia = 200  # Indicamos la distancia
    print(avion.distancia)  # Obtenemos su atriDbuto distancia
"""

class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave
        
Usuario1 = usuario ("Roberto", "qwerty")

print (Usuario1.nombre, Usuario1._usuario__clave)