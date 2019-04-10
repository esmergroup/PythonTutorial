import time

def kelimeAyikla():
    a = int(input("LUETFEN KELIME BOYUTUNU VERINIZ: "))
    time.sleep(0.1)

    if a>0:

        items = []

        for i in range(0, a):
            print("",i,". KELIMEYI GIRINIZ")
            items.append(input())
            time.sleep(0.2)

        b = len(items)
        c = sorted(items)

        for j in range(0, b):
            print(j, " ",c[j])
            time.sleep(0.2)

        print("BITTI")
        time.sleep(0.8)

def sayilariSayikla():
    a = int(input("LUETFEN KELIME BOYUTUNU VERINIZ: "))

    if a > 0:

        items_nr = []

        for k in range(0, a):
            print("",k,". SAYISAL DEGERI GIRINIZ")
            items_nr.append(input())
            time.sleep(0.2)

        b = len(items_nr)
        c = sorted(items_nr)

        for l in range(0, b):
            print(l, " ",c[l])
            time.sleep(0.2)

        print("BITTI")
        time.sleep(0.8)

def ende():
    print("")
    print("*************")
    print("PROGRAM BITTI")
    print("*************")
    print("")
    time.sleep(0.8)
    exit()

def menue():
    while(True):
        print("")
        print("1 = KELIMELERI SIRALA")
        print("2 = SAYILARI SIRALA")
        print("3 = ENDE")

        eingabe = int(input())

        if eingabe == 1:
            kelimeAyikla()
        elif eingabe == 2:
            sayilariSayikla()
        elif eingabe == 3:
            ende()
        else:
            print("HATA")

print("**************")
print("PROGRAM BASLAT")
print("**************")
print("")
time.sleep(0.8)
menue()
