#Autor: Luis Renteria
#calcular de que triangulo se trata



def definirTriangulo(ladoA,ladoB,ladoC):
    if ladoA + ladoB > ladoC or ladoA + ladoC > ladoB or ladoB + ladoC > ladoA:
        return True

def definirElTriangulo(ladoA,ladoB,ladoC):
    if definirTriangulo(ladoA,ladoB,ladoC) == True:
        if ladoA==ladoB==ladoC:
            print "Triangulo Equilatero"
        elif ladoA==ladoB!=ladoC:
            print "Triangulo Isosceles"
        elif (ladoA**2)+(ladoB**2)-(ladoC**2)==0 or (ladoB**2)+(ladoC**2)-(ladoA**2)==0 or (ladoC**2)+(ladoA**2)-(ladoB**2)==0:
            print "Triangulo Rectangulo"
        else:
            print "Otro"

def main():
    ladoA=int(input("teclea la medida del primer lado"))
    ladoB=int(input("teclea la medida del segundo lado"))
    ladoC=int(input("teclea la medida del tercer lado"))
    definirTriangulo(ladoA,ladoB,ladoC)
    print(definirElTriangulo(ladoA,ladoB,ladoC))


main()

