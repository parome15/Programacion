# coding=utf-8

'''Modifica el programa anterior para que en vez de mostrar un mensaje 
genérico en el caso de que alguno o los dos números sean negativos, 
escriba una salida diferenciada para cada una de las situaciones que se puedan producir,
utilizando los siguientes mensajes:
No se calcula la suma porque el primer número es negativo.
No se calcula la suma porque el segundo número es negativo.
No se calcula la suma porque los dos números son negativos.'''



numeroA = int(input('Escribe un numero entero:'))
numeroB = int(input('Escribe un numero entero:'))

if numeroA >= 0 and numeroB >= 0:
	print('La suma de los dos numeros es:', numeroA+numeroB)
elif numeroA < 0 and numeroB < 0:
	print ('No se calcula la suma porque los dos números son negativos')
elif numeroA < 0:
	print ('No se calcula la suma porque el primer número es negativo')
else:
	print ('No se calcula la suma porque el segundo número es negativo')
