#Escribe un programa que convierta la hora en formato de 24 horas al formato de 12 hrs. Recuerda que en el formato de 24
#hrs. las horas van de 0 a 23. Las 0:00:00 hrs. corresponden a la medianoche. El programa lee la hora, el minuto y el segundo
#por separado e imprime la hora correspondiente en formato de 12 hrs.


def transformarHorario(hora, mins, segs):
    if hora>12 and hora<=23:
        h = hora-10
    elif hora==0:
        h = 12
    elif hora>1 and hora<=12:
        h = hora
    elif mins<0 or mins>59 or segs<0 or segs>59:
        print("Error")
        exit()
    else:
        print("Error")
        exit()
    return h

def main():
    hora = int(input("Teclea la hora: "))
    mins = int(input("Teclea los minutos: "))
    segs = int(input("Teclea los segundos: "))
    Horario = transformarHorario(hora, mins, segs)
    print(Horario, ":", mins, ":", segs, "hrs")

main()