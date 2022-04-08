import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break # este break me ayuda a optimizar el mejor caso, que es cuando lo encuentra en algún punto de la lista y para de buscar en todo lo que resta de la lista. Sin embargo, puede ser que no sirva de nada ya que a veces lo voy a encontrar hasta el final o no lo voy a encontrar. 

    return match

if __name__ == '__main__': # "si se ejecuta desde la consola"; es lo que quiere decir esta sentencia
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista') # aquí uso operadores ternarios para usar una sola línea de código con el if