# Luis Alberto Zepeda Hernadez
# Descripción: Escribe un programa que lea el valor de cada uno de los lados de un triángulo,
# escribe el tipo de triángulo de acuerdo a la longitud de sus lados

#Esta función clasifica que tipo de triángulo es.
def clasificaTriangulo(ladoA,ladoB,ladoC):
    if ladoA == ladoB and ladoC == ladoA:
        return "Es un triángulo Equilátero."
    elif ladoA != ladoB and ladoA == ladoC:
        return "Es un triángulo Isóseles."
    elif ladoA != ladoC and ladoA == ladoB:
        return "Es un triángulo Isóseles."
    elif ladoB !=ladoA and ladoB == ladoC:
        return "Es un triángulo Isóseles."
    elif ladoA**2 == (ladoB**2 + ladoC**2):
        return "Es un triángulo Rectángulo."
    elif ladoB**2 == (ladoC**2+ladoA**2):
        return "Es un triángulo Rectángulo."
    elif ladoC**2 == (ladoA**2+ladoB**2):
        return "Es un triángulo Rectángulo."
    elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
        return "Es un triángulo Escaleno"
    else:
        return "Estos lados no corresponden a un triángulo."

#Esta función llama a la función que clasifica y pide los datos al usuario.
def main():
    ladoA=int(input("Teclea valor del lado A:"))
    ladoB=int(input("Teclea valor del lado B:"))
    ladoC=int(input("Teclea valor del lado C:"))

    tipoDeTriangulo = clasificaTriangulo(ladoA,ladoB,ladoC)
    print(tipoDeTriangulo)

main()