#Autor: Daniela Estrella Tovar
#Dados tres lados, calcular que tipo de triángulo es.

#Esta función comprueba que las medidas sean de un triángulo

def comprobarSiEsTriangulo(ladoUno, ladoDos, ladoTres):
    if (ladoDos+ladoTres)>=ladoUno:
        result= "Si es un triángulo."
    else:
        result="Estos lados no corresponden a un triángulo"
    return result

#Esta función especifica el tipo de triángulo que corresponde a las medidas dadas.
def especificarTipoDeTriangulo(ladoUno, ladoDos, ladoTres):
    if ladoUno==ladoDos and ladoUno==ladoTres:
        tipoTriangulo= "El triángulo es equilatero."
    elif ladoUno==ladoDos or ladoUno==ladoTres or ladoTres==ladoDos:
        tipoTriangulo= "El triángulo es isósceles."
    elif ladoUno**2== ladoDos**2 + ladoTres**2:
        tipoTriangulo="El triángulo es rectángulo"
    elif(ladoDos+ladoTres)>=ladoUno:
        tipoTriangulo= "Es otro tipo de triángulo"
    else:
        tipoTriangulo="Error"
    return tipoTriangulo


#Función principal que lee e imprime valores

def main():
    ladoUno=int(input("Teclea la medida del lado más grande: "))
    ladoDos= int(input("Teclea la medida del lado mediano: "))
    ladoTres= int(input("Teclea la medida del lado más pequeño: "))
    comprobacion=comprobarSiEsTriangulo(ladoUno, ladoDos, ladoTres)
    print(comprobacion)
    tipo=especificarTipoDeTriangulo(ladoUno, ladoDos, ladoTres)
    print(tipo)
main()