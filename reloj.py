#RafaelRomeroBello
#A01747730
#Convierte de 24hr a 12 hr

def calculalahoraenescalade12hr(h):
    if h <=0 and h>23:
        h="numero incorrecto"
    elif h==1:
        h=1
    elif h==2:
        h=2
    elif h==3:
        h=3
    elif h==4:
        h=4
    elif h==5:
        h=5
    elif h==6:
        h=6
    elif h==7:
        h=7
    elif h==8:
        h=8
    elif h==9:
        h=9
    elif h==10:
        h=10
    elif h==11:
        h=11
    elif h==12:
        h=12
    elif h==13:
        h=1
    if h == 14:
        h = 2
    elif h == 15:
        h = 3
    elif h == 16:
        h = 4
    elif h == 17:
        h = 5
    elif h == 18:
        h = 6
    elif h == 19:
        h = 7
    elif h == 20:
        h = 8
    elif h == 21:
        h = 9
    elif h == 22:
        h = 10
    elif h == 23:
        h = 11
    elif h == 00:
        h = 12
    else:
        h ="algo esa mal"
    return h


def comprobarminutos(m):
    if m>=0 and m<=59:
        m = m
    else:
        m = ("esta mal los datos")
    return m


def comprobarS(s):
    if s>=0 and s<=59:
        s = s
    else:
        s = "algo esta mal"
    return s

def main():
    hora=int(input("inerte la hora:"))
    minutoa=int(input("inserte minutos"))
    Segundos=int(input("inserte segundos"))
    ht=calculalahoraenescalade12hr(hora)
    mt=comprobarminutos(minutoa)
    st=comprobarS(Segundos)
    print(ht)
    print(mt)
    print(st)
    print("son las :" ,(ht) ," horas con:" ,(mt),"minutos y:",(st),"segundos")

main()




