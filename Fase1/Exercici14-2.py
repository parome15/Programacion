# coding=utf-8

'''Escribe  un programa que pida por teclado una cantidad de dinero y 
que a continuación muestre la descomposición de dicho importe en el menor 
número de billetes y monedas de 100, 50, 20, 10, 5, 2 y 1 	euro. 
En el caso de que alguna moneda no intervenga en la descomposición no se 
tiene que visualizar nada en la pantalla. Para una cantidad de 2236 euros 
la salida que generaría el programa sería:

22 billetes de 100 euros
1 billete de 20 euros
1 billete de 10 euros
1 billete de 5 euros
1 moneda de 1 euro'''

'''Propuesto por compañeros'''


dinero = int(input("Introduce una cantidad de dinero: "))

def contarDinero(cantidad, valor):
	if valor <= cantidad & cantidad > 4:
		contador = cantidad // valor
		cantidad = cantidad % valor
		print("Hay ", contador, " billetes de ", valor, "€")
		return cantidad
	elif valor <= cantidad & cantidad > 0 & cantidad < 4:
		contador = cantidad // valor
		cantidad = cantidad % valor
		print ("Hay ", contador, " monedas de ", valor, "€")
		return cantidad
	else:
		return cantidad
		
tipos = [500, 200, 100, 50, 20, 10, 5, 2, 1]
for x in tipos: dinero = contarDinero(dinero, x)