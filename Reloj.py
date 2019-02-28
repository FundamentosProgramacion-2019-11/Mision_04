# Autor: Paulina Guerrero Ruiz
#  Convertir la hora en formato de 24 hrs


def calcularHora (hora):         # Funcion que convierte la hora
    if hora>12 and hora<24:
        hora = hora-12
    elif hora<=12 and hora>=0:
        hora = hora

    return hora

def dimePeriodo (hora):                    #Funcion que calcula periodo
    if hora>12 and hora<24:
        Periodo= "pm"
    elif hora<=12 and hora>=0:
        Periodo= "am"
    return Periodo



def main():                                # Funcion que pide datos e imprime resultado
    hora = int(input("Teclea la hora: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))
    if hora>23 or hora<0 or minutos>60 or minutos<0 or segundos >60 or segundos<0:
        print("error")
    else:
        print (calcularHora(hora),":",minutos,":",segundos,dimePeriodo(hora))



main()