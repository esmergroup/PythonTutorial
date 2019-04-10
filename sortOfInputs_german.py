import time

def sortierenVonStrings():
    a = int(input("GEBEN SIE DIE ANZAHL DER ELEMENTE EIN: "))
    time.sleep(0.1)

    if a>0:

        items = []

        for i in range(0, a):
            print("GEBEN SIE DAS ",i," ELEMENT EIN: ")
            items.append(input())
            time.sleep(0.2)

        b = len(items)
        c = sorted(items)

        for j in range(0, b):
            print(j, " ",c[j])
            time.sleep(0.2)

        print("FERTIG")
        time.sleep(0.8)

def sortierenVonZahlen():
    a = int(input("GEBEN SIE DIE ANZAHL DER ELEMENTE EIN: "))

    if a > 0:

        items_nr = []

        for k in range(0, a):
            print("GEBEN SIE DAS ",k," ELEMENT EIN: ")
            items_nr.append(input())
            time.sleep(0.2)

        b = len(items_nr)
        c = sorted(items_nr)

        for l in range(0, b):
            print(l, " ",c[l])
            time.sleep(0.2)

        print("FERIG")
        time.sleep(0.8)

def ende():
    print("")
    print("*************")
    print("PROGRAMM ENDE")
    print("*************")
    print("")
    time.sleep(0.8)
    exit()

def menue():
    while(True):
        print("")
        print("1 = SORTIEREN VON STRINGS")
        print("2 = SORTIEREN VON ZAHLEN")
        print("3 = ENDE")

        eingabe = int(input())

        if eingabe == 1:
            sortierenVonStrings()
        elif eingabe == 2:
            sortierenVonZahlen()
        elif eingabe == 3:
            ende()
        else:
            print("FALSCHE EINGABE")

print("**************")
print("PROGRAMM START")
print("**************")
print("")
time.sleep(0.8)
menue()
