#María Angélica Hernández Parada
#Calcular área/perímetro de dos rectangulos y decir si son mayor o iguales

def calculaArea1(altura1,base1):
    area1 = altura1 * base1
    return area1

def calculaArea2(altura2,base2):
    area2= altura2 * base2
    return  area2

def calcularPerimetro(altura1,base1,altura2,base2):
    perimetro1= (altura1*2)+(base1*2)
    perimetro2= (altura2*2)+(base2*2)
    return perimetro1 , perimetro2

def esMayorOIgual(area1,area2):
    if area1 > area2:
        return "El primer rectangulo es mayor"
    if area2 > area1:
        return "El segundo rectangulo es mayor"
    if area1 == area2:
        return "Tienen la misma área"


def main():
    altura1 = int(input("Dame la altura del primer rectangulo"))
    base1 = int(input("Dame la base del primer rectangulo"))
    altura2 = int(input("Dame la altura del primer rectangulo"))
    base2 = int(input("Dame la base del primer rectangulo"))
    print("(",(calculaArea1(altura1, base1)),",",(calculaArea2(altura2, base2)),")")
    print (calcularPerimetro(altura1, base1, altura2, base2))
    calculaArea2(altura2, base2)
    calcularPerimetro(altura1, base1, altura2, base2)
    area2= calculaArea1( altura2, base2)
    area1= calculaArea2(altura1, base1)
    print(esMayorOIgual(area1,area2))

main()