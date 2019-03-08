#Autor: Mariana Teyssier Cervantes
#Convertir la hora de 24hrs. al de 12hrs.


#Convertir el formato de 24hrs al formato de 12hrs con -if/else-
def convertirHora(hora):
    if hora==00:
        h = 12
    elif hora==13:
        h = 1
    elif hora==14:
        h = 2
    elif hora==15:
        h = 3
    elif hora==16:
        h = 4
    elif hora==17:
        h = 5
    elif hora==18:
        h = 6
    elif hora==19:
        h = 7
    elif hora==20:
        h = 8
    elif hora==21:
        h = 9
    elif hora==22:
        h = 10
    elif hora==23:
        h = 11
    else:
        h = "Error"

    return h


#Definir la hora, minutos y segundos. Imprimir la cadena de la hora en formato de 12hrs.
def main():
    hora = int(input("Escribe la hora: "))
    minuto = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))
    horario = convertirHora(hora)
    print("Hora: %d:%d:%d" % (horario, minuto, segundos))


#Llamar a la funcion -main-
main()
