# Autor: Sofía Daniela Méndez Sandoval, A01242259
# Descripción: Este programa lee el número de paquetes vendidos y despliega la cantidad descontada y el total a pagar

#Llama a las funciones utilizadas
def main():

    #Pide al usuario la información necesaria
    paquetes = int(input("Ingrese la cantidad de paquetes a pagar: "))

    #Imprime resultados
    total = calcularPrecio(paquetes)
    print("El monto total es: $ ", total)

#Define lo que se hará
def calcularPrecio(paquetes):

    #Calcula el costo
    coston = paquetes*2300

    #Se utiliza if para determinar la cantidad de paquetes y por ende el porcentaje de descuento
    if paquetes<10 and paquetes>=1:
        costod = coston

    elif paquetes>=10 and paquetes<=19:
        costod = coston-coston*0.15

    elif paquetes>=20 and paquetes<=49:
        costod = coston-coston*0.22

    elif paquetes>=50 and paquetes<=99:
        costod = coston-coston*0.35

    elif paquetes>=100:
        costod = coston-coston*0.42

    else:
        costod = "Error"

    return costod

#Llama a función principal
main()

