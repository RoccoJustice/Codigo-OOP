"""
class CasillaVotacion:

    def __init__(self, indentificador,pais):
        self._identificador = indentificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self,reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self._pais}')

casilla = CasillaVotacion(123,['Bogota','Medellin'])
print(casilla.region)
casilla.region = 'Bogota'
print(casilla.region)
"""

class CasillaVotacion:

    def __init__(self, identificador,pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self,reg):
        if reg in self.__pais:
            self.__region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self.__pais}')

casilla = CasillaVotacion(123,['Bogota','Medellin'])
print(casilla.region)
casilla.region = 'Medellin'
print(casilla.region)
