#Autor: María Fernanda García Gastélum A01376181
#Convertir horas en formato 24hrs a 12hrs

#importar tortuga
import turtle

#convertir hora en formato de 24hrs a formato de 12hrs
def calcularHora(horasEn24):
    if horasEn24 > 12:
        return horasEn24-12
    else:
        return horasEn24


#EXTRA:dibujar reloj analógico
def dibujarReloj(horaEn12, minEn24, segEn24):
    #circulo
    turtle.pensize(2)
    turtle.setposition(0, 0)
    turtle.circle(150)
    #marcar las horas
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180+30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(90+30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(90 + 60)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180-30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(180 - 30)
    turtle.forward(150)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.goto(0,150)
    turtle.left(90+30)
    turtle.pendown()
    #manecilla de hora
    turtle.pensize(6)
    turtle.right(horaEn12*30)
    turtle.forward(70)
    #manecilla de min
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(horaEn12*30)
    turtle.right(minEn24 * 6)
    turtle.pendown()
    turtle.forward(100)
    #manecilla de seg
    turtle.pensize(1)
    turtle.penup()
    turtle.goto(0, 150)
    turtle.left(minEn24 * 6)
    turtle.right(segEn24 * 6)
    turtle.color("red")
    turtle.pendown()
    turtle.forward(100)
    #Esconder tortuga
    turtle.hideturtle()


def main():
    horasEn24= int(input("Escribe la hora: "))
    if horasEn24>24 or horasEn24<0:
        return print("Error")
    else:
        minEn24= int(input("Escribe los minutos: "))
        if minEn24>59 or minEn24 <0:
            return print("Error")
        else:
            segEn24= int(input("Escribe los segundos: "))
            if segEn24>59 or segEn24<0:
                return print("Error")
            else:
                horasEn12= calcularHora(horasEn24)
                if horasEn24 >= 12 and horasEn24 < 24:
                    print(horasEn12, ":", minEn24, ":", segEn24, "pm")
                else:
                    print(horasEn12, ":", minEn24, ":", segEn24, "am")
    dibujarReloj(horasEn12, minEn24, segEn24)
    turtle.exitonclick()


main()