# coding=utf-8

'''Escribe 	un programa que calcule y escriba la suma de los números pares por un lado, y 
de los impares por otro, de los números comprendidos entre dos número introducidos por teclado.'''


numeroA = int(input('Numero entero:'))
numeroB = int(input('Numero entero:'))

listaPares = []
listaImpares = []

for numero in range(numeroA, numeroB+1):
	if numero %2 == 0:
		listaPares.append(numero)
	else:
		listaImpares.append(numero)

sumaPares = sum(listaPares)
sumaImpares = sum(listaImpares)

print ('La suma de los pares:,', sumaPares) 
print ('La suma de los impares:', sumaImpares)
