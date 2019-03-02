# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que convierta la hora en formato de 24 horas al formato de 12 hrs.
# Recuerda que en el formato de 24hrs. las horas van de 0 a 23. Las 0:00:00 hrs.
# corresponden a la medianoche. El programa lee la hora, el minuto y el segundo
# por separado e imprime la hora correspondiente en formato de 12 hrs.
# Calcula y define la hora dada.


def calcularHora(horas, minutos, segundos):
    if 13 <= horas <= 23:
        hora = (horas - 12), minutos, segundos
        return hora

    elif 1 <= horas <= 12:
        hora = horas, minutos, segundos
        return hora

    elif horas == 0:
        hora = (horas + 12), minutos, segundos
        return hora


def main():
    # Lee la hora.
    horas = int(input("Teclea las horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    # Establecemos un filtro para los numeros introducidos por el usuario.
    if (0 <= horas <= 23) and (0 <= minutos < 60) and (0 <= segundos < 60):
        # Calcula la hora.
        hora = calcularHora(horas, minutos, segundos)

        print("__________________________________________________")
        print("Son las %d horas con %d minutos y %d segundos" % hora)
        print("- - - - -")
        print("%0d:%0d:%0d" % hora)
        print("- - - - -")

    else:
        print("ERROR")


main()