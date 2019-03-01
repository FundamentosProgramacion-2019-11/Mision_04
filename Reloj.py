# Autor: Itzel Yanabany Castro Becerril
# Convirtir las horas de 24hrs a 12hr


# La funcion calculara el horario de 12 hrs.
def caclcularHoras(hora, minutos, segundos):
    if hora > 0 and hora <= 11 and minutos >=0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
        ho = "La hora es de: " + str(hora) + ": " + str(minutos) + ": " + str(segundos) + " A.M"
        return ho
    else:
        if hora >= 12 and hora <= 23 and minutos >= 0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
            h = hora - 12
            ho = "La hora es de: " + str(h) + ":" + str(minutos) + ":" + str(segundos) + " P.M"
            return ho
        else:
            if hora == 0 and minutos == 0 and segundos == 0:
                ho = "Es media Noche "
                return ho
            else:
                if hora == 0 and minutos >=0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
                    ho = "Son las 12:" + str(minutos) + ":" + str(segundos) + "A.M"
                    return ho
                else:
                    print("error")


# La funcin imprimira la hora en horario de 12 hrs.
def imprimirHorario(hora, minutos, segundos):
    horario = caclcularHoras(hora, minutos, segundos)
    print(horario)


def main():
    hora = int(input("Teclea la hora en formato de 24 hrs: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))
    imprimirHorario(hora, minutos, segundos)


main()

