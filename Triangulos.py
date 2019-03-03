# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que recibe los lados de un triángulo y le dice al usuario si es equilátero, isósceles, retángulo o no existe.

# Esta función recibe los lados del triángulo y luego devuelve el tipo de triángulo que es.
def calcularTriangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        tipo = "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = "Isósceles"
    elif (l1 ** 2 == l2 ** 2 + l3 ** 2) or (l2 ** 2 == l1 ** 2 + l3 ** 2) or (l3 ** 2 == l1 ** 2 + l2 ** 2):
        tipo = "Rectángulo"
    else:
        tipo = "Otro"
    return tipo


# Función principal.
def main():
    lado1 = int(input("Teclea el valor del primer lado del triángulo: "))
    lado2 = int(input("Teclea el valor del segundo lado del triángulo: "))
    lado3 = int(input("Teclea el valor del tercer lado del triángulo: "))

    # Esta condición indica si el triángulo existe o no e imprime el resultado.
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            tipoTriangulo = calcularTriangulo(lado1, lado2, lado3)
            print("El tipo de triángulo es: ", tipoTriangulo)
        else:
            print("El triángulo no existe")
    else:
        print("El triángulo no existe")


# Llamada a la función principal.
main()
