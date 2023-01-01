import numpy as np
from modulos import *

iniciar=input('Inicial app? (si/no): ').upper()

while iniciar=='SI':
    menu()
    while True:
        try:
            op=int(input('\nIngrese una de las opciones mostradas: '))
            break
        except ValueError:
            print('ERROR.Ingrese un valor valido.')

    if op!=0:
        opciones(op)
    else:
        break

    iniciar=input('\nContinuar en la app? (si/no): ').upper()

print('Gracias por usar mi App!!!')