#Autor: Karla Ximena Rueda Ruiz
#Este programa convierte la hora de formato de 24 horas a un formato de 12 horas.

def main():
    hra=int(input("Indica la hora:"))
    min=int(input("Indica los minutos:"))
    seg=int(input("Indica los segundos:"))

    formato12=calcularHora(hra)
    minutos=calcularMinutos(min)
    segundos=calcularSegundos(seg)

    print("La hora corresponde a",formato12,"hras.",minutos,"min.",segundos,"seg.")

def calcularHora(hra):
    if hra>12 and hra<=23:
        return "%d"%(hra-12)
    elif hra<=12 and hra>0:
        return hra
    else:
        return "Error"

def calcularMinutos(min):
    if min>=0 and min<60:
        return "%02d"%min
    else:
        return "Error"

def calcularSegundos(seg):
    if seg>=0 and seg<60:
        return "%02d"%seg
    else:
        return "Error"

main()

