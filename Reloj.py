#Autor Sofía Trujillo Vargas
#Covertir un formato de 24 hrs a 12 hrs

def main():
    h = int(input("Dame la hora (00-23) : "))
    m = int(input("Dame los minutos (0-59): "))
    s = int(input("Dame los segundos (0-59) : "))
    if h<0 or h >24:
        print("Hora inválida")
    elif m<0 or m >60:
        print("Minutos invalidos")
    elif s<0 or s>60:
        print("Segundos invalidos")
    else:
        hora12 = ConvertirHoras(h)
        print("Son las : ",hora12, ":",m, ":",s)
def ConvertirHoras(h):
    if h <= 12:
        return h
    elif h > 12 and h <= 24:
        hora12 = (h-12)
        return hora12
main()