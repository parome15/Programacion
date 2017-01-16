# coding=utf-8

'''Escribe un programa que pida por teclado el radio de una circunferencia,
 y que a continuación calcule y escriba en pantalla la longitud 
 de la circunferencia y del área del círculo.'''

PI = 3.14159
radioCircumferencia = int(input('Escriba el radio de la circumferencia: '))
longitudCircumferencia = 2 * PI * radioCircumferencia
areaCircumferencia = (radioCircumferencia ** 2) * PI

print ("La longitud de la circumferencia es: ", longitudCircumferencia)
print ("El area de la circumferencia es: ", areaCircumferencia)

