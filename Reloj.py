#FRANCISCO JAVIER GONZALEZ MOLINA
#Convertir la hora en formato 12hrs

#Esta funcion calcula la hora ingresada en formato 24hrs y la convierte en
#formato 12hrs
def calcularHora (hrs,min,seg):
    if hrs == 00 and hrs == 0 or hrs == 12:
        hrss = 12
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs== 1:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 2:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 3:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 4:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 5:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 6:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 7:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 8:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 9:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 10:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"

    elif hrs == 11:
        if min <= 59 and min >= 0 and seg <= 59 and seg >= 0:
            return "0%d:%d:%d hrs" % (hrs, min, seg)
        else:
            return "Por favor inserta minutos/segundos correctos"
    else:
        return "Inserta una hora correcta"

#Esta funcion lee datos y llama funciones
def main():
    hrs=int(input(("Dame el valor de hora: ")))
    min=int(input(("Dame el valor de minutos: ")))
    seg=int(input(("Dame el valor de segundos: ")))
    hrs12=calcularHora(hrs,min,seg)
    print(hrs12)

main()