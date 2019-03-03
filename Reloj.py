# Autor : Guillermo De Anda Casas , A01375892
# Código que transforma la hora en formato de 24 horas a formato 12 horas.


# Función que cambia las horas.
def transformarHoras(horas24):
        if horas24 > 12:
            return horas24-12
        else:
            return horas24


# Función main que lee los parámetros, valida e imprime el nuevo formato.
def main():
    horas24 = int(input("¿Qué hora es? "))
    if horas24 > 24 or horas24 < 0:
        return print("ERROR")
    else:
        minutos24= int(input("¿Con cuántos minutos? "))
        if minutos24 > 59 or minutos24 < 0:
            return print("ERROR")
        else:
            segundos24= int(input("¿Con cuántos segundos? "))
            if segundos24 > 59 or segundos24 < 0:
                return print("ERROR")
            else:
                horas12 = transformarHoras(horas24)
                if horas24 >= 12 and horas24 < 24:
                    print(horas12, ":", minutos24, ":", segundos24, "p.m.")
                else:
                    print(horas12, ":", minutos24, ":", segundos24, "a.m.")


main()