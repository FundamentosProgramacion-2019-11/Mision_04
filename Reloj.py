# Autor: Elizabeth Citlalli Zapata Cortes
# Convierte la hora de formato 24hrs. a formato 12 hrs.

import turtle

def convertirFormato(hora, minuto, segundo):
    if hora<=12 and minuto<=59 and segundo <=59:
        relojNuevo = hora,":%02d"%minuto, ":%02d"%segundo
        return relojNuevo
    elif hora>12 and hora<= 23   and minuto<=59 and segundo <=59:
        relojNuevo = (hora-12),":%02d"%minuto, ":%02d"%segundo
        return relojNuevo
    elif hora==24  and minuto<=59 and segundo <=59:
        relojNuevo= 0,":%02d"%minuto, ":%02d"%segundo
        return relojNuevo
    else:
        return "Error"


#EXTRA
def dibujaRelojHora(hora):
    turtle.color("blue")
    if hora ==0 or hora==12 or hora ==24:
        turtle.left(90)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-90)
    elif hora==1 or hora==13:
        turtle.left(60)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-60)
    elif hora==2 or hora==14:
        turtle.left(30)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-30)
    elif hora==3 or hora==15:
        turtle.forward(20)
        turtle.forward(-20)
    elif hora==4 or hora==16:
        turtle.left(-30)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(30)
    elif hora==5 or hora==17:
        turtle.left(-60)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(60)
    elif hora==6 or hora==18:
        turtle.left(-90)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(90)
    elif hora==7 or hora==19:
        turtle.left(240)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-240)
    elif hora==8 or hora==20:
        turtle.left(210)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-210)
    elif hora==9 or hora==21:
        turtle.left(180)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-180)
    elif hora==10 or hora==22:
        turtle.left(150)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-150)
    elif hora==11 or hora==23:
        turtle.left(120)
        turtle.forward(20)
        turtle.forward(-20)
        turtle.left(-120)


def dibujaRelojMinuto(minuto):
    turtle.color("green")
    if minuto ==0 and minuto ==60:
        turtle.left(90)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-90)
    elif minuto>=1 and minuto<=5:
        turtle.left(60)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-60)
    elif minuto>5 and minuto<=10:
        turtle.left(30)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-30)
    elif minuto>10 and minuto<=15:
        turtle.forward(15)
        turtle.forward(-15)
    elif minuto>15 and minuto<=20:
        turtle.left(-30)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(30)
    elif minuto>20 and minuto<=25:
        turtle.left(-60)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(60)
    elif minuto>25 and minuto<=30:
        turtle.left(-90)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(90)
    elif minuto>30 and minuto<=35:
        turtle.left(240)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-240)
    elif minuto>35 and minuto<=40:
        turtle.left(210)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-210)
    elif minuto>40 and minuto<=45:
        turtle.left(180)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-180)
    elif minuto>45 and minuto<=50:
        turtle.left(150)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-150)
    elif minuto>50 and minuto<=55:
        turtle.left(120)
        turtle.forward(15)
        turtle.forward(-15)
        turtle.left(-120)


def dibujaRelojSegundo(segundo):
    turtle.color("red")
    if segundo ==0 and segundo ==60:
        turtle.left(90)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-90)
    elif segundo>=1 and segundo<=5:
        turtle.left(60)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-60)
    elif segundo>5 and segundo<=10:
        turtle.left(30)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-30)
    elif segundo>10 and segundo<=15:
        turtle.forward(10)
        turtle.forward(-10)
    elif segundo>15 and segundo<=20:
        turtle.left(-30)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(30)
    elif segundo>20 and segundo<=25:
        turtle.left(-60)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(60)
    elif segundo>25 and segundo<=30:
        turtle.left(-90)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(90)
    elif segundo>30 and segundo<=35:
        turtle.left(240)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-240)
    elif segundo>35 and segundo<=40:
        turtle.left(210)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-210)
    elif segundo>40 and segundo<=45:
        turtle.left(180)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-180)
    elif segundo>45 and segundo<=50:
        turtle.left(150)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-150)
    elif segundo>50 and segundo<=55:
        turtle.left(120)
        turtle.forward(10)
        turtle.forward(-10)
        turtle.left(-120)


def main():
    hora = int(input("Teclea la hora: "))
    minuto = int(input("Teclea el minuto: "))
    segundo = int(input("Teclea el segundo: "))

    #Formato 12hrs
    horaNuevoFormato = convertirFormato(hora,minuto,segundo)

    print(horaNuevoFormato, "hrs.")

    #EXTRA
    dibujaRelojHora(hora)
    dibujaRelojMinuto(minuto)
    dibujaRelojSegundo(segundo)
    turtle.exitonclick()


main()