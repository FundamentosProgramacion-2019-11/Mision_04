# Autor Sofía Trujillo Vargas
# Dado la base y la altura de dos rectángulos y decir cuál es el más grande.

def main():
    base1 = float(input("Dame la base del rectángulo uno: "))
    altura1 = float(input("Dame la altura del rectángulo uno: "))
    base2 = float(input("Dame la base del rectángulo dos: "))
    altura2 = float(input("Dame la altura del rectángulo dos: "))

    area1 = areaRectangulo(base1,altura1)
    perimetro1 = perimetroRectangulo(base1,altura1)
    area2 = areaRectangulo(base2,altura2)
    perimetro2 = perimetroRectangulo(base2,altura2)
    mayor = mayorRectangulo(area1,area2)
    print("El area del rectángulo uno es de: ",area1)
    print("El perimetro del rectángulo uno es de: ",perimetro1)
    print("El area del rectángulo dos es de: ", area2)
    print("El perimetro  del rectángulo dos es de: ",perimetro2)
    print("El mayor es o son iguales = ",mayor)

def areaRectangulo(b, a):
    area = b * a
    return area

def perimetroRectangulo(b, a):
    perimetro = b + b + a + a
    return perimetro

def mayorRectangulo(primero,segundo):
    if primero > segundo:
        return "primero"
    elif primero < segundo:
        return "segundo"
    elif primero == segundo:
        return "son iguales"

main()