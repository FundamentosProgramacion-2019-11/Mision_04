#Autor Dabid Yair Fernández Salas  #Matícula A01747088
# Este programa te dice el descuento que se aplica a los articulos comprados


PRECIO=2300


"""En esta función main, nos ayuda a calcuñar los parametros que el usario ha ingresado y nos da el precio " 
adceudado, y realiza las operaciones necesarias para mostrar el resultado"""
def calcularCosto(paquetes):
    if paquetes>=1 and paquetes>10:
        costo=2300
        return costo
    if paquetes>=10 and paquetes<19:
        costo=PRECIO-(PRECIO*.15)
        return costo
    if paquetes>=20 and paquetes<49:
        costo=PRECIO-(PRECIO*.22)
        return costo
    if paquetes>=50 and paquetes<99:
        costo=PRECIO-(PRECIO*.35)
        return costo
    elif paquetes>=100:
        costo=PRECIO-(PRECIO*.42)
        return costo


"En esta función se esta caluclando el precio de cada paquete, para saber cuanto cuesta comprar mas de uno"
def Calcularprecio(paquetes):
    precio=(paquetes*2300)
    return precio


"""En esta parte, la función main, le pregunta al usario los parametros, numero de paquetes, que ha comprado
y le da el valor a la función de arriba para caluclar el resultado y está lo imprime"""
def main():
    paquetes=float(input("¿Cuántos paquetes has comprado?: "))
    print("Lo que vas a pagar sin descuento es",Calcularprecio(paquetes))
    print("Lo que vas a pagar con descuento es",calcularCosto(paquetes))

main()

