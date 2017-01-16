# coding=utf-8

'''Escribe	un programa que pida por teclado dos números y 
que calcule y muestre su suma solamente si:

-los dos son pares 
-el primero es menor que cincuenta 
-y el segundo está dentro del intervalo cerrado 100-500. 

En el caso de que no se cumplan las condiciones, en vez de la suma ha de 
visualizarse un mensaje de error.'''


numeroA = int(input('Introduzca un numero'))
numeroB = int(input('Introduzca un numero'))

if (numeroA%2 == 0) and (numeroB%2 == 0):
	if numeroA < 50:
		if numeroB < 100 > 500:
			print('La suma de los numeros es:', numeroA + numeroB)
else:
	print ('Alguno de los térnminos es erroneo')