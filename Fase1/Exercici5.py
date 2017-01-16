# coding=utf-8


'''Escribe un programa que calcule lo que tiene que cobrar un 
empleado sabiendo que se le tiene que aplicar al sueldo una 
retención del 20%.'''

sueldoEmpleado = int(input('Sueldo empleado:'))
retencion = (sueldoEmpleado * 20) // 100
sueldoFinal = sueldoEmpleado - retencion

print('El sueldo del empleado es:', sueldoFinal)