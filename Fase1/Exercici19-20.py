# coding=utf-8

'''Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números introducidos.'''

numeroA = int(input('Introduce un número entero positivo:'))
numeroB = int(input('Introduce un número entero positivo:'))
numeroC = int(input('Introduce un número entero positivo:'))
numeroD = int(input('Introduce un número entero positivo:'))
numeroE = int(input('Introduce un número entero positivo:'))

#asserts

assert isinstance(numeroA,int)
assert isinstance(numeroB,int)
assert isinstance(numeroC,int)
assert isinstance(numeroD,int)
assert isinstance(numeroE,int)

listaNumeros = (numeroA,numeroB, numeroC, numeroD, numeroE)
numeroMayor = max(listaNumeros)

print (numeroMayor)