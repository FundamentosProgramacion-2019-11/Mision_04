#Autor: Ivana Olvera Mérida
#Escribe un programa que convierta la hora en formato de 24 horas al formato de 12 hrs.
import time

def calcularHora(hora):
    if hora > 12:
        horaF = hora - 12
        return horaF
    elif hora <= 12:
        return hora

def main():
    hora = int(input("Introduce la hora:"))
    minutos = int(input("Introduce los minutos:"))
    segundos = int(input("Introduce los segundos:"))
    horas = calcularHora(hora)
    horaFinal = str(horas) + str(minutos) + str(segundos)
    print("La hora es: ", hora ,  minutos , segundos)
    

main()