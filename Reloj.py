#Autor: Santiago España Vázquez A01748311
#Descripción: Conversion de 24 horas a 12 horas


def convertHour(hour, minute, second):
    if hour<0 or hour>23:
        return "Error"
    elif minute<0 or minute>59:
        return "Error"
    elif second<0 or second>59:
        return "Error"
    elif hour<12:
        r=("La hora es: %i:%i:%i am" %(hour, minute, second))
        return r
    elif hour==12:
        r = ("La hora es: %i:%i:%i pm" % (hour, minute, second))
        return r
    else:
        hour-=12
        r = ("La hora es: %i:%i:%i pm" % (hour, minute, second))
        return r

def main():
    h=int(input("Por favor introduzca la hora: "))
    m=int(input("Por favor introduzca los minutos: "))
    s=int(input("Por favor introduzca los segundos: "))
    hour= convertHour(h, m, s)
    print(hour)

main()