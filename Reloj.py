#Autor: Michel Antoine Dionne Gutierrez Grupo:03 A01748632
#Transforma el formato de 24hrs al de 12 hrs

#Convierte las horas al formato de 12 y detecta si los valores son imposibles
def convertirHora(horas,minutos,segundos):
    if horas>23 or minutos>59 or segundos>59 or horas<0:
        return "Error"
    else:
        if horas>12:
            horasPm = horas-12
            return "Son las: %02d:%02d:%02d,PM"%(horasPm, minutos, segundos)
        else:
            return "Son las: %02d:%02d:%02d,AM"%(horas, minutos, segundos)


def main():
    horas = int(input("Que hora es ?"))
    minutos = int(input("Con cuantos minutos ?"))
    segundos = int(input("Con cuantos segundos ?"))
    r = convertirHora(horas,minutos,segundos)
    print(r)


main()