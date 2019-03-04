#Autor: Aline Paulette Villegas Berdejo
#Calcula la conversión de 24 horas a formato de 12 horas


def calcularConversionHora(h,m,s):  #Calcula la conversión de formato de 24 horas a 12 y determina los minutos y segundos
    if h>0 and h<=12 and m<60 and m>=0 and s<60 and s>=0:
        h=h
        m=m
        s=s
    elif h>12 and h<24 and m<60 and m>=0 and s<60 and s>=0:
        h=h-12
        m=m
        s=s
    elif h==0 and m<60 and m>=0 and s<60 and s>=0:
        h=h+12
        m=m
        s=s
    else:
        h=0
        m=0
        s=0
    return h,m,s


def main():                        #Indica las funciones que se van a correr al llamar a la funición "main()"
    h=int(input("Escribe la hora en formato de 24 horas: "))
    m=int(input("Escribe el minuto: "))
    s=int(input("Escribe el segundo: "))
    hora=calcularConversionHora(h, m, s)
    if hora[0]<=0:
        print("Error.")
    else:
         print("Hora en formato de 12 horas: %d:%02d:%02d" % hora)


main()