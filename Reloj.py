# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que convierte la hora del formato 24 horas al formato de 12 horas.

# Esta función convierte las horas del formato 24hrs al formato 12 hrs.
def convertirHoras(h):
    if h == 0 or h == 12:
        horas = 12
    elif h == 1 or h == 13:
        horas = 1
    elif h == 2 or h == 14:
        horas = 2
    elif h == 3 or h == 15:
        horas = 3
    elif h == 4 or h == 16:
        horas = 4
    elif h == 5 or h == 17:
        horas = 5
    elif h == 6 or h == 18:
        horas = 6
    elif h == 7 or h == 19:
        horas = 7
    elif h == 8 or h == 20:
        horas = 8
    elif h == 9 or h == 21:
        horas = 9
    elif h == 10 or h == 22:
        horas = 10
    elif h == 11 or h == 23:
        horas = 11
    return horas


# Esta función  acomoda las horas, minutos y segundos  y decide si la hora es am o pm para regresar una cadena.
def calcularHora(h, hC, m, s):
    if h >= 0 and h <= 11:
        hora = ("La hora es: %02d:%02d:%02d am" % (hC, m, s))
        return str(hora)
    else:
        hora = ("La hora es: %02d:%02d:%02d pm" % (hC, m, s))
        return str(hora)


# Llamada a la función principal.
def main():
    horas = int(input("Teclea la hora en formato 24 horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    # Esta condición decide si la hora ingresada es válida o no e imprime el resultado.
    if horas >= 0 and horas <= 23:
        horasConvertidas = convertirHoras(horas)
        hora = (calcularHora(horas, horasConvertidas, minutos, segundos))
        print(hora)
    else:
        print("error")

# Llamada la función principal.
main()
