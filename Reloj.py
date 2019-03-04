#Autor: Diego Raul Elizalde Uriarte
#convertir hora en formato de 24 horas al formato de 12 hrs







def convertirHora(hora,minuto,segundo):
    if hora <13:
        return hora
    elif hora == 13 :
        Hora = 1
        return Hora
    elif hora == 14 :
        Hora = 2
        return Hora
    elif hora == 15 :
        Hora = 3
        return Hora
    elif hora == 16 :
        Hora = 4
        return Hora
    elif hora == 17 :
        Hora = 5
        return Hora
    elif hora == 18 :
        Hora = 6
        return Hora
    elif hora == 19 :
        Hora = 7
        return Hora
    elif hora == 20 :
        Hora = 8
        return Hora
    elif hora == 21 :
        Hora = 9
        return Hora
    elif hora == 22 :
        Hora = 10
        return Hora
    elif hora == 23 :
        Hora = 11
        return Hora





def main():
    hora = int(input("Dame la hora: "))
    minuto = int(input("Dame el minuto: "))
    segundo = int(input("Dame el segundo: "))
    convertirHora(hora,minuto,segundo)
    if hora <0 and hora>23:
        print("Error")
    elif minuto<0 and minuto>60:
        print("Error")
    elif segundo<0 and minuto>60:
        print("Error")
    else:
        convertirHora(hora,minuto,segundo)
        if hora < 13:
            print(convertirHora(hora,minuto,segundo),":",minuto,":",segundo,"am")
        elif hora >12:
            print(convertirHora(hora, minuto, segundo), ":", minuto, ":", segundo, "pm")



main()