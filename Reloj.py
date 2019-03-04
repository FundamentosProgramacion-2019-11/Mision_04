#Karimn Daniel Hernández Castorena
#Programa que modifique el formato de 24 horas al de 12 horas.

#Función que transforma la hora de 24 horas a 12 horas.
def tranformarHora(h):
    if h>=1 and h<=12:
        h12 = h
    elif h >=13 and h<=23:
        h12= h - 12
    elif h==0:
        h12=12
    else:
        h12= "Error"
    return h12


#Función que limita los minutos que sean ingresados.
def limitarMinutos(m):
    if m>=0 and m<=59:
        mi= m
    else:
        mi="Error"
    return mi


#Función que limita los segundos que sean ingresados.
def limitarSegundos(s):
    if s>=0 and s<=59:
        se=s
    else:
        se="Error"
    return se


#Función que lee los valores del tiempo e imprime los resultados.
def main():
    print()
    h = int(input("Ingresa la horas en formato de 24 horas: "))
    m = int(input("Ingresa los minutos: "))
    s = int(input("Ingresa los segundos: "))
    h12 = tranformarHora(h)
    mi = limitarMinutos(m)
    se = limitarSegundos(s)
    if h12== "Error":
        print()
        print("Error en tus horas.")
    elif mi=="Error":
        print()
        print("Error en tus minutos")
    elif se=="Error":
        print()
        print("Error en tus segundos")
    else:
        print()
        print("Son las", h12, ":", mi, ":", se)

main()





