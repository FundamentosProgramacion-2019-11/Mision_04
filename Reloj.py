# Autor: Rosalía Serrano Herrera
# Convierte la hora de formato 24 horas a formato 12 horas


def convertirHoras(horas24, minutos, segundos): #convierte las horas de formato 24hrs a formato 12hrs
    if horas24 >= 1 and horas24 <= 12:
        horas12 = horas24
    elif horas24 >= 13 and horas24 <= 23:
        horas12 = horas24 - 12
    elif horas24 == 00:
        horas12 = 12
    else:
        return "ERROR"
    return horas12, minutos, segundos


def main():
    horas24 = int(input("Teclea las horas en formato 24 horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))
    if horas24 < 0 or horas24 >= 24:
        print("ERROR")
    elif minutos < 0 or minutos >= 60:
        print("ERROR")
    elif segundos < 0 or segundos >= 60:
        print("ERROR")
    else:
        hora12 = convertirHoras(horas24, minutos, segundos)
        print("La hora es:", hora12)


main()