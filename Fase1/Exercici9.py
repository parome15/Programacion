# coding=utf-8

'''Escribe un programa que nos pida por teclado dos números enteros 
y que a continuación muestre en pantalla la suma de los dos números 
solamente si son los dos positivos. Si no se cumple que los dos números 
sean positivos se visualizará un mensaje indicándolo. 
La salida ha de tener el siguiente formato:
 “La suma de los dos números es: XXX” o
 “No se calcula la suma porque alguno de los números o los dos no son positivos”.'''


numeroA = int(input('Escribe un numero entero:'))
numeroB = int(input('Escribe un numero entero:'))

if numeroA >= 0 and numeroB >= 0:
	print('La suma de los dos numeros es:', numeroA+numeroB)
else:
	print('No se calcula la suma porque alguno de los números o los dos no son positivos.')