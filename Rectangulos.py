#Autor: Martha Margarita Dorantes Cordero
#Calcular área base


def calcularArea(base, altura) :
	#Función que realiza la operación requerida para calcular el área de un rectángulo.
	area = base * altura
	return area


def calcularPerimetro(base, altura) :
	#Función que realiza la operación requerida para calcular el perímetro de un rectángulo.
	perimetro = 2 * (base + altura)
	return perimetro


def main() :
	#Función principal que solicita al usuario los valores de las bases y alturas de dos rectángulos y llama a las funciones
	#previamente descritas para obtener las áreas y perímetros correspondientes y comparar cuál es el de mayor área.
	b1 = float(input("\n Ingrese la base del primer rectángulo: "))
	h1 = float(input(" Ingrese la altura del primer rectángulo: "))
	b2 = float(input("\n Ingrese la base del segundo rectángulo: "))
	h2 = float(input(" Ingrese la altura del segundo rectángulo: "))
	area1 = calcularArea(b1, h1)
	area2 = calcularArea(b2, h2)
	perimetro1 = calcularPerimetro(b1, h1)
	perimetro2 = calcularPerimetro(b2, h2)
	print('\n Área del primer rectángulo: %.2fm2'%(area1))
	print(' Perímetro del primer rectángulo: %.2fm'%(perimetro1))
	print('\n Área del segundo rectángulo: %.2fm2'%(area2))
	print(' Perímetro del segundo rectángulo: %.2fm'%(perimetro2))
	if(area1 > area2) :
		print('\n El área del primer rectángulo es mayor que del segundo.')
	elif(area2 > area1) :
		print('\n El área del segundo rectángulo es mayor que del primero.')
	else :
		print('\n Ambos rectángulos tienen la misma área.')


main()