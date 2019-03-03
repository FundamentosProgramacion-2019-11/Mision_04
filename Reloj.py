# Autor: luis Alberto Zepeda Hernandez
# Descripción: Escribe un programa que convierta la hora en formato de 24 horas
# al formato de 12 hrs.

# Esta función convierte la hora, y determina si la hora está dentro de los parámetros para ser hora.
def convertirHora(horas,minutos,segundos):
    if horas == 00 and minutos <60 and minutos >=00 and segundos <60 and segundos >= 00:
        print("12:",minutos,":",segundos,"AM")
    elif horas == 1 and minutos <60 and minutos >=00 and segundos <60 and segundos >= 00:
        print("1:",minutos,":",segundos,"AM")
    elif horas == 2 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("2:", minutos, ":", segundos, "AM")
    elif horas == 3 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("3:", minutos, ":", segundos, "AM")
    elif horas == 4 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("4:", minutos, ":", segundos, "AM")
    elif horas == 5 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("5:", minutos, ":", segundos, "AM")
    elif horas == 6 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("6:", minutos, ":", segundos, "AM")
    elif horas == 7 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("7:", minutos, ":", segundos, "AM")
    elif horas == 8 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("8:", minutos, ":", segundos, "AM")
    elif horas == 9 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("9:", minutos, ":", segundos, "AM")
    elif horas == 10 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("10:", minutos, ":", segundos, "AM")
    elif horas == 11 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("11:", minutos, ":", segundos, "AM")
    elif horas == 12 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("12:", minutos, ":", segundos, "AM")
    elif horas == 13 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("1:", minutos, ":", segundos, "PM")
    elif horas == 14 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("2:", minutos, ":", segundos, "PM")
    elif horas == 15 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("3:", minutos, ":", segundos, "PM")
    elif horas == 16 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("4:", minutos, ":", segundos, "PM")
    elif horas == 17 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("5:", minutos, ":", segundos, "PM")
    elif horas == 18 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("6:", minutos, ":", segundos, "PM")
    elif horas == 19 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("7:", minutos, ":", segundos, "PM")
    elif horas == 20and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("8:", minutos, ":", segundos, "PM")
    elif horas == 21 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("9:", minutos, ":", segundos, "PM")
    elif horas == 22 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("10:", minutos, ":", segundos, "PM")
    elif horas == 23 and minutos < 60 and minutos >= 00 and segundos < 60 and segundos >= 00:
        print("11:", minutos, ":", segundos, "PM")
    else:
        print("Error")


#Esta función llama a la función que hace la conversión.
def main():
    horas = int(input("Teclea la hora: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    convertirHora(horas,minutos,segundos)



main()