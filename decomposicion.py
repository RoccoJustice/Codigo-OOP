class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo' # estado es una variable privada; esto lo declaro con el '_' antes de la variable
        # self._motor = None # motor también es una variable privada. Aquí la inicializo como 'None', que lo único que significa es que no tiene ningún valor por el momento
        self._motor = Motor(cilindros = 4) # inicializamos la variable y decimos que para que cuando alguien genere la instancia de este coche se va a generar un motor de 4 cilindors
    
    def acelerar(self, tipo = 'despacio'): # una vez que tenemos un automovil, podemos acerelarlo o frenarlo
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en movimiento' # los métodos pueden modificar estados. Así que aquí, con este método, modifico el estado de mi coche

class Motor:

    def __init__(self, cilindros, tipo = 'gasolina'): # 'tipo' viene siendo un 'default keyword' o parámetro por defecto, donde directamente estamos diciendo que su tipo es de gasolina
        self.cilindros = cilindros
        self.tipo = tipo # el hecho de que este parámetro se por default, significa que podemos especificarlo(inicializarlo) directamente o no
        self._temperatura = 0 # variable interna

    def inyecta_gasolina(self, cantidad): # recibe la cantidad de gasolina
        pass # no la vamos a implementar directamente. La finalidad de este ejemplo es empezar a ver como nostros podemos decomponer un problema, sin importar cual es la implementación que utilicemos. Así que regresamos a la línea 8, y e inicializamos la variable privada 'Motor'

# No importa lo que haga este programa, lo importante es percibir como podemos resolver el problema partiéndolo en problemas más pequeños y en componentes re utilizables  (decomponiendolo) . Este programa podríamos utilizarlo con un camión, un go kart, o cualquier tipo de clases. Y también nuestro auto podría definir si queremos tener un motor eléctrico o de combustión o de diesel.