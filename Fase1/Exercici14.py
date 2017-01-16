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


cantidadDinero = int(input('Escribe la cantidad de dinero:'))


Billetes100 = cantidadDinero//100
cantidadDinero = cantidadDinero%100

Billetes50 = cantidadDinero//50
cantidadDinero = cantidadDinero%50

Billetes20 = cantidadDinero//20
cantidadDinero = cantidadDinero%20

Billetes10 = cantidadDinero//10
cantidadDinero = cantidadDinero%10

Billetes5 = cantidadDinero//5
cantidadDinero = cantidadDinero%5

Monedas2 = cantidadDinero//2
cantidadDinero = cantidadDinero%2

Monedas1 = cantidadDinero//1
cantidadDinero = cantidadDinero%1

print ("Billetes de 100: ", Billetes100, "\nBilletes de 50: ", Billetes50, 
	"\nBilletes de 20: ", Billetes20, "\nBilletes de 10: ", Billetes10,
	"\nBilletes de 5: ", Billetes5, "\nMonedas de 2: ", Monedas2,
	"\nMonedas de 1: ", Monedas1)

