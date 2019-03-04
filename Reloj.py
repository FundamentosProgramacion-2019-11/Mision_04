#Mariana Coria Rodríguez, A01374765
# Leer la hora en formato de 24 y trasnformarlo a formato de 12


#Convertir las horas de 24 a 12
def calcularHora (Formato24):
    if Formato24 > 12:
        return Formato24-12
    else:
        return Formato24


#Definir main y preguntas para el usuario
def main():
    Formato24 = int(input("Usando el formato de 24 horas teclea unicamente la hora: "))
    if Formato24>24 or Formato24<0:
        print("Hora no valida")
    else:
        minutos = int(input("Teclea los minutos: "))
        if minutos>59 or minutos<0:
            print ("Minutos no validos")
        else:
            segundos =int(input("Teclea los segundos: "))
            if segundos>59 or segundos<0:
                print("Segundos no validos.")
            else:
                Formato12=calcularHora(Formato24)
                if Formato24 >= 12 and Formato24 <24:
                    print(Formato12, "hrs", minutos, "min" , segundos, "seg")
                else:
                    print(Formato12, "hrs", minutos, "min", segundos, "seg")


main()