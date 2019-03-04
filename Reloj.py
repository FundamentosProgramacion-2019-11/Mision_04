#Autor: Marianela Contreras
#Programa para convertir la hora en formato de 24 horas al formato de 12 hrs.


#función paracalcular la hora en fomrato de 12hrs. (recibe como parámetro la hora, minutos y segundos)
def calcularHora(h,m,s):
    if h==0:
        hora= "12"
    elif h==1:
        hora= "1"
    elif h ==2:
        hora = "2"
    elif h == 3:
        hora = "3"
    elif h== 4:
        hora = "4"
    elif h == 5:
        hora= "5"
    elif h == 6:
        hora = "6"
    elif h == 7:
        hora = "7"
    elif h == 8:
        hora = "8"
    elif h == 9:
        hora = "9"
    elif h == 10:
        hora = "10"
    elif h == 11:
        hora = "11"
    elif h == 12:
        hora = "12"
    elif h == 13:
        hora = "1"
    elif h == 14:
        hora = "2"
    elif h == 15:
        hora = "3"
    elif h== 16:
        hora= "4"
    elif h == 17:
        hora = "5"
    elif h == 18:
        hora = "6"
    elif h == 19:
        hora = "7"
    elif h == 20:
        hora = "8"
    elif h ==21:
        hora = "9"
    elif h == 22:
        hora= "10"
    elif h == 23:
        hora = "11"
    else:
        hora= "Error"

    return hora


#función para calcular el tiempo del día, si es a.m. o p.m.
def calcularTiempoDía(h):
    if h>=0 and h<12:
        tiempo= "a.m."
    else:
        tiempo="p.m."
    return tiempo


# función principal del programa y la que se correrá. Las lecturas e impresiones se hacen en esta función.
def main():
    h= int(input("Introduzca la hora en formato de 24 hrs:"))
    m= int(input("Introduzca los minutos:"))
    s = int(input("Introduzca los segundos:"))
    hora= calcularHora(h,m,s)
    tiempo=calcularTiempoDía(h)
    if hora== "Error":
        print("Error")
    else:
     print("La hora en formato de 12 hrs. es :\n",hora,":%02d"%m,":%02d"%s, tiempo)


main()