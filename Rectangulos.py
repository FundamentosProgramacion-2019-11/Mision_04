#Autor: Diego Raul Elizalde Uriarte
#calcule e imprima el perímetro y área de dos rectangulos



def calcularArea1(base1,altura1):
    Area = base1*altura1
    return Area





def calcularArea2(base2, altura2):
    Area = base2 * altura2
    return Area




def calcularPerimetro1(base1,altura1):
    Perimetro = (base1*2)+(altura1*2)
    return Perimetro



def calcularPerimetro2(base2,altura2):
    Perimetro = (base2 * 2) + (altura2 * 2)
    return Perimetro




def indicarMayor(base1,altura1,base2, altura2):
    if calcularArea1(base1,altura1) > calcularArea2(base2, altura2):
        return "El primer rectangulo tiene mayor area"
    elif calcularArea1(base1,altura1) < calcularArea2(base2, altura2):
        return "El segundo rectangulo tiene mayor area"
    else:
        return "Las areas de los dos rectangulos son iguales"



def main():
    base1 = int(input("Dame la base del primer ractangulo: "))
    altura1 = int(input("Dame la altura del primer ractangulo: "))
    base2 = int(input("Dame la base del segundo ractangulo: "))
    altura2 = int(input("Dame la altura del segundo ractangulo: "))
    calcularArea1(base1,altura1)
    calcularArea2(base2, altura2)
    calcularPerimetro1(base1,altura1)
    calcularPerimetro2(base2, altura2)
    print("El Area del primer rectangulo es: ", calcularArea1(base1,altura1))
    print("El Area del segundo rectangulo es: ", calcularArea2(base2,altura2))
    print("El Perimetro del primer rectangulo es: ", calcularPerimetro1(base1,altura1))
    print("El Perimetro del segundo rectangulo es: ", calcularPerimetro2(base2, altura2))
    print(indicarMayor(base1,altura1,base2, altura2))











main()