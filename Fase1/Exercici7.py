# coding=utf-8

'''Escribe un programa que pida por teclado un número y 
que a continuación muestre el mensaje el número leído es 
positivo o bien el número leído es negativo dependiendo de
 que el número introducido por teclado sea positivo o negativo. 
 Consideramos al número 0 positivo.'''

numero = int(input('Escribe un numero cualquiera:'))


if numero >= 0:
	print('El numero leido es positivo')
else:
 	print('El numero leido es negativo')
