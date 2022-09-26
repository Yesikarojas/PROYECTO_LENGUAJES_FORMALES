#Paradigmas Tecnologicos II - Robotica 2020
#Ing Nestor Adrian Balich
#este material es GNU

numero = 3
while (numero >= 0) :
   	try:
   		division = 10 / numero
   		numero = numero - 1
   	except (ZeroDivisionError, ValueError ):  #intercepta el error
   		print ("Error de división por cero")
   		break							     #sale del bucle		
   	
   	print ("División correcta =", division)	 #si la division es correcta
   		