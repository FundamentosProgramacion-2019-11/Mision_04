#Autor: Mario Hernández Cárdenas
#Cambia las horas de formato 24 hrs. a 12 hrs.


#Lee la hora y define si es a.m. o p.m y cambia el formato a 12 horas
def cambiarFormato(h, m, s):
    if h>=0 and h<=12:
        if h==0:
            hora12 = h+12
            return "La hora es: %d:%2d:%2d a.m."%(hora12, m, s)
        else:
            return "La hora es: %d:%2d:%2d a.m."%(h, m, s)
    else:
        hora12 = h-12
        return "\nLa hora es: %d:%02d:%02d p.m."%(hora12, m, s)


def main():
    hora = int(input("Escribe la hora en formato de 24 horas: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))
    if hora<0 or hora>23 or minutos<0 or minutos>59 or segundos<0 or segundos>59:
        print("\nEsa no es una hora valida")
    else:
        print(cambiarFormato(hora, minutos, segundos))


main()
