#Autor: Eric Andrés Jardón Chao
#Lee los tres lados de un posible triángulo dados por el usuario, y si existe, determina el tipo de triángulo. Si no existe, devuelve error.


def main(): #La función principal recibe las dimensiones de los tres lados del triángulo. Después corre la función que determina el tipo de triángulo, y si es existente, imprime el tipo de triángulo.
    ladoA=int(input("Teclea el lado A: "))
    ladoB=int(input("Teclea el lado B: "))
    ladoC=int(input("Teclea el lado C: "))
    tipoTriangulo=encontrarTipo(ladoA,ladoB,ladoC)
    if tipoTriangulo == "inexistente":
        print("Estos lados no corresponden a un triángulo.")
    else:
        print("El triángulo con esas dimensiones es",tipoTriangulo)


def encontrarTipo(a,b,c): #Esta función determina el tipo de triángulo, dadas las longitudes de sus tres lados.
    if a+b>c and a+c>b and b+c>a: #Primero evalúa que exista el triángulo, dos lados cualquiera de un triángulo sumados deben ser mayores al tercero.
        if a==b and b==c: #Si los tres lados son equivalentes, es equilátero.
            tipo="equilátero"
            return tipo
        else:
            if a==b or a==c or c==b: #Si solamente dos lados son iguales, es escaleno.
                tipo="isóceles"
                return tipo
            else:
                if (a*a==b*b + c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b): #Si sus lados cumplen con el teorema de Pitágoras, es rectángulo.
                    tipo="rectángulo"
                    return tipo
                else:
                    tipo="escaleno" #Si no cumple con ninguna de las condiciones anteriores y existe, debe ser escaleno.
                    return tipo
    else: #Si no cumple con la primera condición, no existe.
        tipo="inexistente"
        return tipo

main()
#Fin del programa