#Una compañía de software vende un paquete por $2,300.00 cuando compras menos de 10 unidades. Si se compran 10 o
#más, se aplica un descuento de acuerdo a la siguiente tabla.

def calcularDescuento(unidades):
    if unidades>0 and unidades<=9:
        des = 0
    elif unidades>9 and unidades<=19:
        des = .15
    elif unidades>19 and unidades<=49:
        des = .22
    elif unidades>49 and unidades<=99:
        des = .35
    elif unidades>99:
        des = .42
    elif unidades<=0:
        print("Error")
        exit()

    return des

def calcularPrecio(unidades):
    p = unidades*2300
    return p

def calcularTotal(precio, descuento):
    Total = precio-(precio*descuento)
    return Total

def main():
    unidades = int(input("Teclea el número de unidades compradas: "))
    descuento = calcularDescuento(unidades)
    precio = calcularPrecio(unidades)
    precioTotal = calcularTotal(precio, descuento)
    print("El total a pagar es: ", precioTotal)

main()