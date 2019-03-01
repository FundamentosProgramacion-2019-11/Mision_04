#Autor: Cesar Guzman Guadarrama
#Este programa convierte la hora en formato de 24 horas al formato de 12 hrs.

import turtle


def convertirFormato(hora,minuto,segundo):        #esta funcion cambia el  formato y verifica que esten bien los datos
    if hora > 23 and minuto > 59 and segundo > 59:
        formato = "ERROR"
        return formato
    else:
        if hora >= 1 and hora <= 12:
            formato= ("%d:%0.2d:%0.2d  AM" % (hora,minuto,segundo))
            return formato
        elif hora >= 13 and hora <= 23:
            horas = hora - 12
            formato = ("%d:%0.2d:%0.2d  PM" % (horas, minuto, segundo))
            return formato
        elif hora == 0 and minuto == 0 and segundo == 0:
            formato = ("%d:%0.2d:%0.2d  PM" % (hora, minuto, segundo))
            return formato
        elif hora == 0 and minuto > 0 and segundo > 0:
            formato = ("%d:%0.2d:%0.2d  AM" % (hora, minuto, segundo))
            return formato
        elif hora > 23:
            formato = ("ERROR")
            return formato
        elif minuto < 0 or minuto >= 59:
            formato = ("ERROR")
            return formato
        elif segundo < 0 or segundo >= 59:
            formato = ("ERROR")
            return formato
        else:
            formato = ("ERROR")
            return formato

def dibujarReloj():
    turtle.speed( 0 )

    turtle.penup()
    turtle.goto( 0, -200 )
    turtle.pd()
    turtle.circle( 200 )
    turtle.left( 90 )
    turtle.fd( 50 )
    turtle.pu()
    turtle.fd( 350 )
    turtle.pd()
    turtle.bk( 50 )

    turtle.pu()
    turtle.bk( 150 )
    turtle.left( 90 )
    turtle.fd( 200 )
    turtle.pd()
    turtle.bk( 50 )
    turtle.pu()
    turtle.bk( 350 )
    turtle.pd()
    turtle.fd( 50 )
    turtle.pu()
    turtle.fd(160)
    turtle.pd()
    turtle.right(90)
    turtle.pu()
    turtle.goto(0,0)
    turtle.pd()


def ponerHora(hora,minuto,segundo):
    dibujarReloj()
    turtle.right(hora*30)
    turtle.fd(70)
    turtle.pu()
    turtle.right(360 - (hora * 30))
    turtle.goto(0,0)
    turtle.pd()
    turtle.right( minuto * 6 )
    turtle.fd(100)
    turtle.pu()
    turtle.right(360 - (minuto * 6))
    turtle.goto(0,0)
    turtle.pd()
    turtle.right(segundo * 6)
    turtle.fd(120)

    turtle.exitonclick()



def main():     #resuelve el problema
    hora = int(input("dame la hora en formato 24h"))
    minuto = int(input("dame los minutos "))
    segundo = int(input("dame los segundos "))
    formato = convertirFormato(hora,minuto,segundo)
    print(formato)
    ponerHora(hora,minuto,segundo)



main()