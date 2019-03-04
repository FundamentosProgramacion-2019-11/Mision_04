#RafaelRomeroBello
#A01747730, calcula el total comprado junto con el descuento
def calculaeldescuento(s):
    if s >= 1 and s <=10:
        r = 0
    elif s >= 11 and s <=19:
        r = (s*2300)*.15
    elif s >= 20 and s <=49:
        r = (s*2300)*.22
    elif s >= 50 and s <=99:
        r =( s*2300)*.35
    elif s >=100:
        r = (s*2300)*.42
    elif s == 0 and s >= -1:
        r = "tu numero es incorrecto"
    else:
        r = "error al colocar los datos"
    return r

def calculartotal(s,p):
    if s > 0:
        total = (s * 2300) - p
    else:
        total = "error al colocar los datos"
    return total

def main():
    Cantidad=int(input("introduce la cantidad de software comprado:"))
    Descuento = calculaeldescuento(Cantidad)
    print("el descuento que te toca es de:",Descuento)
    totalfinal = calculartotal(Cantidad,Descuento)
    print("tu total es:",totalfinal)

main()


