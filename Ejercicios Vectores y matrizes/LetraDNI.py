# coding=utf-8


'''Hacer un programa que dado un número de DNI obtenga la letra del NIF.
La letra correspondiente a un número de DNI se calcula mediante el siguiente algoritmo: 
Se obtiene el resto de dividir el número de DNI entre 23. 
El número resultante nos indica la posición de la letra correspondiente a ese DNI, en la siguiente cadena:'''

listaLetras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]



def darLetraDNI(numero):
	assert isinstance(numero, int), "no estas utilizando un numero entero"
	
	posicionLetra = numero%23

	letraAsignada = listaLetras[posicionLetra]
	
	return letraAsignada


#Casos TEST

print darLetraDNI(43178233)




