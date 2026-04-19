def sağ(adet):  #/ işaretini yapmak için yazdık alt satıra gitmesin diye de end="" yaptık
    for a in range(int(adet)):
        print("/",end="")

def sol(adet):
    for a in range(int(adet)):
        print("\\",end="")

def boşluk(adet):
    for a in range(int(adet)):
        print(" ",end="")

def atla(adet):
    for a in range(int(adet)):
        print(" ")

def üst(çap):
    başlangıç =  çap/2-1
    for a in range(int(çap/2)):
        boşluk(başlangıç-a)
        sağ(1)
        boşluk(a*2)
        sol(1)
        atla(1)


def alt(çap):
    başlangıç = çap-2
    for a in range(int(çap/2)):
        boşluk(a)
        sol(1)
        boşluk(başlangıç-a*2)
        sağ(1)
        atla(1)

def zümrüt(çap):
    üst(çap)
    alt(çap)


while True:
    a = int((input("lütfen elmas çapı gir yada 0 değeri ver çık")))
    if a ==0:

        quit("bay bay")
    else:
        üst(a)
        alt(a)
