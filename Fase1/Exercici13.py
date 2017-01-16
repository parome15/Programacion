# coding=utf-8

'''Diseña un programa que calcule el importe final de una venta considerando 
que sobre el valor bruto se hace un descuento según la siguiente tabla:

-Valores <=20 implican un descuento del 0%
-Valores >20 y <=100 implican un descuento descuento del 5%
-Valores >100 implican un descuento 10%'''


valorBruto = int(input('Introduzca valor de la compra:'))
valorFinal = 0

if valorBruto <= 20:
	valorFinal = valorBruto
elif valorBruto in range(20,100):
	valorFinal = valorBruto - (valorBruto*0.05)
else:
	valorFinal = valorBruto - (valorBruto*0.10)