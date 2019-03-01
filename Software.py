#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#Calcular descuento base a productos adqueridos

def calcularValorUnidades(unidades):
    if unidades<=0:
        return "Error"
    elif unidades <10:
        precio=unidades*2300
        return precio
    elif unidades >=10 and unidades<=19:
        descuento=2300-(2300*.15)
        precio=unidades*descuento
        return precio
    elif unidades>=20 and unidades<=49:
        descuento=2300-(2300*.22)
        precio=unidades*descuento
        return precio
    elif unidades>=50 and unidades<=99:
        descuento=2300-(2300*35)
        precio=unidade*descuento
        return precio
    elif unidades>=100:
        descuento=2300-(2300*.42)
        precio=unidades*descuento
        return precio
    else:
        return "Error"

def main ():
    unidades= int(input("Paquetes adquiridos: "))
    preciofinal=calcularValorUnidades(unidades)
    print(preciofinal)
main()