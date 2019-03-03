# Autor: Daniela Estrella Tovar
# Convertir la hora en formato de 24hrs a un formato de 12 horas

# Esta función convierte la hora en formato de 24 hroas a un formato de doce horas
def convertirHora(hora):
    if hora>=1 and hora<=12:
        formatoDoce= hora
    elif hora>=13 and hora<=23:
        formatoDoce= hora -12
    elif hora==0:
        formatoDoce= 12
    else:
        formatoDoce="Hay un error en la hora"
    return formatoDoce


#Esta función controla que no haya error en los minutos.

def evitarErrorMin (min):
    if min>=0 and min<=59:
        minut= min
    else:
        minut= "Hay un error en los minutos"
    return minut

#Esta función evita que haya errores en los segundos.

def evitarErrorSeg (seg):
    if seg>=0 and seg<=59:
        segund= seg
    else:
        segund= "Hay un error en los segundos"
    return segund

#Esta función lee e imprime las variables.
def main():
    hora= int(input("Teclea la hora en formato de 24 horas: "))
    min= int(input("Teclea los minutos (dos dígitos) :"))
    seg= int(input("Teclea los segundos (dos dígitos):"))
    formatoDoce= convertirHora(hora)
    minut=evitarErrorMin (min)
    segund= evitarErrorSeg(seg)
    print("La hora en formato de doce horas es : ", formatoDoce, ":", minut, ":", segund)


main()


