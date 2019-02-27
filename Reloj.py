#María Angélica Hernández Parada
#convertir las horas del formato de 24 a 12

def recibeHoras(horas,minutos,segundos):
    if horas<0 or horas>24:
        return "error"
    if horas<12:
        return (horas,":",minutos,":",segundos)
    if horas==24:
        horas2=horas-24
        return (horas2,":",minutos,":",segundos)
    if horas>12:
        horas1=horas-12
        return (horas1,":",minutos,":",segundos)

def main():
    horas=int(input("Dime la hora"))
    minutos=int(input("Dime los minutos"))
    segundos=int(input("Dime los segundos"))
    print(recibeHoras(horas, minutos, segundos))

main()