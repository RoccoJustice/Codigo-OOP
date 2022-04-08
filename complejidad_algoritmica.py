import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

if __name__ == '__main__':
    
    sys.setrecursionlimit(20000) # esto solo lo puse para ampliar el límite de recursión del intérprete. No pasa nada silo quito, solo que "n" no podrá pasar de 999 y para ver las comparaciones vale la pena ampliarlo
    n = 5120
    comienzo = time.time() 
    factorial(n)
    final = time.time()
    print(final - comienzo) # para saber cuánto tiempo tarda en calcular el factorial con la función factorial

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo) # para saber cuánto tiempo tarda en calcular el factorial con la función factorial_r