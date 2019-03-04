#Autor: Martha Margarita Dorantes Cordero
#Identificar tipo de triángulo


def identificarTipo(l1, l2, l3) :
	#Función que realiza la operación requerida para identificar el tipo de triángulo con las medidas recibidas.
	#Si todos los lados son iguales es un equilátero.
	#Si dos de los lados son iguales es un isósceles.
	#Si todos los lados son diferentes es un escaleno.
	if((l1 == l2) and (l2 == l3)) :
		return "equilátero"
	elif((l1 == l2) or (l1 == l3) or (l2 == l3)) :
		return "isósceles"
	elif((l1 != l2) or (l1 != l3) or (l2 != l3)) :
		return "escaleno"
	else :
		return "otro"


def main() :
	#Función principal que solicita la longitud de cada uno de los lados de un triángulo y llama a la función
	#previamente definida para identificar el tipo de triángulo.
	#Si alguno de los lados tiene una longitud de 0 o negativa, se imprime la leyenda de que el triángulo no existe.
	lado1 = float(input("\n Ingrese la longitud del primer lado del triángulo: "))
	lado2 = float(input(" Ingrese la longitud del segundo lado del triángulo: "))
	lado3 = float(input(" Ingrese la longitud del tercer lado del triángulo: "))
	if((lado1 <= 0) or (lado2 <= 0) or (lado3 <= 0)) :
		print("\n El triángulo con las medidas ingresadas no existe.")
	else :
		print('\n Las medidas ingresadas corresponden a un triángulo %s.'%(identificarTipo(lado1, lado2, lado3)))


main()