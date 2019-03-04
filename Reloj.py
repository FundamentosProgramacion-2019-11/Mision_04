#Autor: Martha Margarita Dorantes Cordero
#Calcular horas, minutos y segundos


def calcularHora(horas, minutos, segundos) :
	#Función que realiza la operación requerida para calcular la hora recibida en formato de 12 hrs.
	reloj = ""
	if((0 <= minutos <= 59) and (0 <= segundos <= 59)) :
		if(horas == 0) :
			horas = 12
			reloj = str(horas) + ":" + str(minutos) + ":" + str(segundos) + " am"
		elif(horas == 12) :
			reloj = str(horas) + ":" + str(minutos) + ":" + str(segundos) + " pm"
		elif(12 < horas <= 23) :
			horas = horas - 12
			reloj = str(horas) + ":" + str(minutos) + ":" + str(segundos) + " pm"
		elif(1 <= horas < 12) :
			reloj = str(horas) + ":" + str(minutos) + ":" + str(segundos) + " am"
		else :
			reloj = "ERROR"
	else :
		reloj = "ERROR"
	return reloj


def main() :
	#Función principal que solicita las horas, minutos y segundos de la hora actual y llama a la función
	#previamente definida para convertir la hora ingresada al formato de 12 hrs e imprime el resultado.
	horas = int(input("\n Ingrese las horas: "))
	minutos = int(input(" Ingrese los minutos: "))
	segundos = int(input(" Ingrese los segundos: "))
	reloj = calcularHora(horas, minutos, segundos)
	if(reloj == "ERROR") :
		print("\n La hora ingresada es inválida.")
	else :
		print('\n La hora ingresada en formato de 12 hrs. es: %s'%(reloj))

main()