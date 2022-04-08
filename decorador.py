"""
def decorador(funcion): #Creamos la función decorador (A) con el argumento funcion
    def nueva_funcion(): #Creamos la nueva función (C)
        print ("Perro dice:")#Añadimos una modificación a la función (B) dentro de (C)
        funcion() #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A)

    return nueva_funcion #Para devolver (C)

@decorador #Decoramos la función
def saluda():
    print("Guau!")
saluda()
"""
"""
def decorador(funcion): #Creamos la función decorador (A) que recibe como argumento una función (B)
    def nueva_funcion(): #Creamos la nueva función (C)
        print ("Perro dice:") #Añadimos una modificación a la función (B) dentro (C)
        funcion() #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A) para crear (C)
    return nueva_funcion

@decorador #Decoramos la función
def saluda():
    print("Guau!")

@decorador
def despedida():
    print ("Chau")

def movercola():
    print("El perro mueve la cola")

saluda()
despedida()
movercola()
"""
"""
#POO
def decorador(funcion): # Damos como argumento del decorador a una función
    def nueva_funcion(self, mensaje): # Aquí debemos colocar los parámetros con los que trabaja función
        print ("Perro dice:") # Código decorador (lo que le voy a agregar a la función que quiero decorar)
        funcion(self, mensaje) # En funcion agregamos los parámetros con los que trabaja

    return nueva_funcion # Retornamos la nueva función


class perro(object): # Creamos la clase heredando de object
    def __init__(self, nombre):  # Constructor con el atributo nombre
        self.nombre = nombre # Inicializamos el atributo nombre
    
    @decorador # Aqui antes del método se coloca el decorador!!!
    def saluda(self, mensaje): # Método saludar del perro, como siempre
        self.mensaje = mensaje # Inicializamos el argumento del mensaje
        print(mensaje) # Imprimir el mensaje ATENCIÓN.
        print("Guau!") # Resto del código

maty = perro('Maty') # Instanciamos
maty.saluda('Uso Puppy Linux!') # Cuando llamamos al metodo saluda, buscara añadirle el decorador. Osea que se ira hasta arriba. Por ende allí también debimos incluir la instanciacion (self) y el argumento mensaje para ambas (nueva_funcion) y func.
"""


def decorador(func):
    def nueva_funcion(self, mensaje):
        print ("Perro dice:")
        func(self, mensaje) 

    return nueva_funcion 

class perro(object):
    
    def __init__(self, nombre): 
        self.nombre = nombre 
    
    @decorador 
    def saluda(self, mensaje): 
        self.mensaje = mensaje 
        print(mensaje)
        print("Guau!") 
    
    @decorador
    def ordeno(self, orden):
        self.orden = orden
        print(orden)
        print("La pata, la pata afgsad! Guau!")

maty = perro('Maty')
maty.saluda('Uso Puppy Linux!')
maty.ordeno('Doy la pata')