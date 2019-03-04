#RafaelRomeroBello
#A01747730
#Decide que tipo de triangulo es dependiendo de los lados puestos
def comprobarquetrianguloes(l1,l2,l3):
    if l1==l2 and l2==l3 and l3==l1 :
        x="tu triangulo es equilatero"
    elif l1==l2 or l2==l3 or l3==l1:
        x="tu triangulo es isoseles"
    elif l1>0 and l2>0 and l3>0:
        x="tu triangulo es escaleno"
    elif l1<=0 or l2<=0 or l3<=0:
        x="estas incorrecto"
    else:
        print("que ondda")
    return x
def main():
    lado1=int(input("lado 1:"))
    lado2=int(input("lado 2:"))
    lado3=int(input("lado 3:"))
    co=comprobarquetrianguloes(lado1,lado2,lado3)
    print(co)

main()
