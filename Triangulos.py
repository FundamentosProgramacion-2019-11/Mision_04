#FRANCISCO JAVIER G0NZALEZ MOLINA A01748636
#IDENTIFICAR TIPO DE TRIANGULO Y SI EXISTE O NO

#Esta funcion comprueba si los datos igresados, cumplen con la caracteristica
#de un triangulo
def identificarExistencia (a,b,c):
    if (a+b)>c and (b+c)>a and (a+c)>b:
        return True
    else:
        return "Esto lados no corresponden a un triangulo"

#Esta funcion, identifica que tipo de triangulo es y lo dibuja*
#*no me fue posible dibujar los demas...
def identificarTipoyDibujar (a,b,c,existencia):
    import turtle
    if existencia==True:

        if a==b and b==c and c==a:
            print("Es un triangulo Equilatero")
            turtle.fd(a)
            turtle.left(120)
            turtle.fd(b)
            turtle.left(120)
            turtle.fd(c)
            turtle.left(120)
            turtle.exitonclick ()
        elif a==b or b==c or c==a:
            print("Es un triangulo Isosceles")

        else:
            print("Es un triangulo rectangulo")

#Esta funcion lee datos y llama a las funciones
def main():
    a=int(input("Dame lado A: "))
    b=int(input("Dame lado B: "))
    c=int(input("Dame lado C: "))
    existencia=identificarExistencia(a,b,c)
    print(existencia)
    tipo=identificarTipoyDibujar(a,b,c,existencia)
main()