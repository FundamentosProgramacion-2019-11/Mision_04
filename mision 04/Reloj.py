# Luis Duran
# Hacer que el prggrama cambie del formato de 24 horas al de 12 horas, como el de un reloj analogo.


def tranformarHora(hora):
    if hora >= 1 and hora <= 12:
        hora12 = hora
    elif hora >= 13 and hora <= 23:
        hora12 = hora - 12
    elif hora == 0:
        hora12 = 12
    else:
        hora12 = "Error"
    return hora12


def limitarMinutos(minuto):
    if minuto >= 0 and minuto <= 59:
        minutos = minuto
    else:
        minutos = "Error"
    return minutos


def limitarSegundos(segundo):
    if segundo >= 0 and segundo <= 59:
        segundos = segundo
    else:
        segundos = "Error"
    return segundos


def main():
    print()
    hora = int(input("Ingresa la horas en formato de 24 horas: "))
    minuto = int(input("Ingresa los minutos: "))
    segundo = int(input("Ingresa los segundos: "))
    hora12 = tranformarHora(hora)
    minutos = limitarMinutos(minuto)
    segundos = limitarSegundos(segundo)
    if hora12 == "Error":
        print()
        print("Error, revisa tus horas.")
    elif minutos == "Error":
        print()
        print("Error, revisa tus minutos")
    elif segundos == "Error":
        print()
        print("Error, revisa tus segundos")
    else:
        print()
        print("Son las", hora12, ":", minutos, ":", segundos)


main()