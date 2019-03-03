# Autor: Jose Luis Mata Lomeli
# Objetivo: Crear un programa que lea el numero de paquetes vendidos y despliegue la cantidad descontada y el total a pagar

# Una compañia vende un paquete por $2300.00 cuando compras menos de 10 unidades. Si son mayor o igual a 10, se aplica el descuento


#Funciones
def calcularDescuento(cantidad):

    if cantidad > 0 and cantidad < 10:
        precio = 2300*1

    elif cantidad >= 10 and cantidad <=19:
        precio = 2300 * .15

    elif cantidad >= 20 and cantidad <= 49:
        precio = 2300 * .22

    elif cantidad >= 50 and cantidad <= 99:
        precio = 2300 * .35

    elif cantidad >= 100:
        precio = 2300 * .42

    else:
        precio = 'ERROR'

    return precio



#Funcion Principal
def main():
    cantidad = int(input('Teclear la cantidad de paquetes que desea: '))
    total = calcularDescuento(cantidad)
    print('Total a pagar = $', total)

main()