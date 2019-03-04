#Mariana Coria Rodríguez, A01374765
# Leer los valores de un triangulo

#Comprobar si es un triangulo
def pruebaTriangulo (a, b, c):
    if a+b > c and a+c >b and b+c >a:
        return True
    else:
        return False

#Calcular tipo de traingulo
def tipoTriangulo (a,b,c):
    if a == b and b ==c:
        return "Es un Triángulo equilátero"
    elif a == c != b or a == b != c or a == c != b:
        return "Es un triángulo isóceles"
    elif (a**2)+(b**2)== (c**2) or (a**2)+(c**2)== (b**2) or (b**2)+(c**2)== (a**2):
        return "Es un triángulo rectángulo"
    else:
        return "Otro"

#Definir main y preguntas al usuario
def main():
    medida1 = int(input("Teclea tu primer medida: "))
    medida2 = int(input("Teclea tu segunda medida: "))
    medida3 = int(input("Tecle tu tercer medida: "))
    if not pruebaTriangulo(medida1, medida2, medida3):
        print ("Las medidas son incorrectas, triangulo inexistente")
    else: print (tipoTriangulo (medida1,medida2,medida3))



main()