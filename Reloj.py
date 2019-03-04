# Autor: José Luis Macías Vázquez, A01655713, Grupo 03
#Es un programa al que le das la hora en formato de 24 horas y te la regresa en formato de 12 horas, am y pm.


def transformarH(h,m,s):
    if h == 13:
        return "1 pm"
    elif h == 14:
        return "2 pm"
    elif h == 15:
        return "3 pm"
    elif h == 16:
        return "4 pm"
    elif h == 17:
        return "5 pm"
    elif h == 18:
        return "6 pm"
    elif h == 19:
        return "7 pm"
    elif h == 20:
        return "8 pm"
    elif h == 21:
        return "9 pm "
    elif h == 22:
        return "10 pm"
    elif h == 23:
        return "11 pm"
    elif h > 24 or h < 1:
        return "Error"
    elif h == 1:
        return "1"
    elif h == 2:
        return "2"
    elif h == 3:
        return "3"
    elif h == 4:
        return "4"
    elif h == 5:
        return "5"
    elif h == 6:
        return "6"
    elif h == 7:
        return "7"
    elif h == 8:
        return "8"
    elif h == 9:
        return "9"
    elif h == 10:
        return "10"
    elif h == 11:
        return "11"
    elif h == 12:
        return "12"




def main():

    h = int(input("Escribe la hora: "))
    m = int(input("Escribe el minuto: "))
    s = int(input("Escribe el segundo: "))
    print (transformarH(h,m,s), ":", m, ":" ,s)


main()