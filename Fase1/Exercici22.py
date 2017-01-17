# coding=utf-8

'''Repite el programa anterior, pero en vez de leer 5 números, 
el usuario ha de indicar antes cuántos números van a ser leídos, 
indicándolo mediante el mensaje: Introduzca cuántos números tienen que leerse por teclado: _'''


rangoNumeros = int(input ("Escribe el numero de valores que quiere testear: "))
listaNumeros = []
contador = 0


while contador < rangoNumeros:
    valorIntroducido = int(input("Escribe un numero aqui: "))
    listaNumeros.append(valorIntroducido)
    contador = contador + 1

## PreConditions

assert isinstance (listaNumeros,list), "Exception Error"
assert isinstance (valorIntroducido,int), "No es un número"

## Programa Principal

if len(listaNumeros) == rangoNumeros:
    print ("El número mas grande es", max(listaNumeros))
    print ("El número mas pequeño es", min(listaNumeros))
else:
    print ("Rango introducido incorrecto")