#Paradigmas Tecnologicos II - Robotica 2009
#Ing Nestor Adrian Balich
#proyecto Pyzarra Primario
#este material es GNU

import math
from math import sqrt

varX = float(raw_input('Valor de ingresar: '))
Resultado = sqrt(varX**2)

print 'Soluciones de la ecuación: valor=%4.3f Resultado=%4.3f' % (varX, Resultado)

#imprimir caracteres unicode
linea= unicode('1#\xc1\xc9\xcd\xd3\xda\xd1\xe1\xe9\xed\xf3\xfa##PRUEBA(PRUEBA)#06##1#0#\n','iso-8859-15')
print linea
