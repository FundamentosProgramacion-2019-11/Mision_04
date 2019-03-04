# Autor: Victor Manuel Cerón Navarrete
# Descripcion: Convierte la hora de 24 horas a 12 horas

# esta función convierte las horas
def convertirHoras(h24):
        if h24 > 12:
            return h24-12
        else:
            return h24


# lee parametros e imprime convertido
def main():
    h24 = int(input("¿Qué hora es (en formato de 24 horas? "))
    if h24 > 24 or h24 < 0:
        return print("Ese número de horas no es posible, ERROR")
    else:
        min24= int(input("¿Cuántos minutos? "))
        if min24 > 59 or min24 < 0:
            return print("Ése número de minutos no es posible, ERROR")
        else:
            s24= int(input("¿Cuántos segundos? "))
            if s24 > 59 or s24 < 0:
                return print("Ese número de segundos no es posible, ERROR")
            else:
                hrs12 = convertirHoras(h24)
                if h24 >= 12 and h24 < 24:
                    print(hrs12, ":", min24, ":", s24, "p.m.")
                else:
                    print(hrs12,":", min24,":", s24,"a.m.")


main()