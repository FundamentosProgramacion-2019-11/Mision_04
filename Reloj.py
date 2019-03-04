# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Convierte la hora de formato 24 horas a formato 12 horas

#Llama a las funciones utilizadas
def main():

    hora = int(input("¿Qué hora es? "))
    minuto = int(input("¿Qué minuto es? "))
    segundo = int(input("¿Cuáles son los segundos? "))

    hora12 = definirHora(hora)
    minutos = definirMinutos(minuto)
    segundos = definirSegundos(segundo)

    print("Son las ", hora12, ":", minutos, ":", segundos)

#Define la hora y determina si es válida
def definirHora(hora):

    if hora>12 and hora<=23:
        return "%d" % (hora - 12)

    elif hora<=12 and hora>0:
        return hora

    else:
        return "Error"

#Define los minutos y determina si son válidos
def definirMinutos(minuto):

    if minuto>=0 and minuto<60:
        return "%02d" % minuto

    else:
        return "Error"

#Define los segundos y determina si son válidos
def definirSegundos(segundo):

    if segundo>=0 and segundo<60:
        return "%02d" % segundo

    else:
        return "Error"


main()
