# coding=utf-8

'''Escribe un programa que pida por teclado tres valores de tipo entero, 
y que calcule si se cumple que la suma de dos de ellos es igual al tercero.
 La salida del programa tiene que tener el formato:

		Números introducidos: N1 N2 N3 (tabulador)

Y una de las cuatro líneas de salida siguientes:
Se cumple que N1 = N2 + N3
Se cumple que N2 = N1 + N3
Se cumple que N3 = N1 + N2
Los números no cumplen la condición'''

numeroA = int(input('Introduzca numero entero:'))
numeroB = int(input('Introduzca numero entero:'))
numeroC = int(input('Introduzca numero entero:'))


if numeroC + numeroB == numeroA:
	print ('Se cumple que N1 = N2 + N3')
elif numeroA + numeroC == numeroB:
	print ('Se cumple que N2 = N1 + N3')
elif numeroA + numeroB == numeroC:
	print ('Se cumple que N3 = N1 + N2')
else:
	print ('Los números no cumplen la condicion.')

	 	 		
