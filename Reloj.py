# Autor: Cecilia Daniela Olivares Hernández, a01745727
# Este programa convierte la hora en formato de 24 hrs a formato de 12hrs


# Esta función transforma las horas
def transformarHora(h, m, s):
    if  h>24 or h<=0:
        return "Error"
    elif h<=12:
        hora = h
        return hora
    elif h>12 and h<=23:
        hora = h - 12
        return hora
    elif h==24:
        hora = h-24
        return hora


#Esta funcion verifica que los minutos sean correctos
def revisarMinutos(h, m, s):
    if m>60 or m<0:
        return "Error"
    elif m>=0:
        minutos = m
        return minutos


#Esta funcion verifica que los segundos sean correctos
def revisarSegundos(h, m, s):
    if s>60 or s<0:
        return "Error"
    elif s>=0:
        segundos = s
        return segundos


#Funcion principal que resuelve el problema
def main():
    h = int(input("Inserta la hora: "))
    m = int(input("Inserta el minuto: "))
    s = int(input("Inserta el segundo: "))
    hora = transformarHora(h, m, s)
    minutos = revisarMinutos(h, m, s)
    segundos = revisarSegundos(h, m, s)
    print("La hora en formato de 12 hrs es:")
    print(hora,":",minutos,":",segundos, "hrs")


main()
