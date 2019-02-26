#Autor: Eric Andrés Jardón Chao
#Programa que lee las horas, minutos y segundos por separado del formato de 24 hrs y lo convierte a formato de 12 hrs.
#EXTRA: Dibuja el reloj analógico con manecillas para horas, minutos y segundos, de colores rojo, azul y verde respectivamente.
import turtle

def main(): #Recibe las horas, minutos y segundos del formato 24 hrs. Corre la función de conversión y se imprime la variable de salida tiempo, que es una cadena de hora en formato 12hrs.
    horas24=int(input("Ingresa las horas únicamente:"))
    minutos24=int(input("Ingresa los minutos únicamente:"))
    segundos24=int(input("Ingresa los segundos únicamente:"))
    tiempo=str(convertirHora(horas24,minutos24,segundos24))
    print(tiempo) #imprime la cadena devuelta por la función convertirHora.
    dibujarReloj(horas24,minutos24,segundos24)

def convertirHora(h,m,s): #Esta función recibe parámetros numéricos y devuelve una cadena. Sólamente modifica las horas, dependiendo del número.
    if h<0 or h>23 or m<0 or m>59 or s<0 or s>59: #Filtración de las horas inválidas. Devuelve error si se ingresa una hora negativa o que supere 23 horas, 59 minutos o 59 segundos.
        return ("ERROR: la hora ingresada es inválida.")
    else:
        if h>12: #Si la hora es de 13hrs en adelante, restamos 12 para transformar a su equivalente.
            h=(h-12)
            return ("El tiempo es %02d:%02d:%02d pm" % (h, m, s)) #como la hora es posterior al mediodía, la hora es pm.
        if h == 0: #Si la hora son las 0 horas, se revierte a las 12 de la medianoche.
            h=12
        return ("El tiempo es %02d:%02d:%02d am" % (h, m, s)) #Como la hora no es posterior al mediodía, la hora es am.


def dibujarReloj(h,m,s): #Esta función utiliza el módulo tortuga para dibujar un reloj analógico con la hora ingresada.
    wn = turtle.Screen()
    t = turtle.Turtle() #cambiamos el nombre de la tortuga a t

    angHoras=(360/12)*h #El ángulo que la tortuga debe girar desde las 12 hacia la derecha para manecilla de horas.
    angMinutos=(360/60)*m #El ángulo que la tortuga debe girar desde las 12 hacia la derecha para manecilla de minutos.
    angSegundos=(360/60)*s #El ángulo que la tortuga debe girar desde las 12 hacia la derecha para manecilla de segundos.

    t.seth(90) #La tortuga mira hacia las 12
    t.color("red") #Manecilla de horas es roja
    t.right(angHoras)
    t.forward(50)
    t.penup()
    t.goto(0,0) #regresa al origen
    t.seth(90)
    t.color("blue") #Manecilla de minutos es azul
    t.pendown()
    t.right(angMinutos)
    t.forward(80)
    t.penup()
    t.goto(0, 0)
    t.seth(90)
    t.color("green") #Manecilla de segundos es verde
    t.pendown()
    t.right(angSegundos)
    t.forward(90)
    t.penup()
    t.goto(0,0)
    t.seth(0)
    t.forward(100)
    t.left(90)
    t.color("brown") #Marco del reloj es café
    t.pendown()
    t.circle(100) #se posiciona del origen a una distancia de radio, y comienza a trazar el círculo en sentido antihorario.


main()
turtle.exitonclick()
#Fin del programa