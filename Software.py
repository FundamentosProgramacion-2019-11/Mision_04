#Autor: Martha Margarita Dorantes Cordero
#Calcular total de paquetes


def calcularTotal(numPaquetes) :
	#Función que realiza la operación requerida para calcular el total a pagar con el descuento aplicable.
	total = (numPaquetes * 2300) - calcularDescuento(numPaquetes)
	return total


def calcularDescuento(numPaquetes) :
	#Función que realiza la operación requerida para calcular el descuento aplicable con base en el número de paquetes.
	total = numPaquetes * 2300
	descuento = 0
	if(numPaquetes < 10) :
		return descuento
	elif(numPaquetes < 20) :
		descuento = total * 0.15
		return descuento
	elif(numPaquetes < 50) :
		descuento = total * 0.22
		return descuento
	elif(numPaquetes < 100) :
		descuento = total * 0.35
		return descuento
	else :
		descuento = total * 0.42
		return descuento


def main() :
	#Función principal que solictia el número de paquetes de software vendidos y llama a las funciones
	#previamente descritas para calcular el descuento y el total a pagar después del descuento.
	numPaquetes = int(input("\n Ingrese el número de paquetes vendidos: "))
	if(numPaquetes <= 0) :
		print('\n ERROR. El número de paquetes debe ser un entero positivo. GRACIAS.')
	else :
		print('\n Subtotal: $%.2f'%(numPaquetes * 2300))
		print(' Descuento: $%.2f'%(calcularDescuento(numPaquetes)))
		print(' -----------------------')
		print(' Total a pagar: $%.2f'%(calcularTotal(numPaquetes)))


main()