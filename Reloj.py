# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Programa que convierte las horas en formato de 24 horas a formato de 12


#La funcion convierte las horas de 24 a 12
def convertirHoras(horas):
    if horas == 12 or horas == 0:
        horas12 = 12
    elif horas == 13 or horas == 1:
        horas12 = 1
    elif horas == 14 or horas == 2:
        horas12 = 2
    elif horas == 15 or horas == 3:
        horas12 = 3
    elif horas == 16 or horas == 4:
        horas12 = 4
    elif horas == 17 or horas == 5:
        horas12 = 5
    elif horas == 18 or horas == 6:
        horas12 = 6
    elif horas == 19 or horas == 7:
        horas12 = 7
    elif horas == 20 or horas == 8:
        horas12 = 8
    elif horas == 21 or horas == 9:
        horas12 = 9
    elif horas == 22 or horas == 10:
        horas12 = 10
    elif horas == 23 or horas == 11:
        horas12 = 11
    else:
        horas12 = "error"

    return horas12


#función que delimita que los minutos esten en un rango de 0 a 59
def aceptarMinutos(minutos):
    if minutos >= 0 and minutos <= 59:
        minutos = minutos
    else:
        minutos = "error"

    return minutos


#función que delimita que los minutos esten en un rango de 0 a 59
def aceptarSegundos(segundos):
    if segundos>= 0 and segundos<= 59:
        segundos = segundos
    else: segundos = "error"

    return segundos


#función que pide los datos y convierte las horas en formato de 24 a formato de 12 horas
def main():
    print("Introduce la hora en un formato de 24 horas, se te dara en un formato de 12 horas")
    horas = int(input("Introduce la hora/horas "))
    minutos = int(input("Introduce los minutos "))
    segundos = int(input("Introduce los segundos "))

    horas12 = convertirHoras(horas)
    minutos = aceptarMinutos(minutos)
    segundos= aceptarSegundos(segundos)

    if horas12 == "error":
        print("error")
    elif minutos == "error":
        print("error")
    elif segundos == "error":
        print("error")
    else:
        print("Son las:", horas12, ":", minutos, ":", segundos)

e
main()
