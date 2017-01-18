# coding=utf-8

'''Verificar si una cadena de texto leída por teclado es un DNI correcto o no.
SUponer que los DNI tienen 8 dígitos y a continuación una letra mayúscula'''

def checkDNI(string):
	dniIntroducido = string
	dniLetra = dniIntroducido[8:9]
	dniNumeros = dniIntroducido[0:8]

	if len(dniIntroducido) != 9:
		print ('Syntax Error, no es un DNI correcto')
	elif dniNumeros.isdigit() == False:
		print ('No hay 8 números')
	elif dniLetra.isalpha() == False:
		print ('No hay letra')
	else:
		return True



###CASOS TEST###
'''
if checkDNI('43178233b'):
	print('DNI correcto')

checkDNI('423424234')
#Respuesta: No hay letra

checkDNI('213')
#Respuesta: Syntax Error, no es un DNI correcto

checkDNI('jjojojojo')
#Respuesta: No hay 8 números
'''

