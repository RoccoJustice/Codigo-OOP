"""
class Coordenada: # Clase

    def __init__(self, x, y): # generamos nuestro constructor __init__
        self.x = x # una coordenada tiene x y y, así que inicialiazamos nuestras variables
        self.y = y

    def distancia(self, otra_coordendada): # esta clase puede definir la distancia entre 2 coordenadas. "otra coordenada" es otra instancia de Coordenada. Este viene siendo el
        x_diff = (self.x - otra_coordendada.x) ** 2 # para definir la distancia vamos a utilizar el método Euclidiano https://es.wikipedia.org/wiki/Distancia_euclidiana
        y_diff = (self.y - otra_coordendada.y) ** 2

        return (x_diff + y_diff) ** 0.5


if __name__ == '__main__': # con esto le digo que si el archivo se ejecuta desde la terminal, nosotros lo podemos correr
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2)) # le pasamos como segundo parámetro la coordenada 2.Aquí podemos ver que tenemos un molde que se llama Coordenada, que enesta coordenada podemos tener varias instancias, y que podemos ejecutar directamente los métodos que nosotros definimos adentro de esta clase
    print(isinstance(coord_1, Coordenada)) # con esto le preguntamos si coord_1 es una instancia de Coordenada
    print(isinstance(coord_2, Coordenada)) # lo mismo que arriba
"""
class Robot:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce(self):
        return "My name is " + self.name

if __name__ == '__main__':
    r1 = Robot("Memo", "yellow", 3)
    r2 = Robot("Chewbacca", "Gray", 4)
    r3 = Robot("Artemisa", "white/gray", 2.5)
    
    print(r1.introduce())
    print(r2.introduce())
    print(r3.introduce())