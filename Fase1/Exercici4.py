# coding=utf-8

'''Escribe un programa que calcule el área de una finca 
rectangular en metros cuadrados, así como su perímetro exterior, 
también en metros.'''
 
# El perimetro es igual a la suma de los lados
# El area es igual a lado * lado

ladoLateral = int(input('Escriba la medida lateral del edificio:'))
ladoHorizontal  = int(input('Escriba la medida horizontal del edificio'))

perimetroFinca = (ladoLateral * 2) + (ladoHorizontal * 2)
areaFinca = ladoHorizontal * ladoLateral

print ('Perimetro finca:', perimetroFinca)
print ('Area finca:', areaFinca)