# coding=utf-8


'''Escribe 	un programa que solicite por teclado 5 números positivos, 
forzando al usuario a que únicamente introduzca valores positivos. 
A continuación el programa tiene que escribe cuál es el valor más pequeño y 
cuál es el mayor valor de los introducidos por el usuario.'''



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
numeroMinimo = min(listaNumeros)
numeroMayor = max(listaNumeros)

print ('El número mayor introducido por el usuario es:',numeroMayor)
print ('El menor numero en la lista de valores es:',numeroMinimo)