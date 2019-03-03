#Autor Dabid Yair Fernández Salas  #Matícula A01747088
# Este programa te dice la hora en formato de 24hrs a 12 hrs

"""En este problema usamos la funcion para dar la hora en formato de 24 horas, el usario indica cuales son
los parametros, hora,minutos,segundos, y la funcion hace las conversiones necesarias para obtener el resultado deseado"""
def CalcularHora(h,m,s):
    if h>=00 and h<12:
        if m<=59 or s>=00 or s<=59:
            tiempo="am"
            horabien= str(h)+":"+str(m)+":"+str(s),tiempo
            return horabien

    elif h>00 and h<11:
        if m>=00 and m<=59 and s>=00 and s<=59:
            tiempo="am"
            horabien= str(h)+":"+str(m)+":"+str(s),tiempo
            return horabien

    elif h==12 and m>=00:
        if m<=59 and s>=00 and s<=59:
            tiempo="pm"
            h=h-12
            horabien= str(h)+":"+str(m)+":"+str(s),tiempo
            return horabien

    elif h>12 and h>=23:
        if m>=00 and m<=59 and s>=00 and s<=59:
            tiempo="pm"
            h=0
            horabien=str(h)+":"+str(m)+":"+str(s),tiempo
            return horabien

    elif h<00 or h>= 24:
        if m<00 or m >= 60 or s< 00 or s>= 60:
            horabien = "Error"
            return horabien


"""En esta parte la funcion main, nos sirve porque le da los valores a la funcion de arriba y pueda calcular el resultado
y al finla esta fucnion imprime el resultado deseado"""
def main():
    h= int(input("Teclee el número de horas por favor: "))
    m = int(input("Teclee el número de minutos por favor: "))
    s= int(input("Teclee el número de segundos por favor: "))
    print("Tu hora es ",CalcularHora(h,m,s))


main()