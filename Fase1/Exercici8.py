# coding=utf-8


'''Escribe	un programa que pida por teclado dos números y 
que muestre en pantalla uno de los dos mensajes siguientes en 
función de los números leídos: 
-a) el primer número (valor) es mayor que el segundo (valor)
(introduciendo el valor de los números en el mensaje); 
-b) el primer número (valor) es menor que el segundo (valor; 
-c) los dos números son iguales (valor).'''


numeroA = int(input('Escibre un numero:'))
numeroB = int(input('Escibre un numero:'))

if numeroA > numeroB:
	print ('El primer numero:', numeroA, 'Es mayor que el segundo numero:', numeroB)
elif numeroA < numeroB:
	print ('El primer numero:', numeroA, 'Es menor que el segundo numero:', numeroB)
else:
	print ('Los dos numeros son iguales:', numeroA)
