# Autor: Jose Luis Mata Lomeli
# Objetivo: Dado el tiempo en formato de 24 hrs, crear un programa que lo convierta a formato de 12hrs con AM y PM

# Funciones
def convertirTiempo(a,b,c):

    if 13 > a >= 1 and 61 > b >= 0 and 61 > c >=0:
        return ("Hora: %d:%02d:%02d AM" % (a,b,c))

    elif 24 > a >12 and 61 > b >=0 and 61 > c >= 0:
        a = a-12
        return ("Hora: %d:%02d:%02d PM" % (a,b,c))

    elif a == 0 and 61 > b >= 0 and 61 > c >= 0:
        a = 12
        return ("Hora: %d:%02d:%02d AM" % (a,b,c))

    else: #a<0 or a>23 or 0>b>60 or 0>c>60:
        return ("error")


# Funcion Principal
def main():

    #Entrada
    hora = int(input("Introduzca la hora: "))
    minuto = int(input("Introduzca los minutos: "))
    segundo = int(input("Introduzca los segundos: "))

    #Convertir
    formato12 = convertirTiempo(hora,minuto,segundo)
    print(formato12)

main()

