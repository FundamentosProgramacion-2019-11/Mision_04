#Autor: Katia Hernández Barrera
#Progtama que convierte un reloj de 24 h en el formato de 12 h

def convertirHora(h, m, s):  #Funcion que convierte las horas en formato 24 a formato 12
    if h>0 and h<=12:
        hora12 = h
    elif h ==12:
        hora12 = 1
    elif h == 14:
        hora12 = 2
    elif h == 15:
        hora12 = 3
    elif h == 16:
        hora12 = 4
    elif h == 17:
        hora12 = 5
    elif h ==18:
        hora12 = 6
    elif h == 19:
        hora12 = 7
    elif h == 20:
        hora12 = 8
    elif h == 21:
        hora12 = 9
    elif h == 22:
        hora12 = 10
    elif h == 23:
        hora12 = 11
    elif h == 24:
        hora12 = 0
    else:
        hora12 = "Error, inserte hora válida"
    return hora12

def validarMinutos(h,m,s): #Función que se asegura que los minutos que el usuario teclea son válidos
    if m >= 0 and m < 60:
        return m
    else:
        return "Error, inserte minuto válido"
def validarSegundos(h,m,s):  #Función que se asegura que los segundos que el usuario teclea son válidos
    if s >= 0 and s < 60:
        return s
    else:
        return "Error, inserte segundo válido"


def main():
    h = int(input("Teclea la hora"))
    m = int(input("Teclea los minutos"))
    s = int(input("Teclea los segundos"))
    hora = convertirHora(h,m,s)
    minuto = validarMinutos(h,m,s)
    segundo = validarSegundos(h,m,s)
    print("La hora en formato 12 hrs es: ", hora, ":", minuto, ":", segundo)


main()